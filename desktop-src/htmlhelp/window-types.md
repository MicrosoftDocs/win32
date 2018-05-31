---
title: Window Types
description: Window Types
ms.assetid: DCDB5594-1742-4fd4-84F0-8B4F01AFD99F
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Window Types

A window type is used to display a help topic and to provide users with a way to navigate through a compiled help (.chm) file. A help window is based on an [**HH\_WINTYPE**](hh-wintype-structure.md) structure and hosts a Microsoft Internet Explorer DLL (Shdocvw.dll) to display a help topic.

Any help window that you create through the HTML Help API is owned by the calling, or parent, program. This allows the help window to stay on top of its parent, yet not be on top of any other program that has focus.

In addition, any help window that you create through the API is bound by the actions of its owner. For example, if the user minimizes the calling program, the help window goes away until the owner is restored. If the user exits the calling program, the help window also closes without requiring any action from its owner. Because the calling program created the help window, it can change the position and properties of that window without affecting the procedural help of any other program.

## Defining window types

Either the help author can define window types in the project (.hhp) file using HTML Help Workshop, or the developer can define window types programmatically using the HTML Help API.

A window type definition, such as the standard [HTML Help Viewer](about-the-html-help-viewer.md), includes all of the necessary information about the window such as window style attributes and any navigational elements (such as a table of contents, index, or full-text search). When the window type is created, part of its definition are the file locations of its navigational elements. These navigational elements do not change during the life of the window type.

Window types are specific to the compiled help (.chm) file for which they are created, unless the window type is a [global window](about-global-windows.md). Associating a window type with a single compiled help file enables you to create multiple help files that all contain a window type of the same name. For example, you could create fifty compiled help files and define a window type named Main in each file without the different window types conflicting with each other.

The total number of window types that can be defined, and the total number of windows that can be displayed at any one time, is limited solely by available memory and system resources.

## Opening a help window

To create or access a help window, the developer can call the HTML Help API or the user can double-click a compiled help (.chm) file.

If a call to **HtmlHelp()** is made specifying a window type that does not exist, a type will be created using the specified name, but with default properties.

When a user double-clicks a compiled help (.chm) file, the HTML Help executable program (Hh.exe) calls the HTML Help API and the correct help window and topic appears. Accessing a help window using this method is slightly different than invoking a window through the HTML Help API.

By default, when a user double-clicks a help (.chm) file, the file opens in the window type defined in the help project (.hhp) file and displays the default help topic that is also defined in the project file. If no window is defined in the project file, then the default [Help Viewer](about-the-html-help-viewer.md) is used. If no default topic is defined in the project file, then a random help topic appears.

## Related topics

<dl> <dt>

[About the HTML Help API](html-help-api-overview.md)
</dt> </dl>

 

 




