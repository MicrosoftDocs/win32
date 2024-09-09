---
title: Miscellaneous Mouse Operations
description: The previous sections have discussed mouse clicks and mouse movement. Here are some other operations that can be performed with the mouse.
ms.assetid: 6A5B953F-7032-4AA6-8B64-2E9CBB8F59F1
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous Mouse Operations

The previous sections have discussed mouse clicks and mouse movement. Here are some other operations that can be performed with the mouse.

## Dragging UI Elements

If your UI supports dragging of UI elements, there is one other function that you should call in your mouse-down message handler: [**DragDetect**](/windows/desktop/api/winuser/nf-winuser-dragdetect). The **DragDetect** function returns **TRUE** if the user initiates a mouse gesture that should be interpreted as dragging. The following code shows how to use this function.


```C++
    case WM_LBUTTONDOWN: 
        {
            POINT pt = { GET_X_LPARAM(lParam), GET_Y_LPARAM(lParam) };
            if (DragDetect(m_hwnd, pt))
            {
                // Start dragging.
            }
        }
        return 0;
```



Here's the idea: When a program supports drag and drop, you don't want every mouse click to be interpreted as a drag. Otherwise, the user might accidentally drag something when he or she simply meant to click on it (for example, to select it). But if a mouse is particularly sensitive, it can be hard to keep the mouse perfectly still while clicking. Therefore, Windows defines a drag threshold of a few pixels. When the user presses the mouse button, it is not considered a drag unless the mouse crosses this threshold. The [**DragDetect**](/windows/desktop/api/winuser/nf-winuser-dragdetect) function tests whether this threshold is reached. If the function returns **TRUE**, you can interpret the mouse click as a drag. Otherwise, do not.

> [!Note]  
> If [**DragDetect**](/windows/desktop/api/winuser/nf-winuser-dragdetect) returns **FALSE**, Windows suppresses the [**WM\_LBUTTONUP**](/windows/desktop/inputdev/wm-lbuttonup) message when the user releases the mouse button. Therefore, do not call **DragDetect** unless your program is currently in a mode that supports dragging. (For example, if a draggable UI element is already selected.) At the end of this module, we will see a longer code example that uses the **DragDetect** function.

 

## Confining the Cursor

Sometimes you might want to restrict the cursor to the client area or a portion of the client area. The [**ClipCursor**](/windows/desktop/api/winuser/nf-winuser-clipcursor) function restricts the movement of the cursor to a specified rectangle. This rectangle is given in screen coordinates, rather than client coordinates, so the point (0, 0) means the upper left corner of the screen. To translate client coordinates into screen coordinates, call the function [**ClientToScreen**](/windows/desktop/api/winuser/nf-winuser-clienttoscreen).

The following code confines the cursor to the client area of the window.


```C++
    // Get the window client area.
    RECT rc;
    GetClientRect(m_hwnd, &rc);

    // Convert the client area to screen coordinates.
    POINT pt = { rc.left, rc.top };
    POINT pt2 = { rc.right, rc.bottom };
    ClientToScreen(m_hwnd, &pt);
    ClientToScreen(m_hwnd, &pt2);
    SetRect(&rc, pt.x, pt.y, pt2.x, pt2.y);

    // Confine the cursor.
    ClipCursor(&rc);
```



[**ClipCursor**](/windows/desktop/api/winuser/nf-winuser-clipcursor) takes a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure, but [**ClientToScreen**](/windows/desktop/api/winuser/nf-winuser-clienttoscreen) takes a [**POINT**](/windows/win32/api/windef/ns-windef-point) structure. A rectangle is defined by its top-left and bottom-right points. You can confine the cursor to any rectangular area, including areas outside the window, but confining the cursor to the client area is a typical way to use the function. Confining the cursor to a region entirely outside your window would be unusual, and users would probably perceive it as a bug.

To remove the restriction, call [**ClipCursor**](/windows/desktop/api/winuser/nf-winuser-clipcursor) with the value **NULL**.


```C++
ClipCursor(NULL);
```



## Mouse Tracking Events: Hover and Leave

Two other mouse messages are disabled by default, but may be useful for some applications:

-   [**WM\_MOUSEHOVER**](/windows/desktop/inputdev/wm-mousehover): The cursor has hovered over the client area for a fixed period of time.
-   [**WM\_MOUSELEAVE**](/windows/desktop/inputdev/wm-mouseleave): The cursor has left the client area.

To enable these messages, call the [**TrackMouseEvent**](/windows/desktop/api/winuser/nf-winuser-trackmouseevent) function.


```C++
    TRACKMOUSEEVENT tme;
    tme.cbSize = sizeof(tme);
    tme.hwndTrack = hwnd;
    tme.dwFlags = TME_HOVER | TME_LEAVE;
    tme.dwHoverTime = HOVER_DEFAULT;
    TrackMouseEvent(&tme);
```



The [**TRACKMOUSEEVENT**](/windows/win32/api/winuser/ns-winuser-trackmouseevent) structure contains the parameters for the function. The **dwFlags** member of the structure contains bit flags that specify which tracking messages you are interested in. You can choose to get both [**WM\_MOUSEHOVER**](/windows/desktop/inputdev/wm-mousehover) and [**WM\_MOUSELEAVE**](/windows/desktop/inputdev/wm-mouseleave), as shown here, or just one of the two. The **dwHoverTime** member specifies how long the mouse needs to hover before the system generates a hover message. This value is given in milliseconds. The constant **HOVER\_DEFAULT** means to use the system default.

After you get one of the messages that you requested, the [**TrackMouseEvent**](/windows/desktop/api/winuser/nf-winuser-trackmouseevent) function resets. You must call it again to get another tracking message. However, you should wait until the next mouse-move message before calling **TrackMouseEvent** again. Otherwise, your window might be flooded with tracking messages. For example, if the mouse is hovering, the system would continue to generate a stream of [**WM\_MOUSEHOVER**](/windows/desktop/inputdev/wm-mousehover) messages while the mouse is stationary. You don't actually want another **WM\_MOUSEHOVER** message until the mouse moves to another spot and hovers again.

Here is a small helper class that you can use to manage mouse-tracking events.


```C++
class MouseTrackEvents
{
    bool m_bMouseTracking;

public:
    MouseTrackEvents() : m_bMouseTracking(false)
    {
    }
    
    void OnMouseMove(HWND hwnd)
    {
        if (!m_bMouseTracking)
        {
            // Enable mouse tracking.
            TRACKMOUSEEVENT tme;
            tme.cbSize = sizeof(tme);
            tme.hwndTrack = hwnd;
            tme.dwFlags = TME_HOVER | TME_LEAVE;
            tme.dwHoverTime = HOVER_DEFAULT;
            TrackMouseEvent(&tme);
            m_bMouseTracking = true;
        }
    }
    void Reset(HWND hwnd)
    {
        m_bMouseTracking = false;
    }
};
```



The next example shows how to use this class in your window procedure.


```C++
LRESULT MainWindow::HandleMessage(UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_MOUSEMOVE:
        mouseTrack.OnMouseMove(m_hwnd);  // Start tracking.

        // TODO: Handle the mouse-move message.

        return 0;

    case WM_MOUSELEAVE:

        // TODO: Handle the mouse-leave message.

        mouseTrack.Reset(m_hwnd);
        return 0;

    case WM_MOUSEHOVER:

        // TODO: Handle the mouse-hover message.

        mouseTrack.Reset(m_hwnd);
        return 0;

    }
    return DefWindowProc(m_hwnd, uMsg, wParam, lParam);
}
```



Mouse tracking events require additional processing by the system, so leave them disabled if you do not need them.

For completeness, here is a function that queries the system for the default hover timeout.


```C++
UINT GetMouseHoverTime()
{
    UINT msec; 
    if (SystemParametersInfo(SPI_GETMOUSEHOVERTIME, 0, &msec, 0))
    {   
        return msec;
    }
    else
    {
        return 0;
    }
}
```



## Mouse Wheel

The following function checks if a mouse wheel is present.


```C++
BOOL IsMouseWheelPresent()
{
    return (GetSystemMetrics(SM_MOUSEWHEELPRESENT) != 0);
}
```



If the user rotates the mouse wheel, the window with focus receives a [**WM\_MOUSEWHEEL**](/windows/desktop/inputdev/wm-mousewheel) message. The *wParam* parameter of this message contains an integer value called the *delta* that measures how far the wheel was rotated. The delta uses arbitrary units, where 120 units is defined as the rotation needed to perform one "action." Of course, the definition of an action depends on your program. For example, if the mouse wheel is used to scroll text, each 120 units of rotation would scroll one line of text.

The sign of the delta indicates the direction of rotation:

-   Positive: Rotate forward, away from the user.
-   Negative: Rotate backward, toward the user.

The value of the delta is placed in *wParam* along with some additional flags. Use the [**GET\_WHEEL\_DELTA\_WPARAM**](/windows/desktop/api/winuser/nf-winuser-get_wheel_delta_wparam) macro to get the value of the delta.


```C++
int delta = GET_WHEEL_DELTA_WPARAM(wParam);
```



If the mouse wheel has a high resolution, the absolute value of the delta might be less than 120. In that case, if it makes sense for the action to occur in smaller increments, you can do so. For example, text could scroll by increments of less than one line. Otherwise, accumulate the total delta until the wheel rotates enough to perform the action. Store the unused delta in a variable, and when 120 units accumulate (either positive or negative), perform the action.

## Next

[Keyboard Input](keyboard-input.md)

 

 