import os

import reflex as rx

from website.components import layout
from website.utilities import read_yaml, DefaultConfig


def contact() -> rx.Component:
    """Creates the about page."""
    configuration = read_yaml(os.getcwd() + "/configuration.yaml")
    contact_data = configuration["contact"]

    content = [
        rx.box(
            rx.heading(
                contact_data["message"],
                font_size=DefaultConfig.TITLE_TEXT_SIZE,
                font_family=DefaultConfig.DEFAULT_FONT_FAMILY,
            ),
            text_align="left",
            width="clamp(256px, 60%, 1280px)",
        ),
        # TODO center flex
        rx.flex(
            rx.box(
                rx.box(
                    rx.text(
                        contact_data["name"],
                        font_size=DefaultConfig.SUBTITLE_TEXT_SIZE,
                        font_family=DefaultConfig.DEFAULT_FONT_FAMILY,
                    ),
                    text_align="left",
                    width="clamp(256px, 60%, 1280px)",
                    font_size="clamp(1.0rem, 2.0svh, 3.0rem)",
                ),
                rx.box(
                    rx.text(contact_data["email"]),
                    text_align="left",
                    width="clamp(256px, 60%, 1280px)",
                    font_size="clamp(1.0rem, 2.0svh, 3.0rem)",
                ),
                rx.box(
                    rx.text(contact_data["phone"]),
                    text_align="left",
                    width="clamp(256px, 60%, 1280px)",
                    font_size="clamp(1.0rem, 2.0svh, 3.0rem)",
                ),
                rx.box(
                    rx.text(
                        f"{contact_data['city']}, {contact_data['province']}, {contact_data['country']}"
                    ),
                    text_align="left",
                    width="clamp(256px, 60%, 1280px)",
                    font_size="clamp(1.0rem, 2.0svh, 3.0rem)",
                ),
                width="70%",
            ),
            rx.box(
                rx.image(
                    src="/images/avatar.png",  # TODO remove image background
                    width="30%",
                    border_radius="0.5rem",
                ),
            ),
            align="center",
        ),
    ]
    return layout(content, configuration)
