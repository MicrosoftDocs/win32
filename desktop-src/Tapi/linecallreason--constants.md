---
description: The LINECALLREASON\_ bit-flag constants describe the reason for a call.
ms.assetid: 16278146-886f-433a-afe5-64f4894b1428
title: LINECALLREASON_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLREASON\_ Constants

The **LINECALLREASON\_** bit-flag constants describe the reason for a call.

<dl> <dt>

<span id="LINECALLREASON_CALLCOMPLETION"></span><span id="linecallreason_callcompletion"></span>**LINECALLREASON\_CALLCOMPLETION**
</dt> <dd> <dl> <dt>



The call was the result of a call completion request.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_CAMPEDON"></span><span id="linecallreason_campedon"></span>**LINECALLREASON\_CAMPEDON**
</dt> <dd> <dl> <dt>



The call was camped on the address. Usually, it appears initially in the onhold state, and can be switched to using [**lineSwapHold**](/windows/desktop/api/Tapi/nf-tapi-lineswaphold). If an active call becomes idle, the camped-on call may change to the offering state and the device start ringing.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_DIRECT"></span><span id="linecallreason_direct"></span>**LINECALLREASON\_DIRECT**
</dt> <dd> <dl> <dt>



This is a direct incoming or outgoing call.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_FWDBUSY"></span><span id="linecallreason_fwdbusy"></span>**LINECALLREASON\_FWDBUSY**
</dt> <dd> <dl> <dt>



This call was forwarded from another extension that was busy at the time of the call.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_FWDNOANSWER"></span><span id="linecallreason_fwdnoanswer"></span>**LINECALLREASON\_FWDNOANSWER**
</dt> <dd> <dl> <dt>



The call was forwarded from another extension that didn't answer the call after some number of rings.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_FWDUNCOND"></span><span id="linecallreason_fwduncond"></span>**LINECALLREASON\_FWDUNCOND**
</dt> <dd> <dl> <dt>



The call was forwarded unconditionally from another number.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_INTRUDE"></span><span id="linecallreason_intrude"></span>**LINECALLREASON\_INTRUDE**
</dt> <dd> <dl> <dt>



The call intruded onto the line, either by a call completion action invoked by another station or by operator action. Depending on switch implementation, the call may appear either in the connected state, or conferenced with an existing active call on the line.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_PARKED"></span><span id="linecallreason_parked"></span>**LINECALLREASON\_PARKED**
</dt> <dd> <dl> <dt>



The call was parked on the address. Usually, it appears initially in the onhold state.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_PICKUP"></span><span id="linecallreason_pickup"></span>**LINECALLREASON\_PICKUP**
</dt> <dd> <dl> <dt>



The call was picked up from another extension.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_REDIRECT"></span><span id="linecallreason_redirect"></span>**LINECALLREASON\_REDIRECT**
</dt> <dd> <dl> <dt>



The call was redirected to this station.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_REMINDER"></span><span id="linecallreason_reminder"></span>**LINECALLREASON\_REMINDER**
</dt> <dd> <dl> <dt>



The call is a reminder (or "recall") that the user has a call parked or on hold for (potentially) a long time.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_ROUTEREQUEST"></span><span id="linecallreason_routerequest"></span>**LINECALLREASON\_ROUTEREQUEST**
</dt> <dd> <dl> <dt>



The call appears on the address because the switch needs routing instructions from the application. The application should examine the **CalledID** member in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo), and use the [**lineRedirect**](/windows/desktop/api/Tapi/nf-tapi-lineredirect) function to provide a new dialable address for the call. If the call is to be blocked instead, the application may call [**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop). If the application fails to take action within a switch-defined timeout period, a default action will be taken. A service provider can use this constant only if the negotiated version on the line is 2.0 or higher. Otherwise the service provider should substitute LINECALLREASON\_UNAVAIL.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_TRANSFER"></span><span id="linecallreason_transfer"></span>**LINECALLREASON\_TRANSFER**
</dt> <dd> <dl> <dt>



The call has been transferred from another number.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_UNAVAIL"></span><span id="linecallreason_unavail"></span>**LINECALLREASON\_UNAVAIL**
</dt> <dd> <dl> <dt>



The reason for the call is unavailable and will not become known later.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_UNKNOWN"></span><span id="linecallreason_unknown"></span>**LINECALLREASON\_UNKNOWN**
</dt> <dd> <dl> <dt>



The reason for the call is currently unknown but may become known later.


</dt> </dl> </dd> <dt>

<span id="LINECALLREASON_UNPARK"></span><span id="linecallreason_unpark"></span>**LINECALLREASON\_UNPARK**
</dt> <dd> <dl> <dt>



The call was retrieved as a parked call.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

The LINECALLREASON\_ constants are used in the **dwReason** member of the [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) data structure.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo)
</dt> <dt>

[**lineDrop**](/windows/desktop/api/Tapi/nf-tapi-linedrop)
</dt> <dt>

[**lineRedirect**](/windows/desktop/api/Tapi/nf-tapi-lineredirect)
</dt> <dt>

[**lineSwapHold**](/windows/desktop/api/Tapi/nf-tapi-lineswaphold)
</dt> </dl>

 

 




