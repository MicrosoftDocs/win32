---
title: MMCN\_ACTIVATE message
description: The MMCN\_ACTIVATE notification message is sent to the snap-in's IComponent Notify method when a window for which the snap-in owns the result view is being activated or deactivated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51aa4709-6e33-41eb-958a-108fec6865b4
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_ACTIVATE message MMC
topic_type:
- apiref
api_name:
- MMCN_ACTIVATE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_ACTIVATE message

The **MMCN\_ACTIVATE** notification message is sent to the snap-in's [**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify) method when a window for which the snap-in owns the result view is being activated or deactivated.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* 
</dt> <dd>

**TRUE** if the window is activated; otherwise **FALSE**.

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

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify)
</dt> </dl>

 

 





