---
description: Proper functioning of TAPI components requires setting up the communications environment on a computer.
ms.assetid: 3df3d974-629e-4d78-b97d-b8121b185309
title: TAPI Initialization
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Initialization

Proper functioning of TAPI components requires setting up the communications environment on a computer as follows:

-   [Installation](installation.md) is performed when software or hardware is first added to the computer. Detailed procedures depend on the operating system and the software itself.
-   [Primary initialization](primary-initialization.md) creates the objects and communication paths.
-   [Version negotiation](version-negotiation.md) ensures that TAPI components will be able to exchange data.
-   [Resource inventory](resource-inventory.md) retrieves information concerning devices available for use by a TAPI application.
-   [Event notification](event-notification.md) specifies how TAPI and the service providers pass asynchronous operation results and state change information to the application.

## Summary of Related Reference Pages



| TAPI 2.x functions                                        | Description                                                                                                                       |
|-----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**lineInitializeEx**](/windows/win32/api/tapi/nf-tapi-lineinitializeexa)     | Sets up the telephony environment, returns application handle and device count.                                                   |
| [**lineGetDevCaps**](/windows/win32/api/tapi/nf-tapi-linegetdevcaps)         | Gets device capabilities, such as TAPI version or media types supported.                                                          |
| [**lineGetAddressCaps**](/windows/win32/api/tapi/nf-tapi-linegetaddresscaps) | Gets address capabilities, such as whether call park is supported.                                                                |
| [**lineOpen**](/windows/win32/api/tapi/nf-tapi-lineopen)                     | Notifies TAPI that the application will be using the line, and in what way.                                                       |
| [**lineGetMessage**](/windows/win32/api/tapi/nf-tapi-linegetmessage)         | Returns the next TAPI message that is queued for delivery to an application that is using the Event Handle notification mechanism |



 



| TAPI 3.x interfaces or methods                                                | Description                                                                                                                                |
|-------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITTAPI::Initialize**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-initialize)                               | Sets up telephony environment.                                                                                                             |
| [**ITTAPI::EnumerateAddresses**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-enumerateaddresses)               | Enumerates addresses currently available.                                                                                                  |
| [**ITTAPI::get\_Addresses**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-get_addresses)                        | Creates a collection of addresses currently available. Provided for Automation client applications, such as those written in Visual Basic. |
| [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event)       | Determines response to an asynchronous event notification. Implemented by the application, invoked by TAPI.                                |
| [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter)                    | Sets the event filter mask, which notifies TAPI which events the application requires.                                                     |
| [**ITTAPI::RegisterCallNotifications**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-registercallnotifications) | Instructs TAPI to pass the application incoming sessions for a specified address and set of media types.                                   |
| [**ITMediaSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediasupport)                                      | Allows an application to discover the media support capabilities for an address.                                                           |



 

 

 
