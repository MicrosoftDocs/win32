---
title: DRV_FREE message (Mmsystem.h)
description: Notifies the driver that it is being removed from memory. The driver should free any memory and other system resources that it has allocated.
ms.assetid: 0447f8e9-4c4d-4be5-ab1f-ecd3e8cd2e67
keywords:
- DRV_FREE message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_FREE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_FREE message

Notifies the driver that it is being removed from memory. The driver should free any memory and other system resources that it has allocated.

## Parameters

<dl> <dt>

<span id="hdrvr"></span><span id="HDRVR"></span>*hdrvr*
</dt> <dd>

Handle of the installable driver instance.

</dd> </dl>

## Return Value

No return value.

## Remarks

The *dwDriverId*, *lParam1*, and *lParam2* parameters are not used.

The **DRV\_FREE** message is always the last message that a device driver receives.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[Installable Drivers](installable-drivers.md)
</dt> <dt>

[Installable Driver Messages](installable-driver-messages.md)
</dt> </dl>

 

 





