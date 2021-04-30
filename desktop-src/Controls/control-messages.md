---
title: Control Messages
description: This section contains information about how Windows messages are used to communicate with controls.
ms.assetid: 94d34132-25c2-4a1a-bd0e-35e5a666bbfa
ms.topic: article
ms.date: 05/31/2018
---

# Control Messages

This section contains information about how Windows messages are used to communicate with controls.

The following topics are discussed.

-   [Messages to Common Controls](#messages-to-common-controls)
-   [Notifications from Controls](#notifications-from-controls)
-   [Related topics](#related-topics)

## Messages to Common Controls

Because common controls are windows, an application can communicate with them by using common Microsoft Win32 messages such as [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont) or [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext). In addition, the window class of each common control supports a set of control-specific messages. Typically, an application uses [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) or [**SendDlgItemMessage**](/windows/desktop/api/winuser/nf-winuser-senddlgitemmessagea) to pass messages to the control (often receiving information in the return value).

Some common controls also have a set of macros that an application can use instead of [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage). The macros are typically easier to use than the functions. The following example code retrieves the text of the selected tree-view item, first by using the raw messages, and second by using the equivalent macros. Assume that *hwnd* is the handle of the control window.


```
BOOL fSuccess;
WCHAR itemText[99];
TVITEM tvItem = { 0 };
tvItem.mask = TVIF_TEXT;
tvItem.cchTextMax = ARRAYSIZE(itemText);
tvItem.pszText = itemText;

// This...
tvItem.hItem = (HTREEITEM)SendMessage(hwnd, TVM_GETNEXTITEM, TVGN_CARET, NULL);
fSuccess = SendMessage(hwnd, TVM_GETITEM, 0, (LPARAM)&tvItem);

// ... is equivalent to this.
tvItem.hItem = TreeView_GetSelection(hwnd);
fSuccess = TreeView_GetItem(hwnd, &tvItem);
```



When a change is made to the system color settings, Windows sends a [**WM\_SYSCOLORCHANGE**](/windows/desktop/gdi/wm-syscolorchange) message to all top-level windows. Your top-level window must forward the **WM\_SYSCOLORCHANGE** message to its common controls; otherwise, the controls will not be notified of the color change. Forwarding the message ensures that the colors used by your common controls are consistent with those used by other user interface objects. For example, a toolbar control uses the "3-D Objects" color to draw its buttons. If the user changes the 3-D Object's color but the **WM\_SYSCOLORCHANGE** message is not forwarded to the toolbar, the toolbar buttons will remain in their original color (or even change to a combination of old and new colors) while the color of other buttons in the system changes.

## Notifications from Controls

Controls are child windows that send notification messages to the parent window when events, usually triggered by input from the user, occur in the control. The application relies on these notification messages to determine what action the user wants it to take. Except for trackbars, which use the [**WM\_HSCROLL**](wm-hscroll.md) and [**WM\_VSCROLL**](wm-vscroll.md) messages to notify their parent of changes, common controls send notifications as either [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) or [**WM\_NOTIFY**](wm-notify.md) messages, as specified in the reference topic for the notification. Typically, older notifications (those that have been in the API for a long time) use **WM\_COMMAND**.

The *lParam* parameter of [**WM\_NOTIFY**](wm-notify.md) is either the address of an [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure or the address of a larger structure that includes **NMHDR** as its first member. The structure contains the notification code and identifies the common control that sent the notification message. The meaning of the remaining structure members, if any, varies depending on the notification code.

Each type of common control has a corresponding set of notification codes. The common control library also provides notification codes that can be sent by more than one type of common control. See the documentation for the control of interest to determine which notification codes it will send and what format they take.

For example code showing how to handle [**WM\_NOTIFY**](wm-notify.md) messages, see the reference topic for that message.

## Related topics

<dl> <dt>

[General Control Reference](common-control-reference.md)
</dt> </dl>

 

 
