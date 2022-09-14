---
description: The LINEBUSYMODE\_ bit-flag constants describe different busy signals that the switch or network can generate. These busy signals typically indicate that a different resource that is required to make a call is currently in use.
ms.assetid: 4a3fa79f-7a7a-4f9b-9353-e6c5ca4fcb4e
title: LINEBUSYMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEBUSYMODE\_ Constants

The **LINEBUSYMODE\_** bit-flag constants describe different busy signals that the switch or network can generate. These busy signals typically indicate that a different resource that is required to make a call is currently in use.

<dl> <dt>

<span id="LINEBUSYMODE_STATION"></span><span id="linebusymode_station"></span>**LINEBUSYMODE\_STATION**
</dt> <dd> <dl> <dt>



The busy signal indicates that the called party's station is busy. This is usually signaled with a *normal* busy tone.


</dt> </dl> </dd> <dt>

<span id="LINEBUSYMODE_TRUNK"></span><span id="linebusymode_trunk"></span>**LINEBUSYMODE\_TRUNK**
</dt> <dd> <dl> <dt>



The busy signal indicates that a trunk or circuit is busy. This is usually signaled with a *fast* busy tone.


</dt> </dl> </dd> <dt>

<span id="LINEBUSYMODE_UNKNOWN"></span><span id="linebusymode_unknown"></span>**LINEBUSYMODE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The busy signal's specific mode is currently unknown but may become known later.


</dt> </dl> </dd> <dt>

<span id="LINEBUSYMODE_UNAVAIL"></span><span id="linebusymode_unavail"></span>**LINEBUSYMODE\_UNAVAIL**
</dt> <dd> <dl> <dt>



The busy signal's specific mode is unavailable and will not become known.


</dt> </dl> </dd> </dl>

## Remarks

The high-order 16 bits can be assigned for device-specific extensions. The low-order 16 bits are reserved.

> [!Note]  
> Busy signals can be sent as inband tones or out-of-band messages. TAPI makes no assumption about the specific signaling mechanism.

 

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




