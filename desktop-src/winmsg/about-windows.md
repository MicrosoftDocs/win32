---
Description: This topic describes the programming elements that applications use to create and use windows; manage relationships between windows; and size, move, and display windows.
ms.assetid: e325f8dc-004f-44a9-9122-3be5e44764d6
title: About Windows
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Windows

This topic describes the programming elements that applications use to create and use windows; manage relationships between windows; and size, move, and display windows.

The overview includes the following topics.

-   [Desktop Window](#desktop-window)
-   [Application Windows](#application-windows)
    -   [Client Area](#client-area)
    -   [Nonclient Area](#nonclient-area)
-   [Controls and Dialog Boxes](#controls-and-dialog-boxes)
-   [Window Attributes](#window-attributes)
    -   [Class Name](#class-name)
    -   [Window Name](#window-name)
    -   [Window Style](#window-style)
    -   [Extended Window Style](#extended-window-style)
    -   [Position](#position)
    -   [Size](#size)
    -   [Parent or Owner Window Handle](#parent-or-owner-window-handle)
    -   [Menu Handle or Child-Window Identifier](#menu-handle-or-child-window-identifier)
    -   [Application Instance Handle](#application-instance-handle)
    -   [Creation Data](#creation-data)
    -   [Window Handle](#window-handle)
-   [Window Creation](#creation-data)
    -   [Main Window Creation](#main-window-creation)
    -   [Window-Creation Messages](#window-creation-messages)
    -   [Multithread Applications](#multithread-applications)

## Desktop Window

When you start the system, it automatically creates the desktop window. The *desktop window* is a system-defined window that paints the background of the screen and serves as the base for all windows displayed by all applications.

The desktop window uses a bitmap to paint the background of the screen. The pattern created by the bitmap is called the *desktop wallpaper*. By default, the desktop window uses the bitmap from a .bmp file specified in the registry as the desktop wallpaper.

The [**GetDesktopWindow**](https://msdn.microsoft.com/en-us/library/ms633504(v=VS.85).aspx) function returns a handle to the desktop window.

A system configuration application, such as a Control Panel item, changes the desktop wallpaper by using the [**SystemParametersInfo**](https://msdn.microsoft.com/library/windows/desktop/ms724947) function with the *wAction* parameter set to **SPI\_SETDESKWALLPAPER** and the *lpvParam* parameter specifying a bitmap file name. **SystemParametersInfo** then loads the bitmap from the specified file, uses the bitmap to paint the background of the screen, and enters the new file name in the registry.

## Application Windows

Every graphical Windows-based application creates at least one window, called the *main window*, that serves as the primary interface between the user and the application. Most applications also create other windows, either directly or indirectly, to perform tasks related to the main window. Each window plays a part in displaying output and receiving input from the user.

When you start an application, the system also associates a taskbar button with the application. The *taskbar button* contains the program icon and title. When the application is active, its taskbar button is displayed in the pushed state.

An application window includes elements such as a title bar, a menu bar, the window menu (formerly known as the system menu), the minimize button, the maximize button, the restore button, the close button, a sizing border, a client area, a horizontal scroll bar, and a vertical scroll bar. An application's main window typically includes all of these components. The following illustration shows these components in a typical main window.

![typical window](images/cswin-02.png)

### Client Area

The *client area* is the part of a window where the application displays output, such as text or graphics. For example, a desktop publishing application displays the current page of a document in the client area. The application must provide a function, called a window procedure, to process input to the window and display output in the client area. For more information, see [Window Procedures](window-procedures.md).

### Nonclient Area

The title bar, menu bar, window menu, minimize and maximize buttons, sizing border, and scroll bars are referred to collectively as the window's *nonclient area*. The system manages most aspects of the nonclient area; the application manages the appearance and behavior of its client area.

The *title bar* displays an application-defined icon and line of text; typically, the text specifies the name of the application or indicates the purpose of the window. An application specifies the icon and text when creating the window. The title bar also makes it possible for the user to move the window by using a mouse or other pointing device.

Most applications include a *menu bar* that lists the commands supported by the application. Items in the menu bar represent the main categories of commands. Clicking an item on the menu bar typically opens a pop-up menu whose items correspond to the tasks within a given category. By clicking a command, the user directs the application to carry out a task.

The *window menu* is created and managed by the system. It contains a standard set of menu items that, when chosen by the user, set a window's size or position, close the application, or perform tasks. For more information, see [Menus](https://msdn.microsoft.com/library/windows/desktop/ms646977).

The buttons in the upper-right corner affect the size and position of the window. When you click the *maximize button*, the system enlarges the window to the size of the screen and positions the window, so it covers the entire desktop, minus the taskbar. At the same time, the system replaces the maximize button with the restore button. When you click the *restore button*, the system restores the window to its previous size and position. When you click the *minimize button*, the system reduces the window to the size of its taskbar button, positions the window over the taskbar button, and displays the taskbar button in its normal state. To restore the application to its previous size and position, click its taskbar button. When you click the *close button*, the application exits.

The *sizing border* is an area around the perimeter of the window that enables the user to size the window by using a mouse or other pointing device.

The *horizontal scroll bar* and *vertical scroll bar* convert mouse or keyboard input into values that an application uses to shift the contents of the client area either horizontally or vertically. For example, a word-processing application that displays a lengthy document typically provides a vertical scroll bar to enable the user to page up and down through the document.

## Controls and Dialog Boxes

An application can create several types of windows in addition to its main window, including controls and dialog boxes.

A *control* is a window that an application uses to obtain a specific piece of information from the user, such as the name of a file to open or the desired point size of a text selection. Applications also use controls to obtain information needed to control a particular feature of an application. For example, a word-processing application typically provides a control to let the user turn word wrapping on and off. For more information, see [Windows Controls](https://msdn.microsoft.com/library/windows/desktop/bb773173).

Controls are always used in conjunction with another window—typically, a dialog box. A *dialog box* is a window that contains one or more controls. An application uses a dialog box to prompt the user for input needed to complete a command. For example, an application that includes a command to open a file would display a dialog box that includes controls in which the user specifies a path and file name. Dialog boxes do not typically use the same set of window components as does a main window. Most have a title bar, a window menu, a border (non-sizing), and a client area, but they typically do not have a menu bar, minimize and maximize buttons, or scroll bars. For more information, see [Dialog Boxes](https://msdn.microsoft.com/library/windows/desktop/ms632588).

A *message box* is a special dialog box that displays a note, caution, or warning to the user. For example, a message box can inform the user of a problem the application has encountered while performing a task. For more information, see [Message Boxes](https://msdn.microsoft.com/library/windows/desktop/ms644994#message-boxes).

## Window Attributes

An application must provide the following information when creating a window. (With the exception of the [Window Handle](#window-handle), which the creation function returns to uniquely identify the new window.)

-   [Class Name](#class-name)
-   [Window Name](#window-name)
-   [Window Style](#window-style)
-   [Extended Window Style](#extended-window-style)
-   [Position](#position)
-   [Size](#size)
-   [Parent or Owner Window Handle](#parent-or-owner-window-handle)
-   [Menu Handle or Child-Window Identifier](#menu-handle-or-child-window-identifier)
-   [Application Instance Handle](#application-instance-handle)
-   [Creation Data](#creation-data)
-   [Window Handle](#window-handle)

These window attributes are described in the following sections.

### Class Name

Every window belongs to a window class. An application must register a window class before creating any windows of that class. The *window class* defines most aspects of a window's appearance and behavior. The chief component of a window class is the *window procedure*, a function that receives and processes all input and requests sent to the window. The system provides the input and requests in the form of *messages*. For more information, see [Window Classes](window-classes.md), [Window Procedures](window-procedures.md), and [Messages and Message Queues](messages-and-message-queues.md).

### Window Name

A *window name* is a text string that identifies a window for the user. A main window, dialog box, or message box typically displays its window name in its title bar, if present. A control may display its window name, depending on the control's class. For example, buttons, edit controls, and static controls displays their window names within the rectangle occupied by the control. However, controls such as list boxes and combo boxes do not display their window names.

To change the window name after creating a window, use the [**SetWindowText**](https://msdn.microsoft.com/en-us/library/ms633546(v=VS.85).aspx) function . This function uses the [**GetWindowTextLength**](https://msdn.microsoft.com/en-us/library/ms633521(v=VS.85).aspx) and [**GetWindowText**](https://msdn.microsoft.com/en-us/library/ms633520(v=VS.85).aspx) functions to retrieve the current window-name string from the window.

### Window Style

Every window has one or more window styles. A window style is a named constant that defines an aspect of the window's appearance and behavior that is not specified by the window's class. An application usually sets window styles when creating windows. It can also set the styles after creating a window by using the [**SetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633591(v=VS.85).aspx) function.

The system and, to some extent, the window procedure for the class, interpret the window styles.

Some window styles apply to all windows, but most apply to windows of specific window classes. The general window styles are represented by constants that begin with the WS\_ prefix; they can be combined with the OR operator to form different types of windows, including main windows, dialog boxes, and child windows. The class-specific window styles define the appearance and behavior of windows belonging to the predefined control classes. For example, the **SCROLLBAR** class specifies a scroll bar control, but the [**SBS\_HORZ**](https://www.bing.com/search?q=**SBS\_HORZ**) and **SBS\_VERT** styles determine whether a horizontal or vertical scroll bar control is created.

For lists of styles that can be used by windows, see the following topics:

-   [**Window Styles**](window-styles.md)
-   [Button Styles](https://www.bing.com/search?q=Button+Styles)
-   [Combo Box Styles](https://www.bing.com/search?q=Combo+Box+Styles)
-   [Edit Control Styles](https://www.bing.com/search?q=Edit+Control+Styles)
-   [List Box Styles](https://www.bing.com/search?q=List+Box+Styles)
-   [Rich Edit Control Styles](https://www.bing.com/search?q=Rich+Edit+Control+Styles)
-   [Scroll Bar Control Styles](https://www.bing.com/search?q=Scroll+Bar+Control+Styles)
-   [Static Control Styles](https://www.bing.com/search?q=Static+Control+Styles)

### Extended Window Style

Every window can optionally have one or more extended window styles. An *extended window style* is a named constant that defines an aspect of the window's appearance and behavior that is not specified by the window class or the other window styles. An application usually sets extended window styles when creating windows. It can also set the styles after creating a window by using the [**SetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633591(v=VS.85).aspx) function.

For more information, see [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx).

### Position

A window's position is defined as the coordinates of its upper left corner. These coordinates, sometimes called window coordinates, are always relative to the upper left corner of the screen or, for a child window, the upper left corner of the parent window's client area. For example, a top-level window having the coordinates (10,10) is placed 10 pixels to the right of the upper left corner of the screen and 10 pixels down from it. A child window having the coordinates (10,10) is placed 10 pixels to the right of the upper left corner of its parent window's client area and 10 pixels down from it.

The [**WindowFromPoint**](https://msdn.microsoft.com/en-us/library/ms633558(v=VS.85).aspx) function retrieves a handle to the window occupying a particular point on the screen. Similarly, the [**ChildWindowFromPoint**](https://msdn.microsoft.com/en-us/library/ms632676(v=VS.85).aspx) and [**ChildWindowFromPointEx**](https://msdn.microsoft.com/en-us/library/ms632677(v=VS.85).aspx) functions retrieve a handle to the child window occupying a particular point in the parent window's client area. Although **ChildWindowFromPointEx** can ignore invisible, disabled, and transparent child windows, **ChildWindowFromPoint** cannot.

### Size

A window's size (width and height) is given in pixels. A window can have zero width or height. If an application sets a window's width and height to zero, the system sets the size to the default minimum window size. To discover the default minimum window size, an application uses the [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) function with the **SM\_CXMIN** and **SM\_CYMIN** flags.

An application may need to create a window with a client area of a particular size. The [**AdjustWindowRect**](https://msdn.microsoft.com/en-us/library/ms632665(v=VS.85).aspx) and [**AdjustWindowRectEx**](https://msdn.microsoft.com/en-us/library/ms632667(v=VS.85).aspx) functions calculate the required size of a window based on the desired size of the client area. The application can pass the resulting size values to the [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function.

An application can size a window so that it is extremely large; however, it should not size a window so that it is larger than the screen. Before setting a window's size, the application should check the width and height of the screen by using [**GetSystemMetrics**](https://msdn.microsoft.com/library/windows/desktop/ms724385) with the **SM\_CXSCREEN** and **SM\_CYSCREEN** flags.

### Parent or Owner Window Handle

A window can have a parent window. A window that has a parent is called a *child window*. The *parent window* provides the coordinate system used for positioning a child window. Having a parent window affects aspects of a window's appearance; for example, a child window is clipped so that no part of the child window can appear outside the borders of its parent window. A window that has no parent, or whose parent is the desktop window, is called a *top-level window*. An application uses the [**EnumWindows**](https://msdn.microsoft.com/en-us/library/ms633497(v=VS.85).aspx) function to obtain a handle to each of its top-level windows. **EnumWindows** passes the handle to each top-level window, in turn, to an application-defined callback function, [**EnumWindowsProc**](https://msdn.microsoft.com/en-us/library/ms633498(v=VS.85).aspx).

A window can own, or be owned by, another window. An owned window always appears in front of its owner window, is hidden when its owner window is minimized, and is destroyed when its owner window is destroyed. For more information, see [Owned Windows](window-features.md).

### Menu Handle or Child-Window Identifier

A child window can have a *child-window* identifier, a unique, application-defined value associated with the child window. Child-window identifiers are especially useful in applications that create multiple child windows. When creating a child window, an application specifies the identifier of the child window. After creating the window, the application can change the window's identifier by using the [**SetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633591(v=VS.85).aspx) function, or it can retrieve the identifier by using the [**GetWindowLong**](https://msdn.microsoft.com/en-us/library/ms633584(v=VS.85).aspx) function.

Every window, except a child window, can have a menu. An application can include a menu by providing a menu handle either when registering the window's class or when creating the window.

### Application Instance Handle

Every application has an instance handle associated with it. The system provides the instance handle to an application when the application starts. Because it can run multiple copies of the same application, the system uses instance handles internally to distinguish one instance of an application from another. The application must specify the instance handle in many different windows, including those that create windows.

### Creation Data

Every window can have application-defined creation data associated with it. When the window is first created, the system passes a pointer to the data on to the window procedure of the window being created. The window procedure uses the data to initialize application-defined variables.

### Window Handle

After creating a window, the creation function returns a *window handle* that uniquely identifies the window. A window handle has the **HWND** data type; an application must use this type when declaring a variable that holds a window handle. An application uses this handle in other functions to direct their actions to the window.

An application can use the [**FindWindow**](https://msdn.microsoft.com/en-us/library/ms633499(v=VS.85).aspx) function to discover whether a window with the specified class name or window name exists in the system. If such a window exists, **FindWindow** returns a handle to the window. To limit the search to the child windows of a particular application, use the [**FindWindowEx**](https://msdn.microsoft.com/en-us/library/ms633500(v=VS.85).aspx) function.

The [**IsWindow**](https://msdn.microsoft.com/en-us/library/ms633528(v=VS.85).aspx) function determines whether a window handle identifies a valid, existing window. There are special constants that can replace a window handle in certain functions. For example, an application can use **HWND\_BROADCAST** in the [**SendMessage**](https://msdn.microsoft.com/en-us/library/ms644950(v=VS.85).aspx) and [**SendMessageTimeout**](https://msdn.microsoft.com/en-us/library/ms644952(v=VS.85).aspx) functions, or **HWND\_DESKTOP** in the [**MapWindowPoints**](https://msdn.microsoft.com/library/windows/desktop/dd145046) function.

## Window Creation

To create application windows, use the [**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx) or [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function. You must provide the information required to define the window attributes. **CreateWindowEx** has a parameter, *dwExStyle*, that **CreateWindow** does not have; otherwise, the functions are identical. In fact, **CreateWindow** simply calls **CreateWindowEx** with the *dwExStyle* parameter set to zero. For this reason, the remainder of this overview refers only to **CreateWindowEx**.

This section contains the following topics:

-   [Main Window Creation](#main-window-creation)
-   [Window-Creation Messages](#window-creation-messages)
-   [Multithread Applications](#multithread-applications)

> [!Note]  
> There are additional functions for creating special-purpose windows such as dialog boxes and message boxes. For more information, see [**DialogBox**](https://msdn.microsoft.com/library/windows/desktop/ms645452), [**CreateDialog**](https://msdn.microsoft.com/library/windows/desktop/ms645434), and [**MessageBox**](https://msdn.microsoft.com/library/windows/desktop/ms645505).

 

### Main Window Creation

Every Windows-based application must have [**WinMain**](https://msdn.microsoft.com/en-us/library/ms633559(v=VS.85).aspx) as its entry point function. **WinMain** performs a number of tasks, including registering the window class for the main window and creating the main window. **WinMain** registers the main window class by calling the [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx) function, and it creates the main window by calling the [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function.

Your [**WinMain**](https://msdn.microsoft.com/en-us/library/ms633559(v=VS.85).aspx) function can also limit your application to a single instance. Create a named mutex using the [**CreateMutex**](https://msdn.microsoft.com/library/windows/desktop/ms682411) function. If [**GetLastError**](https://msdn.microsoft.com/library/windows/desktop/ms679360) returns **ERROR\_ALREADY\_EXISTS**, another instance of your application exists (it created the mutex) and you should exit **WinMain**.

The system does not automatically display the main window after creating it; instead, an application must use the [**ShowWindow**](https://msdn.microsoft.com/en-us/library/ms633548(v=VS.85).aspx) function to display the main window. After creating the main window, the application's [**WinMain**](https://msdn.microsoft.com/en-us/library/ms633559(v=VS.85).aspx) function calls **ShowWindow**, passing it two parameters: a handle to the main window and a flag specifying whether the main window should be minimized or maximized when it is first displayed. Normally, the flag can be set to any of the constants beginning with the SW\_ prefix. However, when **ShowWindow** is called to display the application's main window, the flag must be set to **SW\_SHOWDEFAULT**. This flag tells the system to display the window as directed by the program that started the application.

If a window class was registered with the Unicode version of [**RegisterClass**](https://msdn.microsoft.com/en-us/library/ms633586(v=VS.85).aspx), the window receives only Unicode messages. To determine whether a window uses the Unicode character set or not, call [**IsWindowUnicode**](https://msdn.microsoft.com/en-us/library/ms633529(v=VS.85).aspx).

### Window-Creation Messages

When creating any window, the system sends messages to the window procedure for the window. The system sends the [**WM\_NCCREATE**](wm-nccreate.md) message after creating the window's nonclient area and the [**WM\_CREATE**](wm-create.md) message after creating the client area. The window procedure receives both messages before the system displays the window. Both messages include a pointer to a [**CREATESTRUCT**](https://msdn.microsoft.com/en-us/library/ms632603(v=VS.85).aspx) structure that contains all the information specified in the [**CreateWindowEx**](https://msdn.microsoft.com/en-us/library/ms632680(v=VS.85).aspx) function. Typically, the window procedure performs initialization tasks upon receiving these messages.

When creating a child window, the system sends the [**WM\_PARENTNOTIFY**](https://msdn.microsoft.com/library/windows/desktop/hh454920) message to the parent window after sending the [**WM\_NCCREATE**](wm-nccreate.md) and [**WM\_CREATE**](wm-create.md) messages. It also sends other messages while creating a window. The number and order of these messages depend on the window class and style and on the function used to create the window. These messages are described in other topics in this help file.

### Multithread Applications

A Windows-based application can have multiple threads of execution, and each thread can create windows. The thread that creates a window must contain the code for its window procedure.

An application can use the [**EnumThreadWindows**](https://msdn.microsoft.com/en-us/library/ms633495(v=VS.85).aspx) function to enumerate the windows created by a particular thread. This function passes the handle to each thread window, in turn, to an application-defined callback function, [**EnumThreadWndProc**](https://msdn.microsoft.com/en-us/library/ms633496(v=VS.85).aspx).

The [**GetWindowThreadProcessId**](https://msdn.microsoft.com/en-us/library/ms633522(v=VS.85).aspx) function returns the identifier of the thread that created a particular window.

To set the show state of a window created by another thread, use the [**ShowWindowAsync**](https://msdn.microsoft.com/en-us/library/ms633549(v=VS.85).aspx) function.

 

 



