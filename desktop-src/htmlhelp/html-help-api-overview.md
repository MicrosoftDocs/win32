---
title: HTML Help API Overview
description: HTML Help API Overview
ms.assetid: F1FC7E13-7A29-45d4-8E2E-F21A3C885D04
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HTML Help API Overview

The HTML Help application programming interface (API) enables a Windows program to create a help window that displays a help topic. The Windows program has complete control over the type, style, and position of the help window.

The fundamental feature of the HTML Help API is the [help window](window-types.md). Through the API commands, you can create a help window that hosts a Microsoft Internet Explorer DLL (Shdocvw.dll) and displays an HTML file that you specify. The help window is owned by the window you specify. As an owned window, a help window automatically stays on top of its owner and closes when the owner is closed.

You define the styles, coordinates, captions, and display state of the help window. This level of control allows you to embed the help window in a non-OLE activated Windows program.

In addition to creating help windows, the HTML Help API commands also enable you to provide:

-   Context-sensitive help.
-   Keyword lookups.
-   Interaction between a Windows program and a compiled help (.chm) file.
-   Control over the Navigation pane in the standard HTML Help Viewer.

## ANSI and Unicode versions of the HTML Help API

The HTML Help API supports both ANSI (**HtmlHelpA**) and Unicode (**HtmlHelpW**) parameters. Specify the appropriate version of the API in your code:

-   When a program is compiled ANSI, the ANSI version of the API is used by default, allowing you to specify either **HtmlHelpA()** or **HtmlHelp()**.
-   When a program is compiled Unicode, **HtmlHelpW()** becomes the default and you can specify either **HtmlHelpW()** or **HtmlHelp()**.

## Note

The HTML Help API function is modeled after the WinHelp API function to simplify the process of updating existing programs from WinHelp to HTML Help. However, the HTML Help API command names and parameters are not the same as those in the WinHelp API, and the output file formats are very different.

 

 




