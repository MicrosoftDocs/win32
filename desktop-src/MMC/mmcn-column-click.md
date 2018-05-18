---
title: MMCN\_COLUMN\_CLICK message
description: The MMCN\_COLUMN\_CLICK notification message is sent to the snap-in's IComponent implementation when the user clicks a list view column header.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '92e98c31-032c-48ca-ba1c-a4062b208d6d'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCN_COLUMN_CLICK message MMC"]
topic_type:
- apiref
api_name:
- MMCN_COLUMN_CLICK
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# MMCN\_COLUMN\_CLICK message

The **MMCN\_COLUMN\_CLICK** notification message is sent to the snap-in's [**IComponent**](icomponent.md) implementation when the user clicks a list view column header.

## Parameters

<dl> <dt>

*lpDataObject* 
</dt> <dd>

NULL.

</dd> <dt>

*arg* 
</dt> <dd>

Column number.

</dd> <dt>

*param* 
</dt> <dd>

Sort options:

<dt>

<span id="RSI_DESCENDING___0x0001"></span><span id="rsi_descending___0x0001"></span><span id="RSI_DESCENDING___0X0001"></span>

<span id="RSI_DESCENDING___0x0001"></span><span id="rsi_descending___0x0001"></span><span id="RSI_DESCENDING___0X0001"></span>**RSI\_DESCENDING = 0x0001**


</dt> <dd>

The sort should be in descending order. The default is to sort in ascending order.

</dd> </dl> </dd> </dl>

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

The snap-in should not perform a sort in response to this notification. MMC will initiate a sort after the notification is processed.

**MMCN\_COLUMN\_CLICK** does not receive the RSI\_NOSORTICON sort option.

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



 

 





