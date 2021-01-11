---
description: The TAPI Object is the main object for TAPI 3.
ms.assetid: 046f2646-6043-4d68-a42a-8750c016b3c8
title: TAPI Object Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Object Interfaces

The [TAPI Object](tapi-object.md) is the main object for TAPI 3.

The [**ITTAPIObjectEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapiobjectevent) interface is not directly exposed on the TAPI Object, but is tightly related to it and is listed here for reference convenience.



| Interfaces                                                 | Description                                                                                                                                            |
|------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITTAPI**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapi)                                   | Primary TAPI 3 interface.                                                                                                                              |
| [**ITTAPI2**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapi2)                                 | Derives from [**ITTAPI**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapi); provides additional methods that support phone devices.                                                         |
| [**ITTAPIEventNotification**](/windows/desktop/api/Tapi3if/nn-tapi3if-ittapieventnotification) | Outgoing interface used to receive asynchronous information about TAPI 3 events.                                                                       |
| [**ITTAPICallCenter**](/windows/win32/api/tapi3cc/nn-tapi3cc-ittapicallcenter)               | Provides an entry interface into call center controls.                                                                                                 |
| [**ITTAPIObjectEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapiobjectevent)             | Provides methods to retrieve information concerning TAPI object events.                                                                                |
| [**ITTAPIObjectEvent2**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapiobjectevent2)           | Extends [**ITTAPIObjectEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-ittapiobjectevent); provides a method to retrieve a pointer to the phone object that caused the TAPI object event. |



 

 

 
