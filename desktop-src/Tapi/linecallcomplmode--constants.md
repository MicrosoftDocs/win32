---
description: The LINECALLCOMPLMODE\_ bit-flag constants describe different ways in which a call can be completed.
ms.assetid: 68f755a1-586b-4c5b-b8e8-c8b40eb71685
title: LINECALLCOMPLMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLCOMPLMODE\_ Constants

The **LINECALLCOMPLMODE\_** bit-flag constants describe different ways in which a call can be completed.

<dl> <dt>

<span id="LINECALLCOMPLMODE_CALLBACK"></span><span id="linecallcomplmode_callback"></span>**LINECALLCOMPLMODE\_CALLBACK**
</dt> <dd> <dl> <dt>



Requests the called station to return the call when it returns to idle.


</dt> </dl> </dd> <dt>

<span id="LINECALLCOMPLMODE_CAMPON"></span><span id="linecallcomplmode_campon"></span>**LINECALLCOMPLMODE\_CAMPON**
</dt> <dd> <dl> <dt>



Queues the call until the call can be completed.


</dt> </dl> </dd> <dt>

<span id="LINECALLCOMPLMODE_INTRUDE"></span><span id="linecallcomplmode_intrude"></span>**LINECALLCOMPLMODE\_INTRUDE**
</dt> <dd> <dl> <dt>



Adds the application to the existing call at the called station (barge in).


</dt> </dl> </dd> <dt>

<span id="LINECALLCOMPLMODE_MESSAGE"></span><span id="linecallcomplmode_message"></span>**LINECALLCOMPLMODE\_MESSAGE**
</dt> <dd> <dl> <dt>



Leaves a short predefined message for the called station (Leave Word Calling). The message to be sent is specified separately.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




