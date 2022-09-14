---
title: Drag and Drop
description: Drag and drop refers to data transfers in which a mouse or other pointing device is used to specify both the data source and its destination.
ms.assetid: bba0ddf8-fcf9-4827-bf85-7ac597d33b4b
ms.topic: article
ms.date: 05/31/2018
---

# Drag and Drop

*Drag and drop* refers to data transfers in which a mouse or other pointing device is used to specify both the data source and its destination. In a typical drag and drop operation, a user selects the object to be transferred by moving the mouse pointer to it and holding down either the left button or some other button designated for this purpose. While continuing to hold down the button, the user initiates the transfer by dragging the object to its destination, which can be any OLE container. Drag and drop provides exactly the same functionality as the OLE clipboard copy and paste but adds visual feedback and eliminates the need for menus. In fact, if an application supports clipboard copy and paste, little extra is needed to support drag and drop.

During an OLE drag and drop operation, the following three separate pieces of code are used.



| Drag-and-drop code source                               | Implementation and use                                                                                                                                                                      |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource) interface<br/> | Implemented by the object containing the dragged data, referred to as the *drag source*.<br/>                                                                                         |
| [**IDropTarget**](/windows/desktop/api/OleIdl/nn-oleidl-idroptarget) interface<br/> | Implemented by the object that is intended to accept the drop, referred to as the *drop target*.<br/>                                                                                 |
| [**DoDragDrop**](/windows/desktop/api/Ole2/nf-ole2-dodragdrop) function<br/>    | Implemented by OLE and used to initiate a drag and drop operation. After the operation is in progress, it facilitates communication between the drag source and the drop target.<br/> |



 

The [**IDropSource**](/windows/desktop/api/OleIdl/nn-oleidl-idropsource) and [**IDropTarget**](/windows/desktop/api/OleIdl/nn-oleidl-idroptarget) interfaces can be implemented in either a container or in an object application. The role of drag source or drop target is not limited to any one type of OLE application.

The OLE function [**DoDragDrop**](/windows/desktop/api/Ole2/nf-ole2-dodragdrop) implements a loop that tracks mouse and keyboard movement until such time as the drag is canceled or a drop occurs. **DoDragDrop** is the key function in the drag and drop process, facilitating communication between the drag source and drop target.

During a drag and drop operation, three types of feedback can be displayed to the user.



| Type of feedback            | Description                                                                                                                                                                                                                                                                                                                                                      |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Source feedback<br/>  | Provided by the drag source, the source feedback indicates the data is being dragged and does not change during the course of the drag. Typically, the data is highlighted to signal it has been selected.<br/>                                                                                                                                            |
| Pointer feedback<br/> | Provided by the drag source, the pointer feedback indicates what happens if the mouse is released at any given moment. Pointer feedback changes continually as the user moves the mouse and/or presses a modifier key. For example, if the pointer is moved into a window that cannot accept a drop, the pointer changes to the "not allowed" symbol.<br/> |
| Target feedback<br/>  | Provided by the drop target, target feedback indicates where the drop is to occur.<br/>                                                                                                                                                                                                                                                                    |



 

For more information, see [Drag Source Responsibilities](drag-source-responsibilities.md).

## Related topics

<dl> <dt>

[Data Transfer](data-transfer.md)
</dt> </dl>

 

 





