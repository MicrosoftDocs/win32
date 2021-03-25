---
description: This overview discusses features of windows such as window types, states, size, and position.
ms.assetid: 8318c22f-85a2-490e-8233-ee1e234890d9
title: Window Features
ms.topic: article
ms.date: 05/31/2018
---

# Window Features

This overview discusses features of windows such as window types, states, size, and position.

-   [Window Types](#window-types)
    -   [Overlapped Windows](#overlapped-windows)
    -   [Pop-up Windows](#pop-up-windows)
    -   [Child Windows](#child-windows)
        -   [Positioning](#positioning)
        -   [Clipping](#clipping)
        -   [Relationship to Parent Window](#relationship-to-parent-window)
        -   [Messages](#size-and-position-messages)
    -   [Layered Windows](#layered-windows)
    -   [Message-Only Windows](#message-only-windows)
-   [Window Relationships](#window-relationships)
    -   [Foreground and Background Windows](#foreground-and-background-windows)
    -   [Owned Windows](#owned-windows)
    -   [Z-Order](#z-order)
-   [Window Show State](#window-show-state)
    -   [Active Window](#active-window)
    -   [Disabled Windows](#disabled-windows)
    -   [Window Visibility](#window-visibility)
    -   [Minimized, Maximized, and Restored Windows](#minimized-maximized-and-restored-windows)
-   [Window Size and Position](#window-size-and-position)
    -   [Default Size and Position](#default-size-and-position)
    -   [Tracking Size](#tracking-size)
    -   [System Commands](#system-commands)
    -   [Size and Position Functions](#size-and-position-functions)
    -   [Size and Position Messages](#size-and-position-messages)
-   [Window Animation](#window-animation)
-   [Window Layout and Mirroring](#window-layout-and-mirroring)
    -   [Mirroring Dialog Boxes and Message Boxes](#mirroring-dialog-boxes-and-message-boxes)
    -   [Mirroring Device Contexts Not Associated with a Window](#mirroring-device-contexts-not-associated-with-a-window)
-   [Window Destruction](#window-destruction)

## Window Types

This section contains the following topics that describe window types.

-   [Overlapped Windows](#overlapped-windows)
-   [Pop-up Windows](#pop-up-windows)
-   [Child Windows](#child-windows)
-   [Layered Windows](#layered-windows)
-   [Message-Only Windows](#message-only-windows)

### Overlapped Windows

An *overlapped window* is a top-level window (non-child window) that has a title bar, border, and client area; it is meant to serve as an application's main window. It can also have a window menu, minimize and maximize buttons, and scroll bars. An overlapped window used as a main window typically includes all of these components.

By specifying the [**WS\_OVERLAPPED**](window-styles.md) or **WS\_OVERLAPPEDWINDOW** style in the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function, an application creates an overlapped window. If you use the **WS\_OVERLAPPED** style, the window has a title bar and border. If you use the **WS\_OVERLAPPEDWINDOW** style, the window has a title bar, sizing border, window menu, and minimize and maximize buttons.

### Pop-up Windows

A *pop-up window* is a special type of overlapped window used for dialog boxes, message boxes, and other temporary windows that appear outside an application's main window. Title bars are optional for pop-up windows; otherwise, pop-up windows are the same as overlapped windows of the [**WS\_OVERLAPPED**](window-styles.md) style.

You create a pop-up window by specifying the [**WS\_POPUP**](window-styles.md) style in [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa). To include a title bar, specify the **WS\_CAPTION** style. Use the **WS\_POPUPWINDOW** style to create a pop-up window that has a border and a window menu. The **WS\_CAPTION** style must be combined with the **WS\_POPUPWINDOW** style to make the window menu visible.

### Child Windows

A *child window* has the [**WS\_CHILD**](window-styles.md) style and is confined to the client area of its parent window. An application typically uses child windows to divide the client area of a parent window into functional areas. You create a child window by specifying the **WS\_CHILD** style in the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function.

A child window must have a parent window. The parent window can be an overlapped window, a pop-up window, or even another child window. You specify the parent window when you call [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa). If you specify the [**WS\_CHILD**](window-styles.md) style in **CreateWindowEx** but do not specify a parent window, the system does not create the window.

A child window has a client area but no other features, unless they are explicitly requested. An application can request a title bar, a window menu, minimize and maximize buttons, a border, and scroll bars for a child window, but a child window cannot have a menu. If the application specifies a menu handle, either when it registers the child's window class or creates the child window, the menu handle is ignored. If no border style is specified, the system creates a borderless window. An application can use borderless child windows to divide a parent window's client area while keeping the divisions invisible to the user.

This section discusses the following aspects of child windows:

-   [Positioning](#positioning)
-   [Clipping](#clipping)
-   [Relationship to Parent Window](#relationship-to-parent-window)
-   [Messages](#size-and-position-messages)

#### Positioning

The system always positions a child window relative to the upper left corner of its parent window's client area. No part of a child window ever appears outside the borders of its parent window. If an application creates a child window that is larger than the parent window or positions a child window so that some or all of the child window extends beyond the borders of the parent, the system clips the child window; that is, the portion outside the parent window's client area is not displayed. Actions that affect the parent window can also affect the child window, as follows.



| Parent Window | Child Window                                                                                                             |
|---------------|--------------------------------------------------------------------------------------------------------------------------|
| Destroyed     | Destroyed before the parent window is destroyed.                                                                         |
| Hidden        | Hidden before the parent window is hidden. A child window is visible only when the parent window is visible.             |
| Moved         | Moved with the parent window's client area. The child window is responsible for painting its client area after the move. |
| Shown         | Shown after the parent window is shown.                                                                                  |



 

#### Clipping

The system does not automatically clip a child window from the parent window's client area. This means the parent window draws over the child window if it carries out any drawing in the same location as the child window. However, the system does clip the child window from the parent window's client area if the parent window has the [**WS\_CLIPCHILDREN**](window-styles.md) style. If the child window is clipped, the parent window cannot draw over it.

A child window can overlap other child windows in the same client area. A child window that shares the same parent window as one or more other child windows is called a *sibling window*. Sibling windows can draw in each other's client area, unless one of the child windows has the [**WS\_CLIPSIBLINGS**](window-styles.md) style. If a child window does have this style, any portion of its sibling window that lies within the child window is clipped.

If a window has either the [**WS\_CLIPCHILDREN**](window-styles.md) or **WS\_CLIPSIBLINGS** style, a slight loss in performance occurs. Each window takes up system resources, so an application should not use child windows indiscriminately. For best performance, an application that needs to logically divide its main window should do so in the window procedure of the main window rather than by using child windows.

#### Relationship to Parent Window

An application can change the parent window of an existing child window by calling the [**SetParent**](/windows/win32/api/winuser/nf-winuser-setparent) function. In this case, the system removes the child window from the client area of the old parent window and moves it to the client area of the new parent window. If **SetParent** specifies a **NULL** handle, the desktop window becomes the new parent window. In this case, the child window is drawn on the desktop, outside the borders of any other window. The [**GetParent**](/windows/win32/api/winuser/nf-winuser-getparent) function retrieves a handle to a child window's parent window.

The parent window relinquishes a portion of its client area to a child window, and the child window receives all input from this area. The window class need not be the same for each of the child windows of the parent window. This means that an application can fill a parent window with child windows that look different and carry out different tasks. For example, a dialog box can contain many types of controls, each one a child window that accepts different types of data from the user.

A child window has only one parent window, but a parent can have any number of child windows. Each child window, in turn, can have child windows. In this chain of windows, each child window is called a descendant window of the original parent window. An application uses the [**IsChild**](/windows/win32/api/winuser/nf-winuser-ischild) function to discover whether a given window is a child window or a descendant window of a given parent window.

The [**EnumChildWindows**](/windows/win32/api/winuser/nf-winuser-enumchildwindows) function enumerates the child windows of a parent window. Then, **EnumChildWindows** passes the handle to each child window to an application-defined callback function. Descendant windows of the given parent window are also enumerated.

#### Messages

The system passes a child window's input messages directly to the child window; the messages are not passed through the parent window. The only exception is if the child window has been disabled by the [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow) function. In this case, the system passes any input messages that would have gone to the child window to the parent window instead. This permits the parent window to examine the input messages and enable the child window, if necessary.

A child window can have a unique integer identifier. Child window identifiers are important when working with control windows. An application directs a control's activity by sending it messages. The application uses the control's child window identifier to direct the messages to the control. In addition, a control sends notification messages to its parent window. A notification message includes the control's child window identifier, which the parent uses to identify which control sent the message. An application specifies the child-window identifier for other types of child windows by setting the *hMenu* parameter of the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function to a value rather than a menu handle.

### Layered Windows

Using a layered window can significantly improve performance and visual effects for a window that has a complex shape, animates its shape, or wishes to use alpha blending effects. The system automatically composes and repaints layered windows and the windows of underlying applications. As a result, layered windows are rendered smoothly, without the flickering typical of complex window regions. In addition, layered windows can be partially translucent, that is, alpha-blended.

To create a layered window, specify the **WS\_EX\_LAYERED** extended window style when calling the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function, or call the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function to set **WS\_EX\_LAYERED** after the window has been created. After the **CreateWindowEx** call, the layered window will not become visible until the [**SetLayeredWindowAttributes**](/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes) or [**UpdateLayeredWindow**](/windows/win32/api/winuser/nf-winuser-updatelayeredwindow) function has been called for this window.

> [!Note]  
> Beginning with Windows 8, **WS\_EX\_LAYERED** can be used with child windows and top-level windows. Previous Windows versions support **WS\_EX\_LAYERED** only for top-level windows.

 

To set the opacity level or the transparency color key for a given layered window, call [**SetLayeredWindowAttributes**](/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes). After the call, the system may still ask the window to paint when the window is shown or resized. However, because the system stores the image of a layered window, the system will not ask the window to paint if parts of it are revealed as a result of relative window moves on the desktop. Legacy applications do not need to restructure their painting code if they want to add translucency or transparency effects for a window, because the system redirects the painting of windows that called **SetLayeredWindowAttributes** into off-screen memory and recomposes it to achieve the desired effect.

For faster and more efficient animation or if per-pixel alpha is needed, call [**UpdateLayeredWindow**](/windows/win32/api/winuser/nf-winuser-updatelayeredwindow). **UpdateLayeredWindow** should be used primarily when the application must directly supply the shape and content of a layered window, without using the redirection mechanism the system provides through [**SetLayeredWindowAttributes**](/windows/win32/api/winuser/nf-winuser-setlayeredwindowattributes). In addition, using **UpdateLayeredWindow** directly uses memory more efficiently, because the system does not need the additional memory required for storing the image of the redirected window. For maximum efficiency in animating windows, call **UpdateLayeredWindow** to change the position and the size of a layered window. Please note that after **SetLayeredWindowAttributes** has been called, subsequent **UpdateLayeredWindow** calls will fail until the layering style bit is cleared and set again.

Hit testing of a layered window is based on the shape and transparency of the window. This means that the areas of the window that are color-keyed or whose alpha value is zero will let the mouse messages through. However, if the layered window has the **WS\_EX\_TRANSPARENT** extended window style, the shape of the layered window will be ignored and the mouse events will be passed to other windows underneath the layered window.

### Message-Only Windows

A *message-only window* enables you to send and receive messages. It is not visible, has no z-order, cannot be enumerated, and does not receive broadcast messages. The window simply dispatches messages.

To create a message-only window, specify the [HWND\_MESSAGE](#message-only-windows) constant or a handle to an existing message-only window in the *hWndParent* parameter of the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function. You can also change an existing window to a message-only window by specifying HWND\_MESSAGE in the *hWndNewParent* parameter of the [**SetParent**](/windows/win32/api/winuser/nf-winuser-setparent) function.

To find message-only windows, specify [HWND\_MESSAGE](#message-only-windows) in the *hwndParent* parameter of the [**FindWindowEx**](/windows/win32/api/winuser/nf-winuser-findwindowexa) function. In addition, **FindWindowEx** searches message-only windows as well as top-level windows if both the *hwndParent* and *hwndChildAfter* parameters are **NULL**.

## Window Relationships

There are many ways that a window can relate to the user or another window. A window may be an owned window, foreground window, or background window. A window also has a z-order relative to other windows. For more information, see the following topics:

-   [Foreground and Background Windows](#foreground-and-background-windows)
-   [Owned Windows](#owned-windows)
-   [Z-Order](#z-order)

### Foreground and Background Windows

Each process can have multiple threads of execution, and each thread can create windows. The thread that created the window with which the user is currently working is called the foreground thread, and the window is called the *foreground window*. All other threads are background threads, and the windows created by background threads are called *background windows*.

Each thread has a priority level that determines the amount of CPU time the thread receives. Although an application can set the priority level of its threads, normally the foreground thread has a slightly higher priority level than the background threads. Because it has a higher priority, the foreground thread receives more CPU time than the background threads. The foreground thread has a normal base priority of 9; a background thread has a normal base priority of 7.

The user sets the foreground window by clicking a window, or by using the ALT+TAB or ALT+ESC key combination. To retrieve a handle to the foreground window, use the [**GetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-getforegroundwindow) function. To check if your application window is the foreground window, compare the handle returned by **GetForegroundWindow** to that of your application window.

An application sets the foreground window by using the [**SetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-setforegroundwindow) function.

The system restricts which processes can set the foreground window. A process can set the foreground window only if:

- All of the following conditions are true:
  - The process calling **SetForegroundWindow** belongs to a desktop application, not a UWP app or a Windows Store app designed for Windows 8 or 8.1.
  - The foreground process has not disabled calls to **SetForegroundWindow** by a previous call to the [**LockSetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-locksetforegroundwindow) function.
  - The foreground lock time-out has expired (see [**SPI_GETFOREGROUNDLOCKTIMEOUT** in **SystemParametersInfo**](/windows/win32/api/winuser/nf-winuser-systemparametersinfoa#SPI_GETFOREGROUNDLOCKTIMEOUT)).
  - No menus are active.
- Additionally, at least one of the following conditions is true:
  - The calling process is the foreground process.
  - The calling process was started by the foreground process.
  - There is currently no foreground window, and thus no foreground process.
  - The calling process received the last input event.
  - Either the foreground process or the calling process is being debugged.

It is possible for a process to be denied the right to set the foreground window even if it meets these conditions.

A process that can set the foreground window can enable another process to set the foreground window by calling the [**AllowSetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-allowsetforegroundwindow) function, or by calling the [**BroadcastSystemMessage**](/windows/win32/api/winuser/nf-winuser-broadcastsystemmessage) function with the **BSF\_ALLOWSFW** flag. The foreground process can disable calls to [**SetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-setforegroundwindow) by calling the [**LockSetForegroundWindow**](/windows/win32/api/winuser/nf-winuser-locksetforegroundwindow) function.

### Owned Windows

An overlapped or pop-up window can be owned by another overlapped or pop-up window. Being owned places several constraints on a window.

-   An owned window is always above its owner in the z-order.
-   The system automatically destroys an owned window when its owner is destroyed.
-   An owned window is hidden when its owner is minimized.

Only an overlapped or pop-up window can be an owner window; a child window cannot be an owner window. An application creates an owned window by specifying the owner's window handle as the *hwndParent* parameter of [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) when it creates a window with the [**WS\_OVERLAPPED**](window-styles.md) or **WS\_POPUP** style. The *hwndParent* parameter must identify an overlapped or pop-up window. If *hwndParent* identifies a child window, the system assigns ownership to the top-level parent window of the child window. After creating an owned window, an application cannot transfer ownership of the window to another window.

Dialog boxes and message boxes are owned windows by default. An application specifies the owner window when calling a function that creates a dialog box or message box.

An application can use the [**GetWindow**](/windows/win32/api/winuser/nf-winuser-getwindow) function with the **GW\_OWNER** flag to retrieve a handle to a window's owner.

### Z-Order

The *z-order* of a window indicates the window's position in a stack of overlapping windows. This window stack is oriented along an imaginary axis, the z-axis, extending outward from the screen. The window at the top of the z-order overlaps all other windows. The window at the bottom of the z-order is overlapped by all other windows.

The system maintains the z-order in a single list. It adds windows to the z-order based on whether they are topmost windows, top-level windows, or child windows. A *topmost window* overlaps all other non-topmost windows, regardless of whether it is the active or foreground window. A topmost window has the **WS\_EX\_TOPMOST** style. All topmost windows appear in the z-order before any non-topmost windows. A child window is grouped with its parent in z-order.

When an application creates a window, the system puts it at the top of the z-order for windows of the same type. You can use the [**BringWindowToTop**](/windows/win32/api/winuser/nf-winuser-bringwindowtotop) function to bring a window to the top of the z-order for windows of the same type. You can rearrange the z-order by using the [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos) and [**DeferWindowPos**](/windows/win32/api/winuser/nf-winuser-deferwindowpos) functions.

The user changes the z-order by activating a different window. The system positions the active window at the top of the z-order for windows of the same type. When a window comes to the top of z-order, so do its child windows. You can use the [**GetTopWindow**](/windows/win32/api/winuser/nf-winuser-gettopwindow) function to search all child windows of a parent window and return a handle to the child window that is highest in z-order. The [**GetNextWindow**](/windows/win32/api/winuser/nf-winuser-getnextwindow) function retrieves a handle to the next or previous window in z-order.

## Window Show State

At any one given time, a window may be active or inactive; hidden or visible; and minimized, maximized, or restored. These qualities are referred to collectively as the *window show state*. The following topics discuss the window show state:

-   [Active Window](#active-window)
-   [Disabled Windows](#disabled-windows)
-   [Window Visibility](#window-visibility)
-   [Minimized, Maximized, and Restored Windows](#minimized-maximized-and-restored-windows)

### Active Window

An *active window* is the top-level window of the application with which the user is currently working. To allow the user to easily identify the active window, the system places it at the top of the z-order and changes the color of its title bar and border to the system-defined active window colors. Only a top-level window can be an active window. When the user is working with a child window, the system activates the top-level parent window associated with the child window.

Only one top-level window in the system is active at a time. The user activates a top-level window by clicking it (or one of its child windows), or by using the ALT+ESC or ALT+TAB key combination. An application activates a top-level window by calling the [**SetActiveWindow**](/windows/win32/api/winuser/nf-winuser-setactivewindow) function. Other functions can cause the system to activate a different top-level window, including [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos), [**DeferWindowPos**](/windows/win32/api/winuser/nf-winuser-deferwindowpos), [**SetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-setwindowplacement), and [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow). Although an application can activate a different top-level window at any time, to avoid confusing the user, it should do so only in response to a user action. An application uses the [**GetActiveWindow**](/windows/win32/api/winuser/nf-winuser-getactivewindow) function to retrieve a handle to the active window.

When the activation changes from a top-level window of one application to the top-level window of another, the system sends a [**WM\_ACTIVATEAPP**](wm-activateapp.md) message to both applications, notifying them of the change. When the activation changes to a different top-level window in the same application, the system sends both windows a [**WM\_ACTIVATE**](../inputdev/wm-activate.md) message.

### Disabled Windows

A window can be disabled. A *disabled window* receives no keyboard or mouse input from the user, but it can receive messages from other windows, from other applications, and from the system. An application typically disables a window to prevent the user from using the window. For example, an application may disable a push button in a dialog box to prevent the user from choosing it. An application can enable a disabled window at any time; enabling a window restores normal input.

By default, a window is enabled when created. An application can specify the [**WS\_DISABLED**](window-styles.md) style, however, to disable a new window. An application enables or disables an existing window by using the [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow) function. The system sends a [**WM\_ENABLE**](wm-enable.md) message to a window when its enabled state is about to change. An application can determine whether a window is enabled by using the [**IsWindowEnabled**](/windows/win32/api/winuser/nf-winuser-iswindowenabled) function.

When a child window is disabled, the system passes the child's mouse input messages to the parent window. The parent uses the messages to determine whether to enable the child window. For more information, see [Mouse Input](../inputdev/mouse-input.md).

Only one window at a time can receive keyboard input; that window is said to have the keyboard focus. If an application uses the [**EnableWindow**](/windows/win32/api/winuser/nf-winuser-enablewindow) function to disable a keyboard-focus window, the window loses the keyboard focus in addition to being disabled. **EnableWindow** then sets the keyboard focus to **NULL**, meaning no window has the focus. If a child window, or other descendant window, has the keyboard focus, the descendant window loses the focus when the parent window is disabled. For more information, see [Keyboard Input](../inputdev/keyboard-input.md).

### Window Visibility

A window can be either visible or hidden. The system displays a *visible window* on the screen. It hides a *hidden window* by not drawing it. If a window is visible, the user can supply input to the window and view the window's output. If a window is hidden, it is effectively disabled. A hidden window can process messages from the system or from other windows, but it cannot process input from the user or display output. An application sets a window's visibility state when creating the window. Later, the application can change the visibility state.

A window is visible when the [**WS\_VISIBLE**](window-styles.md) style is set for the window. By default, the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function creates a hidden window unless the application specifies the **WS\_VISIBLE** style. Typically, an application sets the **WS\_VISIBLE** style after it has created a window to keep details of the creation process hidden from the user. For example, an application may keep a new window hidden while it customizes the window's appearance. If the **WS\_VISIBLE** style is specified in **CreateWindowEx**, the system sends the [**WM\_SHOWWINDOW**](wm-showwindow.md) message to the window after creating the window, but before displaying it.

An application can determine whether a window is visible by using the [**IsWindowVisible**](/windows/win32/api/winuser/nf-winuser-iswindowvisible) function. An application can show (make visible) or hide a window by using the [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow), [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos), [**DeferWindowPos**](/windows/win32/api/winuser/nf-winuser-deferwindowpos), or [**SetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-setwindowplacement) or [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function. These functions show or hide a window by setting or removing the [**WS\_VISIBLE**](window-styles.md) style for the window. They also send the [**WM\_SHOWWINDOW**](wm-showwindow.md) message to the window before showing or hiding it.

When an owner window is minimized, the system automatically hides the associated owned windows. Similarly, when an owner window is restored, the system automatically shows the associated owned windows. In both cases, the system sends the [**WM\_SHOWWINDOW**](wm-showwindow.md) message to the owned windows before hiding or showing them. Occasionally, an application may need to hide the owned windows without having to minimize or hide the owner. In this case, the application uses the [**ShowOwnedPopups**](/windows/win32/api/winuser/nf-winuser-showownedpopups) function. This function sets or removes the [**WS\_VISIBLE**](window-styles.md) style for all owned windows and sends the **WM\_SHOWWINDOW** message to the owned windows before hiding or showing them. Hiding an owner window has no effect on the visibility state of the owned windows.

When a parent window is visible, its associated child windows are also visible. Similarly, when the parent window is hidden, its child windows are also hidden. Minimizing the parent window has no effect on the visibility state of the child windows; that is, the child windows are minimized along with the parent, but the [**WS\_VISIBLE**](window-styles.md) style is not changed.

Even if a window has the [**WS\_VISIBLE**](window-styles.md) style, the user may not be able to see the window on the screen; other windows may completely overlap it or it may have been moved beyond the edge of the screen. Also, a visible child window is subject to the clipping rules established by its parent-child relationship. If the window's parent window is not visible, it will also not be visible. If the parent window moves beyond the edge of the screen, the child window also moves because a child window is drawn relative to the parent's upper left corner. For example, a user may move the parent window containing the child window far enough off the edge of the screen that the user may not be able to see the child window, even though the child window and its parent window both have the **WS\_VISIBLE** style.

### Minimized, Maximized, and Restored Windows

A *maximized window* is a window that has the [**WS\_MAXIMIZE**](window-styles.md) style. By default, the system enlarges a maximized window so that it fills the screen or, in the case of a child window, the parent window's client area. Although a window's size can be set to the same size of a maximized window, a maximized window is slightly different. The system automatically moves the window's title bar to the top of the screen or to the top of the parent window's client area. Also, the system disables the window's sizing border and the window-positioning capability of the title bar (so that the user cannot move the window by dragging the title bar).

A *minimized window* is a window that has the [**WS\_MINIMIZE**](window-styles.md) style. By default, the system reduces a minimized window to the size of its taskbar button and moves the minimized window to the taskbar. A *restored window* is a window that has been returned to its previous size and position, that is, the size it was before it was minimized or maximized.

If an application specifies the [**WS\_MAXIMIZE**](window-styles.md) or **WS\_MINIMIZE** style in the [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) function, the window is initially maximized or minimized. After creating a window, an application can use the [**CloseWindow**](/windows/win32/api/winuser/nf-winuser-closewindow) function to minimize the window. The [**ArrangeIconicWindows**](/windows/win32/api/winuser/nf-winuser-arrangeiconicwindows) function arranges the icons on the desktop, or it arranges a parent window's minimized child windows in the parent window. The [**OpenIcon**](/windows/win32/api/winuser/nf-winuser-openicon) function restores a minimized window to its previous size and position.

The [**ShowWindow**](/windows/win32/api/winuser/nf-winuser-showwindow) function can minimize, maximize, or restore a window. It can also set the window's visibility and activation states. The [**SetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-setwindowplacement) function includes the same functionality as **ShowWindow**, but it can override the window's default minimized, maximized, and restored positions.

The [**IsZoomed**](/windows/win32/api/winuser/nf-winuser-iszoomed) and [**IsIconic**](/windows/win32/api/winuser/nf-winuser-isiconic) functions determine whether a given window is maximized or minimized, respectively. The [**GetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-getwindowplacement) function retrieves the minimized, maximized, and restored positions for the window, and also determines the window's show state.

When the system receives a command to maximize or restore a minimized window, it sends the window a [**WM\_QUERYOPEN**](wm-queryopen.md) message. If the window procedure returns **FALSE**, the system ignores the maximize or restore command.

The system automatically sets the size and position of a maximized window to the system-defined defaults for a maximized window. To override these defaults, an application can either call the [**SetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-setwindowplacement) function or process the [**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md) message that is received by a window when the system is about to maximize the window. **WM\_GETMINMAXINFO** includes a pointer to a [**MINMAXINFO**](/windows/win32/api/winuser/ns-winuser-minmaxinfo) structure containing values the system uses to set the maximized size and position. Replacing these values overrides the defaults.

## Window Size and Position

A window's size and position are expressed as a bounding rectangle, given in coordinates relative to the screen or the parent window. The coordinates of a top-level window are relative to the upper left corner of the screen; the coordinates of a child window are relative to the upper left corner of the parent window. An application specifies a window's initial size and position when it creates the window, but it can change the window's size and position at any time. For more information, see [Filled Shapes](../gdi/filled-shapes.md).

This section contains the following topics:

-   [Default Size and Position](#default-size-and-position)
-   [Tracking Size](#tracking-size)
-   [System Commands](#system-commands)
-   [Size and Position Functions](#size-and-position-functions)
-   [Size and Position Messages](#size-and-position-messages)

### Default Size and Position

An application can allow the system to calculate the initial size or position of a top-level window by specifying CW\_USEDEFAULT in [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa). If the application sets the window's coordinates to CW\_USEDEFAULT and has created no other top-level windows, the system sets the new window's position relative to the upper left corner of the screen; otherwise, it sets the position relative to the position of the top-level window that the application created most recently. If the width and height parameters are set to CW\_USEDEFAULT, the system calculates the size of the new window. If the application has created other top-level windows, the system bases the size of the new window on the size of the application's most recently created top-level window. Specifying CW\_USEDEFAULT when creating a child or pop-up window causes the system to set the window's size to the default minimum window size.

### Tracking Size

The system maintains a minimum and maximum tracking size for a window of the [**WS\_THICKFRAME**](window-styles.md) style; a window with this style has a sizing border. The *minimum tracking size* is the smallest window size you can produce by dragging the window's sizing border. Similarly, the *maximum tracking size* is the largest window size you can produce by dragging the sizing border.

A window's minimum and maximum tracking sizes are set to system-defined default values when the system creates the window. An application can discover the defaults and override them by processing the [**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md) message. For more information, see [Size and Position Messages](#size-and-position-messages).

### System Commands

An application that has a window menu can change the size and position of that window by sending system commands. System commands are generated when the user chooses commands from the window menu. An application can emulate the user action by sending a [**WM\_SYSCOMMAND**](../menurc/wm-syscommand.md) message to the window. The following system commands affect the size and position of a window.



| Command      | Description                                                                                                                                                          |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SC\_CLOSE    | Closes the window. This command sends a [**WM\_CLOSE**](wm-close.md) message to the window. The window carries out any steps needed to clean up and destroy itself. |
| SC\_MAXIMIZE | Maximizes the window.                                                                                                                                                |
| SC\_MINIMIZE | Minimizes the window.                                                                                                                                                |
| SC\_MOVE     | Moves the window.                                                                                                                                                    |
| SC\_RESTORE  | Restores a minimized or maximized window to its previous size and position.                                                                                          |
| SC\_SIZE     | Starts a size command. To change the size of the window, use the mouse or keyboard.                                                                                  |



 

### Size and Position Functions

After creating a window, an application can set the window's size or position by calling one of several different functions, including [**SetWindowPlacement**](/windows/win32/api/winuser/nf-winuser-setwindowplacement), [**MoveWindow**](/windows/win32/api/winuser/nf-winuser-movewindow), [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos), and [**DeferWindowPos**](/windows/win32/api/winuser/nf-winuser-deferwindowpos). **SetWindowPlacement** sets a window's minimized position, maximized position, restored size and position, and show state. The **MoveWindow** and **SetWindowPos** functions are similar; both set the size or position of a single application window. The **SetWindowPos** function includes a set of flags that affect the window's show state; **MoveWindow** does not include these flags. Use the [**BeginDeferWindowPos**](/windows/win32/api/winuser/nf-winuser-begindeferwindowpos), **DeferWindowPos**, and [**EndDeferWindowPos**](/windows/win32/api/winuser/nf-winuser-enddeferwindowpos) functions to simultaneously set the position of a number of windows, including the size, position, position in the z-order, and show state.

An application can retrieve the coordinates of a window's bounding rectangle by using the [**GetWindowRect**](/windows/win32/api/winuser/nf-winuser-getwindowrect) function. **GetWindowRect** fills a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure with the coordinates of the window's upper left and lower right corners. The coordinates are relative to the upper left corner of the screen, even for a child window. The [**ScreenToClient**](/windows/win32/api/winuser/nf-winuser-screentoclient) or [**MapWindowPoints**](/windows/win32/api/winuser/nf-winuser-mapwindowpoints) function maps the screen coordinates of a child window's bounding rectangle to coordinates relative to the parent window's client area.

The [**GetClientRect**](/windows/win32/api/winuser/nf-winuser-getclientrect) function retrieves the coordinates of a window's client area. **GetClientRect** fills a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure with the coordinates of the upper left and lower right corners of the client area, but the coordinates are relative to the client area itself. This means the coordinates of a client area's upper left corner are always (0,0), and the coordinates of the lower right corner are the width and height of the client area.

The [**CascadeWindows**](/windows/win32/api/winuser/nf-winuser-cascadewindows) function cascades the windows on the desktop or cascades the child windows of the specified parent window. The [**TileWindows**](/windows/win32/api/winuser/nf-winuser-tilewindows) function tiles the windows on the desktop or tiles the child windows of the specified parent window.

### Size and Position Messages

The system sends the [**WM\_GETMINMAXINFO**](wm-getminmaxinfo.md) message to a window whose size or position is about to change. For example, the message is sent when the user clicks **Move** or **Size** from the window menu or clicks the sizing border or title bar; the message is also sent when an application calls [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos) to move or size the window. **WM\_GETMINMAXINFO** includes a pointer to a [**MINMAXINFO**](/windows/win32/api/winuser/ns-winuser-minmaxinfo) structure containing the default maximized size and position for the window, as well as the default minimum and maximum tracking sizes. An application can override the defaults by processing **WM\_GETMINMAXINFO** and setting the appropriate members of **MINMAXINFO**. A window must have the [**WS\_THICKFRAME**](window-styles.md) or **WS\_CAPTION** style to receive **WM\_GETMINMAXINFO**. A window with the **WS\_THICKFRAME** style receives this message during the window-creation process, as well as when it is being moved or sized.

The system sends the [**WM\_WINDOWPOSCHANGING**](wm-windowposchanging.md) message to a window whose size, position, position in the z-order, or show state is about to change. This message includes a pointer to a [**WINDOWPOS**](/windows/win32/api/winuser/ns-winuser-windowpos) structure that specifies the window's new size, position, position in the z-order, and show state. By setting the members of **WINDOWPOS**, an application can affect the window's new size, position, and appearance.

After changing a window's size, position, position in the z-order, or show state, the system sends the [**WM\_WINDOWPOSCHANGED**](wm-windowposchanged.md) message to the window. This message includes a pointer to [**WINDOWPOS**](/windows/win32/api/winuser/ns-winuser-windowpos) that informs the window of its new size, position, position in the z-order, and show state. Setting the members of the **WINDOWPOS** structure that is passed with **WM\_WINDOWPOSCHANGED** has no effect on the window. A window that must process [**WM\_SIZE**](wm-size.md) and [**WM\_MOVE**](wm-move.md) messages must pass **WM\_WINDOWPOSCHANGED** to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function; otherwise, the system does not send **WM\_SIZE** and **WM\_MOVE** messages to the window.

The system sends the [**WM\_NCCALCSIZE**](wm-nccalcsize.md) message to a window when the window is created or sized. The system uses the message to calculate the size of a window's client area and the position of the client area relative to the upper left corner of the window. A window typically passes this message to the default window procedure; however, this message can be useful in applications that customize a window's nonclient area or preserve portions of the client area when the window is sized. For more information, see [Painting and Drawing](../gdi/painting-and-drawing.md).

## Window Animation

You can produce special effects when showing or hiding windows by using the [**AnimateWindow**](/windows/win32/api/winuser/nf-winuser-animatewindow) function. When the window is animated in this manner, the system will either roll, slide, or fade the window, depending on the flags you specify in a call to **AnimateWindow**.

By default, the system uses *roll animation*. With this effect, the window appears to roll open (showing the window) or roll closed (hiding the window). You can use the *dwFlags* parameter to specify whether the window rolls horizontally, vertically, or diagonally.

When you specify the **AW\_SLIDE** flag, the system uses *slide animation*. With this effect, the window appears to slide into view (showing the window) or slide out of view (hiding the window). You can use the *dwFlags* parameter to specify whether the window slides horizontally, vertically, or diagonally.

When you specify the **AW\_BLEND** flag, the system uses an *alpha-blended fade*.

You can also use the **AW\_CENTER** flag to make a window appear to collapse inward or expand outward.

## Window Layout and Mirroring

The window layout defines how text and Windows Graphics Device Interface (GDI) objects are laid out in a window or device context (DC). Some languages, such as English, French, and German, require a left-to-right (LTR) layout. Other languages, such as Arabic and Hebrew, require right-to-left (RTL) layout. The window layout applies to text but also affects the other GDI elements of the window, including bitmaps, icons, the location of the origin, buttons, cascading tree controls, and whether the horizontal coordinate increases as you go left or right. For example, after an application has set RTL layout, the origin is positioned at the right edge of the window or device, and the number representing the horizontal coordinate increases as you move left. However, not all objects are affected by the layout of a window. For example, the layout for dialog boxes, message boxes, and device contexts that are not associated with a window, such as metafile and printer DCs, must be handled separately. Specifics for these are mentioned later in this topic.

The window functions allow you to specify or change the window layout in Arabic and Hebrew versions of Windows. Note that changing to a RTL layout (also known as mirroring) is not supported for windows that have the style [CS\_OWNDC](about-window-classes.md) or for a DC with the GM\_ADVANCED graphic mode.

By default, the window layout is left-to-right (LTR). To set the RTL window layout, call [**CreateWindowEx**](/windows/win32/api/winuser/nf-winuser-createwindowexa) with the style **WS\_EX\_LAYOUTRTL**. Also by default, a child window (that is, one created with the [**WS\_CHILD**](window-styles.md) style and with a valid parent *hWnd* parameter in the call to [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) or **CreateWindowEx**) has the same layout as its parent. To disable inheritance of mirroring to all child windows, specify **WS\_EX\_NOINHERITLAYOUT** in the call to **CreateWindowEx**. Note, mirroring is not inherited by owned windows (those created without the **WS\_CHILD** style) or those created with the parent *hWnd* parameter in **CreateWindowEx** set to **NULL**. To disable inheritance of mirroring for an individual window, process the [**WM\_NCCREATE**](wm-nccreate.md) message with [**GetWindowLong**](/windows/win32/api/winuser/nf-winuser-getwindowlonga) and [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) to turn off the **WS\_EX\_LAYOUTRTL** flag. This processing is in addition to whatever other processing is needed. The following code fragment shows how this is done.


```
SetWindowLong (hWnd, 
               GWL_EXSTYLE, 
               GetWindowLong(hWnd,GWL_EXSTYLE) & ~WS_EX_LAYOUTRTL))
```



You can set the default layout to RTL by calling [**SetProcessDefaultLayout**](/windows/win32/api/winuser/nf-winuser-setprocessdefaultlayout)(LAYOUT\_RTL). All windows created after the call will be mirrored, but existing windows are not affected. To turn off default mirroring, call **SetProcessDefaultLayout**(0).

Note, [**SetProcessDefaultLayout**](/windows/win32/api/winuser/nf-winuser-setprocessdefaultlayout) mirrors the DCs only of mirrored windows. To mirror any DC, call [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout)(hdc, LAYOUT\_RTL). For more information, see the discussion on mirroring device contexts not associated with windows, which comes later in this topic.

Bitmaps and icons in a mirrored window are also mirrored by default. However, not all of these should be mirrored. For example, those with text, a business logo, or an analog clock should not be mirrored. To disable mirroring of bitmaps, call [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout) with the LAYOUT\_BITMAPORIENTATIONPRESERVED bit set in *dwLayout*. To disable mirroring in a DC, call **SetLayout**(hdc, 0).

To query the current default layout, call [**GetProcessDefaultLayout**](/windows/win32/api/winuser/nf-winuser-getprocessdefaultlayout). Upon a successful return, *pdwDefaultLayout* contains LAYOUT\_RTL or 0. To query the layout settings of the device context, call [**GetLayout**](/windows/win32/api/wingdi/nf-wingdi-getlayout). Upon a successful return, **GetLayout** returns a **DWORD** that indicates the layout settings by the settings of the LAYOUT\_RTL and the LAYOUT\_BITMAPORIENTATIONPRESERVED bits.

After a window has been created, you change the layout using the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function. For example, this is necessary when the user changes the user interface language of an existing window from Arabic or Hebrew to German. However, when changing the layout of an existing window, you must invalidate and update the window to ensure that the contents of the window are all drawn on the same layout. The following code example is from sample code that changes the window layout as needed:


```
// Using ANSI versions of GetWindowLong and SetWindowLong because Unicode
// is not needed for these calls

lExStyles = GetWindowLongA(hWnd, GWL_EXSTYLE);

// Check whether new layout is opposite the current layout
if (!!(pLState -> IsRTLLayout) != !!(lExStyles & WS_EX_LAYOUTRTL))
{
    // the following lines will update the window layout

    lExStyles ^= WS_EX_LAYOUTRTL;        // toggle layout
    SetWindowLongA(hWnd, GWL_EXSTYLE, lExStyles);
    InvalidateRect(hWnd, NULL, TRUE);    // to update layout in the client area
}
```



In mirroring, you should think in terms of "near" and "far" instead of "left" and "right". Failure to do so can cause problems. One common coding practice that causes problems in a mirrored window occurs when mapping between screen coordinates and client coordinates. For example, applications often use code similar to the following to position a control in a window:


```
// DO NOT USE THIS IF APPLICATION MIRRORS THE WINDOW

// get coordinates of the window in screen coordinates
GetWindowRect(hControl, (LPRECT) &rControlRect);  

// map screen coordinates to client coordinates in dialog
ScreenToClient(hDialog, (LPPOINT) &rControlRect.left); 
ScreenToClient(hDialog, (LPPOINT) &rControlRect.right);
```



This causes problems in mirroring because the left edge of the rectangle becomes the right edge in a mirrored window, and vice versa. To avoid this problem, replace the [**ScreenToClient**](/windows/win32/api/winuser/nf-winuser-screentoclient) calls with a call to [**MapWindowPoints**](/windows/win32/api/winuser/nf-winuser-mapwindowpoints) as follows:


```
// USE THIS FOR MIRRORING

GetWindowRect(hControl, (LPRECT) &rControlRect);
MapWindowPoints(NULL, hDialog, (LPPOINT) &rControlRect, 2)
```



This code works because, on platforms that support mirroring, [**MapWindowPoints**](/windows/win32/api/winuser/nf-winuser-mapwindowpoints) is modified to swap the left and right point coordinates when the client window is mirrored. For more information, see the Remarks section of **MapWindowPoints**.

Another common practice that can cause problems in mirrored windows is positioning objects in a client window using offsets in screen coordinates instead of client coordinates. For example, the following code uses the difference in screen coordinates as the x position in client coordinates to position a control in a dialog box.


```
// OK if LTR layout and mapping mode of client is MM_TEXT,
// but WRONG for a mirrored dialog 

RECT rdDialog;
RECT rcControl;

HWND hControl = GetDlgItem(hDlg, IDD_CONTROL);
GetWindowRect(hDlg, &rcDialog);             // gets rect in screen coordinates
GetWindowRect(hControl, &rcControl);
MoveWindow(hControl,
           rcControl.left - rcDialog.left,  // uses x position in client coords
           rcControl.top - rcDialog.top,
           nWidth,
           nHeight,
           FALSE);
```



This code is fine when the dialog window has left-to-right (LTR) layout and the mapping mode of the client is MM\_TEXT, because the new x position in client coordinates corresponds to the difference in left edges of the control and the dialog in screen coordinates. However, in a mirrored dialog, left and right are reversed, so instead you should use [**MapWindowPoints**](/windows/win32/api/winuser/nf-winuser-mapwindowpoints) as follows:


```
RECT rcDialog;
RECT rcControl;

HWND hControl - GetDlgItem(hDlg, IDD_CONTROL);
GetWindowRect(hControl, &rcControl);

// MapWindowPoints works correctly in both mirrored and non-mirrored windows.
MapWindowPoints(NULL, hDlg, (LPPOINT) &rcControl, 2);

// Now rcControl is in client coordinates.
MoveWindow(hControl, rcControl.left, rcControl.top, nWidth, nHeight, FALSE)
```



### Mirroring Dialog Boxes and Message Boxes

Dialog boxes and message boxes do not inherit layout, so you must set the layout explicitly. To mirror a message box, call [**MessageBox**](/windows/win32/api/winuser/nf-winuser-messagebox) or [**MessageBoxEx**](/windows/win32/api/winuser/nf-winuser-messageboxexa) with the **MB\_RTLREADING** option. To layout a dialog box right-to-left, use the extended style WS\_EX\_LAYOUTRTL in the dialog template structure [**DLGTEMPLATEEX**](../dlgbox/dlgtemplateex.md). Property sheets are a special case of dialog boxes. Each tab is treated as a separate dialog box, so you need to include the WS\_EX\_LAYOUTRTL style in every tab that you want mirrored.

### Mirroring Device Contexts Not Associated with a Window

DCs that are not associated with a window, such as metafile or printer DCs, do not inherit layout, so you must set the layout explicitly. To change the device context layout, use the [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout) function.

The [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout) function is rarely used with windows. Typically, windows receive an associated DC only in processing a [**WM\_PAINT**](../gdi/wm-paint.md) message. Occasionally, a program creates a DC for a window by calling [**GetDC**](/windows/win32/api/winuser/nf-winuser-getdc). Either way, the initial layout for the DC is set by [**BeginPaint**](/windows/win32/api/winuser/nf-winuser-beginpaint) or **GetDC** according to the window's WS\_EX\_LAYOUTRTL flag.

The values returned by [**GetWindowOrgEx**](/windows/win32/api/wingdi/nf-wingdi-getwindoworgex), [**GetWindowExtEx**](/windows/win32/api/wingdi/nf-wingdi-getwindowextex), [**GetViewportOrgEx**](/windows/win32/api/wingdi/nf-wingdi-getviewportorgex) and [**GetViewportExtEx**](/windows/win32/api/wingdi/nf-wingdi-getviewportextex) are not affected by calling [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout).

When the layout is RTL, [**GetMapMode**](/windows/win32/api/wingdi/nf-wingdi-getmapmode) will return MM\_ANISOTROPIC instead of MM\_TEXT. Calling [**SetMapMode**](/windows/win32/api/wingdi/nf-wingdi-setmapmode) with MM\_TEXT will function correctly; only the return value from **GetMapMode** is affected. Similarly, calling [**SetLayout**](/windows/win32/api/wingdi/nf-wingdi-setlayout)(hdc, LAYOUT\_RTL) when the mapping mode is MM\_TEXT causes the reported mapping mode to change to MM\_ANISOTROPIC.

## Window Destruction

In general, an application must destroy all the windows it creates. It does this by using the [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function. When a window is destroyed, the system hides the window, if it is visible, and then removes any internal data associated with the window. This invalidates the window handle, which can no longer be used by the application.

An application destroys many of the windows it creates soon after creating them. For example, an application usually destroys a dialog box window as soon as the application has sufficient input from the user to continue its task. An application eventually destroys the main window of the application (before terminating).

Before destroying a window, an application should save or remove any data associated with the window, and it should release any system resources allocated for the window. If the application does not release the resources, the system will free any resources not freed by the application.

Destroying a window does not affect the window class from which the window is created. New windows can still be created using that class, and any existing windows of that class continue to operate. Destroying a window also destroys the window's descendant windows. The [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function sends a [**WM\_DESTROY**](wm-destroy.md) message first to the window, then to its child windows and descendant windows. In this way, all descendant windows of the window being destroyed are also destroyed.

A window with a window menu receives a [**WM\_CLOSE**](wm-close.md) message when the user clicks **Close**. By processing this message, an application can prompt the user for confirmation before destroying the window. If the user confirms that the window should be destroyed, the application can call the [**DestroyWindow**](/windows/win32/api/winuser/nf-winuser-destroywindow) function to destroy the window.

If the window being destroyed is the active window, both the active and focus states are transferred to another window. The window that becomes the active window is the next window, as determined by the ALT+ESC key combination. The new active window then determines which window receives the keyboard focus.

 

 
