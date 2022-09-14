---
title: DRV_LOAD message (Mmsystem.h)
description: Notifies the driver that it has been loaded. The driver should make sure that any hardware and supporting drivers it needs to function properly are present.
ms.assetid: f3642d91-cea8-499d-8d2e-bf01a59a7d72
keywords:
- DRV_LOAD message Windows Multimedia
topic_type:
- apiref
api_name:
- DRV_LOAD
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# DRV\_LOAD message

Notifies the driver that it has been loaded. The driver should make sure that any hardware and supporting drivers it needs to function properly are present.

## Parameters

The *hdrvr* parameter is always zero. The *dwDriverId*, *lParam1*, and *lParam2* parameters are not used.

## Return Value

Returns nonzero if successful or zero otherwise.

## Remarks

The **DRV\_LOAD** message is always the first message that a device driver receives.

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

 

 





