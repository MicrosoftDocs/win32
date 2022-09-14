---
description: The LINEAGENTSESSIONSTATE\_ constants describe various agent session states.
ms.assetid: 8a0d06bb-51ba-4eaf-8719-120aed817f63
title: LINEAGENTSESSIONSTATE_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINEAGENTSESSIONSTATE\_ Constants

The **LINEAGENTSESSIONSTATE\_ constants** describe various agent session states.

<dl> <dt>

<span id="LINEAGENTSESSIONSTATE_BUSYONCALL"></span><span id="lineagentsessionstate_busyoncall"></span>**LINEAGENTSESSIONSTATE\_BUSYONCALL**
</dt> <dd> <dl> <dt>



The agent is busy handling a call.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSESSIONSTATE_BUSYWRAPUP"></span><span id="lineagentsessionstate_busywrapup"></span>**LINEAGENTSESSIONSTATE\_BUSYWRAPUP**
</dt> <dd> <dl> <dt>



The agent is busy handling the wrap-up of the call.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSESSIONSTATE_ENDED"></span><span id="lineagentsessionstate_ended"></span>**LINEAGENTSESSIONSTATE\_ENDED**
</dt> <dd> <dl> <dt>



The agent session has ended.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSESSIONSTATE_NOTREADY"></span><span id="lineagentsessionstate_notready"></span>**LINEAGENTSESSIONSTATE\_NOTREADY**
</dt> <dd> <dl> <dt>



The agent is logged in, but occupied with a task other than serving a call (such as on a break). No additional calls should be routed to the agent.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSESSIONSTATE_READY"></span><span id="lineagentsessionstate_ready"></span>**LINEAGENTSESSIONSTATE\_READY**
</dt> <dd> <dl> <dt>



The agent is ready to accept calls.


</dt> </dl> </dd> <dt>

<span id="LINEAGENTSESSIONSTATE_RELEASED"></span><span id="lineagentsessionstate_released"></span>**LINEAGENTSESSIONSTATE\_RELEASED**
</dt> <dd> <dl> <dt>



The agent session has been released.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




