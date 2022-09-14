---
description: The LINEAGENTSTATE\_ constants describe the state of an agent on an address.
ms.assetid: 1dbc33e7-05cc-4cb9-8904-f495b884b8db
title: LINEAGENTSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEAGENTSTATE\_ Constants

The **LINEAGENTSTATE\_ constants** describe the state of an agent on an address.

<dl> <dt>

<span id="LINEAGENTSTATE_BUSYACD"></span><span id="lineagentstate_busyacd"></span>**LINEAGENTSTATE\_BUSYACD**
</dt> <dd> <dl> <dt>



The agent is busy handling a call routed from an ACD queue.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_BUSYINCOMING"></span><span id="lineagentstate_busyincoming"></span>**LINEAGENTSTATE\_BUSYINCOMING**
</dt> <dd> <dl> <dt>



The agent is busy handling an incoming call that was not transferred to the agent from an ACD queue in which the agent is logged in.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_BUSYOTHER"></span><span id="lineagentstate_busyother"></span>**LINEAGENTSTATE\_BUSYOTHER**
</dt> <dd> <dl> <dt>



The agent is busy handling another type of call, such as an outgoing personal call not transferred to the agent by a predictive dialer. This value can also be used when the agent is known to be busy on a call but the type of call is unknown.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_BUSYOUTBOUND"></span><span id="lineagentstate_busyoutbound"></span>**LINEAGENTSTATE\_BUSYOUTBOUND**
</dt> <dd> <dl> <dt>



The agent is busy handling an outgoing call, such as one routed from a predictive dialing queue.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_LOGGEDOFF"></span><span id="lineagentstate_loggedoff"></span>**LINEAGENTSTATE\_LOGGEDOFF**
</dt> <dd> <dl> <dt>



No agent is logged in on the address.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_NOTREADY"></span><span id="lineagentstate_notready"></span>**LINEAGENTSTATE\_NOTREADY**
</dt> <dd> <dl> <dt>



The agent is logged in, but occupied with a task other than serving a call (such as on a break). No additional calls should be routed to the agent.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_READY"></span><span id="lineagentstate_ready"></span>**LINEAGENTSTATE\_READY**
</dt> <dd> <dl> <dt>



The agent is ready to accept calls.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_UNAVAIL"></span><span id="lineagentstate_unavail"></span>**LINEAGENTSTATE\_UNAVAIL**
</dt> <dd> <dl> <dt>



The agent state is unknown and will never become known. In [**LINEADDRESSSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineaddressstatus), this condition can also be represented by the **dwAgentState** member being set to 0.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_UNKNOWN"></span><span id="lineagentstate_unknown"></span>**LINEAGENTSTATE\_UNKNOWN**
</dt> <dd> <dl> <dt>



The agent state is currently unknown, but may become known later. This can be a transitional state when a line or address is first opened.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATE_WORKINGAFTERCALL"></span><span id="lineagentstate_workingaftercall"></span>**LINEAGENTSTATE\_WORKINGAFTERCALL**
</dt> <dd> <dl> <dt>



The agent has completed the preceding call, but is still occupied with work related to that call. The agent should not receive additional calls.


</dt> </dl> </dd> </dl>

## Remarks

The upper 16 bits of this set of constants are reserved for device-specific extensions.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




