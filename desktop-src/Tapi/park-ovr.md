---
description: The park operation allows an application to send a session to a special address where it will be held until unparked.
ms.assetid: 6a82f03e-d8fd-4d0b-8f5d-f7934ba86759
title: Park
ms.topic: article
ms.date: 05/31/2018
---

# Park

The park operation allows an application to send a session to a special address where it will be held until unparked. From the point of view of the application, this looks much like a transfer. To the party on the other end of the connection, this resembles being put on hold.

The difference between park and transfer is that the parked address is not a connection point for the session, and the session does not alert or time out. The difference between park and hold is that once park operation completes, the session is no longer associated with the application's address.

Two forms of parking a session are provided: *directed park* and *nondirected park*. In directed call park, the application specifies the destination address where the call is to be parked. With nondirected park, the service provider or underlying hardware determines the address and returns it to the application.

A parked session typically enters the idle state after it has been successfully parked, and the application should then release the resources associated with it. See [Terminate a Session](terminate-a-session-ovr.md) for a summary of how to do this.

If the application unparks the session, new session resources are allocated even if the application has returned the previous pointers, so failure to do proper releases can result in a variety of problems.

Some service providers can remind the user after a session has been parked for some long amount of time. The application sees an offering call with a call [reason](reason-ovr.md) set to reminder.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**linePark**](/windows/win32/api/tapi/nf-tapi-linepark), [**lineUnpark**](/windows/win32/api/tapi/nf-tapi-lineunpark).

**TAPI 3:** See [**ITBasicCallControl::ParkDirect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-parkdirect), [**ITBasicCallControl::ParkIndirect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-parkindirect), [**ITBasicCallControl::Unpark**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-unpark).

 

 
