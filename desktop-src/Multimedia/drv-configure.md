---
title: DRV_CONFIGURE message (Mmsystem.h)
description: Directs the installable driver to display its configuration dialog box and let the user specify new settings for the given installable driver instance.
ms.assetid: 0d99fad7-ce79-4574-9fd8-262f7e758866
keywords:
- DRV_CONFIGURE message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_CONFIGURE
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_CONFIGURE message

Directs the installable driver to display its configuration dialog box and let the user specify new settings for the given installable driver instance.

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

Handle of the parent window. This window is used as the parent window for the configuration dialog box.

</dd> <dt>

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Address of a [**DRVCONFIGINFO**](/windows/win32/api/mmiscapi/ns-mmiscapi-drvconfiginfo) structure or **NULL**. If the structure is given, it contains the names of the registry key and value associated with the driver.

</dd> </dl>

## Return Value

Returns one of these values:



| Requirement | Value |
|-----------------|----------------------------------------------------------------------------------------------------|
| DRVCNF\_OK      | The configuration is successful; no further action is required.                                    |
| DRVCNF\_CANCEL  | The user canceled the dialog box; no further action is required.                                   |
| DRVCNF\_RESTART | The configuration is successful, but the changes do not take effect until the system is restarted. |



 

## Remarks

Some installable drivers append configuration information to the value assigned to the registry value associated with the driver.

The DRV\_CANCEL, DRV\_OK, and DRV\_RESTART return values are obsolete; they have been replaced by DRVCNF\_CANCEL, DRVCNF\_OK, and DRVCNF\_RESTART, respectively.

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

 

