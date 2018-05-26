---
title: MMCN\_PRELOAD message
description: The MMCN\_PRELOAD notification is introduced in MMC 1.1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a648e5f5-e3da-45d7-8e8f-a3f67699ccdc
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_PRELOAD message MMC
topic_type:
- apiref
api_name:
- MMCN_PRELOAD
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_PRELOAD message

The **MMCN\_PRELOAD** notification is introduced in MMC 1.1.

The **MMCN\_PRELOAD** notification message is sent to the snap-in's [**IComponentData**](/windows/win32/Mmc/nn-mmc-icomponentdata?branch=master) implementation if the snap-in returned **TRUE** when MMC called [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) with the [**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md) format.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the static node of the snap-in being preloaded.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

HSCOPEITEM of the static node of the snap-in being preloaded.

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

When a console file is saved, MMC calls [**IDataObject::GetDataHere**](_ole_idataobject_getdatahere) on each loaded snap-in using the CCF\_SNAPIN\_PRELOADS clipboard format. If the snap-in handles the [**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md) clipboard format and returns **TRUE**, MMC calls the [**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master) method of the snap-in with the **MMCN\_PRELOAD** notification when the snap-in's parent is first selected. If a preload is not requested, MMC does not load a snap-in until the snap-in's static node is selected. Until then MMC displays a cached icon and name for the snap-in's static node.

The preloaded snap-in can handle this notification by performing any actions required before it displays its static node or its child items (for example, a dynamic name for an item based on context such as a file name or computer name).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponentData::Notify**](/windows/win32/Mmc/nf-mmc-icomponentdata-notify?branch=master)
</dt> <dt>

[**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md)
</dt> </dl>

 

 





