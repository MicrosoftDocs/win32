---
Description: The system reduces an application's main window (overlapping style) to a minimized window when the user clicks Minimize from the window menu or the application calls the ShowWindow function and specifies a value such as SW\_MINIMIZE.
ms.assetid: a52dba49-e4ec-45e2-a00f-211a58e28773
title: Minimized Windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Minimized Windows

The system reduces an application's main window (overlapping style) to a minimized window when the user clicks Minimize from the window menu or the application calls the [**ShowWindow**](https://msdn.microsoft.com/library/ms633548(v=VS.85).aspx) function and specifies a value such as SW\_MINIMIZE. Minimizing a window speeds up system performance by reducing the amount of work an application must do when updating its main window.

For a typical application, the system draws an icon, called the class icon, when the window is minimized, labeling the icon with the name of the window. The class icon, a static image that represents the application, is specified by the application when it registers the window class. The application assigns a handle to the class icon to the **hIcon** member of [**WNDCLASS**](https://msdn.microsoft.com/library/ms633576(v=VS.85).aspx) before calling [**RegisterClass**](https://msdn.microsoft.com/library/ms633586(v=VS.85).aspx). The application can use the [**LoadIcon**](https://msdn.microsoft.com/library/ms648072(v=VS.85).aspx) function to retrieve the icon handle.

 

 



