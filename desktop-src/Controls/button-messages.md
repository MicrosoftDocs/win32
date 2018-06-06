---
title: Button Messages
description: A button can send messages to its parent window, and a parent window can send messages to a button.
ms.assetid: 2d2358fb-b17d-48a9-8def-15ae8bad9162
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Button Messages

A button can send messages to its parent window, and a parent window can send messages to a button.

The following topics are discussed in this section.

-   [Sending Messages to Buttons](#sending-messages-to-buttons)
-   [Handling Messages from a Button](#handling-messages-from-a-button)
-   [Notification Messages from Buttons](#notification-messages-from-buttons)
-   [Button Color Messages](#button-color-messages)
-   [Button Default Message Processing](#button-default-message-processing)
-   [Related topics](#related-topics)

## Sending Messages to Buttons

A parent window can send messages to a button in an overlapped or child window by using the [**SendMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644950) function, or it can send messages to a button in a dialog box by using the [**SendDlgItemMessage**](https://msdn.microsoft.com/library/windows/desktop/ms645515), [**CheckDlgButton**](/windows/desktop/api/Winuser/nf-winuser-checkdlgbutton), [**CheckRadioButton**](/windows/desktop/api/Winuser/nf-winuser-checkradiobutton), and [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) functions.

An application can use the [**BM\_GETCHECK**](bm-getcheck.md) message to retrieve the check state of a check box or radio button. An application can also use the [**BM\_GETSTATE**](bm-getstate.md) message to retrieve the button's current states (the check state, push state, and focus state). To get information about a specific state, use a bitmask on the returned state value.

The [**BM\_SETCHECK**](bm-setcheck.md) message sets the check state of a check box or radio button; the message returns zero. The [**BM\_SETSTATE**](bm-setstate.md) message sets the push state of a button; this message also returns zero. The [**BM\_SETSTYLE**](bm-setstyle.md) message changes the style of a button. It is designed for changing button styles within a type (for example, changing a check box to an automatic check box). It is not designed for changing between types (for example, changing a check box to a radio button). An application should not change a button from one type to another.

A button of the [**BS\_BITMAP**](button-styles.md#bs-bitmap) or [**BS\_ICON**](button-styles.md#bs-icon) style displays a bitmap or icon instead of text. The [**BM\_SETIMAGE**](bm-setimage.md) message associates a handle to a bitmap or icon with a button. The [**BM\_GETIMAGE**](bm-getimage.md) message retrieves a handle to the bitmap or icon associated with a button.

An application can also use the [**DM\_GETDEFID**](https://msdn.microsoft.com/library/windows/desktop/ms645406) message to retrieve the identifier of the default push button control in a dialog box. An application can use the [**DM\_SETDEFID**](https://msdn.microsoft.com/library/windows/desktop/ms645413) message to set the default push button for a dialog box.

Calling the [**CheckDlgButton**](/windows/desktop/api/Winuser/nf-winuser-checkdlgbutton) or [**CheckRadioButton**](/windows/desktop/api/Winuser/nf-winuser-checkradiobutton) function is equivalent to sending a [**BM\_SETCHECK**](bm-setcheck.md) message. Calling the [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) function is equivalent to sending a [**BM\_GETCHECK**](bm-getcheck.md) message.

## Handling Messages from a Button

Notifications from a button are sent as either [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) or [**WM\_NOTIFY**](wm-notify.md) messages. Information about which message is used can be found on the reference page for each notification.

For more information on how to handle messages, see [Control Messages](control-messages.md). See also Button Messages.

## Notification Messages from Buttons

When the user clicks a button, its state changes, and the button sends notification codes, in the form of [**WM\_COMMAND**](https://msdn.microsoft.com/library/windows/desktop/ms647591) messages, to its parent window. For example, a push button control sends the [BN\_CLICKED](bn-clicked.md) notification code whenever the user chooses the button. In all cases (except for [BCN\_HOTITEMCHANGE](bcn-hotitemchange.md)), the low-order word of the *wParam* parameter contains the control identifier, the high-order word of *wParam* contains the notification code, and the *lParam* parameter contains the control window handle.

Both the message and the parent window's response depend on the type, style, and current state of the button. Following are the button notification codes an application should monitor and process.



| Notification code                                                        | Description                                            |
|--------------------------------------------------------------------------|--------------------------------------------------------|
| [BCN\_HOTITEMCHANGE](bcn-hotitemchange.md)                              | The mouse entered or left the client area of a button. |
| [BN\_CLICKED](bn-clicked.md)                                            | The user clicked a button.                             |
| [BN\_DBLCLK](bn-dblclk.md) or [BN\_DOUBLECLICKED](bn-doubleclicked.md) | The user double-clicked a button.                      |
| [BN\_DISABLE](bn-disable.md)                                            | A button is disabled.                                  |
| [BN\_PUSHED](bn-pushed.md) or [BN\_HILITE](bn-hilite.md)               | The user pushed a button.                              |
| [BN\_KILLFOCUS](bn-killfocus.md)                                        | The button lost the keyboard focus.                    |
| [BN\_PAINT](bn-paint.md)                                                | The button should be painted.                          |
| [BN\_SETFOCUS](bn-setfocus.md)                                          | The button gained the keyboard focus.                  |
| [BN\_UNPUSHED](bn-unpushed.md) or [BN\_UNHILITE](bn-unhilite.md)       | The button is no longer pushed.                        |



 

A button sends the [BN\_DISABLE](bn-disable.md), [BN\_PUSHED](bn-pushed.md), [BN\_KILLFOCUS](bn-killfocus.md), [BN\_PAINT](bn-paint.md), [BN\_SETFOCUS](bn-setfocus.md), and [BN\_UNPUSHED](bn-unpushed.md) notification codes only if it has the [**BS\_NOTIFY**](button-styles.md#bs-notify) style. [BN\_DBLCLK](bn-dblclk.md) notification codes are sent automatically for [**BS\_USERBUTTON**](button-styles.md#bs-userbutton), [**BS\_RADIOBUTTON**](button-styles.md#bs-radiobutton), and [**BS\_OWNERDRAW**](button-styles.md#bs-ownerdraw) buttons. Other button types send BN\_DBLCLK only if they have the **BS\_NOTIFY** style. All buttons send the [BN\_CLICKED](bn-clicked.md) notification code regardless of their button styles.

For automatic buttons, the system changes the push state and paints the button. In this case, the application typically processes only the [BN\_CLICKED](bn-clicked.md) and [BN\_DBLCLK](bn-dblclk.md) notification codes. For buttons that are not automatic, the application typically responds to the notification code by sending a message to change the state of the button. For information about sending messages to buttons, see [Sending Messages to Buttons](#sending-messages-to-buttons).

When the user selects an owner-drawn button, the button sends its parent window a [**WM\_DRAWITEM**](wm-drawitem.md) message containing the identifier of the control to be drawn and information about its dimensions and state.

## Button Color Messages

The system provides default color values for buttons. An application can retrieve the default values for these colors by calling the [**GetSysColor**](https://msdn.microsoft.com/library/windows/desktop/ms724371) function, or set the values by calling the [**SetSysColors**](https://msdn.microsoft.com/library/windows/desktop/ms724940) function. The following table shows the default button-color values.



| Value               | Element colored                                                                                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------|
| COLOR\_BTNFACE      | Button faces.                                                                                                              |
| COLOR\_BTNHIGHLIGHT | Highlight area (the top and left edges) of a button.                                                                       |
| COLOR\_BTNSHADOW    | Shadow area (the bottom and right edges) of a button.                                                                      |
| COLOR\_BTNTEXT      | Regular (nongrayed) text in buttons.                                                                                       |
| COLOR\_GRAYTEXT     | Disabled (gray) text in buttons. This color is set to 0 if the current display driver does not support a solid gray color. |
| COLOR\_WINDOW       | Window backgrounds.                                                                                                        |
| COLOR\_WINDOWFRAME  | Window frames.                                                                                                             |
| COLOR\_WINDOWTEXT   | Text in windows.                                                                                                           |



 

However, calling [**SetSysColors**](https://msdn.microsoft.com/library/windows/desktop/ms724940) affects all applications, so you should not call this function to customize buttons for your application.

The system sends a [**WM\_CTLCOLORBTN**](wm-ctlcolorbtn.md) message to a button's parent window before drawing a button. This message contains a handle to the button's device context and a handle to the child window. The parent window can use these handles to change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing the message.

## Button Default Message Processing

The window procedure for the predefined button control window class carries out default processing for all messages that the button control procedure does not process. When the button control procedure returns **FALSE** for any message, the predefined window procedure checks the messages and performs the default actions listed in the following table.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Message</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>BM_CLICK</strong>](bm-click.md)</td>
<td>Sends the button a [<strong>WM_LBUTTONDOWN</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645607) and a [<strong>WM_LBUTTONUP</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645608) message, and sends the parent window a [BN_CLICKED](bn-clicked.md) notification code.</td>
</tr>
<tr class="even">
<td>[<strong>BM_GETCHECK</strong>](bm-getcheck.md)</td>
<td>Returns the check state of the button.</td>
</tr>
<tr class="odd">
<td>[<strong>BM_GETIMAGE</strong>](bm-getimage.md)</td>
<td>Returns a handle to the bitmap or icon associated with the button or <strong>NULL</strong> if the button has no bitmap or icon.</td>
</tr>
<tr class="even">
<td>[<strong>BM_GETSTATE</strong>](bm-getstate.md)</td>
<td>Returns the current check state, push state, and focus state of the button.</td>
</tr>
<tr class="odd">
<td>[<strong>BM_SETCHECK</strong>](bm-setcheck.md)</td>
<td>Sets the check state for all styles of radio buttons and check boxes. If the <em>wParam</em> parameter is greater than zero for radio buttons, the button is given the [<strong>WS_TABSTOP</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632600#ws-tabstop) style.</td>
</tr>
<tr class="even">
<td>[<strong>BM_SETIMAGE</strong>](bm-setimage.md)</td>
<td>Associates the specified bitmap or icon handle with the button and returns a handle to the previous bitmap or icon.</td>
</tr>
<tr class="odd">
<td>[<strong>BM_SETSTATE</strong>](bm-setstate.md)</td>
<td>Sets the push state of the button. For owner-drawn buttons, a [<strong>WM_DRAWITEM</strong>](wm-drawitem.md) message is sent to the parent window if the state of the button has changed.</td>
</tr>
<tr class="even">
<td>[<strong>BM_SETSTYLE</strong>](bm-setstyle.md)</td>
<td>Sets the button style. If the low-order word of the <em>lParam</em> parameter is <strong>TRUE</strong>, the button is redrawn.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_CHAR</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646276)</td>
<td>Checks a check box or automatic check box when the user presses the plus (+) or equal (=) keys. Clears a check box or automatic check box when the user presses the minus (–) key.</td>
</tr>
<tr class="even">
<td>[<strong>WM_ENABLE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632621)</td>
<td>Paints the button.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_ERASEBKGND</strong>](https://msdn.microsoft.com/library/windows/desktop/ms648055)</td>
<td>Erases the background for owner-drawn buttons. The backgrounds of other buttons are erased as part of the [<strong>WM_PAINT</strong>](https://msdn.microsoft.com/library/windows/desktop/dd145213) and [<strong>WM_ENABLE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632621) processing.</td>
</tr>
<tr class="even">
<td>[<strong>WM_GETDLGCODE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645425)</td>
<td>Returns values that indicate the type of input processed by the default button procedure, as shown in the following table. 
<table>
<thead>
<tr class="header">
<th>Button style</th>
<th>Returns</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>BS_AUTOCHECKBOX</strong>](button-styles.md#bs-autocheckbox)</td>
<td>DLGC_WANTCHARS | DLGC_BUTTON</td>
</tr>
<tr class="even">
<td>[<strong>BS_AUTORADIOBUTTON</strong>](button-styles.md#bs-autoradiobutton)</td>
<td>DLGC_RADIOBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td>[<strong>BS_CHECKBOX</strong>](button-styles.md#bs-checkbox)</td>
<td>DLGC_WANTCHARS | DLGC_BUTTON</td>
</tr>
<tr class="even">
<td>[<strong>BS_DEFPUSHBUTTON</strong>](button-styles.md#bs-defpushbutton)</td>
<td>DLGC_DEFPUSHBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td>[<strong>BS_GROUPBOX</strong>](button-styles.md#bs-groupbox)</td>
<td>DLGC_STATIC</td>
</tr>
<tr class="even">
<td>[<strong>BS_PUSHBUTTON</strong>](button-styles.md#bs-pushbutton)</td>
<td>DLGC_UNDEFPUSHBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td>[<strong>BS_RADIOBUTTON</strong>](button-styles.md#bs-radiobutton)</td>
<td>DLGC_RADIOBUTTON | DLGC_BUTTON</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td>[<strong>WM_GETFONT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632624)</td>
<td>Returns a handle to the current font.</td>
</tr>
<tr class="even">
<td>[<strong>WM_KEYDOWN</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646280)</td>
<td>Pushes the button if the user presses the SPACEBAR.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_KEYUP</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646281)</td>
<td>Releases the mouse capture for all cases except the TAB key.</td>
</tr>
<tr class="even">
<td>[<strong>WM_KILLFOCUS</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646282)</td>
<td>Removes the focus rectangle from a button. For push buttons and default push buttons, the focus rectangle is invalidated. If the button has the mouse capture, the capture is released, the button is not clicked, and any push state is removed.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_LBUTTONDBLCLK</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645606)</td>
<td>Sends a [BN_DBLCLK](bn-dblclk.md) notification code to the parent window for radio buttons and owner-drawn buttons. For other buttons, a double-click is processed as a [<strong>WM_LBUTTONDOWN</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645607) message.</td>
</tr>
<tr class="even">
<td>[<strong>WM_LBUTTONDOWN</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645607)</td>
<td>Highlights the button if the position of the mouse cursor is within the button's client rectangle.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_LBUTTONUP</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645608)</td>
<td>Releases the mouse capture if the button had the mouse capture.</td>
</tr>
<tr class="even">
<td>[<strong>WM_MOUSEMOVE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645616)</td>
<td>Performs the same action as [<strong>WM_LBUTTONDOWN</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645607), if the button has the mouse capture. Otherwise, no action is performed.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_NCCREATE</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632635)</td>
<td>Turns any [<strong>BS_OWNERDRAW</strong>](button-styles.md#bs-ownerdraw) button into a [<strong>BS_PUSHBUTTON</strong>](button-styles.md#bs-pushbutton) button.</td>
</tr>
<tr class="even">
<td>[<strong>WM_NCHITTEST</strong>](https://msdn.microsoft.com/library/windows/desktop/ms645618)</td>
<td>Returns HTTRANSPARENT, if the button control is a group box.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_PAINT</strong>](https://msdn.microsoft.com/library/windows/desktop/dd145213)</td>
<td>Draws the button according to its style and current state.</td>
</tr>
<tr class="even">
<td>[<strong>WM_SETFOCUS</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646283)</td>
<td>Draws a focus rectangle on the button getting the focus. For radio buttons and automatic radio buttons, the parent window is sent a [BN_CLICKED](bn-clicked.md) notification code.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_SETFONT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632642)</td>
<td>Sets a new font and optionally updates the window.</td>
</tr>
<tr class="even">
<td>[<strong>WM_SETTEXT</strong>](https://msdn.microsoft.com/library/windows/desktop/ms632644)</td>
<td>Sets the text of the button. In the case of a group box, the message paints over the preexisting text before repainting the group box with the new text.</td>
</tr>
<tr class="odd">
<td>[<strong>WM_SYSKEYUP</strong>](https://msdn.microsoft.com/library/windows/desktop/ms646287)</td>
<td>Releases the mouse capture for all cases except the TAB key.</td>
</tr>
</tbody>
</table>



 

The predefined window procedure passes all other messages to the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function for default processing.

## Related topics

<dl> <dt>

[Control Messages](control-messages.md)
</dt> </dl>

 

 




