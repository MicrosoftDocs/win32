---
Description: The System Event Notification Service (SENS) defines the SENS coclass as part of the SENS type library.
ms.assetid: b494808c-1116-47ac-8713-0d515b312368
title: SENS Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SENS Object

The System Event Notification Service (SENS) defines the SENS coclass as part of the SENS type library.

## Implementation

The SENS object implementation is provided by the operating system.

## Creation/Access Functions



| Function                                      | Description                                             |
|-----------------------------------------------|---------------------------------------------------------|
| [**CoCreateInstance**](_com_cocreateinstance) | Creates an instance of the SENS object using its CLSID. |



 

## Interfaces



| Interface                            | Description                                                                                         |
|--------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**IsensNetwork**](/windows/win32/Sensevts/nn-sensevts-isensnetwork?branch=master) | Default. Outgoing interface implemented by sink object in subscriber application.                   |
| [**IsensOnNow**](/windows/win32/Sensevts/nn-sensevts-isensonnow?branch=master)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon**](/windows/win32/Sensevts/nn-sensevts-isenslogon?branch=master)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon2**](/windows/win32/Sensevts/nn-sensevts-isenslogon2?branch=master)   | Outgoing interface implemented by sink object in subscriber application. Available with Windows XP. |



 

## Related topics

<dl> <dt>

[**ISensLogon**](/windows/win32/Sensevts/nn-sensevts-isenslogon?branch=master)
</dt> <dt>

[**ISensNetwork**](/windows/win32/Sensevts/nn-sensevts-isensnetwork?branch=master)
</dt> <dt>

[**ISensOnNow**](/windows/win32/Sensevts/nn-sensevts-isensonnow?branch=master)
</dt> <dt>

[About System Event Notification Service](about-system-event-notification-service.md)
</dt> </dl>

 

 



