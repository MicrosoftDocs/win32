---
title: Using Drag to Result Pane Items
description: In MMC 2.0, a snap-in can enable its result pane (or leaf) item as a drop target in drag-and-drop operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a48823af-2de6-465b-913c-7cdcdbd04040
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Drag to Result Pane Items

In MMC 2.0, a snap-in can enable its result pane (or leaf) item as a drop target in drag-and-drop operations. A drop target refers to the destination of the drag-and-drop operation (the dragged content is referred to as the drag source). In MMC 1.2, only scope (or container) items were allowed as drop targets.

To facilitate result pane items as drop targets, MMC 2.0 supports a new interface, [**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2). **IComponent2** is implemented by your snap-in, and MMC calls your snap-in's [**IComponent2::GetResultViewType2**](/windows/desktop/api/Mmc/nf-mmc-icomponent2-getresultviewtype2) method to determine the type of the snap-in's result view. Specify the RVTI\_LIST\_OPTIONS\_ALLOWPASTE option when your snap-in's **IComponent2::GetResultViewType2** method is called to inform MMC that your snap-in supports dropping to a result pane item The RVTI\_LIST\_OPTIONS\_ALLOWPASTE view option applies to the dwListOptions member of the [**RESULT\_VIEW\_TYPE\_INFO**](/windows/desktop/api/Mmc/ns-mmc-_result_view_type_info) structure (a pointer to this structure is a parameter of **IComponent2::GetResultViewType2**). By specifying the RVTI\_LIST\_OPTIONS\_ALLOWPASTE view option, your snap-in will receive [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notifications for the data object corresponding to the result pane item drop target; the notifications are sent when the cursor is dragging an item over the result pane item, or if the result pane item is selected. The **MMCN\_QUERY\_PASTE** notification provides the result pane item's data object (as the lpDataObject parameter) when the snap-in receives the notification.

By design, multiple selected items cannot be dropped into a result pane item (only one item can be dropped). In addition MMC does not support drag-and-drop operations into an OCX (OLE Custom Control) or webpage that serves as the result view. If your snap-in requires this functionality, consider using the COM [**Drag and Drop**](https://www.bing.com/search?q=**Drag and Drop**) interfaces.

## Related topics

<dl> <dt>

[**IComponent2**](/windows/desktop/api/Mmc/nn-mmc-icomponent2)
</dt> </dl>

 

 




