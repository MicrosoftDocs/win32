---
Description: This overview discusses window properties.
ms.assetid: 67ca264e-af8e-41bf-b9d1-d3db8cf1cdc3
title: About Window Properties
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# About Window Properties

A *window property* is any data assigned to a window. A window property is usually a handle of the window-specific data, but it may be any value. Each window property is identified by a string name. There are several functions that enable applications to use window properties. This overview discusses the following topics:

-   [Advantages of Using Window Properties](#advantages-of-using-window-properties)
-   [Assigning Window Properties](#assigning-window-properties)
-   [Enumerating Window Properties](#enumerating-window-properties)

## Advantages of Using Window Properties

Window properties are typically used to associate data with a subclassed window or a window in a multiple-document interface (MDI) application. In either case, it is not convenient to use the extra bytes specified in the [**CreateWindow**](https://msdn.microsoft.com/en-us/library/ms632679(v=VS.85).aspx) function or class structure for the following two reasons:

-   An application might not know how many extra bytes are available or how the space is being used. By using window properties, the application can associate data with a window without accessing the extra bytes.
-   An application must access the extra bytes by using offsets. However, window properties are accessed by their string identifiers, not by offsets.

For more information about subclassing, see [Window Procedure Subclassing](about-window-procedures.md). For more information about MDI windows, see [Multiple Document Interface](multiple-document-interface.md).

## Assigning Window Properties

The [**SetProp**](https://msdn.microsoft.com/en-us/library/ms633568(v=VS.85).aspx) function assigns a window property and its string identifier to a window. The [**GetProp**](https://msdn.microsoft.com/en-us/library/ms633564(v=VS.85).aspx) function retrieves the window property identified by the specified string. The [**RemoveProp**](https://msdn.microsoft.com/en-us/library/ms633567(v=VS.85).aspx) function destroys the association between a window and a window property but does not destroy the data itself. To destroy the data itself, use the appropriate function to free the handle that is returned by **RemoveProp**.

## Enumerating Window Properties

The [**EnumProps**](https://msdn.microsoft.com/en-us/library/ms633562(v=VS.85).aspx) and [**EnumPropsEx**](https://msdn.microsoft.com/en-us/library/ms633563(v=VS.85).aspx) functions enumerate all of a window's properties by using an application-defined callback function. For more information about the callback function, see [*PropEnumProc*](https://msdn.microsoft.com/en-us/library/ms633565(v=VS.85).aspx).

[**EnumPropsEx**](https://msdn.microsoft.com/en-us/library/ms633563(v=VS.85).aspx) includes an extra parameter for application-defined data used by the callback function. For more information about the callback function, see [*PropEnumProcEx*](https://msdn.microsoft.com/en-us/library/ms633566(v=VS.85).aspx).

 

 



