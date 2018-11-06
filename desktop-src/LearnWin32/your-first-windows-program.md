---
title: Module 1. Your First Windows Program
description: .
ms.assetid: 73848144-bf02-4382-a476-7f5a35447727
ms.topic: article
ms.date: 05/31/2018
---

# Module 1. Your First Windows Program

In this module, we will write a minimal Windows program. All it does is create and show a blank window. This first program contains about 50 lines of code, not counting blank lines and comments. It will be our starting point; later we'll add graphics, text, user input, and other features.

![screen shot of the example program](images/window01.png)

Here is the complete code for the program:


```C++
#ifndef UNICODE
#define UNICODE
#endif 

#include <windows.h>

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int WINAPI wWinMain(HINSTANCE hInstance, HINSTANCE, PWSTR pCmdLine, int nCmdShow)
{
    // Register the window class.
    const wchar_t CLASS_NAME[]  = L"Sample Window Class";
    
    WNDCLASS wc = { };

    wc.lpfnWndProc   = WindowProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    // Create the window.

    HWND hwnd = CreateWindowEx(
        0,                              // Optional window styles.
        CLASS_NAME,                     // Window class
        L"Learn to Program Windows",    // Window text
        WS_OVERLAPPEDWINDOW,            // Window style

        // Size and position
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

        NULL,       // Parent window    
        NULL,       // Menu
        hInstance,  // Instance handle
        NULL        // Additional application data
        );

    if (hwnd == NULL)
    {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    // Run the message loop.

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0))
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;

    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

```

<span codelanguage="ManagedCPlusPlus"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>C++</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>            FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));

            EndPaint(hwnd, &ps);
        }
        return 0;

    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}</code></pre></td>
</tr>
</tbody>
</table>



You can download the complete Visual Studio project from [Windows Hello World Sample](windows-hello-world-sample.md).

It may be useful to give a brief outline of what this code does. Later topics will examine the code in detail.

1.  **wWinMain** is the program entry point. When the program starts, it registers some information about the behavior of the application window. One of the most important items is the address of a function, named `WindowProc` in this example. This function defines the behavior of the window—its appearance, how it interacts with the user, and so forth.
2.  Next, the program creates the window and receives a handle that uniquely identifies the window.
3.  If the window is created successfully, the program enters a **while** loop. The program remains in this loop until the user closes the window and exits the application.

Notice that the progam does not explicitly call the `WindowProc` function, even though we said this is where most of the application logic is defined. Windows communicates with your program by passing it a series of *messages*. The code inside the **while** loop drives this process. Each time the program calls the [**DispatchMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644934) function, it indirectly causes Windows to invoke the WindowProc function, once for each message.

## In this section

-   [Creating a Window](creating-a-window.md)
-   [Window Messages](window-messages.md)
-   [Writing the Window Procedure](writing-the-window-procedure.md)
-   [Painting the Window](painting-the-window.md)
-   [Closing the Window](closing-the-window.md)
-   [Managing Application State](managing-application-state-.md)

## Related topics

<dl> <dt>

[Learn to Program for Windows in C++](learn-to-program-for-windows.md)
</dt> <dt>

[Windows Hello World Sample](windows-hello-world-sample.md)
</dt> </dl>

 

 




