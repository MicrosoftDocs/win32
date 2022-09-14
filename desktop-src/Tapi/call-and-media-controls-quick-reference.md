---
description: The following table lists TAPI version 3 COM interfaces by category in order of importance.
ms.assetid: fafb6d6e-934e-4942-8b90-dacb7ba09752
title: Call and Media Controls Quick Reference
ms.topic: article
ms.date: 05/31/2018
---

# Call and Media Controls Quick Reference

\[ The [IPConf MSP Interfaces](ipconf-msp-interfaces.md) are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following table lists TAPI version 3 COM interfaces by category in order of importance. The interfaces are grouped according to TAPI 3's five basic call control objects: TAPI, Address, Terminal, Call, and CallHub. Remaining interfaces are grouped according to Automatic Call Distribution (ACD) interfaces, which provide call-center functionality; enumerator interfaces, and stand-alone objects.



| Interface groupings                                          | Description                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [TAPI Object Interfaces](tapi-object-interfaces.md)         | The TAPI object is the main object for TAPI 3.                                                                                                                                                                                                              |
| [Address Object Interfaces](address-object-interfaces.md)   | The Address object represents an entity that can make or receive calls. The associated interfaces and methods allow an application to get and set information concerning the address, such as whether it has caller ID support.                             |
| [Terminal Object Interfaces](terminal-object-interfaces.md) | The Terminal object represents the sink or source at the termination or origination point of a call. The associated interfaces and methods allow an application to get and set information concerning the terminal, such as whether it is currently in use. |
| [Call Object Interfaces](call-object-interfaces.md)         | The Call object represents a call and is created when a call comes into existence. The associated interfaces and methods get and set information concerning the call, such as current call state.                                                           |
| [Phone Object Interfaces](phone-object-interfaces.md)       | The Phone object is the entity that represents the actual phone device and all of its controls.                                                                                                                                                             |
| [IPConf MSP Interfaces](ipconf-msp-interfaces.md)           | The IP conferencing MSP implements several interfaces for participant control that are exposed on the call object.                                                                                                                                          |
| [CallHub Object Interfaces](callhub-object-interfaces.md)   | The CallHub object represents a third-party view of a multi-party call. The associated interfaces and methods get and set information concerning the call, such as whether the call hub is active.                                                          |
| [Enumerator Interfaces](enumerator-interfaces.md)           | COM-standard enumerator interfaces.                                                                                                                                                                                                                         |
| [Event Interfaces](./event-interfaces.md)            | The event interfaces are also shown with their object or function groupings.                                                                                                                                                                                |
| [Stand-Alone Objects](stand-alone-objects.md)               | The TAPI 3 miscellaneous stand-alone objects provide interfaces and methods for operations such as assisted telephony or event handling.                                                                                                                    |



 

 

 
