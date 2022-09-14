---
title: DRV_OPEN message (Mmsystem.h)
description: Directs the driver to open an new instance.
ms.assetid: 6b5e21e3-dc29-4f0f-84cb-bd2d2e3c54e9
keywords:
- DRV_OPEN message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_OPEN
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_OPEN message

Directs the driver to open an new instance.

## Parameters

<dl> <dt>

<span id="dwDriverId"></span><span id="dwdriverid"></span><span id="DWDRIVERID"></span>*dwDriverId*
</dt> <dd>

Identifier of the installable driver.

</dd> <dt>

<span id="hdrvr"></span><span id="HDRVR"></span>*hdrvr*
</dt> <dd>

Handle of the installable driver instance.

</dd> <dt>

<span id="lParam1"></span><span id="lparam1"></span><span id="LPARAM1"></span>*lParam1*
</dt> <dd>

Address of a null-terminated, wide-character string that specifies configuration information used to open the instance. If no configuration information is available, either this string is empty or the parameter is **NULL**.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

32-bit driver-specific data.

</dd> </dl>

## Return Value

Returns a nonzero value if successful or zero otherwise.

## Remarks

If the driver returns a nonzero value, the system uses that value as the driver identifier (the *dwDriverId* parameter) in messages it subsequently sends to the driver instance. The driver can return any type of value as the identifier. For example, some drivers return memory addresses that point to instance-specific information. Using this method of specifying identifiers for a driver instance gives the drivers ready access to the information while they are processing messages.

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

 

 





