---
description: The TAPI LINE\_AGENTSTATUS message is sent when the status of an ACD agent changes on a line the application currently has open. The application can invoke lineGetAgentStatus to determine the current status of the agent.
ms.assetid: 48f5d9bc-f20d-4364-8ec1-0b4bdc9cfcb4
title: LINE_AGENTSTATUS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_AGENTSTATUS message

The TAPI **LINE\_AGENTSTATUS** message is sent when the status of an ACD agent changes on a line the application currently has open. The application can invoke [**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa) to determine the current status of the agent.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

The application's handle to the line device on which the agent status has changed.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Identifier of the address on the line on which the agent status changed. An address identifier is permanently associated with an address; the identifier remains constant across operating system upgrades.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Specifies the agent status that has changed; can be a combination of [**LINEAGENTSTATUS\_ constants**](lineagentstatus--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

If *dwParam2* includes the LINEAGENTSTATUS\_STATE bit, then *dwParam3* indicates the new value of the **dwState** member in [**LINEAGENTSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineagentstatus). Otherwise, this parameter is set to zero.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_AGENTSTATUS** message is not sent to applications that support older versions of TAPI.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEAGENTSTATUS**](/windows/desktop/api/Tapi/ns-tapi-lineagentstatus)
</dt> <dt>

[**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa)
</dt> </dl>

 

 




