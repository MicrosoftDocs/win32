---
description: An operation that completes asynchronously performs part of its processing in the function call made by the application and the remainder of it in an independent execution thread after TAPI 2.x has returned from the function call.
ms.assetid: 37b544e4-6413-4741-b8b6-ec676ce4ca97
title: Asynchronous Functions
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Functions

An operation that completes asynchronously performs part of its processing in the function call made by the application and the remainder of it in an independent execution thread after TAPI 2.x has returned from the function call. To ensure completion of the call's processing, the service provider vectors the request to another active entity in the system—such as a LAN server, add-in hardware, a switch, or a network—and then returns to the application. At this time, either a negative error result or a positive request identifier is returned to the application.

At the time of asynchronous completion (the service provider has received an interrupt from the hardware, meaning that a message must be delivered), the service provider calls TAPISRV and reports that "Event *X* has just taken place. Deliver an appropriate message to all concerned applications." When TAPISRV receives this message, it forwards the message to the TAPI dynamic-link library, in the application's process, which in turn posts a window message, signals an event handle, or posts to an I/O completion port, according to the message notification scheme selected by the application in [**lineInitializeEx**](/windows/win32/api/tapi/nf-tapi-lineinitializeexa) or [**phoneInitializeEx**](/windows/win32/api/tapi/nf-tapi-phoneinitializeexa).

When the asynchronous portion of the operation completes, a [**LINE\_REPLY**](./line-reply.md) (or [**PHONE\_REPLY**](./phone-reply.md)) message is sent to the application. This message contains, as one of its parameters, the request identifier returned by the function call. This request identifier allows the application to determine which original request has completed. (Applications should remember the request identifiers of all their requests in progress so that reply messages can be properly handled.) A second parameter to the LINE\_REPLY (or PHONE\_REPLY) message is the asynchronous return value. This is either a negative value (for an error) or zero if the operation completed successfully. For asynchronous operations, any of the return values may be returned as part of the function return or as the *dwParam2* parameter in the LINE\_REPLY or PHONE\_REPLY message. The value 0, which indicates success, will only be returned in the LINE\_REPLY message, and never as the function's return value.

The initialize functions ( [**lineInitializeEx**](/windows/win32/api/tapi/nf-tapi-lineinitializeexa) and [**phoneInitializeEx**](/windows/win32/api/tapi/nf-tapi-phoneinitializeexa)) tell TAPI how to send these messages to the application.

> [!Note]  
> In some cases, if a multithreaded application calls an asynchronous function from a thread other than the thread from which the application initialized the line or phone device, the application may receive the [**LINE\_REPLY**](./line-reply.md) or [**PHONE\_REPLY**](./phone-reply.md) message before the asynchronous function has returned. In such cases, the application should save the message parameters and wait until the asynchronous function returns and the request identifier is known before processing the message.

 

 

 
