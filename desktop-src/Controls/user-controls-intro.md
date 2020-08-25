---
title: Custom Controls
description: This section contains information about application-defined or custom controls.
ms.assetid: 220f7058-db04-46d0-acee-ed5e676790b3
ms.topic: article
ms.date: 05/31/2018
---

# Custom Controls

This section contains information about application-defined or custom controls.

The following topics are discussed.

-   [Creating Owner-Drawn Controls](#creating-owner-drawn-controls)
-   [Subclassing the Window Class of an Existing Control](#subclassing-the-window-class-of-an-existing-control)
-   [Implementing an Application-Defined Window Class](#implementing-an-application-defined-window-class)
-   [Sending Notifications from a Control](#sending-notifications-from-a-control)
-   [Accessibility](#accessibility)
-   [Related topics](#related-topics)

## Creating Owner-Drawn Controls

Buttons, menus, static text controls, list boxes, and combo boxes can be created with an owner-drawn style flag. When a control has the owner-drawn style, the system handles the user's interaction with the control as usual, performing such tasks as detecting when a user has chosen a button and notifying the button's owner of the event. However, because the control is owner-drawn, the parent window of the control is responsible for the visual appearance of the control. The parent window receives a message whenever the control must be drawn.

For buttons and static text controls, the owner-drawn style affects how the system draws the entire control. For list boxes and combo boxes, the parent window draws the items within the control, and the control draws its own outline. For example, an application can customize a list box so that it displays a small bitmap next to each item in the list.

The following example code shows how to create an owner-drawn static text control. Assume that Unicode is defined.


```
// g_myStatic is a global HWND variable.
g_myStatic = CreateWindowEx(0, L"STATIC", L"Some static text", 
            WS_CHILD | WS_VISIBLE | SS_OWNERDRAW, 
            25, 125, 150, 20, hDlg, 0, 0, 0);
```



In the following example, from the window procedure for the dialog box that contains the control created in the previous example, the [**WM\_DRAWITEM**](wm-drawitem.md) message is handled by displaying the text in a custom color, using the default font. Note that you do not need to call [**BeginPaint**](/windows/desktop/api/winuser/nf-winuser-beginpaint) and [**EndPaint**](/windows/desktop/api/winuser/nf-winuser-endpaint) when handling **WM\_DRAWITEM**.


```
case WM_DRAWITEM:
{
    LPDRAWITEMSTRUCT pDIS = (LPDRAWITEMSTRUCT)lParam;
    if (pDIS->hwndItem == g_myStatic)
    {
        SetTextColor(pDIS->hDC, RGB(100, 0, 100));
        WCHAR staticText[99];
        int len = SendMessage(myStatic, WM_GETTEXT, 
            ARRAYSIZE(staticText), (LPARAM)staticText);
        TextOut(pDIS->hDC, pDIS->rcItem.left, pDIS->rcItem.top, staticText, len);
    }
    return TRUE;
}
```



For more information about owner-drawn controls, see [Creating an Owner-drawn List Box](using-list-boxes.md) and [Owner Drawn Combo Boxes](about-combo-boxes.md).

## Subclassing the Window Class of an Existing Control

Subclassing an existing control is another way to create a custom control. The subclass procedure can alter selected behaviors of the control by processing those messages that affect the selected behaviors. All other messages pass to the original window procedure for the control. For example, an application can display a small bitmap next to the text in a read-only, single-line edit control by subclassing the control and processing the [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message. For more information, see [About Window Procedures](/windows/desktop/winmsg/about-window-procedures) and [Subclassing Controls](subclassing-overview.md).

## Implementing an Application-Defined Window Class

To create a control that is not explicitly based on an existing control, the application must create and register a window class. The process for registering an application-defined window class for a custom control is the same as registering a class for an ordinary window. To create a custom control, specify the name of the window class in the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function or in a dialog box template. Each class must have a unique name, a corresponding window procedure, and other information.

At a minimum, the window procedure draws the control. If an application uses the control to let the user type information, the window procedure also processes input messages from the keyboard and mouse and sends notification messages to the parent window. In addition, if the control supports control messages, the window procedure processes messages sent to it by the parent window or other windows. For example, controls often process the [**WM\_GETDLGCODE**](/windows/desktop/dlgbox/wm-getdlgcode) message sent by dialog boxes to direct a dialog box to process keyboard input in a given way.

The window procedure for an application-defined control should process any predefined control message in the following table if the message affects the operation of the control.



| Message                                          | Recommendation                                                                                                                                                                                                                                  |
|--------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_GETDLGCODE**](/windows/desktop/dlgbox/wm-getdlgcode)       | Process if the control uses the ENTER, ESC, TAB, or arrow keys. The [**IsDialogMessage**](/windows/desktop/api/winuser/nf-winuser-isdialogmessagea) function sends this message to controls in a dialog box to determine whether to process the keys or pass them to the control. |
| [**WM\_GETFONT**](/windows/desktop/winmsg/wm-getfont)             | Process if the [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont) message is also processed.                                                                                                                                                                  |
| [**WM\_GETTEXT**](/windows/desktop/winmsg/wm-gettext)             | Process if the control text is not the same as the title specified by the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function.                                                                                                                 |
| [**WM\_GETTEXTLENGTH**](/windows/desktop/winmsg/wm-gettextlength) | Process if the control text is not the same as the title specified by the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function.                                                                                                                 |
| [**WM\_KILLFOCUS**](/windows/desktop/inputdev/wm-killfocus)       | Process if the control displays a caret, a focus rectangle, or another item to indicate that it has the input focus.                                                                                                                            |
| [**WM\_SETFOCUS**](/windows/desktop/inputdev/wm-setfocus)         | Process if the control displays a caret, a focus rectangle, or another item to indicate that it has the input focus.                                                                                                                            |
| [**WM\_SETTEXT**](/windows/desktop/winmsg/wm-settext)             | Process if the control text is not the same as the title specified by the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function.                                                                                                                 |
| [**WM\_SETFONT**](/windows/desktop/winmsg/wm-setfont)             | Process if the control displays text. The system sends this message when creating a dialog box that has the DS\_SETFONT style.                                                                                                                  |



 

Application-defined control messages are specific to the given control and must be explicitly sent to the control by using a [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) or [**SendDlgItemMessage**](/windows/desktop/api/winuser/nf-winuser-senddlgitemmessagea) function. The numeric value for each message must be unique and must not conflict with the values of other window messages. To ensure that application-defined message values do not conflict, an application should create each value by adding a unique number to the [**WM\_USER**](/windows/desktop/winmsg/wm-user) value.

## Sending Notifications from a Control

Custom controls might be required to send notifications of events to the parent window so that the host application can respond to these events. For example, a custom list view might send a notification when the user selects an item, and another notification when an item is double-clicked.

Notifications are sent as [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) or [**WM\_NOTIFY**](wm-notify.md) messages. **WM\_NOTIFY** messages carry more information than **WM\_COMMAND** messages.

The control identifier is a unique number the application uses to identify the control sending the message. The application sets the identifier for a control when it creates the control. The application specifies the identifier either in the *hMenu* parameter of the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function or in the **id** member of the [**DLGITEMTEMPLATEEX**](/windows/desktop/dlgbox/dlgitemtemplateex) structure.

Because the control itself does not set the control identifier, the control must retrieve the identifier before it can send notification messages. A control must use the [**GetDlgCtrlID**](/windows/desktop/api/winuser/nf-winuser-getdlgctrlid) function to retrieve its own control identifier. Although the control identifier is specified as the menu handle when the control is created, the [**GetMenu**](/windows/desktop/api/winuser/nf-winuser-getmenu) function cannot be used to retrieve the identifier. Alternatively, a control can retrieve the identifier from the **hMenu** member in the [**CREATESTRUCT**](/windows/win32/api/winuser/ns-winuser-createstructa) structure while processing the [**WM\_CREATE**](/windows/desktop/winmsg/wm-create) message.

The following examples, where *hwndControl* is the handle of the control window and CN\_VALUECHANGED is a custom notification definition, show the two ways of sending a control-specific notification.


```
 // Send as WM_COMMAND.
SendMessage(GetParent(hwndControl), 
    WM_COMMAND,
    MAKEWPARAM(GetDlgCtrlID(hwndControl), CN_VALUECHANGED),
    (LPARAM)hwndControl);

// Send as WM_NOTIFY.           
NMHDR nmh;
nmh.code = CN_VALUECHANGED;
nmh.idFrom = GetDlgCtrlID(hwndControl);
nmh.hwndFrom = hwndControl;
SendMessage(GetParent(hwndControl), 
    WM_NOTIFY, 
    (WPARAM)hwndControl, 
    (LPARAM)&nmh);
```



Note that the [**NMHDR**](/windows/desktop/api/richedit/ns-richedit-nmhdr) structure can be part of a larger control-defined structure that contains additional information. In the example, the old and new values of the control might be contained in this structure. (Such extended structures are used with many standard notifications; for example, see [LVN\_INSERTITEM](lvn-insertitem.md), which uses the [**NMLISTVIEW**](/windows/win32/api/commctrl/ns-commctrl-nmlistview) structure.)

## Accessibility

All the common controls support Microsoft Active Accessibility (MSAA), which enables programmatic access by accessible-technology applications such as screen-readers. MSAA also enables UI Automation, a newer technology, to interact with controls.

Custom controls should implement either the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface (to support MSAA) or the UI Automation interfaces, or both. Otherwise, accessible-technology products will be able to obtain only very limited information about the control window, will not have access to the control's properties, and will be unable to trigger events in the control.

For more information about making your control accessible, see [Windows Automation API](/windows/desktop/WinAuto/windows-automation-api-portal).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[General Control Reference](common-control-reference.md)
</dt> <dt>

[Customizing a Control's Appearance Using Custom Draw](custom-draw.md)
</dt> <dt>

[Control Messages](control-messages.md)
</dt> <dt>

[Using Visual Styles with Owner-Drawn Controls](using-visual-styles.md)
</dt> </dl>

 

 