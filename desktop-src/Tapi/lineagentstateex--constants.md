---
description: The LINEAGENTSTATEEX\_ constants describe the state of an agent on an address.
ms.assetid: d49025c5-f1db-4b71-a2d5-1cf3df66f3e5
title: LINEAGENTSTATEEX_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEAGENTSTATEEX\_ Constants

The **LINEAGENTSTATEEX\_ constants** describe the state of an agent on an address.

<dl> <dt>

<span id="LINEAGENTSTATEEX_BUSYACD"></span><span id="lineagentstateex_busyacd"></span>**LINEAGENTSTATEEX\_BUSYACD**
</dt> <dd> <dl> <dt>



The agent is busy handling a call routed from an ACD queue.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_BUSYINCOMING"></span><span id="lineagentstateex_busyincoming"></span>**LINEAGENTSTATEEX\_BUSYINCOMING**
</dt> <dd> <dl> <dt>



The agent is busy handling an incoming call that was not transferred to the agent from an ACD queue in which the agent is logged in.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_BUSYOUTGOING"></span><span id="lineagentstateex_busyoutgoing"></span>**LINEAGENTSTATEEX\_BUSYOUTGOING**
</dt> <dd> <dl> <dt>



The agent is busy handling an outgoing call, such as one routed from a predictive dialing queue.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_NOTREADY"></span><span id="lineagentstateex_notready"></span>**LINEAGENTSTATEEX\_NOTREADY**
</dt> <dd> <dl> <dt>



The agent is logged in, but occupied with a task other than serving a call (such as on a break). No additional calls should be routed to the agent.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_READY"></span><span id="lineagentstateex_ready"></span>**LINEAGENTSTATEEX\_READY**
</dt> <dd> <dl> <dt>



The agent is ready to accept calls.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_RELEASED"></span><span id="lineagentstateex_released"></span>**LINEAGENTSTATEEX\_RELEASED**
</dt> <dd> <dl> <dt>



The agent has been released, probably because they logged off.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSTATEEX_UNKNOWN"></span><span id="lineagentstateex_unknown"></span>**LINEAGENTSTATEEX\_UNKNOWN**
</dt> <dd> <dl> <dt>



The agent state is currently unknown, but may become known later. This can be a transitional state when a line or address is first opened.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




