---
description: The LINETERMDEV\_ bit-flag constants describe different types of terminal devices.
ms.assetid: 3444d022-8225-4956-89a1-721b4662d557
title: LINETERMDEV_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINETERMDEV\_ Constants

The **LINETERMDEV\_** bit-flag constants describe different types of terminal devices.

<dl> <dt>

<span id="LINETERMDEV_HEADSET"></span><span id="linetermdev_headset"></span>**LINETERMDEV\_HEADSET**
</dt> <dd> <dl> <dt>



The terminal is a headset.


</dt> </dl> </dd> <dt>

<span id="LINETERMDEV_PHONE"></span><span id="linetermdev_phone"></span>**LINETERMDEV\_PHONE**
</dt> <dd> <dl> <dt>



The terminal is a phone set.


</dt> </dl> </dd> <dt>

<span id="LINETERMDEV_SPEAKER"></span><span id="linetermdev_speaker"></span>**LINETERMDEV\_SPEAKER**
</dt> <dd> <dl> <dt>



The terminal is an external speaker and microphone.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

These constants are used to characterize a line's terminal device and help an application to determine the nature of a terminal device.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




