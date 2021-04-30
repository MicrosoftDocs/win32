---
description: Proper shutdown of communications sessions and of an entire application is required to prevent resources from remaining tied up in calls or applications that no longer need them.
ms.assetid: '40694b7f-474b-41aa-be3f-48e4ca517a6f'
title: TAPI Shutdown
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Shutdown

Proper shutdown of communications sessions and of an entire application is required to prevent resources from remaining tied up in calls or applications that no longer need them.

TAPI provides a series of functions and methods to assist in the process. Obviously, the application must also take responsibility for properly releasing allocated memory, whether in the form of data structures or COM references.



| TAPI 2.x functions                                                            | Description                                                            |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**lineRegisterRequestRecipient**](/windows/win32/api/tapi/nf-tapi-lineregisterrequestrecipient) | Unregisters the application as a handler for assisted telephony calls. |
| [**lineClose**](/windows/win32/api/tapi/nf-tapi-lineclose)                                       | Disconnects the application as a manager for calls on the given line.  |
| [**lineShutdown**](/windows/win32/api/tapi/nf-tapi-lineshutdown)                                 | Shuts down the application's usage of the line abstraction.            |



 



| TAPI 3.x interfaces or methods                                            | Description                                                                |
|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**ITTAPI::UnregisterNotifications**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-unregisternotifications) | Removes any event notification registrations performed by the application. |
| [**ITTAPI::Shutdown**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-shutdown)                               | Disconnects the application as a call manager.                             |



 

 

 
