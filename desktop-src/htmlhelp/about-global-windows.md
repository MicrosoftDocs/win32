---
title: About Global Windows
description: About Global Windows
ms.assetid: D6723AA1-CDC5-4eff-BB80-E33438E204D0
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Global Windows

A global window is a help window that can be used to display one or more compiled help (.chm) files. Global window types provide backward compatibility for a bug in HTML Help version 1.1/1.1a. Unlike the current version of HTML Help, previous versions did not require a window type to be owned by a specific compiled help (.chm) file.

By default, all [window types](window-types.md) are specific to the compiled help (.chm) file for which they were defined. That is, a window type is owned by a particular .chm file. However, after you define a global window type, it is not specific to a particular .chm file and can be shared by an unlimited number of .chm files.

A popular use for global window types is to provide a simple help window to display a topic from any .chm file. Global window types are most useful when they do not include a Navigation pane because the data in the Navigation pane does not update when a different .chm is loaded.

### Defining global window types

There are two ways to define a global window type:

-   Call the [HH\_SET\_WIN\_TYPE](hh-set-win-type-command.md) command with NULL as the value of the *pszFile* parameter.
-   Add the prefix $global\_ to your window type name.

For example, MyWindow is a standard window type name, but $global\_MyWindow is a global window type name.

### Working with global windows

Like a standard window type, which is associated with a single set of navigational elements (toc, index, and full text search), a global window type is also associated with navigational elements that cannot be modified. Therefore, even though you can use one global window type to view multiple .chm files, the global window will not update the table of contents (.hhc) file, the index (.hhk) file, or any other navigational element to match the current .chm file.

For example, if A.chm and B.chm each have a global window type named $global\_main, the two definitions will conflict with each other. In most cases, the first global window type that is created controls the navigational elements that display. This means that if A.chm creates $global\_main first, you will see the navigational elements defined in A.chm. However, if B.chm creates $global\_main first, you will see the navigational elements defined in B.chm. After a global window is created, the navigational elements cannot be refreshed.

### Notes

-   If you plan to use global windows, define only one global window type for a single .chm file and make sure to load that .chm before loading any other .chm that uses the global window type.
-   After you define a global window type, all navigational elements are frozen. Regardless of the .chm file being displayed, the table of contents, index, and search information is based on the first .chm that is loaded in the window.
-   Due to a bug in HTML Help v1.1/1.1a, all window types were treated as global. Starting with HTML Help v1.3, global window types are provided to ensure backward compatibility.

## Related topics

<dl> <dt>

[About Window Types](window-types.md)
</dt> </dl>

 

 




