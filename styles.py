# Base styles (unchanged definitions for fonts, padding, etc.)
# For inputs, we use the same value in both themes.
TIME_LIMIT_INPUT_STYLE = """
    QLineEdit {
        background-color: #FFDDD2;
        color: black;
        font: 16pt 'Segoe UI';
        padding: 10px;
        border: 2px solid #FFDDD2;
        border-radius: 6px;
    }
"""
QUESTION_LABEL_STYLE = """
    font: 18pt 'Segoe UI';
    padding: 15px;
"""
ANSWER_BUTTON_STYLE = """
    QRadioButton {
        font: 14pt 'Segoe UI';  # decreased font size by 25%
        padding: 11.25px;  # decreased padding by 25%
        border-radius: 6px;
        margin: 5px;
    }
    QRadioButton:hover {
        /* will be set in theme */
    }
    QRadioButton::indicator:checked {
        border: 2px solid currentColor;
    }
"""
RATING_SLIDER_STYLE = """
    QSlider::groove:horizontal {
        border: 1px solid #3E4451;
        height: 8px;
        margin: 2px 0;
        border-radius: 4px;
    }
    QSlider::handle:horizontal {
        width: 20px;
        margin: -6px 0;
        border-radius: 10px;
    }
"""
# Define DARK THEME using requested values
DARK_THEME = {
    "MAIN_WINDOW_STYLE": "background-color: #17153B;",
    "HEADER_LABEL_STYLE": "font: 22pt 'Segoe UI'; color: #C8ACD6; padding: 10px;",
    "MENU_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "SCOREBOARD_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "EXIT_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "TIME_LIMIT_INPUT_STYLE": (
        "QLineEdit {"
        " background-color: #7A0BC0;"  # updated color
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: 2px solid #7A0BC0;"  # updated color
        " border-radius: 6px;"
        "}"
    ),
    "QUESTION_LABEL_STYLE": "font: 18pt 'Segoe UI'; color: #C8ACD6; padding: 15px;",
    "ANSWER_BUTTON_STYLE": (
        "QRadioButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 18pt 'Segoe UI';"  # increased font size by 50%
        " padding: 15px;"  # increased padding by 50%
        " border-radius: 6px;"
        " margin: 5px;"
        " } "
        "QRadioButton:hover { background-color: #2E236C; }"
    ),
    "NAV_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "RETURN_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "PROGRESS_BAR_STYLE": (
        "QProgressBar {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " border: none;"
        " border-radius: 6px;"
        " text-align: center;"
        " font: 14pt 'Segoe UI';"
        "} "
        "QProgressBar::chunk { background-color: #2E236C; border-radius: 6px; }"
    ),
    "RESULTS_LABEL_STYLE": "font: 20pt 'Segoe UI'; color: #C8ACD6; padding: 10px;",
    "FEEDBACK_INPUT_STYLE": (
        "QLineEdit {"
        " background-color: #FFDDD2;"
        " color: black;"
        " font: 12pt 'Segoe UI';"
        " padding: 10px;"
        " border: 2px solid #FFDDD2;"
        " border-radius: 6px;"
        "}"
    ),
    "SUBMIT_FEEDBACK_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "SCOREBOARD_STYLE": (
        "QTableWidget {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 14pt 'Segoe UI';"
        " border: none;"
        "} "
        "QTableWidget::item { border: 1px solid #17153B; padding: 6px; }"
        "QTableWidget::item:selected { background-color: #2E236C; }"
    ),
    "SCOREBOARD_HEADER_STYLE": (
        "QHeaderView::section {"
        " background-color: #17153B;"
        " color: #C8ACD6;"
        " font: bold 14pt 'Segoe UI';"
        " padding: 8px;"
        " border: 1px solid #433D8B;"
        "}"
    ),
    "INCORRECT_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 14pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
    "SKIPPED_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #433D8B;"
        " color: #ECDBBA;"
        " font: 14pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #2E236C; }"
    ),
}

# Define PINK THEME using requested values
PINK_THEME = {
    "MAIN_WINDOW_STYLE": "background-color: #FFB9B9;",
    "HEADER_LABEL_STYLE": "font: 22pt 'Segoe UI'; color: black; padding: 10px;",  # changed color to black
    "MENU_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "SCOREBOARD_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "EXIT_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 12px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "TIME_LIMIT_INPUT_STYLE": TIME_LIMIT_INPUT_STYLE,
    "QUESTION_LABEL_STYLE": "font: 18pt 'Segoe UI'; color: black; padding: 15px;",  # changed color to black
    "ANSWER_BUTTON_STYLE": (
        "QRadioButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 18pt 'Segoe UI';"  # decreased font size by 25%
        " padding: 11.25px;"  # decreased padding by 25%
        " border-radius: 6px;"
        " }"
        "QRadioButton:hover { background-color: #FFACC7; }"
    ),
    "NAV_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "RETURN_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "PROGRESS_BAR_STYLE": (
        "QProgressBar {"
        " background-color: #FF8DC7;"
        " color: black;"
        " border: none;"
        " border-radius: 6px;"
        " text-align: center;"
        " font: 14pt 'Segoe UI';"
        "} "
        "QProgressBar::chunk { background-color: #FFACC7; border-radius: 6px; }"
    ),
    "RESULTS_LABEL_STYLE": "font: 20pt 'Segoe UI'; color: black; padding: 10px;",  # changed color to black
    "FEEDBACK_INPUT_STYLE": """
        QLineEdit {
            background-color: #FFDDD2;
            color: black;
            font: 12pt 'Segoe UI';
            padding: 10px;
            border: 2px solid #FFDDD2;
            border-radius: 6px;
        }
    """,
    "RATING_SLIDER_STYLE": RATING_SLIDER_STYLE,
    "SUBMIT_FEEDBACK_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 16pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "SCOREBOARD_STYLE": (
        "QTableWidget {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 14pt 'Segoe UI';"
        " border: none;"
        "} "
        "QTableWidget::item { border: 1px solid #FFB9B9; padding: 6px; }"
        "QTableWidget::item:selected { background-color: #FFACC7; }"
    ),
    "SCOREBOARD_HEADER_STYLE": (
        "QHeaderView::section {"
        " background-color: #FFB9B9;"
        " color: black;"  # changed color to black
        " font: bold 14pt 'Segoe UI';"
        " padding: 8px;"
        " border: 1px solid #FF8DC7;"
        "}"
    ),
    "INCORRECT_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 14pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
    "SKIPPED_BUTTON_STYLE": (
        "QPushButton {"
        " background-color: #FF8DC7;"
        " color: black;"
        " font: 14pt 'Segoe UI';"
        " padding: 10px;"
        " border: none;"
        " border-radius: 8px;"
        "} "
        "QPushButton:hover { background-color: #FFACC7; }"
    ),
}

def get_theme(theme_name):
    return PINK_THEME if theme_name == "pink" else DARK_THEME