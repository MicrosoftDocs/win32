---
title: MMCN\_ADD\_IMAGES message
description: Sent to the snap-ins IComponent implementation to add images for the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26f4b8da-f490-4b8d-8016-1aa50dd21f62
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_ADD_IMAGES message MMC
topic_type:
- apiref
api_name:
- MMCN_ADD_IMAGES
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MMCN\_ADD\_IMAGES message

The **MMCN\_ADD\_IMAGES** notification message is sent to the snap-in's [**IComponent**](/windows/win32/Mmc/ns-wmidata-_msmcaevent_pcicomponenterror?branch=master) implementation to add images for the result pane. MMC provides a pointer to the [**IImageList**](iimagelist.md) interface when this notification message is sent to the snap-in.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope item.

</dd> <dt>

*arg* 
</dt> <dd>

A pointer to the result pane image list ([**IImageList**](iimagelist.md)). This pointer is valid only while the specific **MMCN\_ADD\_IMAGES** notification is being processed and should not be stored for later use. Additionally, the snap-in must not call the Release method of IImageList because MMC must release it.

</dd> <dt>

*param* 
</dt> <dd>

A value that specifies the HSCOPEITEM of the currently selected scope item. The snap-in can use this parameter to add images that apply specifically to the result items of this scope item, or the snap-in can ignore this parameter and add all possible images.

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

The primary snap-in should add images for both folders and leaf items. Extension snap-ins should add only folder images. A snap-in must load and destroy its image bitmap each time it responds to a **MMCN\_ADD\_IMAGES** notification; failure to do so can result in undesirable results if the user changes display settings.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[**IComponent::Notify**](icomponent-notify.md)
</dt> <dt>

[**IComponentData::Notify**](icomponentdata-notify.md)
</dt> <dt>

[**IExtendControlbar::ControlbarNotify**](iextendcontrolbar-controlbarnotify.md)
</dt> <dt>

[**IImageList**](iimagelist.md)
</dt> </dl>

 

 





