---
description: The Phone object is the entity that represents the actual phone device and all of its controls.
ms.assetid: 5bc2f595-8e2b-4938-b813-1574a9390084
title: Phone Object Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Phone Object Interfaces

The Phone object is the entity that represents the actual phone device and all of its controls.

The [**ITPhoneEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itphoneevent) and [**IEnumPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumphone) interfaces are not directly exposed on the Phone object, but are tightly related to it and are listed here for convenience of reference.



| Interface                                                  | Description                                                                                                                               |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-itphone)                                 | Allows access to the phone device at a level comparable to that available with the TAPI 2.*x* C API.                                      |
| [**ITAutomatedPhoneControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itautomatedphonecontrol) | Provides methods for automated control of a phone's tones and rings, and for automated call handling based on a phone's hookswitch state. |
| [**ITPhoneEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itphoneevent)                       | Retrieves the description of phone events.                                                                                                |
| [**IEnumPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumphone)                           | Enumerates [**ITPhone**](/windows/desktop/api/tapi3if/nn-tapi3if-itphone).                                                                                                    |



 

 

 



