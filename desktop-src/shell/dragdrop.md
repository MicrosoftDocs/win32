---
Description: Many applications allow users to transfer data to another application by dragging and dropping the data with the mouse, or by using the Clipboard.
title: Transferring Shell Objects with Drag-and-Drop and the Clipboard
ms.topic: article
ms.date: 05/31/2018
ms.assetid: bd73098b-2f69-48a4-bb06-e1e0a452e69d
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Transferring Shell Objects with Drag-and-Drop and the Clipboard

Many applications allow users to transfer data to another application by dragging and dropping the data with the mouse, or by using the Clipboard. Among the many types of data that can be transferred are Shell objects such as files or folders. Shell data transfer can take place between two applications, but users can also transfer Shell data to or from the desktop or Windows Explorer.

Although files are the most commonly transferred Shell object, Shell data transfer can involve any of the variety of objects found in the [Shell namespace](namespace-intro.md). For instance, your application might need to transfer a file to a virtual folder such as the Recycle Bin, or accept an object from a non-Microsoft namespace extension. If you are implementing a namespace extension, it must be able to behave properly as a drop source and target.

This document discusses how applications can implement drag-and-drop and Clipboard data transfers with Shell objects.

-   [The Shell Data Object](dataobject.md)
-   [Shell Clipboard Formats](clipboard.md)
-   [Handling Shell Data Transfer Scenarios](datascenarios.md)

## How Drag-and-Drop Works with Shell Objects

Applications often need to provide users with a way to transfer Shell data. Some examples are:

-   Dragging a file from Windows Explorer or the desktop and dropping it on an application.
-   Copying a file to the Clipboard in Windows Explorer and pasting it into an application.
-   Dragging a file from an application to the Recycle Bin.

For a detailed discussion of how to handle these and other scenarios, see [Handling Shell Data Transfer Scenarios](datascenarios.md). This document focuses on the general principles behind Shell data transfer.

Windows provides two standard ways for applications to transfer Shell data:

-   A user cuts or copies Shell data, such as one or more files, to the Clipboard. The other application retrieves the data from the Clipboard.
-   A user drags an icon that represents the data from the source application and drops the icon on a window owned by the target.

In both cases, the transferred data is contained in a *data object*. Data objects are Component Object Model (COM) objects that expose the [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface. Schematically, there are three essential steps that all Shell data transfers must follow:

1.  The source creates a data object that represents the data that is to be transferred.
2.  The target receives a pointer to the data object's [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface.
3.  The target calls the [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface to extract the data from it.

The difference between Clipboard and drag-and-drop data transfers lies primarily in how the [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) pointer is transferred from the source to the target.

### Clipboard Data Transfers

The Clipboard is the simplest way to transfer Shell data. The basic procedure is similar to standard Clipboard data transfers. However, because you are transferring a pointer to a data object, not the data itself, you must use the OLE clipboard API instead of the standard clipboard API. The following procedure outlines how to use the OLE clipboard API to transfer Shell data with the Clipboard:

1.  The data source creates a data object to contain the data.
2.  The data source calls [**OleSetClipboard**](https://msdn.microsoft.com/library/ms686623(v=VS.85).aspx), which places a pointer to the data object's [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface on the Clipboard.
3.  The target calls [**OleGetClipboard**](https://msdn.microsoft.com/library/ms692778(v=VS.85).aspx) to retrieve the pointer to the data object's [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface.
4.  The target extracts the data by calling the [**IDataObject::GetData**](https://msdn.microsoft.com/library/ms678431(v=VS.85).aspx) method.
5.  With some Shell data transfers, the target might also need to call the data object's [**IDataObject::SetData**](https://msdn.microsoft.com/library/ms686626(v=VS.85).aspx) method to provide feedback to the data object on the outcome of the data transfer. See [Handling Optimized Move Operations](datascenarios.md) for an example of this type of operation.

### Drag-and-Drop Data Transfers

While somewhat more complex to implement, drag-and-drop data transfer has some significant advantages over the Clipboard:

-   Drag-and-drop transfers can be done with a simple mouse movement, making operation more flexible and intuitive to use than the Clipboard.
-   Drag-and-drop provides the user with a visual representation of the operation. The user can follow the icon as it moves from source to target.
-   Drag-and-drop notifies the target when the data is available.

Drag-and-drop operations also use data objects to transfer data. However, the drop source must provide functionality beyond that required for Clipboard transfers:

-   The drop source must also create an object that exposes an [**IDropSource**](https://msdn.microsoft.com/library/ms690071(v=VS.85).aspx) interface. The system uses **IDropSource** to communicate with the source while the operation is in progress.
-   The drag-and-drop data object is responsible for tracking cursor movement and displaying an icon to represent the data object.

Drop targets must also provide more functionality than is needed to handle Clipboard transfers:

-   The drop target must expose an [**IDropTarget**](https://msdn.microsoft.com/library/ms679679(v=VS.85).aspx) interface. When the cursor is over a target window, the system uses **IDropTarget** to provide the target with information such as the cursor position, and to notify it when the data is dropped.
-   The drop target must register itself with the system by calling [**RegisterDragDrop**](https://msdn.microsoft.com/library/ms678405(v=VS.85).aspx). This function provides the system with the handle to a target window and a pointer to the target application's [**IDropTarget**](https://msdn.microsoft.com/library/ms679679(v=VS.85).aspx) interface.

> [!Note]  
> For drag-and-drop operations, your application must initialize COM with [**OleInitialize**](https://msdn.microsoft.com/library/ms690134(v=VS.85).aspx), not [**CoInitialize**](https://msdn.microsoft.com/library/ms678543(v=VS.85).aspx).

 

The following procedure outlines the essential steps that are typically used to transfer Shell data with drag-and-drop:

1.  The target calls [**RegisterDragDrop**](https://msdn.microsoft.com/library/ms678405(v=VS.85).aspx) to give the system a pointer to its [**IDropTarget**](https://msdn.microsoft.com/library/ms679679(v=VS.85).aspx) interface and register a window as a drop target.
2.  When the user starts a drag-and-drop operation, the source creates a data object and initiates a *drag loop* by calling [**DoDragDrop**](https://msdn.microsoft.com/library/ms678486(v=VS.85).aspx).
3.  When the cursor is over the target window, the system notifies the target by calling one of the target's [**IDropTarget**](https://msdn.microsoft.com/library/ms679679(v=VS.85).aspx) methods. The system calls [**IDropTarget::DragEnter**](https://msdn.microsoft.com/library/ms680106(v=VS.85).aspx) when the cursor enters the target window, and [**IDropTarget::DragOver**](https://msdn.microsoft.com/library/ms680129(v=VS.85).aspx) as the cursor passes over the target window. Both methods provide the drop target with the current cursor position and the state of keyboard modifier keys such as CTRL or ALT. When the cursor leaves the target window, the system notifies the target by calling [**IDropTarget::DragLeave**](https://msdn.microsoft.com/library/ms680110(v=VS.85).aspx). When any of these methods return, the system calls the [**IDropSource**](https://msdn.microsoft.com/library/ms690071(v=VS.85).aspx) interface to pass the return value to the source.
4.  When the user releases the mouse button to drop the data, the system calls the target's [**IDropTarget::Drop**](https://msdn.microsoft.com/library/ms687242(v=VS.85).aspx) method. Among the method's parameters is a pointer to the data object's [**IDataObject**](https://msdn.microsoft.com/library/ms688421(v=VS.85).aspx) interface.
5.  The target calls the data object's [**IDataObject::GetData**](https://msdn.microsoft.com/library/ms678431(v=VS.85).aspx) method to extract the data.
6.  With some Shell data transfers, the target might also need to call the data object's [**IDataObject::SetData**](https://msdn.microsoft.com/library/ms686626(v=VS.85).aspx) method to provide feedback to the source on the outcome of the data transfer.
7.  When the target is finished with the data object, it returns from [**IDropTarget::Drop**](https://msdn.microsoft.com/library/ms687242(v=VS.85).aspx). The system returns the source's [**DoDragDrop**](https://msdn.microsoft.com/library/ms678486(v=VS.85).aspx) call to notify the source that the data transfer is complete.
8.  Depending on the particular [data transfer scenario](datascenarios.md), the source might need to take additional action based on the value returned by [**DoDragDrop**](https://msdn.microsoft.com/library/ms678486(v=VS.85).aspx) and the values that are passed to the data object by the target. For instance, when a file is moved, the source must check these values to determine whether it must delete the original file.
9.  The source releases the data object.

While the procedures outlined above provide a good general model for Shell data transfer, there are many different types of data that can be contained in a Shell data object. There are also a number of different data transfer scenarios that your application might need to handle. Each data type and scenario requires a somewhat different approach to three key steps in the procedure:

-   How a source constructs a data object to contain the Shell data.
-   How a target extracts Shell data from the data object.
-   How the source completes the data transfer operation.

The [Shell Data Object](dataobject.md) provides a general discussion of how a source constructs a Shell data object, and how that data object can be handled by the target. [Handling Shell Data Transfer Scenarios](datascenarios.md) discusses in detail how to handle a number of common Shell data transfer scenarios.

 

 



