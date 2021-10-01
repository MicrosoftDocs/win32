---
title: Button Messages
description: A button can send messages to its parent window, and a parent window can send messages to a button.
ms.assetid: 2d2358fb-b17d-48a9-8def-15ae8bad9162
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

A parent window can send messages to a button in an overlapped or child window by using the [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) function, or it can send messages to a button in a dialog box by using the [**SendDlgItemMessage**](/windows/desktop/api/winuser/nf-winuser-senddlgitemmessagea), [**CheckDlgButton**](/windows/desktop/api/Winuser/nf-winuser-checkdlgbutton), [**CheckRadioButton**](/windows/desktop/api/Winuser/nf-winuser-checkradiobutton), and [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) functions.

An application can use the [**BM\_GETCHECK**](bm-getcheck.md) message to retrieve the check state of a check box or radio button. An application can also use the [**BM\_GETSTATE**](bm-getstate.md) message to retrieve the button's current states (the check state, push state, and focus state). To get information about a specific state, use a bitmask on the returned state value.

The [**BM\_SETCHECK**](bm-setcheck.md) message sets the check state of a check box or radio button; the message returns zero. The [**BM\_SETSTATE**](bm-setstate.md) message sets the push state of a button; this message also returns zero. The [**BM\_SETSTYLE**](bm-setstyle.md) message changes the style of a button. It is designed for changing button styles within a type (for example, changing a check box to an automatic check box). It is not designed for changing between types (for example, changing a check box to a radio button). An application should not change a button from one type to another.

A button of the [**BS\_BITMAP**](button-styles.md) or [**BS\_ICON**](button-styles.md) style displays a bitmap or icon instead of text. The [**BM\_SETIMAGE**](bm-setimage.md) message associates a handle to a bitmap or icon with a button. The [**BM\_GETIMAGE**](bm-getimage.md) message retrieves a handle to the bitmap or icon associated with a button.

An application can also use the [**DM\_GETDEFID**](/windows/desktop/dlgbox/dm-getdefid) message to retrieve the identifier of the default push button control in a dialog box. An application can use the [**DM\_SETDEFID**](/windows/desktop/dlgbox/dm-setdefid) message to set the default push button for a dialog box.

Calling the [**CheckDlgButton**](/windows/desktop/api/Winuser/nf-winuser-checkdlgbutton) or [**CheckRadioButton**](/windows/desktop/api/Winuser/nf-winuser-checkradiobutton) function is equivalent to sending a [**BM\_SETCHECK**](bm-setcheck.md) message. Calling the [**IsDlgButtonChecked**](/windows/desktop/api/Winuser/nf-winuser-isdlgbuttonchecked) function is equivalent to sending a [**BM\_GETCHECK**](bm-getcheck.md) message.

## Handling Messages from a Button

Notifications from a button are sent as either [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) or [**WM\_NOTIFY**](wm-notify.md) messages. Information about which message is used can be found on the reference page for each notification.

For more information on how to handle messages, see [Control Messages](control-messages.md). See also Button Messages.

## Notification Messages from Buttons

When the user clicks a button, its state changes, and the button sends notification codes, in the form of [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) messages, to its parent window. For example, a push button control sends the [BN\_CLICKED](bn-clicked.md) notification code whenever the user chooses the button. In all cases (except for [BCN\_HOTITEMCHANGE](bcn-hotitemchange.md)), the low-order word of the *wParam* parameter contains the control identifier, the high-order word of *wParam* contains the notification code, and the *lParam* parameter contains the control window handle.

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



 

A button sends the [BN\_DISABLE](bn-disable.md), [BN\_PUSHED](bn-pushed.md), [BN\_KILLFOCUS](bn-killfocus.md), [BN\_PAINT](bn-paint.md), [BN\_SETFOCUS](bn-setfocus.md), and [BN\_UNPUSHED](bn-unpushed.md) notification codes only if it has the [**BS\_NOTIFY**](button-styles.md) style. [BN\_DBLCLK](bn-dblclk.md) notification codes are sent automatically for [**BS\_USERBUTTON**](button-styles.md), [**BS\_RADIOBUTTON**](button-styles.md), and [**BS\_OWNERDRAW**](button-styles.md) buttons. Other button types send BN\_DBLCLK only if they have the **BS\_NOTIFY** style. All buttons send the [BN\_CLICKED](bn-clicked.md) notification code regardless of their button styles.

For automatic buttons, the system changes the push state and paints the button. In this case, the application typically processes only the [BN\_CLICKED](bn-clicked.md) and [BN\_DBLCLK](bn-dblclk.md) notification codes. For buttons that are not automatic, the application typically responds to the notification code by sending a message to change the state of the button. For information about sending messages to buttons, see [Sending Messages to Buttons](#sending-messages-to-buttons).

When the user selects an owner-drawn button, the button sends its parent window a [**WM\_DRAWITEM**](wm-drawitem.md) message containing the identifier of the control to be drawn and information about its dimensions and state.

## Button Color Messages

The system provides default color values for buttons. An application can retrieve the default values for these colors by calling the [**GetSysColor**](/windows/desktop/api/winuser/nf-winuser-getsyscolor) function, or set the values by calling the [**SetSysColors**](/windows/desktop/api/winuser/nf-winuser-setsyscolors) function. The following table shows the default button-color values.



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



 

However, calling [**SetSysColors**](/windows/desktop/api/winuser/nf-winuser-setsyscolors) affects all applications, so you should not call this function to customize buttons for your application.

The system sends a [**WM\_CTLCOLORBTN**](wm-ctlcolorbtn.md) message to a button's parent window before drawing a button. This message contains a handle to the button's device context and a handle to the child window. The parent window can use these handles to change the button's text and background colors. However, only owner-drawn buttons respond to the parent window processing the message.

## Button Default Message Processing

The window procedure for the predefined button control window class carries out default processing for all messages that the button control procedure does not process. When the button control procedure returns **FALSE** for any message, the predefined window procedure checks the messages and performs the default actions listed in the following table.



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Message</th>
<th>Default action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="bm-click.md"><strong>BM_CLICK</strong></a></td>
<td>Sends the button a <a href="/windows/desktop/inputdev/wm-lbuttondown"><strong>WM_LBUTTONDOWN</strong></a> and a <a href="/windows/desktop/inputdev/wm-lbuttonup"><strong>WM_LBUTTONUP</strong></a> message, and sends the parent window a <a href="bn-clicked.md">BN_CLICKED</a> notification code.</td>
</tr>
<tr class="even">
<td><a href="bm-getcheck.md"><strong>BM_GETCHECK</strong></a></td>
<td>Returns the check state of the button.</td>
</tr>
<tr class="odd">
<td><a href="bm-getimage.md"><strong>BM_GETIMAGE</strong></a></td>
<td>Returns a handle to the bitmap or icon associated with the button or <strong>NULL</strong> if the button has no bitmap or icon.</td>
</tr>
<tr class="even">
<td><a href="bm-getstate.md"><strong>BM_GETSTATE</strong></a></td>
<td>Returns the current check state, push state, and focus state of the button.</td>
</tr>
<tr class="odd">
<td><a href="bm-setcheck.md"><strong>BM_SETCHECK</strong></a></td>
<td>Sets the check state for all styles of radio buttons and check boxes. If the <em>wParam</em> parameter is greater than zero for radio buttons, the button is given the <a href="/windows/desktop/winmsg/window-styles"><strong>WS_TABSTOP</strong></a> style.</td>
</tr>
<tr class="even">
<td><a href="bm-setimage.md"><strong>BM_SETIMAGE</strong></a></td>
<td>Associates the specified bitmap or icon handle with the button and returns a handle to the previous bitmap or icon.</td>
</tr>
<tr class="odd">
<td><a href="bm-setstate.md"><strong>BM_SETSTATE</strong></a></td>
<td>Sets the push state of the button. For owner-drawn buttons, a <a href="wm-drawitem.md"><strong>WM_DRAWITEM</strong></a> message is sent to the parent window if the state of the button has changed.</td>
</tr>
<tr class="even">
<td><a href="bm-setstyle.md"><strong>BM_SETSTYLE</strong></a></td>
<td>Sets the button style. If the low-order word of the <em>lParam</em> parameter is <strong>TRUE</strong>, the button is redrawn.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/inputdev/wm-char"><strong>WM_CHAR</strong></a></td>
<td>Checks a check box or automatic check box when the user presses the plus (+) or equal (=) keys. Clears a check box or automatic check box when the user presses the minus (–) key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/winmsg/wm-enable"><strong>WM_ENABLE</strong></a></td>
<td>Paints the button.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/winmsg/wm-erasebkgnd"><strong>WM_ERASEBKGND</strong></a></td>
<td>Erases the background for owner-drawn buttons. The backgrounds of other buttons are erased as part of the <a href="/windows/desktop/gdi/wm-paint"><strong>WM_PAINT</strong></a> and <a href="/windows/desktop/winmsg/wm-enable"><strong>WM_ENABLE</strong></a> processing.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/dlgbox/wm-getdlgcode"><strong>WM_GETDLGCODE</strong></a></td>
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
<td><a href="button-styles.md"><strong>BS_AUTOCHECKBOX</strong></a></td>
<td>DLGC_WANTCHARS | DLGC_BUTTON</td>
</tr>
<tr class="even">
<td><a href="button-styles.md"><strong>BS_AUTORADIOBUTTON</strong></a></td>
<td>DLGC_RADIOBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td><a href="button-styles.md"><strong>BS_CHECKBOX</strong></a></td>
<td>DLGC_WANTCHARS | DLGC_BUTTON</td>
</tr>
<tr class="even">
<td><a href="button-styles.md"><strong>BS_DEFPUSHBUTTON</strong></a></td>
<td>DLGC_DEFPUSHBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td><a href="button-styles.md"><strong>BS_GROUPBOX</strong></a></td>
<td>DLGC_STATIC</td>
</tr>
<tr class="even">
<td><a href="button-styles.md"><strong>BS_PUSHBUTTON</strong></a></td>
<td>DLGC_UNDEFPUSHBUTTON | DLGC_BUTTON</td>
</tr>
<tr class="odd">
<td><a href="button-styles.md"><strong>BS_RADIOBUTTON</strong></a></td>
<td>DLGC_RADIOBUTTON | DLGC_BUTTON</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/winmsg/wm-getfont"><strong>WM_GETFONT</strong></a></td>
<td>Returns a handle to the current font.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-keydown"><strong>WM_KEYDOWN</strong></a></td>
<td>Pushes the button if the user presses the SPACEBAR.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/inputdev/wm-keyup"><strong>WM_KEYUP</strong></a></td>
<td>Releases the mouse capture for all cases except the TAB key.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-killfocus"><strong>WM_KILLFOCUS</strong></a></td>
<td>Removes the focus rectangle from a button. For push buttons and default push buttons, the focus rectangle is invalidated. If the button has the mouse capture, the capture is released, the button is not clicked, and any push state is removed.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/inputdev/wm-lbuttondblclk"><strong>WM_LBUTTONDBLCLK</strong></a></td>
<td>Sends a <a href="bn-dblclk.md">BN_DBLCLK</a> notification code to the parent window for radio buttons and owner-drawn buttons. For other buttons, a double-click is processed as a <a href="/windows/desktop/inputdev/wm-lbuttondown"><strong>WM_LBUTTONDOWN</strong></a> message.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-lbuttondown"><strong>WM_LBUTTONDOWN</strong></a></td>
<td>Highlights the button if the position of the mouse cursor is within the button's client rectangle.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/inputdev/wm-lbuttonup"><strong>WM_LBUTTONUP</strong></a></td>
<td>Releases the mouse capture if the button had the mouse capture.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-mousemove"><strong>WM_MOUSEMOVE</strong></a></td>
<td>Performs the same action as <a href="/windows/desktop/inputdev/wm-lbuttondown"><strong>WM_LBUTTONDOWN</strong></a>, if the button has the mouse capture. Otherwise, no action is performed.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/winmsg/wm-nccreate"><strong>WM_NCCREATE</strong></a></td>
<td>Turns any <a href="button-styles.md"><strong>BS_OWNERDRAW</strong></a> button into a <a href="button-styles.md"><strong>BS_PUSHBUTTON</strong></a> button.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-nchittest"><strong>WM_NCHITTEST</strong></a></td>
<td>Returns HTTRANSPARENT, if the button control is a group box.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/gdi/wm-paint"><strong>WM_PAINT</strong></a></td>
<td>Draws the button according to its style and current state.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/inputdev/wm-setfocus"><strong>WM_SETFOCUS</strong></a></td>
<td>Draws a focus rectangle on the button getting the focus. For radio buttons and automatic radio buttons, the parent window is sent a <a href="bn-clicked.md">BN_CLICKED</a> notification code.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/winmsg/wm-setfont"><strong>WM_SETFONT</strong></a></td>
<td>Sets a new font and optionally updates the window.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/winmsg/wm-settext"><strong>WM_SETTEXT</strong></a></td>
<td>Sets the text of the button. In the case of a group box, the message paints over the preexisting text before repainting the group box with the new text.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/inputdev/wm-syskeyup"><strong>WM_SYSKEYUP</strong></a></td>
<td>Releases the mouse capture for all cases except the TAB key.</td>
</tr>
</tbody>
</table>



 

The predefined window procedure passes all other messages to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function for default processing.

## Related topics

<dl> <dt>

[Control Messages](control-messages.md)
</dt> </dl>

 

 
