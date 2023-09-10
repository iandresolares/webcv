from typing import Any

import reflex as rx

from website.utilities import DefaultConfig


def heading(content: list[rx.Component], **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            *content,
            wrap="nowrap",
            direction="column",
            text_align="center",
        ),
        # Font
        font_weight="400",
        font_family=DefaultConfig.DEFAULT_FONT_FAMILY,
        letter_spacing="-0.112rem",
        font_size="clamp(2.0rem, 6.0svh, 16.0rem)",
        line_height="clamp(3.25rem, 7.8svh, 20.8rem)",
        # Size
        padding="1.0rem",
        width="clamp(10rem, 85%, 1280px)",
        height="clamp(10rem, 40%, 40rem)",
        **props,
    )


def heading2(component: rx.Component, **props: Any) -> rx.Component:
    return rx.center(
        rx.flex(
            component,
            wrap="nowrap",
            direction="column",
            text_align="center",
        ),
        # Font
        font_weight="200",
        font_family=DefaultConfig.DEFAULT_FONT_FAMILY,
        letter_spacing="-0.112rem",
        font_size="clamp(2.0rem, 6.0svh, 16.0rem)",
        line_height="clamp(3.25rem, 7.8svh, 20.8rem)",
        # Size
        padding="1.0rem",
        width="clamp(10rem, 85%, 1280px)",
        height="clamp(10rem, 40%, 40rem)",
        **props,
    )
