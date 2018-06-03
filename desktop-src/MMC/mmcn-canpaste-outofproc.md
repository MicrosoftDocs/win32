---
title: MMCN\_CANPASTE\_OUTOFPROC message
description: The MMCN\_CANPASTE\_OUTOFPROC notification message is sent to the snap-in so that MMC can determine whether the snap-in supports paste operations from another MMC process. This notification message is introduced in MMC 2.0.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9759e321-b3f4-42a8-a3dd-446cb6bc6b27
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_CANPASTE_OUTOFPROC message MMC
topic_type:
- apiref
api_name:
- MMCN_CANPASTE_OUTOFPROC
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_CANPASTE\_OUTOFPROC message

The **MMCN\_CANPASTE\_OUTOFPROC** notification message is sent to the snap-in so that MMC can determine whether the snap-in supports paste operations from another MMC process. This notification message is introduced in MMC 2.0.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

Not used.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

</dd> <dt>

*param* 
</dt> <dd>

A pointer to a BOOL type; the snap-in sets \**param* to **TRUE** if it handles data objects from other MMC processes.

</dd> </dl>

## Return value

<dl> <dt>

**S\_OK**
</dt> <dd>

The snap-in accepts data objects from other MMC processes (note the snap-in must also set \**param* to **TRUE**).

</dd> <dt>

**S\_FALSE**
</dt> <dd>

The snap-in does not accept data objects from other MMC processes.

</dd> </dl>

## Remarks

If the snap-in indicates that it can accept data objects from other MMC processes, it will receive [**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md) notifications that correspond to those data objects (provided the user attempts to paste from another MMC process).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**MMCN\_QUERY\_PASTE**](mmcn-query-paste.md)
</dt> <dt>

[Inter-process Drag and Drop](inter-process-drag-and-drop.md)
</dt> </dl>

 

 





