---
Description: 'The System Event Notification Service (SENS) defines the SENS coclass as part of the SENS type library.'
ms.assetid: 'b494808c-1116-47ac-8713-0d515b312368'
title: SENS Object
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
| [**IsensNetwork**](isensnetwork.md) | Default. Outgoing interface implemented by sink object in subscriber application.                   |
| [**IsensOnNow**](isensonnow.md)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon**](isenslogon.md)     | Outgoing interface implemented by sink object in subscriber application.                            |
| [**IsensLogon2**](isenslogon2.md)   | Outgoing interface implemented by sink object in subscriber application. Available with Windows XP. |



 

## Related topics

<dl> <dt>

[**ISensLogon**](isenslogon.md)
</dt> <dt>

[**ISensNetwork**](isensnetwork.md)
</dt> <dt>

[**ISensOnNow**](isensonnow.md)
</dt> <dt>

[About System Event Notification Service](about-system-event-notification-service.md)
</dt> </dl>

 

 



