pyside2-uic.exe --from-imports --output .\ui\auto_generated\find_and_replace.py .\ui\find_and_replace.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\ui_intro_window.py .\ui\forms\intro_window.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\warning_dialog.py .\ui\forms\warning_dialog.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\interface_dialog.py .\ui\forms\interface_dialog.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\device_dialog.py .\ui\forms\device_dialog.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\common_chart_form.py .\ui\forms\common_chart_form.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\common_docked_widget.py .\ui\forms\common_docked_widget.ui
@REM pyside2-uic.exe --from-imports --output .\ui\auto_generated\common_dialog_window.py .\ui\forms\common_dialog_window.ui




@REM pyside2-uic.exe .\ui\forms\ui_main.ui --from-imports > .\ui\auto_generated\ui_main.py
@REM pyside2-uic.exe .\ui\forms\intro_window.ui --from-imports > .\ui\auto_generated\ui_intro_window.py
@REM pyside2-uic.exe .\ui\forms\warning_dialog.ui --from-imports > .\ui\auto_generated\warning_dialog.py
@REM pyside2-uic.exe .\ui\forms\interface_dialog.ui --from-imports > .\ui\auto_generated\interface_dialog.py
@REM pyside2-uic.exe .\ui\forms\device_dialog.ui --from-imports > .\ui\auto_generated\device_dialog.py
@REM pyside2-uic.exe .\ui\forms\common_chart_form.ui --from-imports > .\ui\auto_generated\common_chart_form.py
@REM pyside2-uic.exe .\ui\forms\common_docked_widget.ui --from-imports > .\ui\auto_generated\common_docked_widget.py
@REM pyside2-uic.exe .\ui\forms\common_dialog_window.ui --from-imports > .\ui\auto_generated\common_dialog_window.py

@REM pyside2-rcc.exe .\ui\forms\files.qrc > .\ui\auto_generated\files_rc.py