---
description: Monitoring and control of ACD agent status on stations is supported through these functions lineGetAgentCaps lineGetAgentStatus lineGetAgentGroupList lineGetAgentActivityList lineSetAgentGroup lineSetAgentState and lineSetAgentActivity.
ms.assetid: 2851fe54-f807-4cef-b6ca-2dcc7e1ae6fb
title: ACD Agent Monitoring and Control
ms.topic: article
ms.date: 05/31/2018
---

# ACD Agent Monitoring and Control

Monitoring and control of ACD agent status on stations is supported through these functions: [**lineGetAgentCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetagentcapsa), [**lineGetAgentStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetagentstatusa), [**lineGetAgentGroupList**](/windows/desktop/api/Tapi/nf-tapi-linegetagentgrouplista), [**lineGetAgentActivityList**](/windows/desktop/api/Tapi/nf-tapi-linegetagentactivitylista), [**lineSetAgentGroup**](/windows/desktop/api/Tapi/nf-tapi-linesetagentgroup), [**lineSetAgentState**](/windows/desktop/api/Tapi/nf-tapi-linesetagentstate), and [**lineSetAgentActivity**](/windows/desktop/api/Tapi/nf-tapi-linesetagentactivity).

The [**LINE\_AGENTSTATUS**](line-agentstatus.md) message is used to indicate when agent information has changed.

These controls are associated with an address instead of a line because many ACD systems are implemented with different ACD queues associated with buttons on the phone terminal (and separate call appearances). Also, ACD agent phones can often have separate call appearances for personal calls.

Architecturally, ACD functionality should be implemented in a server-based application. The client functions mentioned above, rather than mapping to the telephony service provider, are conveyed to a server application that has registered (using an option of [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)) as a handler for such functions. The [**LINE\_PROXYREQUEST**](line-proxyrequest.md) message is used to signal to the handler application when a request has been made; it calls the [**lineProxyResponse**](/windows/desktop/api/Tapi/nf-tapi-lineproxyresponse) function to return results and data. Handler applications can also call [**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage) to generate LINE\_AGENTSTATUS messages when required. In the case of a legacy PBX or stand-alone ACD that implements ACD functionality itself, the telephony service provider for the switch must include a proxy server application that accepts the requests and routes them (possibly using [**lineDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-linedevspecific) functions or a private interface) to the service provider, which routes them to the switch.

 

 



