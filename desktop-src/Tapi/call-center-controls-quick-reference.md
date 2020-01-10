---
Description: The call center interfaces provide methods that queue and distribute calls within a call center.
ms.assetid: 0b9a455d-a614-4698-90ab-e81f020fad3e
title: Call Center Controls Quick Reference
ms.topic: article
ms.date: 05/31/2018
---

# Call Center Controls Quick Reference

The call center interfaces provide methods that queue and distribute calls within a call center. TAPI 3.x defines five main call center objects: ACDGroup, Agent, AgentHandler, AgentSession, and Queue. All of these objects can be extended to provide implementation-specific methods. In addition, the [**ITTAPICallCenter**](https://msdn.microsoft.com/library/ms732497(v=VS.85).aspx) interface on the TAPI object provides methods to enumerate AgentHandler objects.



| Call center interface                              | Description                                                              |
|----------------------------------------------------|--------------------------------------------------------------------------|
| [**ITACDGroup**](https://msdn.microsoft.com/library/ms728176(v=VS.85).aspx)                   | Gets name and queue information for an ACD group.                        |
| [**ITACDGroupEvent**](https://msdn.microsoft.com/library/ms728177(v=VS.85).aspx)         | Gets description of ACD group events.                                    |
| [**ITAgent**](https://msdn.microsoft.com/library/Aa379958(v=VS.85).aspx)                         | Provides methods to set and get information concerning an agent.         |
| [**ITAgentEvent**](https://msdn.microsoft.com/library/Aa380140(v=VS.85).aspx)               | Notification interface for [**ITAgent**](https://msdn.microsoft.com/library/Aa379958(v=VS.85).aspx).                   |
| [**ITAgentHandler**](https://msdn.microsoft.com/library/Aa380394(v=VS.85).aspx)           | Provides methods to create Agent objects and enumerate ACD groups.       |
| [**ITAgentHandlerEvent**](https://msdn.microsoft.com/library/Aa380631(v=VS.85).aspx) | Gets description of AgentHandler events.                                 |
| [**ITAgentSession**](https://msdn.microsoft.com/library/Aa381285(v=VS.85).aspx)           | Provides methods to set and get information concerning an agent session. |
| [**ITAgentSessionEvent**](https://msdn.microsoft.com/library/Aa381304(v=VS.85).aspx) | Notification interface for [**ITAgentSession**](https://msdn.microsoft.com/library/Aa381285(v=VS.85).aspx).     |
| [**ITQueue**](https://msdn.microsoft.com/library/ms731449(v=VS.85).aspx)                         | Gets and sets information concerning a queue.                            |
| [**ITQueueEvent**](https://msdn.microsoft.com/library/ms731451(v=VS.85).aspx)               | Gets information concerning a queue event.                               |
| [**IEnumACDGroup**](https://msdn.microsoft.com/library/ms727023(v=VS.85).aspx)             | Enumerates [**ITACDGroup**](https://msdn.microsoft.com/library/ms728176(v=VS.85).aspx).                             |
| [**IEnumAgent**](https://msdn.microsoft.com/library/ms727033(v=VS.85).aspx)                   | Enumerates [**ITAgent**](https://msdn.microsoft.com/library/Aa379958(v=VS.85).aspx).                                   |
| [**IEnumAgentHandler**](https://msdn.microsoft.com/library/ms727034(v=VS.85).aspx)     | Enumerates [**ITAgentHandler**](https://msdn.microsoft.com/library/Aa380394(v=VS.85).aspx).                     |
| [**IEnumAgentSession**](https://msdn.microsoft.com/library/ms727039(v=VS.85).aspx)     | Enumerates [**ITAgentSession**](https://msdn.microsoft.com/library/Aa381285(v=VS.85).aspx).                     |
| [**IEnumQueue**](https://msdn.microsoft.com/library/ms727545(v=VS.85).aspx)                   | Enumerates [**ITQueue**](https://msdn.microsoft.com/library/ms731449(v=VS.85).aspx).                                   |



 

The following interfaces enumerate TAPI 3.x elements according to COM standards. These interfaces constitute stand-alone objects, and are also summarized with their related objects.



| Enumerator interface                           | Description                                          |
|------------------------------------------------|------------------------------------------------------|
| [**IEnumACDGroup**](https://msdn.microsoft.com/library/ms727023(v=VS.85).aspx)         | Enumerates [**ITACDGroup**](https://msdn.microsoft.com/library/ms728176(v=VS.85).aspx).         |
| [**IEnumAgent**](https://msdn.microsoft.com/library/ms727033(v=VS.85).aspx)               | Enumerates [**ITAgent**](https://msdn.microsoft.com/library/Aa379958(v=VS.85).aspx).               |
| [**IEnumAgentHandler**](https://msdn.microsoft.com/library/ms727034(v=VS.85).aspx) | Enumerates [**ITAgentHandler**](https://msdn.microsoft.com/library/Aa380394(v=VS.85).aspx). |
| [**IEnumAgentSession**](https://msdn.microsoft.com/library/ms727039(v=VS.85).aspx) | Enumerates [**ITAgentSession**](https://msdn.microsoft.com/library/Aa381285(v=VS.85).aspx). |
| [**IEnumQueue**](https://msdn.microsoft.com/library/ms727545(v=VS.85).aspx)               | Enumerates [**ITQueue**](https://msdn.microsoft.com/library/ms731449(v=VS.85).aspx).               |



 

The event (notification) interfaces allow a TAPI 3.x application to respond to asynchronous events. You must call the [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method and set an event filter mask to enable reception of request events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.



| Event interface                                    | Description                                                                  |
|----------------------------------------------------|------------------------------------------------------------------------------|
| [**ITACDGroupEvent**](https://msdn.microsoft.com/library/ms728177(v=VS.85).aspx)         | Retrieves the description of Automatic Call Distribution (ACD) group events. |
| [**ITAgentEvent**](https://msdn.microsoft.com/library/Aa380140(v=VS.85).aspx)               | Retrieves the description of agent events.                                   |
| [**ITAgentHandlerEvent**](https://msdn.microsoft.com/library/Aa380631(v=VS.85).aspx) | Retrieves the description of agent handler events.                           |
| [**ITAgentSessionEvent**](https://msdn.microsoft.com/library/Aa381304(v=VS.85).aspx) | Retrieves the description of agent session events.                           |



 

 

 



