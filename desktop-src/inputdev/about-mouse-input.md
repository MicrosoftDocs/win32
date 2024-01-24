---
title: Mouse Input Overview
description: This topic discusses mouse input.
ms.assetid: 1f945a31-76d5-4e23-a55a-769ca114dbe9
keywords:
- user input,mouse input
- capturing user input,mouse input
- mouse input
- mouse cursor
- cursors,mouse input
- mouse capture
- mouse ClickLock
- XBUTTONs
- mouse configuration
- mouse messages
- WM_NCHITTEST message
- Mouse Vanish accessibility feature
- Mouse Sonar accessibility feature
- mouse wheel
- WM_MOUSEWHEEL message
ms.topic: article
ms.date: 05/31/2018
---

# Mouse Input Overview

The mouse is an important, but optional, user-input device for applications. A well-written application should include a mouse interface, but it should not depend solely on the mouse for acquiring user input. The application should provide full keyboard support as well.

An application receives mouse input in the form of messages that are sent or posted to its windows.

This section covers the following topics:

-   [Mouse Cursor](#mouse-cursor)
-   [Mouse Capture](#mouse-capture)
-   [Mouse ClickLock](#mouse-clicklock)
-   [Mouse Configuration](#mouse-configuration)
-   [XBUTTONs](#xbuttons)
-   [Mouse Messages](#mouse-messages)
    -   [Client Area Mouse Messages](#client-area-mouse-messages)
    -   [Nonclient Area Mouse Messages](#nonclient-area-mouse-messages)
    -   [The WM\_NCHITTEST Message](/windows)
-   [Mouse Sonar](#mouse-sonar)
-   [Mouse Vanish](#mouse-vanish)
-   [The Mouse Wheel](#the-mouse-wheel)
-   [Window Activation](#window-activation)

## Mouse Cursor

When the user moves the mouse, the system moves a bitmap on the screen called the *mouse cursor*. The mouse cursor contains a single-pixel point called the *hot spot*, a point that the system tracks and recognizes as the position of the cursor. When a mouse event occurs, the window that contains the hot spot typically receives the mouse message resulting from the event. The window need not be active or have the keyboard focus to receive a mouse message.

The system maintains a variable that controls mouse speed—that is, the distance the cursor moves when the user moves the mouse. You can use the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function with the **SPI\_GETMOUSE** or **SPI\_SETMOUSE** flag to retrieve or set mouse speed. For more information about mouse cursors, see [Cursors](/windows/desktop/menurc/cursors).

## Mouse Capture

The system typically posts a mouse message to the window that contains the cursor hot spot when a mouse event occurs. An application can change this behavior by using the [**SetCapture**](/windows/win32/api/winuser/nf-winuser-setcapture) function to route mouse messages to a specific window. The window receives all mouse messages until the application calls the [**ReleaseCapture**](/windows/win32/api/winuser/nf-winuser-releasecapture) function or specifies another capture window, or until the user clicks a window created by another thread.

When the mouse capture changes, the system sends a [**WM\_CAPTURECHANGED**](wm-capturechanged.md) message to the window that is losing the mouse capture. The *lParam* parameter of the message specifies a handle to the window that is gaining the mouse capture.

Only the foreground window can capture mouse input. When a background window attempts to capture mouse input, it receives messages only for mouse events that occur when the cursor hot spot is within the visible portion of the window.

Capturing mouse input is useful if a window must receive all mouse input, even when the cursor moves outside the window. For example, an application typically tracks the cursor position after a mouse button down event, following the cursor until a mouse button up event occurs. If an application has not captured mouse input and the user releases the mouse button outside the window, the window does not receive the button-up message.

A thread can use the [**GetCapture**](/windows/win32/api/winuser/nf-winuser-getcapture) function to determine whether one of its windows has captured the mouse. If one of the thread's windows has captured the mouse, **GetCapture** retrieves a handle to the window.

## Mouse ClickLock

The Mouse ClickLock accessibility feature enables a user lock down the primary mouse button after a single click. To an application, the button still appears to be pressed down. To unlock the button, an application can send any mouse message or the user can click any mouse button. This feature lets a user do complex mouse combinations more simply. For example, those with certain physical limitations can highlight text, drag objects, or open menus more easily. For more information, see the following flags and the Remarks in [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa):

-   **SPI\_GETMOUSECLICKLOCK**
-   **SPI\_SETMOUSECLICKLOCK**
-   **SPI\_GETMOUSECLICKLOCKTIME**
-   **SPI\_SETMOUSECLICKLOCKTIME**

## Mouse Configuration

Although the mouse is an important input device for applications, not every user necessarily has a mouse. An application can determine whether the system includes a mouse by passing the **SM\_MOUSEPRESENT** value to the [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function.

Windows supports a mouse having up to three buttons. On a three-button mouse, the buttons are designated as the left, middle, and right buttons. Messages and named constants related to the mouse buttons use the letters L, M, and R to identify the buttons. The button on a single-button mouse is considered to be the left button. Although Windows supports a mouse with multiple buttons, most applications use the left button primarily and the others minimally, if at all.

Applications can also support a mouse wheel. The mouse wheel can be pressed or rotated. When the mouse wheel is pressed, it acts as the middle (third) button, sending normal middle button messages to your application. When it is rotated, a wheel message is sent to your application. For more information, see [The Mouse Wheel](#the-mouse-wheel) section.

Applications can support application-command buttons. These buttons, called X buttons, are designed to allow easier access to an Internet browser, electronic mail, and media services. When an X button is pressed, a [**WM\_APPCOMMAND**](wm-appcommand.md) message is sent to your application. For more information, see the description in the **WM\_APPCOMMAND** message.

An application can determine the number of buttons on the mouse by passing the **SM\_CMOUSEBUTTONS** value to the [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) function. To configure the mouse for a left-handed user, the application can use the [**SwapMouseButton**](/windows/win32/api/winuser/nf-winuser-swapmousebutton) function to reverse the meaning of the left and right mouse buttons. Passing the **SPI\_SETMOUSEBUTTONSWAP** value to the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function is another way to reverse the meaning of the buttons. Note, however, that the mouse is a shared resource, so reversing the meaning of the buttons affects all applications.

## XBUTTONs

Windows supports a mouse with five buttons. In addition to the left, middle, and right buttons there are XBUTTON1 and XBUTTON2, which provide backward and forward navigation when using your browser.

The window manager supports XBUTTON1 and XBUTTON2 through the **WM\_XBUTTON\*** and **WM\_NCXBUTTON\*** messages. The HIWORD of the **WPARAM** in these messages contains a flag indicating which X button was pressed. Because these mouse messages also fit between the constants **WM\_MOUSEFIRST** and **WM\_MOUSELAST**, an application can filter all mouse messages with [**GetMessage**](/windows/desktop/api/winuser/nf-winuser-getmessage) or [**PeekMessage**](/windows/desktop/api/winuser/nf-winuser-peekmessagea).

The following support XBUTTON1 and XBUTTON2:

-   [**WM\_APPCOMMAND**](wm-appcommand.md)
-   [**WM\_NCXBUTTONDBLCLK**](wm-ncxbuttondblclk.md)
-   [**WM\_NCXBUTTONDOWN**](wm-ncxbuttondown.md)
-   [**WM\_NCXBUTTONUP**](wm-ncxbuttonup.md)
-   [**WM\_XBUTTONDBLCLK**](wm-xbuttondblclk.md)
-   [**WM\_XBUTTONDOWN**](wm-xbuttondown.md)
-   [**WM\_XBUTTONUP**](wm-xbuttonup.md)
-   [**MOUSEHOOKSTRUCTEX**](/windows/win32/api/winuser/ns-winuser-mousehookstructex)

The following APIs were modified to support these buttons:

-   [**mouse\_event**](/windows/win32/api/winuser/nf-winuser-mouse_event)
-   [**ShellProc**](../winmsg/shellproc.md)
-   [**MSLLHOOKSTRUCT**](/windows/win32/api/winuser/ns-winuser-msllhookstruct)
-   [**MOUSEINPUT**](/windows/win32/api/winuser/ns-winuser-mouseinput)
-   [**WM\_PARENTNOTIFY**](/previous-versions/windows/desktop/inputmsg/wm-parentnotify)

It is unlikely that a child window in a component application will be able to directly implement commands for the XBUTTON1 and XBUTTON2. So [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) sends a [**WM\_APPCOMMAND**](wm-appcommand.md) message to a window when an X button is clicked. **DefWindowProc** also sends the **WM\_APPCOMMAND** message to its parent window. This is similar to the way context menus are invoked with a right click—**DefWindowProc** sends a [**WM\_CONTEXTMENU**](/windows/desktop/menurc/wm-contextmenu) message to the menu and also sends it to its parent. Additionally, if **DefWindowProc** receives a **WM\_APPCOMMAND** message for a top-level window, it calls a shell hook with code HSHELL\_APPCOMMAND.

There is support for the keyboards that have extra keys for browser functions, media functions, application launching, and power management. For more information, see [Keyboard Keys for Browsing and Other Functions](about-keyboard-input.md).

## Mouse Messages

The mouse generates an input event when the user moves the mouse, or presses or releases a mouse button. The system converts mouse input events into messages and posts them to the appropriate thread's message queue. When mouse messages are posted faster than a thread can process them, the system discards all but the most recent mouse message.

A window receives a mouse message when a mouse event occurs while the cursor is within the borders of the window, or when the window has captured the mouse. Mouse messages are divided into two groups: client area messages and nonclient area messages. Typically, an application processes client area messages and ignores nonclient area messages.

This section covers the following topics:

-   [Client Area Mouse Messages](#client-area-mouse-messages)
-   [Nonclient Area Mouse Messages](#nonclient-area-mouse-messages)
-   [The WM\_NCHITTEST Message](/windows)

### Client Area Mouse Messages

A window receives a client area mouse message when a mouse event occurs within the window's client area. The system posts the [**WM\_MOUSEMOVE**](wm-mousemove.md) message to the window when the user moves the cursor within the client area. It posts one of the following messages when the user presses or releases a mouse button while the cursor is within the client area.



| Message                                       | Meaning                                     |
|-----------------------------------------------|---------------------------------------------|
| [**WM\_LBUTTONDBLCLK**](wm-lbuttondblclk.md) | The left mouse button was double-clicked.   |
| [**WM\_LBUTTONDOWN**](wm-lbuttondown.md)     | The left mouse button was pressed.          |
| [**WM\_LBUTTONUP**](wm-lbuttonup.md)         | The left mouse button was released.         |
| [**WM\_MBUTTONDBLCLK**](wm-mbuttondblclk.md) | The middle mouse button was double-clicked. |
| [**WM\_MBUTTONDOWN**](wm-mbuttondown.md)     | The middle mouse button was pressed.        |
| [**WM\_MBUTTONUP**](wm-mbuttonup.md)         | The middle mouse button was released.       |
| [**WM\_RBUTTONDBLCLK**](wm-rbuttondblclk.md) | The right mouse button was double-clicked.  |
| [**WM\_RBUTTONDOWN**](wm-rbuttondown.md)     | The right mouse button was pressed.         |
| [**WM\_RBUTTONUP**](wm-rbuttonup.md)         | The right mouse button was released.        |
| [**WM\_XBUTTONDBLCLK**](wm-xbuttondblclk.md) | An X mouse button was double-clicked.       |
| [**WM\_XBUTTONDOWN**](wm-xbuttondown.md)     | An X mouse button was pressed.              |
| [**WM\_XBUTTONUP**](wm-xbuttonup.md)         | An X mouse button was released.             |



 

In addition, an application can call the [**TrackMouseEvent**](/windows/win32/api/winuser/nf-winuser-trackmouseevent) function to have the system send two other messages. It posts the [**WM\_MOUSEHOVER**](wm-mousehover.md) message when the cursor hovers over the client area for a certain time period. It posts the [**WM\_MOUSELEAVE**](wm-mouseleave.md) message when the cursor leaves the client area.

### Message Parameters

The *lParam* parameter of a client area mouse message indicates the position of the cursor hot spot. The low-order word indicates the x-coordinate of the hot spot, and the high-order word indicates the y-coordinate. The coordinates are specified in client coordinates. In the client coordinate system, all points on the screen are specified relative to the coordinates (0,0) of the upper-left corner of the client area.

The *wParam* parameter contains flags that indicate the status of the other mouse buttons and the CTRL and SHIFT keys at the time of the mouse event. You can check for these flags when mouse-message processing depends on the state of another mouse button or of the CTRL or SHIFT key. The *wParam* parameter can be a combination of the following values.



| Value            | Description                      |
|------------------|----------------------------------|
| **MK\_CONTROL**  | The CTRL key is down.            |
| **MK\_LBUTTON**  | The left mouse button is down.   |
| **MK\_MBUTTON**  | The middle mouse button is down. |
| **MK\_RBUTTON**  | The right mouse button is down.  |
| **MK\_SHIFT**    | The SHIFT key is down.           |
| **MK\_XBUTTON1** | The first X button is down.      |
| **MK\_XBUTTON2** | The second X button is down.     |



 

### Double-Click Messages

The system generates a double-click message when the user clicks a mouse button twice in quick succession. When the user clicks a button, the system establishes a rectangle centered around the cursor hot spot. It also marks the time at which the click occurred. When the user clicks the same button a second time, the system determines whether the hot spot is still within the rectangle and calculates the time elapsed since the first click. If the hot spot is still within the rectangle and the elapsed time does not exceed the double-click time-out value, the system generates a double-click message.

An application can get and set double-click time-out values by using the [**GetDoubleClickTime**](/windows/win32/api/winuser/nf-winuser-getdoubleclicktime) and [**SetDoubleClickTime**](/windows/win32/api/winuser/nf-winuser-setdoubleclicktime) functions, respectively. Alternatively, the application can set the double-click–time-out value by using the **SPI\_SETDOUBLECLICKTIME** flag with the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function. It can also set the size of the rectangle that the system uses to detect double-clicks by passing the **SPI\_SETDOUBLECLKWIDTH** and **SPI\_SETDOUBLECLKHEIGHT** flags to **SystemParametersInfo**. Note, however, that setting the double-click–time-out value and rectangle affects all applications.

An application-defined window does not, by default, receive double-click messages. Because of the system overhead involved in generating double-click messages, these messages are generated only for windows belonging to classes that have the **CS\_DBLCLKS** class style. Your application must set this style when registering the window class. For more information, see [Window Classes](/windows/desktop/winmsg/window-classes).

A double-click message is always the third message in a four-message series. The first two messages are the button-down and button-up messages generated by the first click. The second click generates the double-click message followed by another button-up message. For example, double-clicking the left mouse button generates the following message sequence:

1.  [**WM\_LBUTTONDOWN**](wm-lbuttondown.md)
2.  [**WM\_LBUTTONUP**](wm-lbuttonup.md)
3.  [**WM\_LBUTTONDBLCLK**](wm-lbuttondblclk.md)
4.  [**WM\_LBUTTONUP**](wm-lbuttonup.md)

Because a window always receives a button-down message before receiving a double-click message, an application typically uses a double-click message to extend a task it began during a button-down message. For example, when the user clicks a color in the color palette of Microsoft Paint, Paint displays the selected color next to the palette. When the user double-clicks a color, Paint displays the color and opens the **Edit Colors** dialog box.

### Nonclient Area Mouse Messages

A window receives a nonclient area mouse message when a mouse event occurs in any part of a window except the client area. A window's nonclient area consists of its border, menu bar, title bar, scroll bar, window menu, minimize button, and maximize button.

The system generates nonclient area messages primarily for its own use. For example, the system uses nonclient area messages to change the cursor to a two-headed arrow when the cursor hot spot moves into a window's border. A window must pass nonclient area mouse messages to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function to take advantage of the built-in mouse interface.

There is a corresponding nonclient area mouse message for each client area mouse message. The names of these messages are similar except that the named constants for the nonclient area messages include the letters NC. For example, moving the cursor in the nonclient area generates a [**WM\_NCMOUSEMOVE**](wm-ncmousemove.md) message, and pressing the left mouse button while the cursor is in the nonclient area generates a [**WM\_NCLBUTTONDOWN**](wm-nclbuttondown.md) message.

The *lParam* parameter of a nonclient area mouse message is a structure that contains the x- and y-coordinates of the cursor hot spot. Unlike coordinates of client area mouse messages, the coordinates are specified in screen coordinates rather than client coordinates. In the screen coordinate system, all points on the screen are relative to the coordinates (0,0) of the upper-left corner of the screen.

The *wParam* parameter contains a hit-test value, a value that indicates where in the nonclient area the mouse event occurred. The following section explains the purpose of hit-test values.

### The WM\_NCHITTEST Message

Whenever a mouse event occurs, the system sends a [**WM\_NCHITTEST**](wm-nchittest.md) message to either the window that contains the cursor hot spot or the window that has captured the mouse. The system uses this message to determine whether to send a client area or nonclient area mouse message. An application that must receive mouse movement and mouse button messages must pass the **WM\_NCHITTEST** message to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function.

The *lParam* parameter of the [**WM\_NCHITTEST**](wm-nchittest.md) message contains the screen coordinates of the cursor hot spot. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function examines the coordinates and returns a hit-test value that indicates the location of the hot spot. The hit-test value can be one of the following values.



| Value             | Location of hot spot                                                                                                                                                                                |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HTBORDER**      | In the border of a window that does not have a sizing border.                                                                                                                                       |
| **HTBOTTOM**      | In the lower-horizontal border of a window.                                                                                                                                                         |
| **HTBOTTOMLEFT**  | In the lower-left corner of a window border.                                                                                                                                                        |
| **HTBOTTOMRIGHT** | In the lower-right corner of a window border.                                                                                                                                                       |
| **HTCAPTION**     | In a title bar.                                                                                                                                                                                     |
| **HTCLIENT**      | In a client area.                                                                                                                                                                                   |
| **HTCLOSE**       | In a **Close** button.                                                                                                                                                                              |
| **HTERROR**       | On the screen background or on a dividing line between windows (same as HTNOWHERE, except that the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function produces a system beep to indicate an error). |
| **HTGROWBOX**     | In a size box (same as **HTSIZE**).                                                                                                                                                                 |
| **HTHELP**        | In a **Help** button.                                                                                                                                                                               |
| **HTHSCROLL**     | In a horizontal scroll bar.                                                                                                                                                                         |
| **HTLEFT**        | In the left border of a window.                                                                                                                                                                     |
| **HTMENU**        | In a menu.                                                                                                                                                                                          |
| **HTMAXBUTTON**   | In a **Maximize** button.                                                                                                                                                                           |
| **HTMINBUTTON**   | In a **Minimize** button.                                                                                                                                                                           |
| **HTNOWHERE**     | On the screen background or on a dividing line between windows.                                                                                                                                     |
| **HTREDUCE**      | In a **Minimize** button.                                                                                                                                                                           |
| **HTRIGHT**       | In the right border of a window.                                                                                                                                                                    |
| **HTSIZE**        | In a size box (same as **HTGROWBOX**).                                                                                                                                                              |
| **HTSYSMENU**     | In a **System** menu or in a **Close** button in a child window.                                                                                                                                    |
| **HTTOP**         | In the upper-horizontal border of a window.                                                                                                                                                         |
| **HTTOPLEFT**     | In the upper-left corner of a window border.                                                                                                                                                        |
| **HTTOPRIGHT**    | In the upper-right corner of a window border.                                                                                                                                                       |
| **HTTRANSPARENT** | In a window currently covered by another window in the same thread.                                                                                                                                 |
| **HTVSCROLL**     | In the vertical scroll bar.                                                                                                                                                                         |
| **HTZOOM**        | In a **Maximize** button.                                                                                                                                                                           |



 

If the cursor is in the client area of a window, [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) returns the **HTCLIENT** hit-test value to the window procedure. When the window procedure returns this code to the system, the system converts the screen coordinates of the cursor hot spot to client coordinates, and then posts the appropriate client area mouse message.

The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function returns one of the other hit-test values when the cursor hot spot is in a window's nonclient area. When the window procedure returns one of these hit-test values, the system posts a nonclient area mouse message, placing the hit-test value in the message's *wParam* parameter and the cursor coordinates in the *lParam* parameter.

## Mouse Sonar

The Mouse Sonar accessibility feature briefly shows several concentric circles around the pointer when the user presses and releases the CTRL key. This feature helps a user locate the mouse pointer on a screen that is cluttered or with resolution set to high, on a poor quality monitor, or for users with impaired vision. For more information, see the following flags in [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa):

**SPI\_GETMOUSESONAR**

**SPI\_SETMOUSESONAR**

## Mouse Vanish

The Mouse Vanish accessibility feature hides the pointer when the user is typing. The mouse pointer reappears when the user moves the mouse. This feature keeps the pointer from obscuring the text being typed, for example, in an e-mail or other document. For more information, see the following flags in [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa):

**SPI\_GETMOUSEVANISH**

**SPI\_SETMOUSEVANISH**

## The Mouse Wheel

The mouse wheel combines the features of a wheel and a mouse button. The wheel has discrete, evenly-spaced notches. When you rotate the wheel, a wheel message is sent to your application as each notch is encountered. The wheel button can also operate as a normal Windows middle (third) button. Pressing and releasing the mouse wheel sends standard [**WM\_MBUTTONUP**](wm-mbuttonup.md) and [**WM\_MBUTTONDOWN**](wm-mbuttondown.md) messages. Double clicking the third button sends the standard [**WM\_MBUTTONDBLCLK**](wm-mbuttondblclk.md) message.

The mouse wheel is supported through the [**WM\_MOUSEWHEEL**](wm-mousewheel.md) message.

Rotating the mouse sends the [**WM\_MOUSEWHEEL**](wm-mousewheel.md) message to the focus window. The [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function propagates the message to the window's parent. There should be no internal forwarding of the message, since **DefWindowProc** propagates it up the parent chain until a window that processes it is found.

### Determining the Number of Scroll Lines

Applications should use the [**SystemParametersInfo**](/windows/desktop/api/winuser/nf-winuser-systemparametersinfoa) function to retrieve the number of lines a document scrolls for each scroll operation (wheel notch). To retrieve the number of lines, an application makes the following call:


```
SystemParametersInfo(SPI_GETWHEELSCROLLLINES, 0, pulScrollLines, 0)
```



The variable "pulScrollLines" points to an unsigned integer value that receives the suggested number of lines to scroll when the mouse wheel is rotated without modifier keys:

-   If this number is 0, no scrolling should occur.
-   If this number is **WHEEL\_PAGESCROLL**, a wheel roll should be interpreted as clicking once in the page down or page up regions of the scroll bar.
-   If the number of lines to scroll is greater than the number of lines viewable, the scroll operation should also be interpreted as a page down or page up operation.

The default value for the number of scroll lines will be 3. If a user changes the number of scroll lines, by using the Mouse Properties sheet in Control Panel, the operating system broadcasts a [**WM\_SETTINGCHANGE**](../winmsg/wm-settingchange.md) message to all top-level windows with **SPI\_SETWHEELSCROLLLINES** specified. When an application receives the **WM\_SETTINGCHANGE** message, it can then get the new number of scroll lines by calling:


```
SystemParametersInfo(SPI_GETWHEELSCROLLLINES, 0, pulScrollLines, 0)
```



### Controls that Scroll

The table below lists the controls with scrolling functionality (including scroll lines set by the user). 

| Control                 | Scrolling                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Edit Control            | Vertical and horizontal.                                                                                                                                                |
| List box Control        | Vertical and horizontal.                                                                                                                                                |
| Combo box               | When not dropped down, each scroll retrieves the next or previous item. When dropped down, each scroll forwards the message to the list box, which scrolls accordingly. |
| CMD (Command line)      | Vertical.                                                                                                                                                               |
| Tree View               | Vertical and horizontal.                                                                                                                                                |
| List View               | Vertical and horizontal.                                                                                                                                                |
| Up/down Scrolls         | One item at a time.                                                                                                                                                     |
| Trackbar Scrolls        | One item at a time.                                                                                                                                                     |
| Microsoft Rich Edit 1.0 | Vertical. Note, the Exchange client has its own versions of the list view and tree view controls that do not have wheel support.                                        |
| Microsoft Rich Edit 2.0 | Vertical.                                                                                                                                                               |



 

### Detecting a Mouse with a Wheel

To determine if a mouse with a wheel is connected, call [**GetSystemMetrics**](/windows/desktop/api/winuser/nf-winuser-getsystemmetrics) with **SM\_MOUSEWHEELPRESENT**. A return value of **TRUE** indicates that the mouse is connected.

The following example is from the window procedure for a multiline edit control:


```
BOOL ScrollLines(
     PWNDDATA pwndData,   //scrolls the window indicated
     int cLinesToScroll); //number of times

short gcWheelDelta; //wheel delta from roll
PWNDDATA pWndData; //pointer to structure containing info about the window
UINT gucWheelScrollLines=0;//number of lines to scroll on a wheel rotation

gucWheelScrollLines = SystemParametersInfo(SPI_GETWHEELSCROLLLINES, 
                             0, 
                             pulScrollLines, 
                             0);

case WM_MOUSEWHEEL:
    /*
     * Do not handle zoom and datazoom.
     */
    if (wParam & (MK_SHIFT | MK_CONTROL)) {
        goto PassToDefaultWindowProc;
    }

    gcWheelDelta -= (short) HIWORD(wParam);
    if (abs(gcWheelDelta) >= WHEEL_DELTA && gucWheelScrollLines > 0) 
    {
        int cLineScroll;

        /*
         * Limit a roll of one (1) WHEEL_DELTA to
         * scroll one (1) page.
         */
        cLineScroll = (int) min(
                (UINT) pWndData->ichLinesOnScreen - 1,
                gucWheelScrollLines);

        if (cLineScroll == 0) {
            cLineScroll++;
        }

        cLineScroll *= (gcWheelDelta / WHEEL_DELTA);
        assert(cLineScroll != 0);

        gcWheelDelta = gcWheelDelta % WHEEL_DELTA;
        return ScrollLines(pWndData, cLineScroll);
    }

    break;
```



## Window Activation

When the user clicks an inactive top-level window or the child window of an inactive top-level window, the system sends the [**WM\_MOUSEACTIVATE**](wm-mouseactivate.md) message (among others) to the top-level or child window. The system sends this message after posting the [**WM\_NCHITTEST**](wm-nchittest.md) message to the window, but before posting the button-down message. When **WM\_MOUSEACTIVATE** is passed to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function, the system activates the top-level window and then posts the button-down message to the top-level or child window.

By processing [**WM\_MOUSEACTIVATE**](wm-mouseactivate.md), a window can control whether the top-level window becomes the active window as a result of a mouse click, and whether the window that was clicked receives the subsequent button-down message. It does so by returning one of the following values after processing **WM\_MOUSEACTIVATE**.



| Value                    | Meaning                                                              |
|--------------------------|----------------------------------------------------------------------|
| **MA\_ACTIVATE**         | Activates the window and does not discard the mouse message.         |
| **MA\_NOACTIVATE**       | Does not activate the window and does not discard the mouse message. |
| **MA\_ACTIVATEANDEAT**   | Activates the window and discards the mouse message.                 |
| **MA\_NOACTIVATEANDEAT** | Does not activate the window but discards the mouse message.         |

## See also

[Taking Advantage of High-Definition Mouse Movement](../dxtecharts/taking-advantage-of-high-dpi-mouse-movement.md)