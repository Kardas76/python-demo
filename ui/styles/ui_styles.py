class UIStyle():


    menu_selected_menu_button_style = (
    """
    QPushButton { border-right: 7px solid rgb(44, 49, 60); }
    """
    )


    style_menu_button = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(27, 29, 35);
        border-right: 5px solid rgb(44, 49, 60);
        background-color: rgb(27, 29, 35);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(37, 43, 52);
        border-left: 28px solid rgb(33, 37, 43);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """
    )

    style_simple_button = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
    }
    """
    )


    style_linedit_on_validation_failed = (
    """
        background-color: rgb(130, 30, 30);
    """
    )