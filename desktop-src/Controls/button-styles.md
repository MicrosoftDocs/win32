---
title: Button Styles (Winuser.h)
description: Specifies a combination of button styles. If you create a button using the BUTTON class with the CreateWindow or CreateWindowEx function, you can specify any of the button styles listed below.
ms.assetid: 30254cb5-43cd-407f-8ad6-bd7f9ec3edc7
topic_type:
- apiref
api_name:
- BS_3STATE
- BS_AUTO3STATE
- BS_AUTOCHECKBOX
- BS_AUTORADIOBUTTON
- BS_BITMAP
- BS_BOTTOM
- BS_CENTER
- BS_CHECKBOX
- BS_COMMANDLINK
- BS_DEFCOMMANDLINK
- BS_DEFPUSHBUTTON
- BS_DEFSPLITBUTTON
- BS_GROUPBOX
- BS_ICON
- BS_FLAT
- BS_LEFT
- BS_LEFTTEXT
- BS_MULTILINE
- BS_NOTIFY
- BS_OWNERDRAW
- BS_PUSHBUTTON
- BS_PUSHLIKE
- BS_RADIOBUTTON
- BS_RIGHT
- BS_RIGHTBUTTON
- BS_SPLITBUTTON
- BS_TEXT
- BS_TOP
- BS_TYPEMASK
- BS_USERBUTTON
- BS_VCENTER
api_location:
- Winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# Button Styles

Specifies a combination of button styles. If you create a button using the BUTTON class with the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, you can specify any of the button styles listed below.

## Example

```cpp
HRESULT Button::CreateText(HWND hParent, const TCHAR *szCaption, int nID, 
                               const Rect& rcBound)
{
    CREATESTRUCT create;
	ZeroMemory(&create, sizeof(CREATESTRUCT));

    create.x = rcBound.left;
    create.y = rcBound.top;
    create.cx = rcBound.right - create.x;
    create.cy = rcBound.bottom - create.y;

    create.hwndParent = hParent;
    create.lpszName = szCaption;
    create.hMenu = (HMENU)(INT_PTR)nID;
    create.lpszClass = TEXT("BUTTON");
    create.style = BS_PUSHBUTTON | BS_FLAT;
    return Control::Create(create);
}
```
Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/Win7Samples/multimedia/directshow/common/button.cpp) on GitHub.


## Constants
| Constant                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="BS_3STATE"></span><span id="bs_3state"></span><dl> <dt>**BS\_3STATE**</dt> </dl>                            | Creates a button that is the same as a check box, except that the box can be grayed as well as checked or cleared. Use the grayed state to show that the state of the check box is not determined.<br/>                                                                                                                                                                                              |
| <span id="BS_AUTO3STATE"></span><span id="bs_auto3state"></span><dl> <dt>**BS\_AUTO3STATE**</dt> </dl>                | Creates a button that is the same as a three-state check box, except that the box changes its state when the user selects it. The state cycles through checked, indeterminate, and cleared.<br/>                                                                                                                                                                                                     |
| <span id="BS_AUTOCHECKBOX"></span><span id="bs_autocheckbox"></span><dl> <dt>**BS\_AUTOCHECKBOX**</dt> </dl>          | Creates a button that is the same as a check box, except that the check state automatically toggles between checked and cleared each time the user selects the check box.<br/>                                                                                                                                                                                                                       |
| <span id="BS_AUTORADIOBUTTON"></span><span id="bs_autoradiobutton"></span><dl> <dt>**BS\_AUTORADIOBUTTON**</dt> </dl> | Creates a button that is the same as a radio button, except that when the user selects it, the system automatically sets the button's check state to checked and automatically sets the check state for all other buttons in the same group to cleared.<br/>                                                                                                                                         |
| <span id="BS_BITMAP"></span><span id="bs_bitmap"></span><dl> <dt>**BS\_BITMAP**</dt> </dl>                            | Specifies that the button displays a bitmap. See the Remarks section for its interaction with BS\_ICON.<br/>                                                                                                                                                                                                                                                                                         |
| <span id="BS_BOTTOM"></span><span id="bs_bottom"></span><dl> <dt>**BS\_BOTTOM**</dt> </dl>                            | Places text at the bottom of the button rectangle.<br/>                                                                                                                                                                                                                                                                                                                                              |
| <span id="BS_CENTER"></span><span id="bs_center"></span><dl> <dt>**BS\_CENTER**</dt> </dl>                            | Centers text horizontally in the button rectangle.<br/>                                                                                                                                                                                                                                                                                                                                              |
| <span id="BS_CHECKBOX"></span><span id="bs_checkbox"></span><dl> <dt>**BS\_CHECKBOX**</dt> </dl>                      | Creates a small, empty check box with text. By default, the text is displayed to the right of the check box. To display the text to the left of the check box, combine this flag with the BS\_LEFTTEXT style (or with the equivalent BS\_RIGHTBUTTON style).<br/>                                                                                                                                    |
| <span id="BS_COMMANDLINK"></span><span id="bs_commandlink"></span><dl> <dt>**BS\_COMMANDLINK**</dt> </dl>             | Creates a command link button that behaves like a BS\_PUSHBUTTON style button, but the command link button has a green arrow on the left pointing to the button text. A caption for the button text can be set by sending the BCM\_SETNOTE message to the button.<br/>                                                                                                                               |
| <span id="BS_DEFCOMMANDLINK"></span><span id="bs_defcommandlink"></span><dl> <dt>**BS\_DEFCOMMANDLINK**</dt> </dl>    | Creates a command link button that behaves like a BS\_PUSHBUTTON style button. If the button is in a dialog box, the user can select the command link button by pressing the ENTER key, even when the command link button does not have the input focus. This style is useful for enabling the user to quickly select the most likely (default) option.<br/>                                         |
| <span id="BS_DEFPUSHBUTTON"></span><span id="bs_defpushbutton"></span><dl> <dt>**BS\_DEFPUSHBUTTON**</dt> </dl>       | Creates a push button that behaves like a BS\_PUSHBUTTON style button, but has a distinct appearance. If the button is in a dialog box, the user can select the button by pressing the ENTER key, even when the button does not have the input focus. This style is useful for enabling the user to quickly select the most likely (default) option.<br/>                                            |
| <span id="BS_DEFSPLITBUTTON"></span><span id="bs_defsplitbutton"></span><dl> <dt>**BS\_DEFSPLITBUTTON**</dt> </dl>    | Creates a split button that behaves like a BS\_PUSHBUTTON style button, but also has a distinctive appearance. If the split button is in a dialog box, the user can select the split button by pressing the ENTER key, even when the split button does not have the input focus. This style is useful for enabling the user to quickly select the most likely (default) option.<br/>                 |
| <span id="BS_GROUPBOX"></span><span id="bs_groupbox"></span><dl> <dt>**BS\_GROUPBOX**</dt> </dl>                      | Creates a rectangle in which other controls can be grouped. Any text associated with this style is displayed in the rectangle's upper left corner.<br/>                                                                                                                                                                                                                                              |
| <span id="BS_ICON"></span><span id="bs_icon"></span><dl> <dt>**BS\_ICON**</dt> </dl>                                  | Specifies that the button displays an icon. See the Remarks section for its interaction with BS\_BITMAP.<br/>                                                                                                                                                                                                                                                                                        |
| <span id="BS_FLAT"></span><span id="bs_flat"></span><dl> <dt>**BS\_FLAT**</dt> </dl>                                  | Specifies that the button is two-dimensional; it does not use the default shading to create a 3-D image. <br/>                                                                                                                                                                                                                                                                                       |
| <span id="BS_LEFT"></span><span id="bs_left"></span><dl> <dt>**BS\_LEFT**</dt> </dl>                                  | Left-justifies the text in the button rectangle. However, if the button is a check box or radio button that does not have the BS\_RIGHTBUTTON style, the text is left justified on the right side of the check box or radio button.<br/>                                                                                                                                                             |
| <span id="BS_LEFTTEXT"></span><span id="bs_lefttext"></span><dl> <dt>**BS\_LEFTTEXT**</dt> </dl>                      | Places text on the left side of the radio button or check box when combined with a radio button or check box style. Same as the BS\_RIGHTBUTTON style.<br/>                                                                                                                                                                                                                                          |
| <span id="BS_MULTILINE"></span><span id="bs_multiline"></span><dl> <dt>**BS\_MULTILINE**</dt> </dl>                   | Wraps the button text to multiple lines if the text string is too long to fit on a single line in the button rectangle.<br/>                                                                                                                                                                                                                                                                         |
| <span id="BS_NOTIFY"></span><span id="bs_notify"></span><dl> <dt>**BS\_NOTIFY**</dt> </dl>                            | Enables a button to send [BN\_KILLFOCUS](bn-killfocus.md) and [BN\_SETFOCUS](bn-setfocus.md) notification codes to its parent window. <br/> Note that buttons send the [BN\_CLICKED](bn-clicked.md) notification code regardless of whether it has this style. To get [BN\_DBLCLK](bn-dblclk.md) notification codes, the button must have the BS\_RADIOBUTTON or BS\_OWNERDRAW style.<br/> |
| <span id="BS_OWNERDRAW"></span><span id="bs_ownerdraw"></span><dl> <dt>**BS\_OWNERDRAW**</dt> </dl>                   | Creates an owner-drawn button. The owner window receives a [**WM\_DRAWITEM**](wm-drawitem.md) message when a visual aspect of the button has changed. Do not combine the BS\_OWNERDRAW style with any other button styles.<br/>                                                                                                                                                                     |
| <span id="BS_PUSHBUTTON"></span><span id="bs_pushbutton"></span><dl> <dt>**BS\_PUSHBUTTON**</dt> </dl>                | Creates a push button that posts a [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message to the owner window when the user selects the button.<br/>                                                                                                                                                                                                                                                           |
| <span id="BS_PUSHLIKE"></span><span id="bs_pushlike"></span><dl> <dt>**BS\_PUSHLIKE**</dt> </dl>                      | Makes a button (such as a check box, three-state check box, or radio button) look and act like a push button. The button looks raised when it isn't pushed or checked, and sunken when it is pushed or checked.<br/>                                                                                                                                                                                 |
| <span id="BS_RADIOBUTTON"></span><span id="bs_radiobutton"></span><dl> <dt>**BS\_RADIOBUTTON**</dt> </dl>             | Creates a small circle with text. By default, the text is displayed to the right of the circle. To display the text to the left of the circle, combine this flag with the BS\_LEFTTEXT style (or with the equivalent BS\_RIGHTBUTTON style). Use radio buttons for groups of related, but mutually exclusive choices.<br/>                                                                           |
| <span id="BS_RIGHT"></span><span id="bs_right"></span><dl> <dt>**BS\_RIGHT**</dt> </dl>                               | Right-justifies text in the button rectangle. However, if the button is a check box or radio button that does not have the BS\_RIGHTBUTTON style, the text is right justified on the right side of the check box or radio button.<br/>                                                                                                                                                               |
| <span id="BS_RIGHTBUTTON"></span><span id="bs_rightbutton"></span><dl> <dt>**BS\_RIGHTBUTTON**</dt> </dl>             | Positions a radio button's circle or a check box's square on the right side of the button rectangle. Same as the BS\_LEFTTEXT style.<br/>                                                                                                                                                                                                                                                            |
| <span id="BS_SPLITBUTTON"></span><span id="bs_splitbutton"></span><dl> <dt>**BS\_SPLITBUTTON**</dt> </dl>             | Creates a split button. A split button has a drop down arrow.<br/>                                                                                                                                                                                                                                                                                                                                   |
| <span id="BS_TEXT"></span><span id="bs_text"></span><dl> <dt>**BS\_TEXT**</dt> </dl>                                  | Specifies that the button displays text.<br/>                                                                                                                                                                                                                                                                                                                                                        |
| <span id="BS_TOP"></span><span id="bs_top"></span><dl> <dt>**BS\_TOP**</dt> </dl>                                     | Places text at the top of the button rectangle.<br/>                                                                                                                                                                                                                                                                                                                                                 |
| <span id="BS_TYPEMASK"></span><span id="bs_typemask"></span><dl> <dt>**BS\_TYPEMASK**</dt> </dl>                      | Do not use this style. A composite style bit that results from using the OR operator on BS\_\* style bits. It can be used to mask out valid BS\_\* bits from a given bitmask. Note that this is out of date and does not correctly include all valid styles. Thus, you should not use this style.<br/>                                                                                               |
| <span id="BS_USERBUTTON"></span><span id="bs_userbutton"></span><dl> <dt>**BS\_USERBUTTON**</dt> </dl>                | Obsolete, but provided for compatibility with 16-bit versions of Windows. Applications should use BS\_OWNERDRAW instead.<br/>                                                                                                                                                                                                                                                                        |
| <span id="BS_VCENTER"></span><span id="bs_vcenter"></span><dl> <dt>**BS\_VCENTER**</dt> </dl>                         | Places text in the middle (vertically) of the button rectangle.<br/>                                                                                                                                                                                                                                                                                                                                 |



## Remarks

For illustrations of the principal button styles such as BS\_CHECKBOX and BS\_GROUPBOX, see [Button Types](button-types-and-styles.md).

The appearance of text or an icon or both on a button control depends on the BS\_ICON and BS\_BITMAP styles, and whether the [**BM\_SETIMAGE**](bm-setimage.md) message is sent. The possible results are as follows.



| BS\_ICON or BS\_BITMAP set? | BM\_SETIMAGE called? | Result              |
|-----------------------------|----------------------|---------------------|
| Yes                         | Yes                  | Show icon only.     |
| No                          | Yes                  | Show icon and text. |
| Yes                         | No                   | Show text only.     |
| No                          | No                   | Show text only      |



 

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h</dt> </dl> |



 

