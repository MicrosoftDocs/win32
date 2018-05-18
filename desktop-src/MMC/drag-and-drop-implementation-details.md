---
title: Drag-and-Drop Implementation Details
description: The following procedure describes how to implement drag-and-drop functionality in your snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '494575ea-a7fb-4baf-a2c3-530ea18ce104'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["drag-and-drop operations MMC , implementation details"]
---

# Drag-and-Drop: Implementation Details

The following procedure describes how to implement drag-and-drop functionality in your snap-in. Be aware that only single-selection drag-and-drop operations are discussed in this topic. Multiselection drag-and-drop operations are implemented in essentially the same way as described in this topic. For more information, see [Multiselection](multiselection.md).

**To implement single-selection drag-and-drop operations**

1.  Enable the delete, copy, and paste standard verbs. Be aware that MMC automatically enables the cut verb when the delete and copy verbs are enabled (as long as the snap-in has not explicitly disabled the cut verb). The source scope or result item (henceforth the "source item") enables the delete and copy verbs (and therefore also the cut verb), and the destination scope or result item (henceforth the "destination item") should enable the paste verb. For more information, see [Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md).
2.  Handle the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md), [**MMCN\_PASTE**](mmcn-paste.md), and [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notifications. All notifications are sent to the snap-in [**IComponent::Notify**](icomponent-notify.md) implementation. The following Steps discuss which snap-in (the source or the destination) must handle which notification.
3.  In the destination snap-in, handle the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) and [**MMCN\_PASTE**](mmcn-paste.md) notifications.

    -   MMC sends the [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notification if there is a data object available to paste. The destination snap-in should examine the data object and return **S\_OK** if the object can be pasted or **S\_FALSE** if the object cannot be pasted. If the data object can be pasted, MMC enables the paste verb for the destination item.
    -   The [**MMCN\_PASTE**](mmcn-paste.md) notification is sent when the user attempts to paste the source item in the destination item. After a successful paste, for delete and paste operations, the destination snap-in must specify a data object for the successfully pasted scope or result item in the *param* parameter (sent through **MMCN\_PASTE**). This data object is forwarded to the source snap-in through the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification.

4.  In the source snap-in, handle the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification. MMC sends this notification after a successful paste in a cut/copy operation. The arg parameter passed through the notification contains the data object for the cut source item.

    Be aware that MMC does not delete a source item that has been cut by the user. If the user cuts a result item from a result pane, and the result pane is still visible after the cut, the snap-in should call [**IResultData::DeleteItem**](iresultdata-deleteitem.md) to remove the cut item. For a cut scope item, the snap-in should call the [**IConsoleNameSpace2::DeleteItem**](iconsolenamespace2-deleteitem.md) method to delete the scope item from the scope pane.

## Related topics

<dl> <dt>

[**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md)
</dt> <dt>

[**MMCN\_PASTE**](mmcn-paste.md)
</dt> <dt>

[**MMCN\_CUTORMOVE**](mmcn-cutormove.md)
</dt> <dt>

[Enabling MMC Standard Verbs](enabling-mmc-standard-verbs.md)
</dt> </dl>

 

 




