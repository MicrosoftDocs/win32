---
Description: 'The system reduces an application''s main window (overlapping style) to a minimized window when the user clicks Minimize from the window menu or the application calls the ShowWindow function and specifies a value such as SW\_MINIMIZE.'
ms.assetid: 'a52dba49-e4ec-45e2-a00f-211a58e28773'
title: Minimized Windows
---

# Minimized Windows

The system reduces an application's main window (overlapping style) to a minimized window when the user clicks Minimize from the window menu or the application calls the [**ShowWindow**](_win32_showwindow_cpp) function and specifies a value such as SW\_MINIMIZE. Minimizing a window speeds up system performance by reducing the amount of work an application must do when updating its main window.

For a typical application, the system draws an icon, called the class icon, when the window is minimized, labeling the icon with the name of the window. The class icon, a static image that represents the application, is specified by the application when it registers the window class. The application assigns a handle to the class icon to the **hIcon** member of [**WNDCLASS**](_win32_wndclass_str_cpp) before calling [**RegisterClass**](_win32_registerclass_cpp). The application can use the [**LoadIcon**](_win32_loadicon_cpp) function to retrieve the icon handle.

 

 



