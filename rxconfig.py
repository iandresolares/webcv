import reflex as rx


class WebsiteConfig(rx.Config):
    pass


config = WebsiteConfig(
    app_name="website",
    env=rx.Env.DEV,
    bun_path="/home/andres/.reflex/.bun/bin/bun"
)
