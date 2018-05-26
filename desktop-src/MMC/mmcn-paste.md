---
title: MMCN\_PASTE message
description: The MMCN\_PASTE notification message is sent to a snap-ins IComponent implementation to tell the snap-ins scope item to paste the selected result items.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2eedeb8-663a-43eb-9b8b-ab419a8b3f79
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_PASTE message MMC
topic_type:
- apiref
api_name:
- MMCN_PASTE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_PASTE message

The **MMCN\_PASTE** notification message is sent to a snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to tell the snap-in's scope item to paste the selected result items.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

The data object of the destination scope item in which to paste the selected items provided by the snap-in.

</dd> <dt>

*arg* 
</dt> <dd>

The data object of the selected item(s) provided by the source snap-in that must be pasted.

</dd> <dt>

*param* 
</dt> <dd>

**NULL** for copy (as opposed to cut).

LPDATAOBJECT\* *ppDataObj* = (LPDATAOBJECT\*)*param*.

Use this to return a pointer to a data object consisting of the items successfully pasted. This data object is in turn forwarded to the source snap-in through the [**MMCN\_CUTORMOVE**](mmcn-cutormove.md) notification.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in successfully handled the notification.

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not handle the notification. MMC then performs a default operation for the notification.

</dd> </dl>

## Remarks

When the items to be pasted were cut or moved from the source, the snap-in has the responsibility to return a data object that identifies those items that were successfully pasted. This is so the source snap-in can know which items it can delete. If all items are successfully pasted the snap-in can simply increment the reference count on the input data object (by calling its **AddRef** method) and then return it.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**MMCN\_CUTORMOVE**](mmcn-cutormove.md)
</dt> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> <dt>

[Multiselection](multiselection.md)
</dt> </dl>

 

 





