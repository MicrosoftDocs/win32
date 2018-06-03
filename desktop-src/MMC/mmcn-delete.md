---
title: MMCN\_DELETE message
description: The MMCN\_DELETE notification message is sent to the snap-in's IComponent and IComponentData implementations to inform the snap-in that the object should be deleted.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eaf6c7de-2b02-4563-9392-588a74c9d744
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_DELETE message MMC
topic_type:
- apiref
api_name:
- MMCN_DELETE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_DELETE message

The **MMCN\_DELETE** notification message is sent to the snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) and [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) implementations to inform the snap-in that the object should be deleted.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope or result item, provided by the snap-in.

</dd> <dt>

*arg* 
</dt> <dd>

Not used.

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

This message is generated when the user presses the delete key or uses the mouse to click the toolbar's delete button.

The snap-in should delete the items specified in the data object.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponent-notify)
</dt> <dt>

[**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)
</dt> </dl>

 

 





