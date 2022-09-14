---
description: The System Event Notification Service (SENS) defines the SENS coclass as part of the SENS type library.
ms.assetid: b494808c-1116-47ac-8713-0d515b312368
title: SENS Object
ms.topic: article
ms.date: 05/31/2018
---

# SENS Object

The System Event Notification Service (SENS) defines the SENS coclass as part of the SENS type library.

## Implementation

The SENS object implementation is provided by the operating system.

## Creation/Access Functions



| Function                                      | Description                                             |
|-----------------------------------------------|---------------------------------------------------------|
| [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) | Creates an instance of the SENS object using its CLSID. |



 

## Interfaces



| Interface                            | Description                                                                                         |
|--------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**IsensNetwork**](/windows/desktop/api/Sensevts/nn-sensevts-isensnetwork) | Default. Outgoing interface implemented by sink object in subscriber application.                   |
| [**IsensOnNow**](/windows/desktop/api/Sensevts/nn-sensevts-isensonnow)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon2**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon2)   | Outgoing interface implemented by sink object in subscriber application. Available with Windows XP. |



 

## Related topics

<dl> <dt>

[**ISensLogon**](/windows/desktop/api/Sensevts/nn-sensevts-isenslogon)
</dt> <dt>

[**ISensNetwork**](/windows/desktop/api/Sensevts/nn-sensevts-isensnetwork)
</dt> <dt>

[**ISensOnNow**](/windows/desktop/api/Sensevts/nn-sensevts-isensonnow)
</dt> <dt>

[About System Event Notification Service](about-system-event-notification-service.md)
</dt> </dl>

 

 
