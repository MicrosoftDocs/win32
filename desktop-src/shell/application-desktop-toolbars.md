---
description: An application desktop toolbar (also called an appbar) is a window that is similar to the Windows taskbar.
ms.assetid: d9f63cb1-e2cc-4a3b-a3b8-de028e0f0123
title: Using Application Desktop Toolbars
ms.topic: article
ms.date: 05/31/2018
---

# Using Application Desktop Toolbars

An *application desktop toolbar* (also called an appbar) is a window that is similar to the Windows taskbar. It is anchored to an edge of the screen, and it typically contains buttons that give the user quick access to other applications and windows. The system prevents other applications from using the desktop area used by an appbar. Any number of appbars can exist on the desktop at any given time.

This topic contains the following sections.

- [About Application Desktop Toolbars](#about-application-desktop-toolbars)
    - [Sending Messages](#sending-messages)
    - [Registration](#registration)
    - [Appbar Size and Position](#appbar-size-and-position)
    - [Autohide Application Desktop Toolbars](#autohide-application-desktop-toolbars)
    - [Appbar Notification Messages](#appbar-notification-messages)
- [Registering an Application Desktop Toolbar](#registering-an-application-desktop-toolbar)
- [Setting the Appbar Size and Position](#setting-the-appbar-size-and-position)
- [Processing Appbar Notification Messages](#processing-appbar-notification-messages)

## About Application Desktop Toolbars

Windows provides an API that lets you take advantage of appbar services provided by the system. The services help ensure that application-defined appbars operate smoothly with one another and with the taskbar. The system maintains information about each appbar and sends the appbars messages to notify them about events that can affect their size, position, and appearance.

### Sending Messages

An application uses a special set of messages, called appbar messages, to add or remove an appbar, set an appbar's size and position, and retrieve information about the size, position, and state of the taskbar. To send an appbar message, an application must use the [**SHAppBarMessage**](/windows/desktop/api/Shellapi/nf-shellapi-shappbarmessage) function. The function's parameters include a message identifier, such as [**ABM\_NEW**](abm-new.md), and the address of an [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure. The structure members contain information that the system needs to process the given message.

For any given appbar message, the system uses some members of the [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure and ignores the others. However, the system always uses the **cbSize** and **hWnd** members, so an application must fill these members for every appbar message. The **cbSize** member specifies the size of the structure, and the **hWnd** member is the handle to the appbar's window.

Some appbar messages request information from the system. When processing these messages, the system copies the requested information into the [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure.

### Registration

The system keeps an internal list of appbars and maintains information about each bar in the list. The system uses the information to manage appbars, perform services for them, and send them notification messages.

An application must register an appbar (that is, add it to the internal list) before it can receive appbar services from the system. To register an appbar, an application sends the [**ABM\_NEW**](abm-new.md) message. The accompanying [**APPBARDATA**](/windows/desktop/api/Shellapi/ns-shellapi-appbardata) structure includes the handle to the appbar's window and an application-defined message identifier. The system uses the message identifier to send notification messages to the window procedure of the appbar window. For more information, see Appbar Notification Messages.

An application unregisters an appbar by sending the [**ABM\_REMOVE**](abm-remove.md) message. Unregistering an appbar removes it from the system's internal list of appbars. The system no longer sends notification messages to the appbar or prevents other applications from using the screen area used by the appbar. An application should always send **ABM\_REMOVE** before destroying an appbar.

### Appbar Size and Position

An application should set an appbar's size and position so that it does not interfere with any other appbars or the taskbar. Every appbar must be anchored to a particular edge of the screen, and multiple appbars can be anchored to an edge. However, if an appbar is anchored to the same edge as the taskbar, the system ensures that the taskbar is always on the outermost edge.

To set the size and position of an appbar, an application first proposes a screen edge and bounding rectangle for the appbar by sending the [**ABM\_QUERYPOS**](abm-querypos.md) message. The system determines whether any part of the screen area within the proposed rectangle is used by the taskbar or another appbar, adjusts the rectangle (if necessary), and returns the adjusted rectangle to the application.

Next, the application sends the [**ABM\_SETPOS**](abm-setpos.md) message to set the new bounding rectangle for the appbar. Again, the system may adjust the rectangle before returning it to the application. For this reason, the application should use the adjusted rectangle returned by **ABM\_SETPOS** to set the final size and position. The application can use the [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow) function to move the appbar into position.

By using a two-step process to set the size and position, the system enables the application to provide intermediate feedback to the user during the move operation. For example, if the user drags an appbar, the application might display a shaded rectangle indicating the new position before the appbar actually moves.

An application should set the size and position of its appbar after registering it and whenever the appbar receives the [**ABN\_POSCHANGED**](abn-poschanged.md) notification message. An appbar receives this notification message whenever a change occurs in the taskbar's size, position, or visibility state and whenever another appbar on the same side of the screen is resized, added, or removed.

Whenever an appbar receives the WM\_ACTIVATE message, it should send the [**ABM\_ACTIVATE**](abm-activate.md) message. Similarly, when an appbar receives a WM\_WINDOWPOSCHANGED message, it must call [**ABM\_WINDOWPOSCHANGED**](abm-windowposchanged.md). Sending these messages ensures that the system properly sets the z-order of any autohide appbars on the same edge.

### Autohide Application Desktop Toolbars

An autohide appbar is one that is normally hidden but becomes visible when the user moves the mouse cursor to the screen edge with which the appbar is associated. The appbar hides itself again when the user moves the mouse cursor out of the bar's bounding rectangle.

Although the system allows a number of different appbars at any given time, it allows only one autohide appbar at a time for each screen edge on a first-come, first-served basis. The system automatically maintains the z-order of an autohide appbar (within its z-order group only).

An application uses the [**ABM\_SETAUTOHIDEBAR**](abm-setautohidebar.md) message to register or unregister an autohide appbar. The message specifies the edge for the appbar and a flag that specifies whether the appbar is to be registered or unregistered. The message fails if an autohide appbar is being registered but one is already associated with the specified edge. An application can retrieve the handle to the autohide appbar associated with an edge by sending the [**ABM\_GETAUTOHIDEBAR**](abm-getautohidebar.md) message.

An autohide appbar does not need to register as a normal appbar; that is, it does not need to be registered by sending the [**ABM\_NEW**](abm-new.md) message. An appbar that is not registered by **ABM\_NEW** overlaps any appbars anchored on the same edge of the screen.

### Appbar Notification Messages

The system sends messages to notify an appbar about events that can affect its position and appearance. The messages are sent in the context of an application-defined message. The application specifies the identifier of the message when it sends the [**ABM\_NEW**](abm-new.md) message to register the appbar. The notification code is in the *wParam* parameter of the application-defined message.

An appbar receives the [**ABN\_POSCHANGED**](abn-poschanged.md) notification message when the taskbar's size, position, or visibility state changes, when another appbar is added to the same edge of the screen, or when another appbar on the same edge of the screen is resized or removed. An appbar should respond to this notification message by sending [**ABM\_QUERYPOS**](abm-querypos.md) and [**ABM\_SETPOS**](abm-setpos.md) messages. If an appbar's position has changed, it should call the [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow) function to move itself to the new position.

The system sends the [**ABN\_STATECHANGE**](abn-statechange.md) notification message whenever the taskbar's autohide or always-on-top state has changed—that is, when the user selects or clears the **Always on top** or **Auto hide** check box on the taskbar's property sheet. An appbar can use this notification message to set its state to conform to that of the taskbar, if desired.

When a full-screen application is started or when the last full-screen application is closed, an appbar receives the [**ABN\_FULLSCREENAPP**](abn-fullscreenapp.md) notification message. The *lParam* parameter indicates whether the full-screen application is opening or closing. If it is opening, the appbar must drop to the bottom of the z-order. The appbar should restore its z-order position when the last full-screen application has closed.

An appbar receives the [**ABN\_WINDOWARRANGE**](abn-windowarrange.md) notification message when the user selects the Cascade, Tile Horizontally, or Tile Vertically command from the taskbar's shortcut menu. The system sends the message two times—before rearranging the windows (*lParam* is **TRUE**) and after arranging the windows (*lParam* is **FALSE**).

An appbar can use [**ABN\_WINDOWARRANGE**](abn-windowarrange.md) messages to exclude itself from the cascade or tile operation. To exclude itself, the appbar should hide itself when *lParam* is **TRUE** and show itself when *lParam* is **FALSE**. If an appbar hides itself in response to this message, it does not need to send the [**ABM\_QUERYPOS**](abm-querypos.md) and [**ABM\_SETPOS**](abm-setpos.md) messages in response to the cascade or tile operation.

## Registering an Application Desktop Toolbar

An application must register an appbar by sending the [**ABM\_NEW**](abm-new.md) message. Registering an appbar adds it to the system's internal list and provides the system with a message identifier to use to send notification messages to the appbar. Before exiting, an application must unregister the appbar by sending the [**ABM\_REMOVE**](abm-remove.md) message. Unregistering removes the appbar from the system's internal list and prevents the bar from receiving appbar notification messages.

The function in the following example either registers or unregisters an appbar, depending on the value of a Boolean flag parameter.


```C++
// RegisterAccessBar - registers or unregisters an appbar. 
// Returns TRUE if successful, or FALSE otherwise. 

// hwndAccessBar - handle to the appbar 
// fRegister - register and unregister flag 

// Global variables 
//     g_uSide - screen edge (defaults to ABE_TOP) 
//     g_fAppRegistered - flag indicating whether the bar is registered 

BOOL RegisterAccessBar(HWND hwndAccessBar, BOOL fRegister) 
{ 
    APPBARDATA abd; 
    
    // An application-defined message identifier
    APPBAR_CALLBACK = (WM_USER + 0x01);
    
    // Specify the structure size and handle to the appbar. 
    abd.cbSize = sizeof(APPBARDATA); 
    abd.hWnd = hwndAccessBar; 

    if (fRegister) 
    { 
        // Provide an identifier for notification messages. 
        abd.uCallbackMessage = APPBAR_CALLBACK; 

        // Register the appbar. 
        if (!SHAppBarMessage(ABM_NEW, &abd)) 
            return FALSE; 

        g_uSide = ABE_TOP;       // default edge 
        g_fAppRegistered = TRUE; 

    } 
    else 
    { 
        // Unregister the appbar. 
        SHAppBarMessage(ABM_REMOVE, &abd); 
        g_fAppRegistered = FALSE; 
    } 

    return TRUE; 
}
```



## Setting the Appbar Size and Position

An application should set an appbar's size and position after registering the appbar, after the user user moves or sizes the appbar, and whenever the appbar receives the [**ABN\_POSCHANGED**](abn-poschanged.md) notification message. Before setting the size and position of the appbar, the application queries the system for an approved bounding rectangle by sending the [**ABM\_QUERYPOS**](abm-querypos.md) message. The system returns a bounding rectangle that does not interfere with the taskbar or any other appbar. The system adjusts the rectangle purely by rectangle subtraction; it makes no effort to preserve the rectangle's initial size. For this reason, the appbar should readjust the rectangle, as necessary, after sending **ABM\_QUERYPOS**.

Next, the application passes the bounding rectangle back to the system by using the [**ABM\_SETPOS**](abm-setpos.md) message. Then it calls the [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow) function to move the appbar into position.

The following example shows how to set an appbar's size and position.


```C++
// AppBarQuerySetPos - sets the size and position of an appbar. 

// uEdge - screen edge to which the appbar is to be anchored 
// lprc - current bounding rectangle of the appbar 
// pabd - address of the APPBARDATA structure with the hWnd and cbSize members filled

void PASCAL AppBarQuerySetPos(UINT uEdge, LPRECT lprc, PAPPBARDATA pabd) 
{ 
    int iHeight = 0; 
    int iWidth = 0; 

    pabd->rc = *lprc; 
    pabd->uEdge = uEdge; 

    // Copy the screen coordinates of the appbar's bounding 
    // rectangle into the APPBARDATA structure. 
    if ((uEdge == ABE_LEFT) || (uEdge == ABE_RIGHT)) 
    { 
        iWidth = pabd->rc.right - pabd->rc.left; 
        pabd->rc.top = 0; 
        pabd->rc.bottom = GetSystemMetrics(SM_CYSCREEN); 
    } 
    else 
    { 
        iHeight = pabd->rc.bottom - pabd->rc.top; 
        pabd->rc.left = 0; 
        pabd->rc.right = GetSystemMetrics(SM_CXSCREEN); 
    } 

    // Query the system for an approved size and position. 
    SHAppBarMessage(ABM_QUERYPOS, pabd); 

    // Adjust the rectangle, depending on the edge to which the appbar is anchored.
    switch (uEdge) 
    { 
        case ABE_LEFT: 
            pabd->rc.right = pabd->rc.left + iWidth; 
            break; 

        case ABE_RIGHT: 
            pabd->rc.left = pabd->rc.right - iWidth; 
            break; 

        case ABE_TOP: 
            pabd->rc.bottom = pabd->rc.top + iHeight; 
            break; 

        case ABE_BOTTOM: 
            pabd->rc.top = pabd->rc.bottom - iHeight; 
            break; 
    } 

    // Pass the final bounding rectangle to the system. 
    SHAppBarMessage(ABM_SETPOS, pabd); 

    // Move and size the appbar so that it conforms to the 
    // bounding rectangle passed to the system. 
    MoveWindow(pabd->hWnd, 
               pabd->rc.left, 
               pabd->rc.top, 
               pabd->rc.right - pabd->rc.left, 
               pabd->rc.bottom - pabd->rc.top, 
               TRUE); 

}
```



## Processing Appbar Notification Messages

An appbar receives a notification message when the state of the taskbar changes, when a full-screen application starts (or the last one closes), or when an event occurs that can affect the appbar's size and position. The following example shows how to process the various notification messages.


```C++
// AppBarCallback - processes notification messages sent by the system. 

// hwndAccessBar - handle to the appbar 
// uNotifyMsg - identifier of the notification message 
// lParam - message parameter 

void AppBarCallback(HWND hwndAccessBar, UINT uNotifyMsg, 
    LPARAM lParam) 
{ 
    APPBARDATA abd; 
    UINT uState; 

    abd.cbSize = sizeof(abd); 
    abd.hWnd = hwndAccessBar; 

    switch (uNotifyMsg) 
    { 
        case ABN_STATECHANGE: 

            // Check to see if the taskbar's always-on-top state has changed
            // and, if it has, change the appbar's state accordingly.
            uState = SHAppBarMessage(ABM_GETSTATE, &abd); 

            SetWindowPos(hwndAccessBar, 
                         (ABS_ALWAYSONTOP & uState) ? HWND_TOPMOST : HWND_BOTTOM, 
                         0, 0, 0, 0, 
                         SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE); 

            break; 

        case ABN_FULLSCREENAPP: 

            // A full-screen application has started, or the last full-screen
            // application has closed. Set the appbar's z-order appropriately.
            if (lParam) 
            { 
                SetWindowPos(hwndAccessBar, 
                             (ABS_ALWAYSONTOP & uState) ? HWND_TOPMOST : HWND_BOTTOM, 
                             0, 0, 0, 0, 
                             SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE); 
            } 
            else 
            { 
                uState = SHAppBarMessage(ABM_GETSTATE, &abd); 

                if (uState & ABS_ALWAYSONTOP) 
                    SetWindowPos(hwndAccessBar, 
                                 HWND_TOPMOST, 
                                 0, 0, 0, 0, 
                                 SWP_NOMOVE | SWP_NOSIZE | SWP_NOACTIVATE); 
            } 

        case ABN_POSCHANGED: 

            // The taskbar or another appbar has changed its size or position.
            AppBarPosChanged(&abd); 
            break; 
    } 
}
```



The following function adjusts an appbar's bounding rectangle and then calls the application-defined AppBarQuerySetPos function (included in the previous section) to set the bar's size and position accordingly.


```C++
// AppBarPosChanged - adjusts the appbar's size and position. 

// pabd - address of an APPBARDATA structure that contains information 
//        used to adjust the size and position. 

void PASCAL AppBarPosChanged(PAPPBARDATA pabd) 
{ 
    RECT rc; 
    RECT rcWindow; 
    int iHeight; 
    int iWidth; 

    rc.top = 0; 
    rc.left = 0; 
    rc.right = GetSystemMetrics(SM_CXSCREEN); 
    rc.bottom = GetSystemMetrics(SM_CYSCREEN); 

    GetWindowRect(pabd->hWnd, &rcWindow); 

    iHeight = rcWindow.bottom - rcWindow.top; 
    iWidth = rcWindow.right - rcWindow.left; 

    switch (g_uSide) 
    { 
        case ABE_TOP: 
            rc.bottom = rc.top + iHeight; 
            break; 

        case ABE_BOTTOM: 
            rc.top = rc.bottom - iHeight; 
            break; 

        case ABE_LEFT: 
            rc.right = rc.left + iWidth; 
            break; 

        case ABE_RIGHT: 
            rc.left = rc.right - iWidth; 
            break; 
    } 

    AppBarQuerySetPos(g_uSide, &rc, pabd); 
}
```



 

 
