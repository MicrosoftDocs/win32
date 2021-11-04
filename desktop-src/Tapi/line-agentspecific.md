---
description: The TAPI LINE\_AGENTSPECIFIC message is sent when the status of an ACD agent changes on a line the application currently has open. The application can invoke lineGetAgentStatus to determine the current status of the agent.
ms.assetid: 67e1796c-02e5-4f81-8086-7c2ff3112ae0
title: LINE_AGENTSPECIFIC message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_AGENTSPECIFIC message

The TAPI **LINE\_AGENTSPECIFIC** message is sent when the status of an ACD agent changes on a line the application currently has open. The application can invoke [**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa) to determine the current status of the agent.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

The application's handle to the line device.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The index into the array of handler extension identifiers in the [**LINEAGENTCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineagentcaps) structure of the handler extension with which the message is associated.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Specific to the handler extension. Generally, this value is used to cause the application to invoke a [**lineAgentSpecific**](/windows/desktop/api/Tapi/nf-tapi-lineagentspecific) function to fetch further details about the message.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Specific to the handler extension.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_AGENTSPECIFIC** message is not sent to applications that support older versions of TAPI.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEAGENTCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineagentcaps)
</dt> <dt>

[**lineAgentSpecific**](/windows/desktop/api/Tapi/nf-tapi-lineagentspecific)
</dt> <dt>

[**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa)
</dt> </dl>

 

 




