---
title: DRV_INSTALL message (Mmsystem.h)
description: Notifies the driver that is it being installed. The driver should create and initialize any needed registry keys and values and verify that the supporting drivers and hardware are installed and properly configured.
ms.assetid: 8ee7b30b-600b-49f3-93a7-8faa7b87cfd8
keywords:
- DRV_INSTALL message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_INSTALL
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_INSTALL message

Notifies the driver that is it being installed. The driver should create and initialize any needed registry keys and values and verify that the supporting drivers and hardware are installed and properly configured.

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

<span id="lParam2"></span><span id="lparam2"></span><span id="LPARAM2"></span>*lParam2*
</dt> <dd>

Address of a [**DRVCONFIGINFO**](/windows/win32/api/mmiscapi/ns-mmiscapi-drvconfiginfo) structure or **NULL**. If a structure is given, it contains the names of the registry key and value associated with the driver.

</dd> </dl>

## Return Value

Returns one of these values:



| Requirement | Value |
|-----------------|--------------------------------------------------------------------------------------------|
| DRVCNF\_OK      | The installation is successful; no further action is required.                             |
| DRVCNF\_CANCEL  | The installation failed..                                                                  |
| DRVCNF\_RESTART | The installation is successful, but it does not take effect until the system is restarted. |



 

## Remarks

The *lParam1* parameter is not used.

Some installable drivers append configuration information to the value assigned to the registry value associated with the driver.

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

 

