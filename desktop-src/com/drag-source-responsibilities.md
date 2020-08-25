---
title: Drag Source Responsibilities
description: Drag Source Responsibilities
ms.assetid: bafef0c1-f78e-424a-9ed0-07764a60b22d
ms.topic: article
ms.date: 05/31/2018
---

# Drag Source Responsibilities

The drag source is responsible for the following tasks:

-   Providing a data-transfer object for the drop target that exposes the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) and [**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource) interfaces.
-   Generating pointer and source feedback.
-   Determining when the drag operation has been canceled or a drop operation has occurred.
-   Performing any action on the original data caused by the drop operation, such as deleting the data or creating a link to it.

The main task is creating a data-transfer object that exposes the [**IDataObject**](/windows/desktop/api/ObjIdl/nn-objidl-idataobject) and [**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource) interfaces. The drag source might or might not include a copy of the selected data. Including it is not mandatory, but doing so helps protect against inadvertent changes and allows the Clipboard operations code to be identical to the drag and drop code.

While a drag operation is in progress, the drag source is responsible for setting the mouse pointer and, if appropriate, for providing additional source feedback to the user. The drag source cannot provide any feedback that tracks the mouse position other than by actually setting the real pointer (see the [**SetCursor**](/windows/win32/api/winuser/nf-winuser-setcursor) function). This rule must be enforced to avoid conflicts with the feedback provided by the drop target. (A drag source can also be a drop target. When dropping on itself, the source/target can, of course, provide target feedback to track the mouse position. In this case, however, it is the drop target tracking the mouse, not the source.) Based on the feedback offered by the drop target, the source sets an appropriate pointer.

## Related topics

<dl> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> </dl>

 

 