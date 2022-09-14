---
title: DRV_DISABLE message (Mmsystem.h)
description: Disables the driver. The driver should place the corresponding device, if any, in an inactive state and terminate any callback functions or threads.
ms.assetid: 83e99397-6f0e-4174-9f96-e10c1f17ef0b
keywords:
- DRV_DISABLE message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_DISABLE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_DISABLE message

Disables the driver. The driver should place the corresponding device, if any, in an inactive state and terminate any callback functions or threads.

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

After disabling the driver, the system typically sends the driver a [**DRV\_FREE**](drv-free.md) message before removing the driver from memory.

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

 

 





