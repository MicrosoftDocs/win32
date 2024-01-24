---
description: The LINEANSWERMODE\_ bit-flag constants describe how an existing active call on a line device is affected by answering another offering call on the same line.
ms.assetid: 35f63d92-970f-4fb8-aba9-179fc7de70f4
title: LINEANSWERMODE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEANSWERMODE\_ Constants

The **LINEANSWERMODE\_** bit-flag constants describe how an existing active call on a line device is affected by answering another *offering* call on the same line.

<dl> <dt>

<span id="LINEANSWERMODE_DROP"></span><span id="lineanswermode_drop"></span>**LINEANSWERMODE\_DROP**
</dt> <dd> <dl> <dt>



The currently active call will automatically be dropped.


</dt> </dl> </dd> <dt>

<span id="LINEANSWERMODE_HOLD"></span><span id="lineanswermode_hold"></span>**LINEANSWERMODE\_HOLD**
</dt> <dd> <dl> <dt>



The currently active call will automatically be placed on hold.


</dt> </dl> </dd> <dt>

<span id="LINEANSWERMODE_NONE"></span><span id="lineanswermode_none"></span>**LINEANSWERMODE\_NONE**
</dt> <dd> <dl> <dt>



Answering another call on the same line has no effect on the existing active call on the line.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

If a call comes in (is offered) at the time another call is already active, the new call is connected to by invoking [**lineAnswer**](/windows/desktop/api/Tapi/nf-tapi-lineanswer). The effect this has on the existing active call depends on the line's device capabilities. The first call may be unaffected, it may automatically be dropped, or it may automatically be placed on hold.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




