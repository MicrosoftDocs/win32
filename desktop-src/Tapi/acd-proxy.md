---
description: An Automatic Call Distribution (ACD) server is a combination of hardware and software that classifies, queues, and distributes incoming calls to agents or outgoing calls to lines.
ms.assetid: 29fb0bd7-0ca9-4490-82d2-39550f00a97b
title: ACD Proxy
ms.topic: article
ms.date: 05/31/2018
---

# ACD Proxy

An Automatic Call Distribution (ACD) server is a combination of hardware and software that classifies, queues, and distributes incoming calls to agents or outgoing calls to lines.

The Server ACD application is a TAPI proxy application, which for maximum efficiency should run on the same server as the telephony service provider (TSP). With a traditional ACD switch, the proxy application would interface to the switch's internal ACD and expose its operation. A software-based or "virtual" ACD proxy application would be fully responsible for the tracking of calls, queues, groups, and agents and would use the standard TAPI interfaces to control the switching hardware. Agent client applications will typically run on the individual agent's workstations and make use of the TAPI Remote Service Provider to communicate with the TAPISRV on the server machine, and hence the proxy application.

Classification of incoming calls is designed to get a call to an agent who will be able to handle it effectively. Classification may be based on the number dialed, an interactive voice recognition (IVR) system, or other criteria. TAPI uses the concept of an [ACD Group](about-call-center-controls.md) to represent this operation.

Queues are a graceful and expected way for call centers to deal with heavy load periods. A queue is normally associated with an ACD Group but may be created to handle outgoing lines or incoming calls waiting for an IVR application. See [Queues](about-call-center-controls.md) for more information.

Call distribution to agents or groups of agents may be uniform but typically is based on data such as call information, agent availability, and ability. TAPI's [Agent Handler](about-call-center-controls.md) provides access to information such as agent availability and addresses for the transfer of calls to agents.

In addition to basic call distribution, an ACD system provides for managing and reporting on the system performance. Statistics gathered on call queues, groups, and agents are used to refine and enhance the performance of the system and are typically used as the basis for Agent remuneration.

 

 



