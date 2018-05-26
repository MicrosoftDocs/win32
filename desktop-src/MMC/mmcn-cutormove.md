---
title: MMCN\_CUTORMOVE message
description: The MMCN\_CUTORMOVE notification message is sent to the snap-ins IComponent after items owned by the snap-in have been cut or moved.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 563d83d1-137b-4fd4-a202-63d51f84dfa8
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_CUTORMOVE message MMC
topic_type:
- apiref
api_name:
- MMCN_CUTORMOVE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_CUTORMOVE message

The **MMCN\_CUTORMOVE** notification message is sent to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) after items owned by the snap-in have been cut or moved.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

NULL.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

A pointer to a data object for the cut or moved items.

</dd> <dt>

*param* 
</dt> <dd>

Not used.

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

When moving items from a source to a destination, a data object that lists the items to be moved is passed from the source to the destination. The destination should copy the items and then return a data object that lists the successfully copied items. That data object is then passed to the source, along with the **MMCN\_CUTORMOVE** notification. The source should then delete the items that were successfully copied.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[Drag and Drop](drag-and-drop.md)
</dt> <dt>

[Multiselection](multiselection.md)
</dt> </dl>

 

 





