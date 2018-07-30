---
Description: A parent process can specify properties associated with the main window of its child process.
ms.assetid: 12547da4-8d41-48c5-8efc-f0423f64caa7
title: Setting Window Properties Using STARTUPINFO
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Window Properties Using STARTUPINFO

A parent process can specify properties associated with the main window of its child process. The [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) function takes a pointer to a [**STARTUPINFO**](https://msdn.microsoft.com/en-us/library/ms686331(v=VS.85).aspx) structure as one of its parameters. Use the members of this structure to specify characteristics of the child process's main window. The **dwFlags** member contains a bitfield that determines which other members of the structure are used. This allows you to specify values for any subset of the window properties. The system uses default values for the properties you do not specify. The **dwFlags** member can also force a feedback cursor to be displayed during the initialization of the new process.

For GUI processes, the [**STARTUPINFO**](https://msdn.microsoft.com/en-us/library/ms686331(v=VS.85).aspx) structure specifies the default values to be used the first time the new process calls the [**CreateWindow**](https://msdn.microsoft.com/library/ms632679(v=VS.85).aspx) and [**ShowWindow**](https://msdn.microsoft.com/library/ms633548(v=VS.85).aspx) functions to create and display an overlapped window. The following default values can be specified:

-   The width and height, in pixels, of the window created by [**CreateWindow**](https://msdn.microsoft.com/library/ms632679(v=VS.85).aspx).
-   The location, in screen coordinates of the window created by [**CreateWindow**](https://msdn.microsoft.com/library/ms632679(v=VS.85).aspx).
-   The *nCmdShow* parameter of [**ShowWindow**](https://msdn.microsoft.com/library/ms633548(v=VS.85).aspx).

For console processes, use the [**STARTUPINFO**](https://msdn.microsoft.com/en-us/library/ms686331(v=VS.85).aspx) structure to specify window properties only when creating a new console (either using [**CreateProcess**](https://msdn.microsoft.com/en-us/library/ms682425(v=VS.85).aspx) with CREATE\_NEW\_CONSOLE or with the [**AllocConsole**](https://msdn.microsoft.com/library/ms681944(v=VS.85).aspx) function). The **STARTUPINFO** structure can be used to specify the following console window properties:

-   The size of the new console window, in character cells.
-   The location of the new console window, in screen coordinates.
-   The size, in character cells, of the new console's screen buffer.
-   The text and background color attributes of the new console's screen buffer.
-   The title of the new console's window.

 

 



