---
title: MMCN\_PRINT message
description: Sent to the snap-in's IComponent implementation when the user clicks the Print button or selects the Print menu item.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '74814817-f93b-476f-a477-e6b65ed229bb'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_PRINT message MMC"]
topic_type:
- apiref
api_name:
- MMCN_PRINT
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_PRINT message

The **MMCN\_PRINT** notification is introduced in MMC 1.1.

The **MMCN\_PRINT** notification message is sent to the snap-in's [**IComponent**](icomponent.md) implementation when the user clicks the **Print** button or selects the **Print** menu item. The snap-in must print the appropriate item or data.

## Parameters

<dl> <dt>

*lpDataObject* \[in\]
</dt> <dd>

A pointer to the data object of the currently selected scope or result item.

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
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





