---
title: MMCN\_PROPERTY\_CHANGE message
description: The MMCN\_PROPERTY\_CHANGE notification message is sent to the snap-in's IComponentData or IComponent implementation, whichever created the property pages, when the snap-in uses the MMCPropertyChangeNotify function to notify its views of changes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4b1c6d78-23b1-4b5a-b913-8a7153471785
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_PROPERTY_CHANGE message MMC
topic_type:
- apiref
api_name:
- MMCN_PROPERTY_CHANGE
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_PROPERTY\_CHANGE message

The **MMCN\_PROPERTY\_CHANGE** notification message is sent to the snap-in's [**IComponentData**](/windows/desktop/api/Mmc/nn-mmc-icomponentdata) or [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation, whichever created the property pages, when the snap-in uses the [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify) function to notify its views of changes.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

This value is **NULL** because a data object is not required.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

**TRUE** if the property change is for a scope item.

</dd> <dt>

*param* 
</dt> <dd>

This is the parameter passed to [**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify).

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
</dt> <dt>

[**IComponentData::Notify**](/windows/desktop/api/Mmc/nf-mmc-icomponentdata-notify)
</dt> <dt>

[**MMCPropertyChangeNotify**](/windows/desktop/api/Mmc/nf-mmc-mmcpropertychangenotify)
</dt> </dl>

 

 





