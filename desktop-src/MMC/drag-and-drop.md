---
title: Enabling Drag-and-Drop in the MMC
description: Drag-and-drop operations work automatically in snap-ins that implement the cut, copy, and paste standard verbs.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bd339966-2c10-492e-a146-92a909bb57b5'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["drag-and-drop operations MMC"]
---

# Enabling Drag-and-Drop in the MMC

Drag-and-drop operations work automatically in snap-ins that implement the cut, copy, and paste standard verbs. This section discusses how to implement these verbs and what the various responsibilities of the source and destination of a drag-and-drop operation are.

To read how to enable MMC standard verbs, see [Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md).

The following drag-and-drop operations are possible in MMC:

-   Items (scope and result items) from one result pane can be dragged and dropped into another result pane or into the scope item that owns the result pane.
-   A scope item in the scope pane can be dragged and dropped into another scope item.

Drag-and-drop operations also apply in multiple views, or even in multiple snap-ins. You can, for example, select a scope or result item in one view of one snap-in, drag it into another snap-in's result pane, and drop it. Of course, you can achieve the same results by cutting or copying the source scope or result item and then pasting it in the destination scope item or its result pane.

Be aware that drag-and-drop operations on snap-in static nodes are not allowed. You cannot, for example, add two snap-ins to a console, select the console root to display the static nodes of the two snap-ins in the result pane, select one of the static nodes and then drag it and drop it in the other static node in the scope pane.

## How Drag-and-Drop Works in MMC

To understand drag-and-drop operations, you really need to understand how the cut, copy, paste, and delete verbs work in a drag-and-drop operation. Basically, the mechanism of cutting or copying a scope or result item and pasting it in another scope item or its result pane works in the following way:

1.  The user selects the source scope or result item (henceforth the *source item*) and either cuts or copies it. If the source item is cut, its icon is grayed out, indicating that the item will be cut after a successful paste. MMC calls the [**IComponent::QueryDataObject**](icomponent-querydataobject.md) method of the source snap-in's current view and requests a data object for the cut or copied source item.
2.  The user then selects the destination scope item or a result item in its result pane (henceforth *destination item*.) MMC then calls the [**IComponent::Notify**](icomponent-notify.md) method of the destination snap-in's current view with the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification. The *lpDataObject* parameter passed in the method call contains the data object for the destination item, and the *arg* parameter contains the data object for the source item.
3.  If the source item can be pasted in the destination item, the destination snap-in's [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification handler returns **S\_OK**. Otherwise, it returns **S\_FALSE**. Also, note the user is allowed to paste the source item in the destination item only if the snap-in returns **S\_OK** in its **MMCN\_QUERY\_PASTE** notification handler. Otherwise, MMC disables the paste verb for the destination item.
4.  If the destination snap-in accepts the paste, MMC then calls the [**IComponent::Notify**](icomponent-notify.md) method of the destination's current view with the [**MMCN\_PASTE**](mmcn-paste.md) notification. Again, the *lpDataObject* parameter contains the destination item's data object, and the *arg* parameter contains the source item's data object. The *param* parameter is an out parameter that will hold a data object for the source item after a successful paste. This is so the source snap-in can know which item to delete after a successful paste.
5.  The destination snap-in performs the paste operation and returns **S\_OK** in its [**MMCN\_PASTE**](mmcn-paste.md) notification handler for the destination item. The destination snap-in must also specify a data object for the successfully pasted source item in the *param* parameter. This data object is in turn forwarded to the source snap-in through the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification. If the operation is a copy operation as opposed to a cut operation, the destination snap-in need not fill the *param* parameter.
6.  In a cut operation, MMC then calls the [**IComponent::Notify**](icomponent-notify.md) method of the source snap-in's current view with the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification. The *arg* parameter passed in the method call contains the data object for the cut source item. The source snap-in handles the notification and then returns **S\_OK**.

    Be aware that MMC does not delete a source item that has been cut by the user. If the user cuts a result item from a result pane, and the result pane is still visible after the cut, the snap-in should call [**IResultData::DeleteItem**](iresultdata-deleteitem.md) to remove the cut item. For a cut scope item, the snap-in should call [**IConsoleNameSpace2::DeleteItem**](iconsolenamespace2-deleteitem.md) to delete the scope item from the scope pane.

## Related topics

<dl> <dt>

[Drag and Drop: Implementation Details](drag-and-drop-implementation-details.md)
</dt> <dt>

[**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md)
</dt> <dt>

[**MMCN\_PASTE**](mmcn-paste.md)
</dt> <dt>

[**MMCN\_CUTORMOVE**](mmcn-cutormove.md)
</dt> <dt>

[Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md)
</dt> <dt>

[Using MMC 2.0 Drag-and-Drop Features](using-mmc-2-0-drag-and-drop-features.md)
</dt> </dl>

 

 




