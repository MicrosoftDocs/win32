---
title: Using Tree-View Controls
description: This section contains implementation details and example code for working with tree-view controls.
ms.assetid: 37736770-5030-4f8a-a020-6897ed5f4e96
ms.topic: article
ms.date: 05/31/2018
---

# Using Tree-View Controls

This section contains implementation details and example code for working with tree-view controls.

## In this section



| Topic                                                                                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [How to Create a Tree-View Control](create-a-tree-view-control.md)<br/>       | To create a tree-view control, use the [**CreateWindowEx**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) function, specifying the [**WC\_TREEVIEW**](common-control-window-classes.md) value for the window class. The tree-view window class is registered in the application's address space when the common control DLL is loaded. To ensure that the DLL is loaded, use the [**InitCommonControls**](/windows/desktop/api/Commctrl/nf-commctrl-initcommoncontrols) function. <br/>                                                                    |
| [How to Initialize the Image List](initialize-the-image-list.md)<br/>         | Every item in a tree-view control can have two images associated with it. An item displays one image when it is selected and the other when it is not. To include images with tree-view items, first use the [Image Lists](image-lists.md) functions to create an image list and add images to it. Then associate the image list with the tree-view control by using the [**TVM\_SETIMAGELIST**](tvm-setimagelist.md) message. <br/>                                                                     |
| [How to Add Tree-View Items](add-tree-view-items.md)<br/>                     | You add an item to a tree-view control by sending the [**TVM\_INSERTITEM**](tvm-insertitem.md) message to the control. The message includes the address of a [**TVINSERTSTRUCT**](/windows/win32/api/commctrl/ns-commctrl-tvinsertstructa) structure, specifying the parent item, the item after which the new item is inserted, and a [**TVITEM**](/windows/win32/api/commctrl/ns-commctrl-tvitema) structure that defines the attributes of the item. The attributes include the item's label, its selected and nonselected images, and a 32-bit application-defined value. <br/> |
| [How to Drag a Tree-View Item](drag-a-tree-view-item.md)<br/>                 | This topic demonstrates code for handling dragging and dropping of tree-view items. The sample code consists of three functions. The first function begins the drag operation, the second function drags the image, and the third function ends the drag operation. <br/>                                                                                                                                                                                                                                  |
| [How to Work With State Image Indexes](work-with-state-image-indexes.md)<br/> | There is often confusion about how to set and retrieve the state image index in a tree-view control. The following examples demonstrate the proper method for setting and retrieving the state image index. The examples assume that there are only two state image indexes in the tree-view control, unchecked and checked. If your application contains more than two, these functions will need to be modified to handle that case. <br/>                                                               |
| [How to Use Tree-View Infotips](use-tree-view-infotips.md)<br/>               | When you apply the [**TVS\_INFOTIP**](tree-view-control-window-styles.md) style to a tree-view control, it generates [TVN\_GETINFOTIP](tvn-getinfotip.md) notifications when the cursor is over an item in the tree view. By responding to this notification, you can set the text that appears in the infotip. <br/>                                                                                                                                                                                    |



 

 

