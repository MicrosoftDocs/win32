---
description: Each window is a member of a particular window class. The window class determines the default window procedure that an individual window uses to process its messages.
ms.assetid: 3a8e8f4e-910d-4863-a4a7-dd37c2dfa402
title: About Window Procedures
ms.topic: article
ms.date: 05/31/2018
---

# About Window Procedures

Each window is a member of a particular window class. The window class determines the default window procedure that an individual window uses to process its messages. All windows belonging to the same class use the same default window procedure. For example, the system defines a window procedure for the combo box class (**COMBOBOX**); all combo boxes then use that window procedure.

An application typically registers at least one new window class and its associated window procedure. After registering a class, the application can create many windows of that class, all of which use the same window procedure. Because this means several sources could simultaneously call the same piece of code, you must be careful when modifying shared resources from a window procedure. For more information, see [Window Classes](window-classes.md).

Window procedures for dialog boxes (called dialog box procedures) have a similar structure and function as regular window procedures. All points referring to window procedures in this section also apply to dialog box procedures. For more information, see [Dialog Boxes](/windows/desktop/dlgbox/dialog-boxes).

This section discusses the following topics.

-   [Structure of a Window Procedure](#structure-of-a-window-procedure)
-   [Default Window Procedure](#default-window-procedure)
-   [Window Procedure Subclassing](#window-procedure-subclassing)
    -   [Instance Subclassing](#instance-subclassing)
    -   [Global Subclassing](#global-subclassing)
-   [Window Procedure Superclassing](#window-procedure-superclassing)

## Structure of a Window Procedure

A window procedure is a function that has four parameters and returns a signed value. The parameters consist of a window handle, a **UINT** message identifier, and two message parameters declared with the **WPARAM** and **LPARAM** data types. For more information, see [**WindowProc**](/previous-versions/windows/desktop/legacy/ms633573(v=vs.85)).

Message parameters often contain information in both their low-order and high-order words. There are several macros an application can use to extract information from the message parameters. The [**LOWORD**](/previous-versions/windows/desktop/legacy/ms632659(v=vs.85)) macro, for example, extracts the low-order word (bits 0 through 15) from a message parameter. Other macros include [**HIWORD**](/previous-versions/windows/desktop/legacy/ms632657(v=vs.85)), [**LOBYTE**](/previous-versions/windows/desktop/legacy/ms632658(v=vs.85)), and [**HIBYTE**](/previous-versions/windows/desktop/legacy/ms632656(v=vs.85)).

The interpretation of the return value depends on the particular message. Consult the description of each message to determine the appropriate return value.

Because it is possible to call a window procedure recursively, it is important to minimize the number of local variables that it uses. When processing individual messages, an application should call functions outside the window procedure to avoid excessive use of local variables, possibly causing the stack to overflow during deep recursion.

## Default Window Procedure

The default window procedure function, [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) defines certain fundamental behavior shared by all windows. The default window procedure provides the minimal functionality for a window. An application-defined window procedure should pass any messages that it does not process to the **DefWindowProc** function for default processing.

## Window Procedure Subclassing

When an application creates a window, the system allocates a block of memory for storing information specific to the window, including the address of the window procedure that processes messages for the window. When the system needs to pass a message to the window, it searches the window-specific information for the address of the window procedure and passes the message to that procedure.

*Subclassing* is a technique that allows an application to intercept and process messages sent or posted to a particular window before the window has a chance to process them. By subclassing a window, an application can augment, modify, or monitor the behavior of the window. An application can subclass a window belonging to a system global class, such as an edit control or a list box. For example, an application could subclass an edit control to prevent the control from accepting certain characters. However, you cannot subclass a window or class that belongs to another application. All subclassing must be performed within the same process.

An application subclasses a window by replacing the address of the window's original window procedure with the address of a new window procedure, called the *subclass procedure*. Thereafter, the subclass procedure receives any messages sent or posted to the window.

The subclass procedure can take three actions upon receiving a message: it can pass the message to the original window procedure, modify the message and pass it to the original window procedure, or process the message and not pass it to the original window procedure. If the subclass procedure processes a message, it can do so before, after, or both before and after it passes the message to the original window procedure.

The system provides two types of subclassing: [instance](#instance-subclassing) and [global](#global-subclassing). In *instance subclassing*, an application replaces the window procedure address of a single instance of a window. An application must use instance subclassing to subclass an existing window. In *global subclassing*, an application replaces the address of the window procedure in the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure of a window class. All subsequent windows created with the class have the address of the subclass procedure, but existing windows of the class are not affected.

### Instance Subclassing

An application subclasses an instance of a window by using the [**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) function. The application passes the **GWL\_WNDPROC** flag, the handle to the window to subclass, and the address of the subclass procedure to **SetWindowLong**. The subclass procedure can reside in either the application's executable or a DLL.

[**SetWindowLong**](/windows/win32/api/winuser/nf-winuser-setwindowlonga) returns the address of the window's original window procedure. The application must save the address, using it in subsequent calls to the [**CallWindowProc**](/windows/win32/api/winuser/nf-winuser-callwindowproca) function, to pass intercepted messages to the original window procedure. The application must also have the original window procedure address to remove the subclass from the window. To remove the subclass, the application calls **SetWindowLong** again, passing the address of the original window procedure with the **GWL\_WNDPROC** flag and the handle to the window.

The system owns the system global classes, and aspects of the controls might change from one version of the system to the next. If the application must subclass a window that belongs to a system global class, the developer may need to update the application when a new version of the system is released.

Because instance subclassing occurs after a window is created, you cannot add any extra bytes to the window. Applications that subclass a window should use the window's property list to store any data needed for an instance of the subclassed window. For more information, see [Window Properties](window-properties.md).

When an application subclasses a subclassed window, it must remove the subclasses in the reverse order they were performed. If the removal order is not reversed, an unrecoverable system error may occur.

### Global Subclassing

To globally subclass a window class, the application must have a handle to a window of the class. The application also needs the handle to remove the subclass. To get the handle, an application typically creates a hidden window of the class to be subclassed. After obtaining the handle, the application calls the [**SetClassLong**](/windows/win32/api/winuser/nf-winuser-setclasslonga) function, specifying the handle, the **GCL\_WNDPROC** flag, and the address of the subclass procedure. **SetClassLong** returns the address of the original window procedure for the class.

The original window procedure address is used in global subclassing in the same way it is used in instance subclassing. The subclass procedure passes messages to the original window procedure by calling [**CallWindowProc**](/windows/win32/api/winuser/nf-winuser-callwindowproca). The application removes the subclass from the window class by calling [**SetClassLong**](/windows/win32/api/winuser/nf-winuser-setclasslonga) again, specifying the address of the original window procedure, the **GCL\_WNDPROC** flag, and the handle to a window of the class being subclassed. An application that globally subclasses a control class must remove the subclass when the application terminates; otherwise, an unrecoverable system error may occur.

Global subclassing has the same limitations as instance subclassing, plus some additional restrictions. An application should not use the extra bytes for either the class or the window instance without knowing exactly how the original window procedure uses them. If the application must associate data with a window, it should use window properties.

## Window Procedure Superclassing

*Superclassing* is a technique that allows an application to create a new window class with the basic functionality of the existing class, plus enhancements provided by the application. A superclass is based on an existing window class called the *base class*. Frequently, the base class is a system global window class such as an edit control, but it can be any window class.

A superclass has its own window procedure, called the superclass procedure. The *superclass procedure* can take three actions upon receiving a message: It can pass the message to the original window procedure, modify the message and pass it to the original window procedure, or process the message and not pass it to the original window procedure. If the superclass procedure processes a message, it can do so before, after, or both before and after it passes the message to the original window procedure.

Unlike a subclass procedure, a superclass procedure can process window creation messages ([**WM\_NCCREATE**](wm-nccreate.md), [**WM\_CREATE**](wm-create.md), and so on), but it must also pass them to the original base-class window procedure so that the base-class window procedure can perform its initialization procedure.

To superclass a window class, an application first calls the [**GetClassInfo**](/windows/win32/api/winuser/nf-winuser-getclassinfoa) function to retrieve information about the base class. **GetClassInfo** fills a [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure with the values from the **WNDCLASS** structure of the base class. Next, the application copies its own instance handle into the **hInstance** member of the **WNDCLASS** structure and copies the name of the superclass into the **lpszClassName** member. If the base class has a menu, the application must provide a new menu with the same menu identifiers and copy the menu name into the **lpszMenuName** member. If the superclass procedure processes the [**WM\_COMMAND**](/windows/desktop/menurc/wm-command) message and does not pass it to the window procedure of the base class, the menu need not have corresponding identifiers. **GetClassInfo** does not return the **lpszMenuName**, **lpszClassName**, or **hInstance** member of the **WNDCLASS** structure.

An application must also set the **lpfnWndProc** member of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure. The [**GetClassInfo**](/windows/win32/api/winuser/nf-winuser-getclassinfoa) function fills this member with the address of the original window procedure for the class. The application must save this address, to pass messages to the original window procedure, and then copy the address of the superclass procedure into the **lpfnWndProc** member. The application can, if necessary, modify any other members of the **WNDCLASS** structure. After it fills the **WNDCLASS** structure, the application registers the superclass by passing the address of the structure to the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa) function. The superclass can then be used to create windows.

Because superclassing registers a new window class, an application can add to both the extra class bytes and the extra window bytes. The superclass must not use the original extra bytes for the base class or the window for the same reasons that an instance subclass or a global subclass should not use them. Also, if the application adds extra bytes for its use to either the class or the window instance, it must reference the extra bytes relative to the number of extra bytes used by the original base class. Because the number of bytes used by the base class may vary from one version of the base class to the next, the starting offset for the superclass's own extra bytes may also vary from one version of the base class to the next.

 

 
