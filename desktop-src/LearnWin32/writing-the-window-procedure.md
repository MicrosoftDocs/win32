---
title: Writing the Window Procedure
description: Writing the Window Procedure
ms.assetid: f022bb88-6e4c-4ec4-9eef-f125ad92167e
ms.topic: article
ms.date: 05/31/2018
---

# Writing the Window Procedure

The [**DispatchMessage**](/windows/desktop/api/winuser/nf-winuser-dispatchmessage) function calls the window procedure of the window that is the target of the message. The window procedure has the following signature.

```C++
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
```

There are four parameters:

- *hwnd* is a handle to the window.
- *uMsg* is the message code; for example, the [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message indicates the window was resized.
- *wParam* and *lParam* contain additional data that pertains to the message. The exact meaning depends on the message code.

**LRESULT** is an integer value that your program returns to Windows. It contains your program's response to a particular message. The meaning of this value depends on the message code. **CALLBACK** is the calling convention for the function.

A typical window procedure is simply a large switch statement that switches on the message code. Add cases for each message that you want to handle.

```C++
switch (uMsg)
{
    case WM_SIZE: // Handle window resizing

    // etc
}
```

Additional data for the message is contained in the *lParam* and *wParam* parameters. Both parameters are integer values the size of a pointer width (32 bits or 64 bits). The meaning of each depends on the message code (*uMsg*). For each message, you will need to look up the message code on MSDN and cast the parameters to the correct data type. Usually the data is either a numeric value or a pointer to a structure. Some messages do not have any data.

For example, the documentation for the [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message states that:

- *wParam* is a flag that indicates whether the window was minimized, maximized, or resized.
- *lParam* contains the new width and height of the window as 16-bit values packed into one 32- or 64-bit number. You will need to perform some bit-shifting to get these values. Fortunately, the header file WinDef.h includes helper macros that do this.

A typical window procedure handles dozens of messages, so it can grow quite long. One way to make your code more modular is to put the logic for handling each message in a separate function. In the window procedure, cast the *wParam* and *lParam* parameters to the correct data type, and pass those values to the function. For example, to handle the [**WM\_SIZE**](/windows/desktop/winmsg/wm-size) message, the window procedure would look like this:

```C++
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_SIZE:
        {
            int width = LOWORD(lParam);  // Macro to get the low-order word.
            int height = HIWORD(lParam); // Macro to get the high-order word.

            // Respond to the message:
            OnSize(hwnd, (UINT)wParam, width, height);
        }
        break;
    }
}

void OnSize(HWND hwnd, UINT flag, int width, int height)
{
    // Handle resizing
}
```

The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) and [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)) macros get the 16-bit width and height values from *lParam*. (You can look up these kinds of details in the MSDN documentation for each message code.) The window procedure extracts the width and height, and then passes these values to the `OnSize` function.

## Default Message Handling

If you don't handle a particular message in your window procedure, pass the message parameters directly to the [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) function. This function performs the default action for the message, which varies by message type.

```C++
return DefWindowProc(hwnd, uMsg, wParam, lParam);
```

## Avoiding Bottlenecks in Your Window Procedure

While your window procedure executes, it blocks any other messages for windows created on the same thread. Therefore, avoid lengthy processing inside your window procedure. For example, suppose your program opens a TCP connection and waits indefinitely for the server to respond. If you do that inside the window procedure, your UI will not respond until the request completes. During that time, the window cannot process mouse or keyboard input, repaint itself, or even close.

Instead, you should move the work to another thread, using one of the multitasking facilities that are built into Windows:

- Create a new thread.
- Use a thread pool.
- Use asynchronous I/O calls.
- Use asynchronous procedure calls.

## Next

[Painting the Window](painting-the-window.md)
