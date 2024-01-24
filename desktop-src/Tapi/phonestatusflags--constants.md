---
description: The PHONESTATUSFLAGS\_ bit-flag constants describe a variety of phone device status information.
ms.assetid: e94da591-49ab-4932-8621-0a62b8a55dd6
title: PHONESTATUSFLAGS_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# PHONESTATUSFLAGS\_ Constants

The **PHONESTATUSFLAGS\_** bit-flag constants describe a variety of phone device status information.

<dl> <dt>

<span id="PHONESTATUSFLAGS_CONNECTED"></span><span id="phonestatusflags_connected"></span>**PHONESTATUSFLAGS\_CONNECTED**
</dt> <dd> <dl> <dt>



Specifies whether the phone is currently connected to TAPI. **TRUE** if connected, **FALSE** otherwise.


</dt> </dl> </dd> <dt>

<span id="PHONESTATUSFLAGS_SUSPENDED"></span><span id="phonestatusflags_suspended"></span>**PHONESTATUSFLAGS\_SUSPENDED**
</dt> <dd> <dl> <dt>



Specifies whether TAPI's manipulation of the phone device is suspended. **TRUE** if suspended, **FALSE** otherwise. An application's use of a phone device can be temporarily suspended when the switch wants to manipulate the phone in a way that cannot tolerate interference from the application.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




