---
title: Button (Windows Controls)
description: This section contains information about the programming elements used with button controls. A button is a control the user can click to provide input to an application.
ms.assetid: 'vs|controls|~\controls\buttons\buttons.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Button (Windows Controls)

This section contains information about the programming elements used with button controls. A *button* is a control the user can click to provide input to an application.

### Overviews



| Topic                                       | Contents                                                                                                           |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| [Button Messages](button-messages.md)      | This topic discusses messages that are used with buttons.<br/>                                               |
| [Button States](button-states.md)          | This section discusses how selecting a button changes its state and how the application should respond.<br/> |
| [Button Types](button-types-and-styles.md) | This topic discusses the different kinds of buttons.<br/>                                                    |
| [Using Buttons](using-buttons.md)          | This section explains how to perform certains tasks associated with buttons.<br/>                            |



 

### Functions



| Topic                                            | Contents                                                                                                                                                                                                  |
|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CheckDlgButton**](/windows/desktop/api/Winuser/nf-winuser-checkdlgbutton)         | Changes the check state of a button control.<br/>                                                                                                                                                   |
| [**CheckRadioButton**](/windows/desktop/api/Winuser/nf-winuser-checkradiobutton)     | Adds a check mark to (checks) a specified radio button in a group and removes a check mark from (clears) all other radio buttons in the group. <br/>                                                |
| [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) | The [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) function determines whether a button control is checked or whether a three-state button control is checked, unchecked, or indeterminate. <br/> |



 

### Macros



| Topic                                                                         | Contents                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Button\_Enable**](/windows/desktop/api/Windowsx/nf-windowsx-button_enable)                                       | Enables or disables a button.<br/>                                                                                                                                                                                                          |
| [**Button\_GetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_getcheck)                                   | Gets the check state of a radio button or check box. You can use this macro or send the [**BM\_GETCHECK**](bm-getcheck.md) message explicitly. <br/>                                                                                       |
| [**Button\_GetIdealSize**](/windows/desktop/api/Commctrl/nf-commctrl-button_getidealsize)                           | Gets the size of the button that best fits the text and image, if an image list is present. You can use this macro or send the [**BCM\_GETIDEALSIZE**](bcm-getidealsize.md) message explicitly. <br/>                                      |
| [**Button\_GetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-button_getimagelist)                           | Gets the [**BUTTON\_IMAGELIST**](/windows/desktop/api/Commctrl/ns-commctrl-button_imagelist) structure that describes the image list that is set for a button control. You can use this macro or send the [**BCM\_GETIMAGELIST**](bcm-getimagelist.md) message explicitly. <br/> |
| [**Button\_GetNote**](/windows/desktop/api/Commctrl/nf-commctrl-button_getnote)                                     | Gets the text of the note associated with a command link button. You can use this macro or send the [**BCM\_GETNOTE**](bcm-getnote.md) message explicitly.<br/>                                                                            |
| [**Button\_GetNoteLength**](/windows/desktop/api/Commctrl/nf-commctrl-button_getnotelength)                         | Gets the length of the note text that may be displayed in the description for a command link. Use this macro or send the [**BCM\_GETNOTELENGTH**](bcm-getnotelength.md) message explicitly.<br/>                                           |
| [**Button\_GetSplitInfo**](/windows/desktop/api/Commctrl/nf-commctrl-button_getsplitinfo)                           | Gets information for a specified split button control. Use this macro or send the [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md) message explicitly.<br/>                                                                                    |
| [**Button\_GetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_getstate)                                   | Gets the check state of a radio button or check box. You can use this macro or send the [**BM\_GETSTATE**](bm-getstate.md) message explicitly. <br/>                                                                                       |
| [**Button\_GetText**](/windows/desktop/api/Windowsx/nf-windowsx-button_gettext)                                     | Gets the text of a button.<br/>                                                                                                                                                                                                             |
| [**Button\_GetTextLength**](/windows/desktop/api/Windowsx/nf-windowsx-button_gettextlength)                         | Gets the number of characters in the text of a button.<br/>                                                                                                                                                                                 |
| [**Button\_GetTextMargin**](/windows/desktop/api/Commctrl/nf-commctrl-button_gettextmargin)                         | Gets the margins used to draw text in a button control. You can use this macro or send the [**BCM\_GETTEXTMARGIN**](bcm-gettextmargin.md) message explicitly. <br/>                                                                        |
| [**Button\_SetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_setcheck)                                   | Sets the check state of a radio button or check box. You can use this macro or send the [**BM\_SETCHECK**](bm-setcheck.md) message explicitly. <br/>                                                                                       |
| [**Button\_SetDropDownState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setdropdownstate)                   | Sets the drop down state for a specified button with style of [**BS\_SPLITBUTTON**](button-styles.md). Use this macro or send the [**BCM\_SETDROPDOWNSTATE**](bcm-setdropdownstate.md) message explicitly. <br/>           |
| [**Button\_SetElevationRequiredState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setelevationrequiredstate) | Sets the elevation required state for a specified button or command link to display an elevated icon. Use this macro or send the [**BCM\_SETSHIELD**](bcm-setshield.md) message explicitly. <br/>                                          |
| [**Button\_SetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-button_setimagelist)                           | Assigns an image list to a button control. You can use this macro or send the [**BCM\_SETIMAGELIST**](bcm-setimagelist.md) message explicitly. <br/>                                                                                       |
| [**Button\_SetNote**](/windows/desktop/api/Commctrl/nf-commctrl-button_setnote)                                     | Sets the text of the note associated with a specified command link button. You can use this macro or send the [**BCM\_SETNOTE**](bcm-setnote.md) message explicitly.<br/>                                                                  |
| [**Button\_SetSplitInfo**](/windows/desktop/api/Commctrl/nf-commctrl-button_setsplitinfo)                           | Sets information for a specified split button control. Use this macro or send the [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md) message explicitly.<br/>                                                                                    |
| [**Button\_SetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_setstate)                                   | Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can use this macro or send the [**BM\_SETSTATE**](bm-setstate.md) message explicitly. <br/>        |
| [**Button\_SetStyle**](/windows/desktop/api/Windowsx/nf-windowsx-button_setstyle)                                   | Sets the style of a button. You can use this macro or send the [**BM\_SETSTYLE**](bm-setstyle.md) message explicitly. <br/>                                                                                                                |
| [**Button\_SetText**](/windows/desktop/api/Windowsx/nf-windowsx-button_settext)                                     | Sets the text of a button.<br/>                                                                                                                                                                                                             |
| [**Button\_SetTextMargin**](/windows/desktop/api/Commctrl/nf-commctrl-button_settextmargin)                         | Sets the margins for drawing text in a button control. You can use this macro or send the [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md) message explicitly. <br/>                                                                         |



 

### Messages



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BCM\_GETIDEALSIZE**](bcm-getidealsize.md)         | Gets the size of the button that best fits its text and image, if an image list is present. You can send this message explicitly or use the [**Button\_GetIdealSize**](/windows/desktop/api/Commctrl/nf-commctrl-button_getidealsize) macro.<br/>                                                                                   |
| [**BCM\_GETIMAGELIST**](bcm-getimagelist.md)         | Gets the [**BUTTON\_IMAGELIST**](/windows/desktop/api/Commctrl/ns-commctrl-button_imagelist) structure that describes the image list assigned to a button control. You can send this message explicitly or use the [**Button\_GetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-button_getimagelist) macro.<br/>                                                  |
| [**BCM\_GETNOTE**](bcm-getnote.md)                   | Gets the text of the note associated with a command link button. You can send this message explicitly or use the [**Button\_GetNote**](/windows/desktop/api/Commctrl/nf-commctrl-button_getnote) macro.<br/>                                                                                                                        |
| [**BCM\_GETNOTELENGTH**](bcm-getnotelength.md)       | Gets the length of the note text that may be displayed in the description for a command link button. Send this message explicitly or by using the [**Button\_GetNoteLength**](/windows/desktop/api/Commctrl/nf-commctrl-button_getnotelength) macro.<br/>                                                                           |
| [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md)         | Gets information for a split button control. Send this message explicitly or by using the [**Button\_GetSplitInfo**](/windows/desktop/api/Commctrl/nf-commctrl-button_getsplitinfo) macro. <br/>                                                                                                                                    |
| [**BCM\_GETTEXTMARGIN**](bcm-gettextmargin.md)       | Gets the margins used to draw text in a button control. You can send this message explicitly or use the [**Button\_GetTextMargin**](/windows/desktop/api/Commctrl/nf-commctrl-button_gettextmargin) macro.<br/>                                                                                                                     |
| [**BCM\_SETDROPDOWNSTATE**](bcm-setdropdownstate.md) | Sets the drop down state for a button with style [**TBSTYLE\_DROPDOWN**](toolbar-control-and-button-styles.md). Send this message explicitly or by using the [**Button\_SetDropDownState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setdropdownstate) macro.<br/>                                        |
| [**BCM\_SETIMAGELIST**](bcm-setimagelist.md)         | Assigns an image list to a button control. You can send this message explicitly or use the [**Button\_SetImageList**](/windows/desktop/api/Commctrl/nf-commctrl-button_setimagelist) macro.<br/>                                                                                                                                    |
| [**BCM\_SETNOTE**](bcm-setnote.md)                   | Sets the text of the note associated with a command link button. You can send this message explicitly or use the [**Button\_SetNote**](/windows/desktop/api/Commctrl/nf-commctrl-button_setnote) macro.<br/>                                                                                                                        |
| [**BCM\_SETSHIELD**](bcm-setshield.md)               | Sets the elevation required state for a specified button or command link to display an elevated icon. Send this message explicitly or by using the [**Button\_SetElevationRequiredState**](/windows/desktop/api/Commctrl/nf-commctrl-button_setelevationrequiredstate) macro.<br/>                                                  |
| [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md)         | Sets information for a split button control. Send this message explicitly or by using the [**Button\_SetSplitInfo**](/windows/desktop/api/Commctrl/nf-commctrl-button_setsplitinfo) macro.<br/>                                                                                                                                     |
| [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md)       | The [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md) message sets the margins for drawing text in a button control. <br/>                                                                                                                                                                      |
| [**BM\_CLICK**](bm-click.md)                         | Simulates the user clicking a button. This message causes the button to receive the [**WM\_LBUTTONDOWN**](/windows/desktop/inputdev/wm-lbuttondown) and [**WM\_LBUTTONUP**](/windows/desktop/inputdev/wm-lbuttonup) messages, and the button's parent window to receive a [BN\_CLICKED](bn-clicked.md) notification code.<br/> |
| [**BM\_GETCHECK**](bm-getcheck.md)                   | Gets the check state of a radio button or check box. You can send this message explicitly or use the [**Button\_GetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_getcheck) macro.<br/>                                                                                                                                  |
| [**BM\_GETIMAGE**](bm-getimage.md)                   | Retrieves a handle to the image (icon or bitmap) associated with the button.<br/>                                                                                                                                                                                                             |
| [**BM\_GETSTATE**](bm-getstate.md)                   | Retrieves the state of a button or check box. You can send this message explicitly or use the [**Button\_GetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_getstate) macro.<br/>                                                                                                                                         |
| [**BM\_SETCHECK**](bm-setcheck.md)                   | Sets the check state of a radio button or check box. You can send this message explicitly or by using the [**Button\_SetCheck**](/windows/desktop/api/Windowsx/nf-windowsx-button_setcheck) macro.<br/>                                                                                                                             |
| [**BM\_SETDONTCLICK**](bm-setdontclick.md)           | Sets a flag on a radio button that controls the generation of [BN\_CLICKED](bn-clicked.md) messages when the button receives focus.<br/>                                                                                                                                                     |
| [**BM\_SETIMAGE**](bm-setimage.md)                   | Associates a new image (icon or bitmap) with the button.<br/>                                                                                                                                                                                                                                 |
| [**BM\_SETSTATE**](bm-setstate.md)                   | Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can send this message explicitly or use the [**Button\_SetState**](/windows/desktop/api/Windowsx/nf-windowsx-button_setstate) macro.<br/>                                                   |
| [**BM\_SETSTYLE**](bm-setstyle.md)                   | Sets the style of a button. You can send this message explicitly or use the [**Button\_SetStyle**](/windows/desktop/api/Windowsx/nf-windowsx-button_setstyle) macro.<br/>                                                                                                                                                           |



 

### Notifications



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Contents</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="bcn-dropdown.md">BCN_DROPDOWN</a></td>
<td>Sent when the user clicks a drop down arrow on a button. The parent window of the control receives this notification code in the form of a <a href="wm-notify.md"><strong>WM_NOTIFY</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="bcn-hotitemchange.md">BCN_HOTITEMCHANGE</a></td>
<td>Notifies the button control owner that the mouse is entering or leaving the client area of the button control. The button control sends this notification code in the form of a <a href="wm-notify.md"><strong>WM_NOTIFY</strong></a> message.<br/></td>
</tr>
<tr class="odd">
<td><a href="bn-clicked.md">BN_CLICKED</a></td>
<td>Sent when the user clicks a button. <br/> The parent window of the button receives the <a href="bn-clicked.md">BN_CLICKED</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message. <br/></td>
</tr>
<tr class="even">
<td><a href="bn-dblclk.md">BN_DBLCLK</a></td>
<td>Sent when the user double-clicks a button. This notification code is sent automatically for <a href="button-styles.md"><strong>BS_USERBUTTON</strong></a>, <a href="button-styles.md"><strong>BS_RADIOBUTTON</strong></a>, and <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> buttons. Other button types send <a href="bn-dblclk.md">BN_DBLCLK</a> only if they have the <a href="button-styles.md"><strong>BS_NOTIFY</strong></a> style.<br/> The parent window of the button receives the <a href="bn-dblclk.md">BN_DBLCLK</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message. <br/></td>
</tr>
<tr class="odd">
<td><a href="bn-disable.md">BN_DISABLE</a></td>
<td>Sent when a button is disabled.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-disable.md">BN_DISABLE</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="bn-doubleclicked.md">BN_DOUBLECLICKED</a></td>
<td>Sent when the user double-clicks a button. This notification code is sent automatically for <a href="button-styles.md"><strong>BS_USERBUTTON</strong></a>, <a href="button-styles.md"><strong>BS_RADIOBUTTON</strong></a>, and <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> buttons. Other button types send <a href="bn-doubleclicked.md">BN_DOUBLECLICKED</a> only if they have the <a href="button-styles.md"><strong>BS_NOTIFY</strong></a> style.<br/> The parent window of the button receives the <a href="bn-doubleclicked.md">BN_DOUBLECLICKED</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message. <br/></td>
</tr>
<tr class="odd">
<td><a href="bn-hilite.md">BN_HILITE</a></td>
<td>Sent when the user selects a button.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-hilite.md">BN_HILITE</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="bn-killfocus.md">BN_KILLFOCUS</a></td>
<td>Sent when a button loses the keyboard focus. The button must have the <a href="button-styles.md"><strong>BS_NOTIFY</strong></a> style to send this notification code. <br/> The parent window of the button receives the <a href="bn-killfocus.md">BN_KILLFOCUS</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message. <br/></td>
</tr>
<tr class="odd">
<td><a href="bn-paint.md">BN_PAINT</a></td>
<td>Sent when a button should be painted.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-paint.md">BN_PAINT</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message. <br/></td>
</tr>
<tr class="even">
<td><a href="bn-pushed.md">BN_PUSHED</a></td>
<td>Sent when the push state of a button is set to pushed.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-pushed.md">BN_PUSHED</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="odd">
<td><a href="bn-setfocus.md">BN_SETFOCUS</a></td>
<td>Sent when a button receives the keyboard focus. The button must have the <a href="button-styles.md"><strong>BS_NOTIFY</strong></a> style to send this notification code. <br/> The parent window of the button receives the <a href="bn-setfocus.md">BN_SETFOCUS</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="bn-unhilite.md">BN_UNHILITE</a></td>
<td>Sent when the highlight should be removed from a button.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-unhilite.md">BN_UNHILITE</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="odd">
<td><a href="bn-unpushed.md">BN_UNPUSHED</a></td>
<td>Sent when the push state of a button is set to unpushed.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button style and the <a href="/windows/win32/api/winuser/ns-winuser-drawitemstruct"><strong>DRAWITEMSTRUCT</strong></a> structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the <a href="bn-unpushed.md">BN_UNPUSHED</a> notification code through the <a href="/windows/desktop/menurc/wm-command"><strong>WM_COMMAND</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="nm-customdraw-button.md">NM_CUSTOMDRAW (button)</a></td>
<td>Notifies the parent window of a button control about custom draw operations on the button. <br/> The button control sends this notification code in the form of a <a href="wm-notify.md"><strong>WM_NOTIFY</strong></a> message.<br/></td>
</tr>
<tr class="odd">
<td><a href="wm-ctlcolorbtn.md"><strong>WM_CTLCOLORBTN</strong></a></td>
<td>The <a href="wm-ctlcolorbtn.md"><strong>WM_CTLCOLORBTN</strong></a> message is sent to the parent window of a button before drawing the button. The parent window can change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing this message. <br/></td>
</tr>
</tbody>
</table>



 

### Structures



| Topic                                         | Contents                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BUTTON\_IMAGELIST**](/windows/desktop/api/Commctrl/ns-commctrl-button_imagelist) | Contains information about an image list that is used with a button control.<br/>                                                                                                                                                                                                                                 |
| [**BUTTON\_SPLITINFO**](/windows/win32/api/commctrl/ns-commctrl-button_splitinfo) | Contains information that defines a split button ([**BS\_SPLITBUTTON**](button-styles.md) and [**BS\_DEFSPLITBUTTON**](button-styles.md) styles). Used with the [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md) and [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md) messages.<br/> |
| [**NMBCDROPDOWN**](/windows/win32/api/commctrl/ns-commctrl-nmbcdropdown)          | Contains information about a [BCN\_DROPDOWN](bcn-dropdown.md) notification.<br/>                                                                                                                                                                                                                                 |
| [**NMBCHOTITEM**](/windows/win32/api/commctrl/ns-commctrl-nmbchotitem)            | Contains information about the movement of the mouse over a button control.<br/>                                                                                                                                                                                                                                  |



 

### Constants



| Topic                              | Contents                                                                                                                                                                                                                                                            |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Button Styles](button-styles.md) | Specifies a combination of button styles. If you create a button using the BUTTON class with the [**CreateWindow**](/windows/desktop/api/winuser/nf-winuser-createwindowa) or [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, you can specify any of the button styles listed below.<br/> |



 

