---
title: DRV_CLOSE message (Mmsystem.h)
description: Directs the driver to close the given instance. If no other instances are open, the driver should prepare for subsequent release from memory.
ms.assetid: 98d7fe47-5194-4912-a9d6-3af3d1fa4e60
keywords:
- DRV_CLOSE message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_CLOSE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_CLOSE message

Directs the driver to close the given instance. If no other instances are open, the driver should prepare for subsequent release from memory.

## Parameters

<dl> <dt>

<span id="dwDriverId"></span><span id="dwdriverid"></span><span id="DWDRIVERID"></span>*dwDriverId*
</dt> <dd>

Identifier of the installable driver. This is the same value previously returned by the driver from the [**DRV\_OPEN**](drv-open.md) message.

</dd> <dt>

<span id="hdrvr"></span><span id="HDRVR"></span>*hdrvr*
</dt> <dd>

Handle of the installable driver instance.

</dd> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

32-bit value specified as the *lParam1* parameter in a call to the **DriverClose** function.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

32-bit value specified as the *lParam2* parameter in a call to the **DriverClose** function.

</dd> </dl>

## Return Value

Returns nonzero if successful or zero otherwise.

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

 

 





