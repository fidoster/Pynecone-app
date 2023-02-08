import pynecone as pc


config = pc.Config(
    app_name="pynetest",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
