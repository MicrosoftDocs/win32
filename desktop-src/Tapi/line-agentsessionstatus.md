---
description: The LINE\_AGENTSESSIONSTATUS message is sent when the status of an ACD agent session changes on an agent handler for which the application currently has an open line. This message is generated using the lineProxyMessage function.
ms.assetid: bb9d2292-8c41-4557-989e-6c5eb785313f
title: LINE_AGENTSESSIONSTATUS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_AGENTSESSIONSTATUS message

The **LINE\_AGENTSESSIONSTATUS** message is sent when the status of an ACD agent session changes on an agent handler for which the application currently has an open line. This message is generated using the [**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage) function.


```C++
        
```



## Parameters

<dl> <dt>

*dwDevice* 
</dt> <dd>

The application's handle to the line device on which the agent session status has changed.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

A handle of the agent session whose status has changed.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Specifies the agent session status that has changed. Can be one or more of the **LINE\_AGENTSESSIONSTATUS**.

</dd> <dt>

*dwParam3* 
</dt> <dd>

If *dwParam2* includes the LINEAGENTSTATUSEX\_STATE bit, *dwParam3* indicates the new value of the agent state, which is one of the [**LINEAGENTSTATEEX\_ constants**](lineagentstateex--constants.md).

Otherwise, *dwParam3* is set to zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineGetAgentSessionInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetagentsessioninfo)
</dt> <dt>

[**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage)
</dt> </dl>

 

 




