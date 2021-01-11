---
description: The IP conferencing MSP implements several provider-specific interfaces for participant control. These interfaces are exposed on the call object, if this MSP is associated with the call.
ms.assetid: 01af2452-de2d-42ce-970d-82a83ae0b428
title: IPConf MSP Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# IPConf MSP Interfaces

\[ The IPConf MSP Interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The IP conferencing MSP implements several provider-specific interfaces for participant control. These interfaces are exposed on the call object, if this MSP is associated with the call.

The [**ITParticipantEvent**](itparticipantevent.md) and [**IEnumParticipant**](ienumparticipant.md) interfaces are stand-alone objects, and are listed here for reference convenience.



| Interface                                            | Description                                                                                                                                               |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IMulticastControl**](imulticastcontrol.md)       | Allows an application to set and get the loopback mode ( [**MULTICAST\_LOOPBACK\_MODE**](multicast-loopback-mode.md)) for a multicast conference object. |
| [**ITParticipant**](itparticipant.md)               | Allows an application to retrieve information on conference participants, and get pointers to the streams associated with those participants.             |
| [**ITParticipantControl**](itparticipantcontrol.md) | Allows an application to retrieve pointers to the participants in a conference.                                                                           |
| [**ITParticipantEvent**](itparticipantevent.md)     | Allows an application to retrieve event information concerning a conference participant.                                                                  |
| [**IEnumParticipant**](ienumparticipant.md)         | Enumerates [**ITParticipant**](itparticipant.md).                                                                                                        |



 

 

 



