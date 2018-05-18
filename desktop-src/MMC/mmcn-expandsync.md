---
title: MMCN\_EXPANDSYNC message
description: Sent to the snap-in's IComponentData implementation when MMC requires a scope item to be expanded synchronously.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '28fbedbf-e7d6-423a-909f-020ff8416cb8'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_EXPANDSYNC message MMC"]
topic_type:
- apiref
api_name:
- MMCN_EXPANDSYNC
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_EXPANDSYNC message

The **MMCN\_EXPANDSYNC** notification is introduced in MMC 1.1.

The **MMCN\_EXPANDSYNC** notification message is sent to the snap-in's [**IComponentData**](icomponentdata.md) implementation when MMC requires a scope item to be expanded synchronously.

At certain times (for example, when a console file is reloaded with a scope item expanded), MMC requires a scope item to be synchronously expanded and sends the snap-in the **MMCN\_EXPANDSYNC** notification. Usually, MMC sends the [**MMCN\_EXPAND**](mmcn-expand.md) notification when a item is expanded or collapsed.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the scope item that must be expanded or collapsed.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

</dd> <dt>

*param* \[in\]
</dt> <dd>

A pointer to an [**MMC\_EXPANDSYNC\_STRUCT**](mmc-expandsync-struct.md) structure.

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

If the snap-in normally responds to [**MMCN\_EXPAND**](mmcn-expand.md) by expanding the scope item specified by *lpDataObject* asynchronously (that is, by spawning a thread to handle the expansion), the snap-in must also handle this notification. When the snap-in receives **MMCN\_EXPANDSYNC**, it must expand the scope item before returning and set the **bHandled** member of [**MMC\_EXPANDSYNC\_STRUCT**](mmc-expandsync-struct.md) to **TRUE**.

If the snap-in always synchronously expands the scope item specified by *lpDataObject*, the snap-in can ignore this notification for this item and instead handle the [**MMCN\_EXPAND**](mmcn-expand.md) notification. The default value for **bHandled** is **FALSE**. If the snap-in does not handle **MMCN\_EXPANDSYNC** or returns with **bHandled** = **FALSE**, MMC will send an **MMCN\_EXPAND** notification to the snap-in.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponentData::Notify**](icomponentdata-notify.md)
</dt> <dt>

[**IConsoleNameSpace2**](iconsolenamespace2.md)
</dt> <dt>

[**MMCN\_EXPAND**](mmcn-expand.md)
</dt> </dl>

 

 





