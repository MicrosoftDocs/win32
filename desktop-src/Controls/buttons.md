---
title: Button
description: This section contains information about the programming elements used with button controls. A button is a control the user can click to provide input to an application.
ms.assetid: '849FFD6B-8CB6-44FA-92EB-35BFA537FB75'
---

# Button

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
| [**CheckDlgButton**](checkdlgbutton.md)         | Changes the check state of a button control.<br/>                                                                                                                                                   |
| [**CheckRadioButton**](checkradiobutton.md)     | Adds a check mark to (checks) a specified radio button in a group and removes a check mark from (clears) all other radio buttons in the group. <br/>                                                |
| [**IsDlgButtonChecked**](isdlgbuttonchecked.md) | The [**IsDlgButtonChecked**](isdlgbuttonchecked.md) function determines whether a button control is checked or whether a three-state button control is checked, unchecked, or indeterminate. <br/> |



 

### Macros



| Topic                                                                         | Contents                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Button\_Enable**](button-enable.md)                                       | Enables or disables a button.<br/>                                                                                                                                                                                                          |
| [**Button\_GetCheck**](button-getcheck.md)                                   | Gets the check state of a radio button or check box. You can use this macro or send the [**BM\_GETCHECK**](bm-getcheck.md) message explicitly. <br/>                                                                                       |
| [**Button\_GetIdealSize**](button-getidealsize.md)                           | Gets the size of the button that best fits the text and image, if an image list is present. You can use this macro or send the [**BCM\_GETIDEALSIZE**](bcm-getidealsize.md) message explicitly. <br/>                                      |
| [**Button\_GetImageList**](button-getimagelist.md)                           | Gets the [**BUTTON\_IMAGELIST**](button-imagelist.md) structure that describes the image list that is set for a button control. You can use this macro or send the [**BCM\_GETIMAGELIST**](bcm-getimagelist.md) message explicitly. <br/> |
| [**Button\_GetNote**](button-getnote.md)                                     | Gets the text of the note associated with a command link button. You can use this macro or send the [**BCM\_GETNOTE**](bcm-getnote.md) message explicitly.<br/>                                                                            |
| [**Button\_GetNoteLength**](button-getnotelength.md)                         | Gets the length of the note text that may be displayed in the description for a command link. Use this macro or send the [**BCM\_GETNOTELENGTH**](bcm-getnotelength.md) message explicitly.<br/>                                           |
| [**Button\_GetSplitInfo**](button-getsplitinfo.md)                           | Gets information for a specified split button control. Use this macro or send the [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md) message explicitly.<br/>                                                                                    |
| [**Button\_GetState**](button-getstate.md)                                   | Gets the check state of a radio button or check box. You can use this macro or send the [**BM\_GETSTATE**](bm-getstate.md) message explicitly. <br/>                                                                                       |
| [**Button\_GetText**](button-gettext.md)                                     | Gets the text of a button.<br/>                                                                                                                                                                                                             |
| [**Button\_GetTextLength**](button-gettextlength.md)                         | Gets the number of characters in the text of a button.<br/>                                                                                                                                                                                 |
| [**Button\_GetTextMargin**](button-gettextmargin.md)                         | Gets the margins used to draw text in a button control. You can use this macro or send the [**BCM\_GETTEXTMARGIN**](bcm-gettextmargin.md) message explicitly. <br/>                                                                        |
| [**Button\_SetCheck**](button-setcheck.md)                                   | Sets the check state of a radio button or check box. You can use this macro or send the [**BM\_SETCHECK**](bm-setcheck.md) message explicitly. <br/>                                                                                       |
| [**Button\_SetDropDownState**](button-setdropdownstate.md)                   | Sets the drop down state for a specified button with style of [**BS\_SPLITBUTTON**](button-styles.md#bs-splitbutton). Use this macro or send the [**BCM\_SETDROPDOWNSTATE**](bcm-setdropdownstate.md) message explicitly. <br/>           |
| [**Button\_SetElevationRequiredState**](button-setelevationrequiredstate.md) | Sets the elevation required state for a specified button or command link to display an elevated icon. Use this macro or send the [**BCM\_SETSHIELD**](bcm-setshield.md) message explicitly. <br/>                                          |
| [**Button\_SetImageList**](button-setimagelist.md)                           | Assigns an image list to a button control. You can use this macro or send the [**BCM\_SETIMAGELIST**](bcm-setimagelist.md) message explicitly. <br/>                                                                                       |
| [**Button\_SetNote**](button-setnote.md)                                     | Sets the text of the note associated with a specified command link button. You can use this macro or send the [**BCM\_SETNOTE**](bcm-setnote.md) message explicitly.<br/>                                                                  |
| [**Button\_SetSplitInfo**](button-setsplitinfo.md)                           | Sets information for a specified split button control. Use this macro or send the [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md) message explicitly.<br/>                                                                                    |
| [**Button\_SetState**](button-setstate.md)                                   | Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can use this macro or send the [**BM\_SETSTATE**](bm-setstate.md) message explicitly. <br/>        |
| [**Button\_SetStyle**](button-setstyle.md)                                   | Sets the style of a button. You can use this macro or send the [**BM\_SETSTYLE**](bm-setstyle.md) message explicitly. <br/>                                                                                                                |
| [**Button\_SetText**](button-settext.md)                                     | Sets the text of a button.<br/>                                                                                                                                                                                                             |
| [**Button\_SetTextMargin**](button-settextmargin.md)                         | Sets the margins for drawing text in a button control. You can use this macro or send the [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md) message explicitly. <br/>                                                                         |



 

### Messages



| Topic                                                 | Contents                                                                                                                                                                                                                                                                                            |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BCM\_GETIDEALSIZE**](bcm-getidealsize.md)         | Gets the size of the button that best fits its text and image, if an image list is present. You can send this message explicitly or use the [**Button\_GetIdealSize**](button-getidealsize.md) macro.<br/>                                                                                   |
| [**BCM\_GETIMAGELIST**](bcm-getimagelist.md)         | Gets the [**BUTTON\_IMAGELIST**](button-imagelist.md) structure that describes the image list assigned to a button control. You can send this message explicitly or use the [**Button\_GetImageList**](button-getimagelist.md) macro.<br/>                                                  |
| [**BCM\_GETNOTE**](bcm-getnote.md)                   | Gets the text of the note associated with a command link button. You can send this message explicitly or use the [**Button\_GetNote**](button-getnote.md) macro.<br/>                                                                                                                        |
| [**BCM\_GETNOTELENGTH**](bcm-getnotelength.md)       | Gets the length of the note text that may be displayed in the description for a command link button. Send this message explicitly or by using the [**Button\_GetNoteLength**](button-getnotelength.md) macro.<br/>                                                                           |
| [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md)         | Gets information for a split button control. Send this message explicitly or by using the [**Button\_GetSplitInfo**](button-getsplitinfo.md) macro. <br/>                                                                                                                                    |
| [**BCM\_GETTEXTMARGIN**](bcm-gettextmargin.md)       | Gets the margins used to draw text in a button control. You can send this message explicitly or use the [**Button\_GetTextMargin**](button-gettextmargin.md) macro.<br/>                                                                                                                     |
| [**BCM\_SETDROPDOWNSTATE**](bcm-setdropdownstate.md) | Sets the drop down state for a button with style [**TBSTYLE\_DROPDOWN**](toolbar-control-and-button-styles.md#tbstyle-dropdown). Send this message explicitly or by using the [**Button\_SetDropDownState**](button-setdropdownstate.md) macro.<br/>                                        |
| [**BCM\_SETIMAGELIST**](bcm-setimagelist.md)         | Assigns an image list to a button control. You can send this message explicitly or use the [**Button\_SetImageList**](button-setimagelist.md) macro.<br/>                                                                                                                                    |
| [**BCM\_SETNOTE**](bcm-setnote.md)                   | Sets the text of the note associated with a command link button. You can send this message explicitly or use the [**Button\_SetNote**](button-setnote.md) macro.<br/>                                                                                                                        |
| [**BCM\_SETSHIELD**](bcm-setshield.md)               | Sets the elevation required state for a specified button or command link to display an elevated icon. Send this message explicitly or by using the [**Button\_SetElevationRequiredState**](button-setelevationrequiredstate.md) macro.<br/>                                                  |
| [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md)         | Sets information for a split button control. Send this message explicitly or by using the [**Button\_SetSplitInfo**](button-setsplitinfo.md) macro.<br/>                                                                                                                                     |
| [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md)       | The [**BCM\_SETTEXTMARGIN**](bcm-settextmargin.md) message sets the margins for drawing text in a button control. <br/>                                                                                                                                                                      |
| [**BM\_CLICK**](bm-click.md)                         | Simulates the user clicking a button. This message causes the button to receive the [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) and [**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608) messages, and the button's parent window to receive a [BN\_CLICKED](bn-clicked.md) notification code.<br/> |
| [**BM\_GETCHECK**](bm-getcheck.md)                   | Gets the check state of a radio button or check box. You can send this message explicitly or use the [**Button\_GetCheck**](button-getcheck.md) macro.<br/>                                                                                                                                  |
| [**BM\_GETIMAGE**](bm-getimage.md)                   | Retrieves a handle to the image (icon or bitmap) associated with the button.<br/>                                                                                                                                                                                                             |
| [**BM\_GETSTATE**](bm-getstate.md)                   | Retrieves the state of a button or check box. You can send this message explicitly or use the [**Button\_GetState**](button-getstate.md) macro.<br/>                                                                                                                                         |
| [**BM\_SETCHECK**](bm-setcheck.md)                   | Sets the check state of a radio button or check box. You can send this message explicitly or by using the [**Button\_SetCheck**](button-setcheck.md) macro.<br/>                                                                                                                             |
| [**BM\_SETDONTCLICK**](bm-setdontclick.md)           | Sets a flag on a radio button that controls the generation of [BN\_CLICKED](bn-clicked.md) messages when the button receives focus.<br/>                                                                                                                                                     |
| [**BM\_SETIMAGE**](bm-setimage.md)                   | Associates a new image (icon or bitmap) with the button.<br/>                                                                                                                                                                                                                                 |
| [**BM\_SETSTATE**](bm-setstate.md)                   | Sets the highlight state of a button. The highlight state indicates whether the button is highlighted as if the user had pushed it. You can send this message explicitly or use the [**Button\_SetState**](button-setstate.md) macro.<br/>                                                   |
| [**BM\_SETSTYLE**](bm-setstyle.md)                   | Sets the style of a button. You can send this message explicitly or use the [**Button\_SetStyle**](button-setstyle.md) macro.<br/>                                                                                                                                                           |



 

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
<td>[BCN_DROPDOWN](bcn-dropdown.md)</td>
<td>Sent when the user clicks a drop down arrow on a button. The parent window of the control receives this notification code in the form of a [<strong>WM_NOTIFY</strong>](wm-notify.md) message.<br/></td>
</tr>
<tr class="even">
<td>[BCN_HOTITEMCHANGE](bcn-hotitemchange.md)</td>
<td>Notifies the button control owner that the mouse is entering or leaving the client area of the button control. The button control sends this notification code in the form of a [<strong>WM_NOTIFY</strong>](wm-notify.md) message.<br/></td>
</tr>
<tr class="odd">
<td>[BN_CLICKED](bn-clicked.md)</td>
<td>Sent when the user clicks a button. <br/> The parent window of the button receives the [BN_CLICKED](bn-clicked.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/></td>
</tr>
<tr class="even">
<td>[BN_DBLCLK](bn-dblclk.md)</td>
<td>Sent when the user double-clicks a button. This notification code is sent automatically for [<strong>BS_USERBUTTON</strong>](button-styles.md#bs-userbutton), [<strong>BS_RADIOBUTTON</strong>](button-styles.md#bs-radiobutton), and [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) buttons. Other button types send [BN_DBLCLK](bn-dblclk.md) only if they have the [<strong>BS_NOTIFY</strong>](button-styles.md#bs-notify) style.<br/> The parent window of the button receives the [BN_DBLCLK](bn-dblclk.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/></td>
</tr>
<tr class="odd">
<td>[BN_DISABLE](bn-disable.md)</td>
<td>Sent when a button is disabled.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_DISABLE](bn-disable.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="even">
<td>[BN_DOUBLECLICKED](bn-doubleclicked.md)</td>
<td>Sent when the user double-clicks a button. This notification code is sent automatically for [<strong>BS_USERBUTTON</strong>](button-styles.md#bs-userbutton), [<strong>BS_RADIOBUTTON</strong>](button-styles.md#bs-radiobutton), and [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) buttons. Other button types send [BN_DOUBLECLICKED](bn-doubleclicked.md) only if they have the [<strong>BS_NOTIFY</strong>](button-styles.md#bs-notify) style.<br/> The parent window of the button receives the [BN_DOUBLECLICKED](bn-doubleclicked.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/></td>
</tr>
<tr class="odd">
<td>[BN_HILITE](bn-hilite.md)</td>
<td>Sent when the user selects a button.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_HILITE](bn-hilite.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="even">
<td>[BN_KILLFOCUS](bn-killfocus.md)</td>
<td>Sent when a button loses the keyboard focus. The button must have the [<strong>BS_NOTIFY</strong>](button-styles.md#bs-notify) style to send this notification code. <br/> The parent window of the button receives the [BN_KILLFOCUS](bn-killfocus.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/></td>
</tr>
<tr class="odd">
<td>[BN_PAINT](bn-paint.md)</td>
<td>Sent when a button should be painted.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_PAINT](bn-paint.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message. <br/></td>
</tr>
<tr class="even">
<td>[BN_PUSHED](bn-pushed.md)</td>
<td>Sent when the push state of a button is set to pushed.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_PUSHED](bn-pushed.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="odd">
<td>[BN_SETFOCUS](bn-setfocus.md)</td>
<td>Sent when a button receives the keyboard focus. The button must have the [<strong>BS_NOTIFY</strong>](button-styles.md#bs-notify) style to send this notification code. <br/> The parent window of the button receives the [BN_SETFOCUS](bn-setfocus.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="even">
<td>[BN_UNHILITE](bn-unhilite.md)</td>
<td>Sent when the highlight should be removed from a button.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_UNHILITE](bn-unhilite.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="odd">
<td>[BN_UNPUSHED](bn-unpushed.md)</td>
<td>Sent when the push state of a button is set to unpushed.
<blockquote>
[!Note]<br />
This notification code is provided only for compatibility with 16-bit versions of Windows earlier than version 3.0. Applications should use the [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button style and the [<strong>DRAWITEMSTRUCT</strong>](drawitemstruct.md) structure for this task.
</blockquote>
<br/> <br/> The parent window of the button receives the [BN_UNPUSHED](bn-unpushed.md) notification code through the [<strong>WM_COMMAND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms647591) message.<br/></td>
</tr>
<tr class="even">
<td>[NM_CUSTOMDRAW (button)](nm-customdraw-button.md)</td>
<td>Notifies the parent window of a button control about custom draw operations on the button. <br/> The button control sends this notification code in the form of a [<strong>WM_NOTIFY</strong>](wm-notify.md) message.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WM_CTLCOLORBTN</strong>](wm-ctlcolorbtn.md)</td>
<td>The [<strong>WM_CTLCOLORBTN</strong>](wm-ctlcolorbtn.md) message is sent to the parent window of a button before drawing the button. The parent window can change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing this message. <br/></td>
</tr>
</tbody>
</table>



 

### Structures



| Topic                                         | Contents                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BUTTON\_IMAGELIST**](button-imagelist.md) | Contains information about an image list that is used with a button control.<br/>                                                                                                                                                                                                                                 |
| [**BUTTON\_SPLITINFO**](button-splitinfo.md) | Contains information that defines a split button ([**BS\_SPLITBUTTON**](button-styles.md#bs-splitbutton) and [**BS\_DEFSPLITBUTTON**](button-styles.md#bs-defsplitbutton) styles). Used with the [**BCM\_GETSPLITINFO**](bcm-getsplitinfo.md) and [**BCM\_SETSPLITINFO**](bcm-setsplitinfo.md) messages.<br/> |
| [**NMBCDROPDOWN**](nmbcdropdown.md)          | Contains information about a [BCN\_DROPDOWN](bcn-dropdown.md) notification.<br/>                                                                                                                                                                                                                                 |
| [**NMBCHOTITEM**](nmbchotitem.md)            | Contains information about the movement of the mouse over a button control.<br/>                                                                                                                                                                                                                                  |



 

### Constants



| Topic                              | Contents                                                                                                                                                                                                                                                            |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Button Styles](button-styles.md) | Specifies a combination of button styles. If you create a button using the BUTTON class with the [**CreateWindow**](https://msdn.microsoft.com/library/windows/desktop/ms632679) or [**CreateWindowEx**](https://msdn.microsoft.com/library/windows/desktop/ms632680) function, you can specify any of the button styles listed below.<br/> |



 

 

 





