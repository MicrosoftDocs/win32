---
description: The Windows interface includes a special application desktop toolbar called the taskbar. You can use the taskbar for such tasks as switching between open windows and starting new applications.
ms.assetid: 14d520e7-7c15-441d-9662-24b972d208ac
title: The Taskbar
ms.topic: article
ms.date: 05/31/2018
---

# The Taskbar

The Windows interface includes a special [application desktop toolbar](application-desktop-toolbars.md) called the *taskbar*. You can use the taskbar for such tasks as switching between open windows and starting new applications.

> [!Note]  
> For information on changes made to the taskbar as of Windows 7, see [Taskbar Extensions](taskbar-extensions.md).

 

This topic contains the following sections.

- [About the Taskbar](#about-the-taskbar)
    - [Taskbar Display Options](#taskbar-display-options)
    - [Adding Shortcuts to the Start Menu](#adding-shortcuts-to-the-start-menu)
    - [Managing Taskbar Buttons](#managing-taskbar-buttons)
    - [Adding, Modifying, and Deleting Icons in the Notification Area](#adding-modifying-and-deleting-icons-in-the-notification-area)
    - [Taskbar Creation Notification](#taskbar-creation-notification)
- [Using the Taskbar](#using-the-taskbar)
    - [Adding and Deleting Taskbar Icons in the Notification Area](#adding-and-deleting-taskbar-icons-in-the-notification-area)
    - [Receiving Mouse Events](#receiving-mouse-events)

## About the Taskbar

The taskbar includes the following:

-   **Start** menu
-   Quick Launch bar (Windows Vista and earlier only)
-   Taskbar buttons
-   Toolbars (optional)
-   Notification area

The **Start** menu contains commands that can access programs, documents, and settings. These commands include **All Programs**, **Documents**, **Control Panel**, **Games**, **Help and Support**, **Shut down**, and **Search programs and files**.

The **Start** in earlier versions of Windows contained items such as **Find** and **Run**, the functionality of which was included in **Search programs and files** in Windows Vista and later.

The Quick Launch bar, available in versions of Windows earlier than Windows 7, contains shortcuts to applications. Windows provides default entries, such as Windows Internet Explorer, and the user can add any further shortcuts that they choose. Icons in this area respond to a single click. In Windows 7 and later, this functionality is included in the taskbar buttons.

The Shell places a button on the taskbar whenever an application creates an unowned window—that is, a window that does not have a parent and that has the appropriate extended style bits (see [Managing Taskbar Buttons](#managing-taskbar-buttons), below). To switch to a window, the user clicks its window button. This functionality has been greatly expanded as of Windows 7. For more information, see [Taskbar Extensions](taskbar-extensions.md).

Applications can put icons in the notification area to indicate the status of an operation or to notify the user about an event. For example, an application might put a printer icon in the notification area to show that a print job is under way. However, in Windows 7 and later, some of the information previously provided by the notification area should be provided through an application's taskbar button. The notification area is located at the right edge of the taskbar (if the taskbar is horizontal) or at the bottom (if the taskbar is vertical). For more information, see [Notifications and the Notification Area](notification-area.md).

The notification area also displays the current time if that option is selected. The option is found as:

-   **Windows 7 and later**: The **Clock** drop-down list in the **Turn system icons on or off** page of the **Notification Area Icons** Control Panel application (also accessible through the notification area properties).
-   **Windows Vista**: The **Clock** check box in the **Notification Area** page of the **Taskbar and Start Menu** properties window.
-   **Windows XP**: The **Show the clock** check box in the **Taskbar and Start Menu** properties window.

The user can right-click the taskbar to display the shortcut menu. The shortcut menu includes commands to cascade windows, stack windows, show windows side-by-side, show the desktop, start Task Manager, and set taskbar properties. The shortcut menu also provides the option to add or remove a set of toolbars from the taskbar. You can add new toolbars to this menu by registering them under the CATID\_DeskBand category. For more information, see [Implementing Band Objects](band-objects.md). Note that as of Windows 7, the taskbar and the notification area have separate shortcut menus. These shortcut menus share some options, such as window arrangement, and add others.

### Taskbar Display Options

The taskbar supports two display options: Auto-Hide and, in Windows Vista and earlier only, Always On Top (the taskbar is always in this mode in Windows 7 and later). To set these options, the user must open the taskbar shortcut menu, click **Properties**, and select or clear the **Auto-hide the taskbar** check box or the **Keep the taskbar on top of other windows** check box. To retrieve the state of these display options, use the [**ABM\_GETSTATE**](abm-getstate.md) message. If you would like to be notified when the state of these display options changes, process the [**ABN\_STATECHANGE**](abn-statechange.md) notification message in your window procedure. To change the state of these display options, use the [**ABM\_SETSTATE**](abm-setstate.md) message.

The *work area* is the portion of the screen not obscured by the taskbar. To retrieve the size of the work area, call the [**SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa) function with the **SPI\_GETWORKAREA** value set. To retrieve the rectangle coordinates that describe the location of the taskbar, use the [**ABM\_GETTASKBARPOS**](abm-gettaskbarpos.md) message.

It is possible to cover the taskbar by explicitly setting the size of the window rectangle equal to the size of the screen with [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos). For Windows 2000 systems or later, the window must lack either [**WS\_CAPTION**](../winmsg/window-styles.md) or [**WS\_THICKFRAME**](../winmsg/window-styles.md), or else the window must be sized so that the client area covers the entire screen. Also particular to those systems, if the taskbar is set to Always On Top, it will remain hidden only while the application is the foreground application.

### Adding Shortcuts to the Start Menu

To add an item to the **Programs** submenu on Microsoft Windows NT 4.0, Windows 2000 and later, or Windows 95 or later, follow these steps.

1.  Create a [shell link](./links.md) by using the [**IShellLink**](/windows/desktop/api/Shobjidl_core/nn-shobjidl_core-ishelllinka) interface.
2.  Obtain the PIDL of the Programs folder by using [**SHGetSpecialFolderLocation**](/windows/desktop/api/shlobj_core/nf-shlobj_core-shgetspecialfolderlocation), passing [**CSIDL\_PROGRAMS**](csidl.md).
3.  Add the Shell link to the Programs folder. You can also create a folder in the Programs folder and add the link to that folder.

### Managing Taskbar Buttons

The Shell creates a button on the taskbar whenever an application creates a window that isn't owned. To ensure that the window button is placed on the taskbar, create an unowned window with the [**WS\_EX\_APPWINDOW**](../winmsg/extended-window-styles.md) extended style. To prevent the window button from being placed on the taskbar, create the unowned window with the [**WS\_EX\_TOOLWINDOW**](../winmsg/extended-window-styles.md) extended style. As an alternative, you can create a hidden window and make this hidden window the owner of your visible window.

The Shell will remove a window's button from the taskbar only if the window's style supports visible taskbar buttons. If you want to dynamically change a window's style to one that does not support visible taskbar buttons, you must hide the window first (by calling [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) with **SW\_HIDE**), change the window style, and then show the window.

The window button typically contains the application icon and title. However, if the application does not contain a system menu, the window button is created without the icon.

If you want your application to get the user's attention when the window is not active, use the [**FlashWindow**](/windows/win32/api/winuser/nf-winuser-flashwindow) function to let the user know that a message is waiting. This function flashes the window button. Once the user clicks the window button to activate the window, your application can display the message.

### Modifying the Contents of the Taskbar

[Version 4.71 and later](versions.md) of Shell32.dll adds the capability to modify the contents of the taskbar. From an application, you can now add, remove, and activate taskbar buttons. Activating the item does not activate the window; it shows the item as pressed on the taskbar.

The taskbar modification capabilities are implemented in a Component Object Model (COM) object (CLSID\_TaskbarList ) that exposes the [**ITaskbarList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist) interface (IID\_ITaskbarList). You must call the [**ITaskbarList::HrInit**](/windows/desktop/api/shobjidl_core/nf-shobjidl_core-itaskbarlist-hrinit) method to initialize the object. You can then use the methods of the [**ITaskbarList**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-itaskbarlist) interface to modify the contents of the taskbar.

### Adding, Modifying, and Deleting Icons in the Notification Area

Use the [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) function to add, modify, or delete icons from the notification area. The *dwMessage* parameter of **Shell\_NotifyIcon** is a message to the taskbar that specifies the action to be taken. The *pnid* parameter is a pointer to a [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure that is used to identify the icon and pass any additional information that is needed for the system to process the message.

You can perform the following actions with notification area icons.

-   To add an icon to the taskbar's notification area, call [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with the *dwMessage* parameter set to NIM\_ADD. The [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure is used to specify the icon's handle and identifier, and any tooltip text. If the user has selected the **Show Clock** check box in the taskbar properties, the system places the icon to the immediate left of the clock. Otherwise, the icon appears on the right side or at the bottom of the taskbar. Any existing icons are shifted to the left to make room for the new icon.
-   To modify an icon's information, including its icon handle, tooltip text, and callback message identifier, call [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with *dwMessage* set to NIM\_MODIFY.
-   To delete an icon from the notification area, call [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with the *dwMessage* parameter set to NIM\_DELETE.

When you have completed a user interface operation, return focus to the notification area by calling [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with *dwMessage* set to NIM\_SETFOCUS. For example, you could do this when a taskbar icon displays a shortcut menu, but the user cancels it by pressing the ESCAPE key.

### Receiving Notification Area Callback Messages

Applications commonly put icons in the notification area of the taskbar to serve as status indicators. You can provide additional information when the user performs mouse actions, such as moving the mouse pointer over the icon or clicking the icon.

The system notifies you of mouse and keyboard events by sending an application-defined callback message that is associated with a particular icon. In this way, the system can notify an application when the user, for instance, clicks the icon or selects it by pressing a key.

You define an icon's callback message when you add the icon to the taskbar. The callback message identifier is specified in the **uCallbackMessage** member of the [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure passed with NIM\_ADD. When an event occurs, the system sends the callback message to the window procedure of the window specified by the **hWnd** member. The *wParam* parameter of the message contains the identifier of the taskbar icon in which the event occurred. The *lParam* parameter holds the mouse or keyboard message associated with the event. For example, when the mouse pointer moves onto a taskbar icon, *lParam* contains [**WM\_MOUSEMOVE**](../inputdev/wm-mousemove.md).

The results of various mouse events can be summarized as follows:

-   When the user moves the mouse pointer over the icon, the system displays the tooltip text that was specified in [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa).
-   When the user clicks the icon, your application receives a [**WM\_LBUTTONDOWN**](../inputdev/wm-lbuttondown.md) notification.
-   When the user right-clicks the icon, your application receives a [**WM\_RBUTTONDOWN**](../inputdev/wm-rbuttondown.md) notification.
-   When the user double-clicks the icon, your application receives a [**WM\_LBUTTONDBLCLK**](../inputdev/wm-lbuttondblclk.md) notification.

Typically, clicking the icon causes the application to display a window with additional information, right-clicking displays a shortcut menu, and double-clicking executes the default shortcut menu command.

For an example of how to change the tooltip text associated with a notification area icon, see [Balloon Tooltips for Status Bar Icons](../controls/tooltip-controls.md).

Versions 5.0 and later of the Shell handle [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) mouse and keyboard events in different ways than earlier Shell versions found on Windows NT 4.0, Windows 95, and Windows 98. The differences are as follows:

-   If a user requests a notify icon's shortcut menu with the keyboard, the version 5.0 Shell sends the associated application a [**WM\_CONTEXTMENU**](../menurc/wm-contextmenu.md) message. Earlier versions send [**WM\_RBUTTONDOWN**](../inputdev/wm-rbuttondown.md) and [**WM\_RBUTTONUP**](../inputdev/wm-rbuttonup.md) messages.
-   If a user selects a notify icon with the keyboard and activates it with the space bar or ENTER key, the version 5.0 Shell sends the associated application an **NIN\_KEYSELECT** notification. Earlier versions send [**WM\_RBUTTONDOWN**](../inputdev/wm-rbuttondown.md) and [**WM\_RBUTTONUP**](../inputdev/wm-rbuttonup.md) messages.
-   If a user selects a notify icon with the mouse and activates it with the ENTER key, the version 5.0 Shell sends the associated application an **NIN\_SELECT** notification. Earlier versions send [**WM\_RBUTTONDOWN**](../inputdev/wm-rbuttondown.md) and [**WM\_RBUTTONUP**](../inputdev/wm-rbuttonup.md) messages.
-   If a user passes the mouse pointer over an icon with which a balloon tooltip is associated, the version 6.0 Shell (Windows XP)sends the following messages.
    -   -   **NIN\_BALLOONSHOW** - Sent when the balloon is shown (balloons are queued).
        -   **NIN\_BALLOONHIDE** - Sent when the balloon disappears—for example, when the icon is deleted. This message is not sent if the balloon is dismissed because of a timeout or a mouse click.
        -   **NIN\_BALLOONTIMEOUT** - Sent when the balloon is dismissed because of a timeout.
        -   **NIN\_BALLOONUSERCLICK** - Sent when the balloon is dismissed because of a mouse click.

You can select which way the Shell should behave by calling [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with *dwMessage* set to **NIM\_SETVERSION**. Set the **uVersion** member of the [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure to indicate whether you want version 5.0 or pre-version 5.0 behavior.

### Taskbar Creation Notification

With Microsoft Internet Explorer 4.0 and later, the Shell notifies applications that the taskbar has been created. When the taskbar is created, it registers a message with the TaskbarCreated string and then broadcasts this message to all top-level windows. When your taskbar application receives this message, it should assume that any taskbar icons it added have been removed and add them again. This feature generally applies only to services that are already running when the Shell launches. The following example shows a very simplified method for handling this case.

On Windows 10, the taskbar also broadcasts this message when the DPI of the primary display changes.

```
LRESULT CALLBACK WndProc(HWND hWnd, 
                         UINT uMessage, 
                         WPARAM wParam, 
                         LPARAM lParam)
{
    static UINT s_uTaskbarRestart;

    switch(uMessage)
    {
        case WM_CREATE:
            s_uTaskbarRestart = RegisterWindowMessage(TEXT("TaskbarCreated"));
            break;
        
        default:
            if(uMessage == s_uTaskbarRestart)
                AddTaskbarIcons();
            break;
    }

    return DefWindowProc(hWnd, uMessage, wParam, lParam);
}
```



## Using the Taskbar

This section includes examples that demonstrate how to add icons to the taskbar notification area and how to process callback messages for taskbar icons.

### Adding and Deleting Taskbar Icons in the Notification Area

You add an icon to the taskbar notification area by filling in a [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure and then passing the structure to [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with *dwMessage* set to **NIM\_ADD**. The structure members must specify the handle to the window that is adding the icon, as well as the icon identifier and icon handle. You can also specify tooltip text for the icon. If you need to receive mouse messages for the icon, specify the identifier of the callback message that the system should use to send the message to the window procedure.

The function in the following example demonstrates how to add an icon to the taskbar.


```
// MyTaskBarAddIcon - adds an icon to the notification area. 
// Returns TRUE if successful, or FALSE otherwise. 
// hwnd - handle to the window to receive callback messages 
// uID - identifier of the icon 
// hicon - handle to the icon to add 
// lpszTip - tooltip text 

BOOL MyTaskBarAddIcon(HWND hwnd, UINT uID, HICON hicon, LPSTR lpszTip) 
{ 
    BOOL res; 
    NOTIFYICONDATA tnid; 
 
    tnid.cbSize = sizeof(NOTIFYICONDATA); 
    tnid.hWnd = hwnd; 
    tnid.uID = uID; 
    tnid.uFlags = NIF_MESSAGE | NIF_ICON | NIF_TIP; 
    tnid.uCallbackMessage = MYWM_NOTIFYICON; 
    tnid.hIcon = hicon; 
    if (lpszTip) 
        hr = StringCbCopyN(tnid.szTip, sizeof(tnid.szTip), lpszTip, 
                           sizeof(tnid.szTip));
        // TODO: Add error handling for the HRESULT.
    else 
        tnid.szTip[0] = (TCHAR)'\0'; 
 
    res = Shell_NotifyIcon(NIM_ADD, &tnid); 
 
    if (hicon) 
        DestroyIcon(hicon); 
 
    return res; 
}
```



To delete an icon from the taskbar notification area, fill a [**NOTIFYICONDATA**](/windows/desktop/api/Shellapi/ns-shellapi-notifyicondataa) structure and call [**Shell\_NotifyIcon**](/windows/desktop/api/Shellapi/nf-shellapi-shell_notifyicona) with *dwMessage* set to **NIM\_DELETE**. When deleting a taskbar icon, specify only the **cbSize**, **hWnd**, and **uID** members of the structure. For example:


```
// MyTaskBarDeleteIcon - deletes an icon from the notification area. 
// Returns TRUE if successful, or FALSE otherwise. 
// hwnd - handle to the window that added the icon. 
// uID - identifier of the icon to delete. 

BOOL MyTaskBarDeleteIcon(HWND hwnd, UINT uID) 
{ 
    BOOL res; 
    NOTIFYICONDATA tnid; 
 
    tnid.cbSize = sizeof(NOTIFYICONDATA); 
    tnid.hWnd = hwnd; 
    tnid.uID = uID; 
         
    res = Shell_NotifyIcon(NIM_DELETE, &tnid); 
    return res; 
}
```



### Receiving Mouse Events

If you specify a callback message for a taskbar icon, the system sends the message to your application whenever a mouse event occurs in the icon's bounding rectangle. The *wParam* parameter of the message specifies the identifier of the taskbar icon, and the *lParam* parameter of the message specifies the message that the system generated as a result of the mouse event.

The function in the following example is from an application that adds both battery and printer icons to the taskbar. The application calls the function when it receives a callback message. The function determines whether the user has clicked one of the icons and, if a click has occurred, calls an application-defined function to display status information.


```
// On_MYWM_NOTIFYICON - processes callback messages for taskbar icons. 
// wParam - first message parameter of the callback message. 
// lParam - second message parameter of the callback message. 

void On_MYWM_NOTIFYICON(WPARAM wParam, LPARAM lParam) 
{ 
    UINT uID; 
    UINT uMouseMsg; 
 
    uID = (UINT) wParam; 
    uMouseMsg = (UINT) lParam; 
 
    if (uMouseMsg == WM_LBUTTONDOWN) 
    { 
        switch (uID) 
        { 
            case IDI_MYBATTERYICON: 
 
                // The user clicked the battery icon. Display the 
                // battery status. 
                ShowBatteryStatus(); 
                break; 
 
            case IDI_MYPRINTERICON: 
 
                // The user clicked the printer icon. Display the 
                // status of the print job. 
                ShowJobStatus(); 
                break; 
 
            default: 
                break; 
        } 
     } 

     return; 
 }
```



 

 
