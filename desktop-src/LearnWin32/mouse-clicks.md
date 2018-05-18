---
title: Responding to Mouse Clicks
description: Responding to Mouse Clicks
ms.assetid: 'FED1CA3B-94C6-4780-B82D-C10171F36D98'
---

# Responding to Mouse Clicks

If the user clicks a mouse button while the cursor is over the client area of a window, the window receives one of the following messages.



| Message                                        | Meaning                   |
|------------------------------------------------|---------------------------|
| [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) | Left button down          |
| [**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608)     | Left button up            |
| [**WM\_MBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645610) | Middle button down        |
| [**WM\_MBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645611)     | Middle button up          |
| [**WM\_RBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646242) | Right button down         |
| [**WM\_RBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms646243)     | Right button up           |
| [**WM\_XBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646245) | XBUTTON1 or XBUTTON2 down |
| [**WM\_XBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms646246)     | XBUTTON1 or XBUTTON2 up   |



 

Recall that the client area is the portion of the window that excludes the frame. For more information about client areas, see [What Is a Window?](what-is-a-window-.md)

### Mouse Coordinates

In all of these messages, the *lParam* parameter contains the x- and y-coordinates of the mouse pointer. The lowest 16 bits of *lParam* contain the x-coordinate, and the next 16 bits contain the y-coordinate. Use the [**GET\_X\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632654) and [**GET\_Y\_LPARAM**](https://msdn.microsoft.com/library/windows/desktop/ms632655) macros to unpack the coordinates from *lParam*.


```C++
int xPos = GET_X_LPARAM(lParam); 
int yPos = GET_Y_LPARAM(lParam);
```



These macros are defined in the header file WindowsX.h.

On 64-bit Windows, *lParam* is 64-bit value. The upper 32 bits of *lParam* are not used. The MSDN documentation mentions the "low-order word" and "high-order word" of *lParam*. In the 64-bit case, this means the low- and high-order words of the lower 32 bits. The macros extract the right values, so if you use them, you will be safe.

Mouse coordinates are given in pixels, not device-independent pixels (DIPs), and are measured relative to the client area of the window. Coordinates are signed values. Positions above and to the left of the client area have negative coordinates, which is important if you track the mouse position outside the window. We will see how to do that in a later topic, [Capturing Mouse Movement Outside the Window](mouse-movement.md).

### Additional Flags

The *wParam* parameter contains a bitwise **OR** of flags, indicating the state of the other mouse buttons plus the SHIFT and CTRL keys.



| Flag             | Meaning                          |
|------------------|----------------------------------|
| **MK\_CONTROL**  | The CTRL key is down.            |
| **MK\_LBUTTON**  | The left mouse button is down.   |
| **MK\_MBUTTON**  | The middle mouse button is down. |
| **MK\_RBUTTON**  | The right mouse button is down.  |
| **MK\_SHIFT**    | The SHIFT key is down.           |
| **MK\_XBUTTON1** | The XBUTTON1 button is down.     |
| **MK\_XBUTTON2** | The XBUTTON2 button is down.     |



 

The absence of a flag means the corresponding button or key was not pressed. For example, to test whether the CTRL key is down:


```C++
if (wParam & MK_CONTROL) { ...
```



If you need to find the state of other keys besides CTRL and SHIFT, use the [**GetKeyState**](https://msdn.microsoft.com/library/windows/desktop/ms646301) function, which is described in [Keyboard Input](keyboard-input.md).

The [**WM\_XBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms646245) and [**WM\_XBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms646246) window messages apply to both XBUTTON1 and XBUTTON2. The *wParam* parameter indicates which button was clicked.


```C++
UINT button = GET_XBUTTON_WPARAM(wParam);  
if (button == XBUTTON1)
{
    // XBUTTON1 was clicked.
}
else if (button == XBUTTON2)
{
    // XBUTTON2 was clicked.
}
```



## Double Clicks

A window does not receive double-click notifications by default. To receive double clicks, set the **CS\_DBLCLKS** flag in the [**WNDCLASS**](https://msdn.microsoft.com/library/windows/desktop/ms633576) structure when you register the window class.


```C++
    WNDCLASS wc = { };
    wc.style = CS_DBLCLKS;

    /* Set other structure members. */

    RegisterClass(&amp;wc);

```



If you set the **CS\_DBLCLKS** flag as shown, the window will receive double-click notifications. A double click is indicated by a window message with "DBLCLK" in the name. For example, a double click on the left mouse button produces the following sequence of messages:

<dl>

[**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607)  
[**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608)  
[**WM\_LBUTTONDBLCLK**](https://msdn.microsoft.com/library/windows/desktop/ms645606)  
[**WM\_LBUTTONUP**](https://msdn.microsoft.com/library/windows/desktop/ms645608)  
</dl>

In effect, the second [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607) message that would normally be generated becomes a [**WM\_LBUTTONDBLCLK**](https://msdn.microsoft.com/library/windows/desktop/ms645606) message. Equivalent messages are defined for right, middle, and XBUTTON buttons.

Until you get the double-click message, there is no way to tell that the first mouse click is the start of a double click. Therefore, a double-click action should continue an action that begins with the first mouse click. For example, in the Windows Shell, a single click selects a folder, while a double click opens the folder.

## Non-client Mouse Messages

A separate set of messages are defined for mouse events that occur within the non-client area of the window. These messages have the letters "NC" in the name. For example, [**WM\_NCLBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645620) is the non-client equivalent of [**WM\_LBUTTONDOWN**](https://msdn.microsoft.com/library/windows/desktop/ms645607). A typical application will not intercept these messages, because the [**DefWindowProc**](https://msdn.microsoft.com/library/windows/desktop/ms633572) function handles these messages correctly. However, they can be useful for certain advanced functions. For example, you could use these messages to implement custom behavior in the title bar. If you do handle these messages, you should generally pass them to **DefWindowProc** afterward. Otherwise, your application will break standard functionality such as dragging or minimizing the window.

## Next

[Mouse Movement](mouse-movement.md)

 

 




