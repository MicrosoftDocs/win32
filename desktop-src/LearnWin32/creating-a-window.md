---
title: Creating a Window
description: Creating a Window
ms.assetid: e036519f-26b5-436c-b909-bb280d758e81
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Window

## Window Classes

A *window class* defines a set of behaviors that several windows might have in common. For example, in a group of buttons, each button has a similar behavior when the user clicks the button. Of course, buttons are not completely identical; each button displays its own text string and has its own screen coordinates. Data that is unique for each window is called *instance data*.

Every window must be associated with a window class, even if your program only ever creates one instance of that class. It is important to understand that a window class is not a "class" in the C++ sense. Rather, it is a data structure used internally by the operating system. Window classes are registered with the system at run time. To register a new window class, start by filling in a [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure:

```C++
// Register the window class.
const wchar_t CLASS_NAME[]  = L"Sample Window Class";

WNDCLASS wc = { };

wc.lpfnWndProc   = WindowProc;
wc.hInstance     = hInstance;
wc.lpszClassName = CLASS_NAME;
```

You must set the following structure members:

- **lpfnWndProc** is a pointer to an application-defined function called the *window procedure* or "window proc." The window procedure defines most of the behavior of the window. We'll examine the window procedure in detail later. For now, just treat this as a forward reference.
- **hInstance** is the handle to the application instance. Get this value from the *hInstance* parameter of **wWinMain**.
- **lpszClassName** is a string that identifies the window class.

Class names are local to the current process, so the name only needs to be unique within the process. However, the standard Windows controls also have classes. If you use any of those controls, you must pick class names that do not conflict with the control class names. For example, the window class for the button control is named "Button".

The [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure has other members not shown here. You can set them to zero, as shown in this example, or fill them in. The MSDN documentation describes the structure in detail.

Next, pass the address of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure to the [**RegisterClass**](/windows/desktop/api/winuser/nf-winuser-registerclassa) function. This function registers the window class with the operating system.

```C++
RegisterClass(&wc);
```

## Creating the Window

To create a new instance of a window, call the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function:

```C++
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
```

You can read detailed parameter descriptions on MSDN, but here is a quick summary:

- The first parameter lets you specify some optional behaviors for the window (for example, transparent windows). Set this parameter to zero for the default behaviors.
- `CLASS_NAME` is the name of the window class. This defines the type of window you are creating.
- The window text is used in different ways by different types of windows. If the window has a title bar, the text is displayed in the title bar.
- The window style is a set of flags that define some of the look and feel of a window. The constant **WS\_OVERLAPPEDWINDOW** is actually several flags combined with a bitwise **OR**. Together these flags give the window a title bar, a border, a system menu, and **Minimize** and **Maximize** buttons. This set of flags is the most common style for a top-level application window.
- For position and size, the constant **CW\_USEDEFAULT** means to use default values.
- The next parameter sets a parent window or owner window for the new window. Set the parent if you are creating a child window. For a top-level window, set this to **NULL**.
- For an application window, the next parameter defines the menu for the window. This example does not use a menu, so the value is **NULL**.
- *hInstance* is the instance handle, described previously. (See [WinMain: The Application Entry Point](winmain--the-application-entry-point.md).)
- The last parameter is a pointer to arbitrary data of type **void\***. You can use this value to pass a data structure to your window procedure. We'll show one possible way to use this parameter in the section [Managing Application State](managing-application-state-.md).

[**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) returns a handle to the new window, or zero if the function fails. To show the window—that is, make the window visible —pass the window handle to the [**ShowWindow**](/windows/desktop/api/winuser/nf-winuser-showwindow) function:

```C++
ShowWindow(hwnd, nCmdShow);
```

The *hwnd* parameter is the window handle returned by [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa). The *nCmdShow* parameter can be used to minimize or maximize a window. The operating system passes this value to the program through the **wWinMain** function.

Here is the complete code to create the window. Remember that `WindowProc` is still just a forward declaration of a function.

```C++
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
```

Congratulations, you've created a window! Right now, the window does not contain any content or interact with the user. In a real GUI application, the window would respond to events from the user and the operating system. The next section describes how window messages provide this sort of interactivity.

### Next

[Window Messages](window-messages.md)
