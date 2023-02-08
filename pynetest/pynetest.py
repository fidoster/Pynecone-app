import pynecone as pc
import random

jokes = [
    "250 lbs here on Earth is 94.5 lbs on Mercury. No, I'm not fat. I’m just not on the right planet.",
    "I used to think I was indecisive. But now I’m not so sure.",
    "Why should you not write with a broken pencil? Because it is pointless.",
    "What did the tomato say to the other tomato during a race? Ketchup",
    "What do you call a factory that sells good products? A satisfactory",
    "You can not trust atoms. They make up everything!",
]

class State(pc.State):
    """The app state."""

    joke = random.choice(jokes)

    def next_joke(self):
        """ Show next joke."""
        current_index = jokes.index(self.joke)
        if current_index == len(jokes) - 1:
            self.joke = jokes[0]
        else:
            self.joke = jokes[current_index + 1]

    def last_joke(self):
        """ Show last joke."""
        current_index = jokes.index(self.joke)
        if current_index == 0:
            self.joke = jokes[-1]
        else:
            self.joke = jokes[current_index - 1]

    def random_joke(self):
        """ Show random joke."""
        self.joke = random.choice(jokes)

def index():
    """The main view."""
    return pc.vstack(
        pc.text("JOKE A DAY..!!", font_size="3em", color="#EEFBFB", font_weight="bold", text_align="center", padding_bottom="1em"),
        pc.center(
            pc.vstack(
                pc.heading(State.joke, font_size="2em", padding_bottom="2em"),
                pc.hstack(
                    pc.button("Last", on_click=State.last_joke, color_scheme="red"),
                    pc.button("Random", on_click=State.random_joke, color_scheme="blue"),
                    pc.button("Next", on_click=State.next_joke, color_scheme="green"),
                ),
                padding="1em",
                bg="#4DA8DA",
                border_radius="1em",
                box_shadow="lg",
                width="50%",
            ),
        ),
        padding_y="5em",
        width="100%",
        height="100vh",
        bg="#12232E",
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Jokes")
app.compile()

