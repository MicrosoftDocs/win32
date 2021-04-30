---
description: The call center interfaces provide methods that queue and distribute calls within a call center.
ms.assetid: 0b9a455d-a614-4698-90ab-e81f020fad3e
title: Call Center Controls Quick Reference
ms.topic: article
ms.date: 05/31/2018
---

# Call Center Controls Quick Reference

The call center interfaces provide methods that queue and distribute calls within a call center. TAPI 3.x defines five main call center objects: ACDGroup, Agent, AgentHandler, AgentSession, and Queue. All of these objects can be extended to provide implementation-specific methods. In addition, the [**ITTAPICallCenter**](/windows/win32/api/tapi3cc/nn-tapi3cc-ittapicallcenter) interface on the TAPI object provides methods to enumerate AgentHandler objects.



| Call center interface                              | Description                                                              |
|----------------------------------------------------|--------------------------------------------------------------------------|
| [**ITACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroup)                   | Gets name and queue information for an ACD group.                        |
| [**ITACDGroupEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroupevent)         | Gets description of ACD group events.                                    |
| [**ITAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagent)                         | Provides methods to set and get information concerning an agent.         |
| [**ITAgentEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentevent)               | Notification interface for [**ITAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagent).                   |
| [**ITAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandler)           | Provides methods to create Agent objects and enumerate ACD groups.       |
| [**ITAgentHandlerEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandlerevent) | Gets description of AgentHandler events.                                 |
| [**ITAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsession)           | Provides methods to set and get information concerning an agent session. |
| [**ITAgentSessionEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsessionevent) | Notification interface for [**ITAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsession).     |
| [**ITQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueue)                         | Gets and sets information concerning a queue.                            |
| [**ITQueueEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueueevent)               | Gets information concerning a queue event.                               |
| [**IEnumACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumacdgroup)             | Enumerates [**ITACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroup).                             |
| [**IEnumAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagent)                   | Enumerates [**ITAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagent).                                   |
| [**IEnumAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagenthandler)     | Enumerates [**ITAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandler).                     |
| [**IEnumAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagentsession)     | Enumerates [**ITAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsession).                     |
| [**IEnumQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumqueue)                   | Enumerates [**ITQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueue).                                   |



 

The following interfaces enumerate TAPI 3.x elements according to COM standards. These interfaces constitute stand-alone objects, and are also summarized with their related objects.



| Enumerator interface                           | Description                                          |
|------------------------------------------------|------------------------------------------------------|
| [**IEnumACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumacdgroup)         | Enumerates [**ITACDGroup**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroup).         |
| [**IEnumAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagent)               | Enumerates [**ITAgent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagent).               |
| [**IEnumAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagenthandler) | Enumerates [**ITAgentHandler**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandler). |
| [**IEnumAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumagentsession) | Enumerates [**ITAgentSession**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsession). |
| [**IEnumQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-ienumqueue)               | Enumerates [**ITQueue**](/windows/win32/api/tapi3cc/nn-tapi3cc-itqueue).               |



 

The event (notification) interfaces allow a TAPI 3.x application to respond to asynchronous events. You must call the [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method and set an event filter mask to enable reception of request events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.



| Event interface                                    | Description                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------|
| [**ITACDGroupEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itacdgroupevent)         | Retrieves the description of Automatic Call Distribution (ACD) group events. |
| [**ITAgentEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentevent)               | Retrieves the description of agent events.                                   |
| [**ITAgentHandlerEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagenthandlerevent) | Retrieves the description of agent handler events.                           |
| [**ITAgentSessionEvent**](/windows/win32/api/tapi3cc/nn-tapi3cc-itagentsessionevent) | Retrieves the description of agent session events.                           |



 

 

 
