---
title: MMCN\_SNAPINHELP message
description: Sent to the snap-in's IComponent implementation when the user requests help about the snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d2f8870-7f06-48f3-aa76-09e99d2c6858
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCN_SNAPINHELP message MMC
topic_type:
- apiref
api_name:
- MMCN_SNAPINHELP
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMCN\_SNAPINHELP message

The **MMCN\_SNAPINHELP** notification message is sent to the snap-in's [**IComponent**](/windows/desktop/api/Mmc/nn-mmc-icomponent) implementation when the user requests help about the snap-in.

**MMCN\_SNAPINHELP** is only sent to snap-ins that do not support HTML Help by implementing the [**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2) interface.

Be aware that snap-ins that provide Help should implement [**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2).

If a snap-in does not support HTML Help ([**ISnapinHelp2**](/windows/desktop/api/Mmc/nn-mmc-isnapinhelp2)), when that snap-in's scope or result item is selected, MMC places a special menu item for it under the console's **Help** menu. The item is named "Help on &lt;snap-in name&gt;". If the user clicks this menu item, MMC sends the **MMCN\_SNAPINHELP** notification to the snap-in. The snap-in should respond by that displays whatever Help information it has.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

NULL.

</dd> <dt>

*arg* 
</dt> <dd>

Zero.

</dd> <dt>

*param* 
</dt> <dd>

Zero.

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



 

 





