---
title: Rich Edit Control Styles (Winuser.h)
description: The following window styles are unique to rich edit controls.
ms.assetid: 0f1b3e01-01cb-4b3e-b959-6f32498f0394
topic_type:
- apiref
api_name:
- ES_DISABLENOSCROLL
- ES_EX_NOCALLOLEINIT
- ES_NOIME
- ES_NOOLEDRAGDROP
- ES_SAVESEL
- ES_SELECTIONBAR
- ES_SELFIME
- ES_SUNKEN
- ES_VERTICAL
- ES_AUTOHSCROLL
- ES_AUTOVSCROLL
- ES_CENTER
- ES_LEFT
- ES_MULTILINE
- ES_NOHIDESEL
- ES_NUMBER
- ES_PASSWORD
- ES_READONLY
- ES_RIGHT
- ES_WANTRETURN
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Rich Edit Control Styles

The following window styles are unique to rich edit controls.



| Constant                                                                                                                                                                         | Description                                                                                                                                                                                                                                         |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ES_DISABLENOSCROLL"></span><span id="es_disablenoscroll"></span><dl> <dt>**ES\_DISABLENOSCROLL**</dt> </dl>     | Disables scroll bars instead of hiding them when they are not needed.<br/>                                                                                                                                                                    |
| <span id="ES_EX_NOCALLOLEINIT"></span><span id="es_ex_nocalloleinit"></span><dl> <dt>**ES\_EX\_NOCALLOLEINIT**</dt> </dl> | Prevents the control from calling the [**OleInitialize**](/windows/desktop/api/ole2/nf-ole2-oleinitialize) function when created. This window style is useful only in dialog templates because [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) does not accept this style.<br/> |
| <span id="ES_NOIME_"></span><span id="es_noime_"></span><dl> <dt>**ES\_NOIME** </dt> </dl>                                | Disables the IME operation. This style is available for Asian language support only.<br/>                                                                                                                                                     |
| <span id="ES_NOOLEDRAGDROP"></span><span id="es_nooledragdrop"></span><dl> <dt>**ES\_NOOLEDRAGDROP**</dt> </dl>           | Disables support for drag-drop of OLE objects.<br/>                                                                                                                                                                                           |
| <span id="ES_SAVESEL"></span><span id="es_savesel"></span><dl> <dt>**ES\_SAVESEL**</dt> </dl>                             | Preserves the selection when the control loses the focus. By default, the entire contents of the control are selected when it regains the focus.<br/>                                                                                         |
| <span id="ES_SELECTIONBAR"></span><span id="es_selectionbar"></span><dl> <dt>**ES\_SELECTIONBAR**</dt> </dl>              | Adds space to the left margin where the cursor changes to a right-up arrow, allowing the user to select full lines of text. <br/>                                                                                                             |
| <span id="ES_SELFIME_"></span><span id="es_selfime_"></span><dl> <dt>**ES\_SELFIME** </dt> </dl>                          | Directs the rich edit control to allow the application to handle all IME operations. This style is available for Asian language support only.<br/>                                                                                            |
| <span id="ES_SUNKEN"></span><span id="es_sunken"></span><dl> <dt>**ES\_SUNKEN**</dt> </dl>                                | Displays the control with a sunken border style so that the rich edit control appears recessed into its parent window. <br/>                                                                                                                  |
| <span id="ES_VERTICAL"></span><span id="es_vertical"></span><dl> <dt>**ES\_VERTICAL**</dt> </dl>                          | Draws text and objects in a vertical direction. This style is available for Asian-language support only.<br/>                                                                                                                                 |



Rich edit controls also support the following edit control styles.



| Constant                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                             |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="ES_AUTOHSCROLL"></span><span id="es_autohscroll"></span><dl> <dt>**ES\_AUTOHSCROLL**</dt> </dl> | Automatically scrolls text to the right by 10 characters when the user types a character at the end of the line. When the user presses the ENTER key, the control scrolls all text back to position zero.<br/>                                                                                                                                                    |
| <span id="ES_AUTOVSCROLL"></span><span id="es_autovscroll"></span><dl> <dt>**ES\_AUTOVSCROLL**</dt> </dl> | Automatically scrolls text up one page when the user presses the ENTER key on the last line.<br/>                                                                                                                                                                                                                                                                 |
| <span id="ES_CENTER"></span><span id="es_center"></span><dl> <dt>**ES\_CENTER**</dt> </dl>                | Centers text in a single-line or multiline edit control.<br/>                                                                                                                                                                                                                                                                                                     |
| <span id="ES_LEFT"></span><span id="es_left"></span><dl> <dt>**ES\_LEFT**</dt> </dl>                      | Left aligns text.<br/>                                                                                                                                                                                                                                                                                                                                            |
| <span id="ES_MULTILINE"></span><span id="es_multiline"></span><dl> <dt>**ES\_MULTILINE**</dt> </dl>       | Designates a multiline edit control. The default is single-line edit control.<br/>                                                                                                                                                                                                                                                                                |
| <span id="ES_NOHIDESEL"></span><span id="es_nohidesel"></span><dl> <dt>**ES\_NOHIDESEL**</dt> </dl>       | Negates the default behavior for an edit control. The default behavior hides the selection when the control loses the input focus and inverts the selection when the control receives the input focus. If you specify [**ES\_NOHIDESEL**](edit-control-styles.md), the selected text is inverted, even if the control does not have the focus.<br/> |
| <span id="ES_NUMBER"></span><span id="es_number"></span><dl> <dt>**ES\_NUMBER**</dt> </dl>                | Allows only digits to be entered into the edit control.<br/>                                                                                                                                                                                                                                                                                                      |
| <span id="ES_PASSWORD"></span><span id="es_password"></span><dl> <dt>**ES\_PASSWORD**</dt> </dl>          | Displays an asterisk (\*) for each character typed into the edit control. This style is valid only for single-line edit controls.<br/>                                                                                                                                                                                                                            |
| <span id="ES_READONLY"></span><span id="es_readonly"></span><dl> <dt>**ES\_READONLY**</dt> </dl>          | Prevents the user from typing or editing text in the edit control.<br/>                                                                                                                                                                                                                                                                                           |
| <span id="ES_RIGHT"></span><span id="es_right"></span><dl> <dt>**ES\_RIGHT**</dt> </dl>                   | Right aligns text in a single-line or multiline edit control.<br/>                                                                                                                                                                                                                                                                                                |
| <span id="ES_WANTRETURN"></span><span id="es_wantreturn"></span><dl> <dt>**ES\_WANTRETURN**</dt> </dl>    | Specifies that a carriage return be inserted when the user presses the ENTER key while entering text into a multiline edit control in a dialog box. If you do not specify this style, pressing the ENTER key has the same effect as pressing the dialog box's default push button. This style has no effect on a single-line edit control.<br/>                   |



Rich edit controls do not support the following edit control styles.

-   [**ES\_LOWERCASE**](edit-control-styles.md)
-   [**ES\_OEMCONVERT**](edit-control-styles.md)
-   [**ES\_UPPERCASE**](edit-control-styles.md)

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



 

