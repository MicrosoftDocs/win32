---
description: The pickup operation allows an application to answer a session that is alerting at another address. The application identifies the target of the pickup and is returned a session identifier for the picked-up call.
ms.assetid: 3dfbb5c0-b533-403f-ad6c-b9e1b52ab47a
title: Pickup
ms.topic: article
ms.date: 05/31/2018
---

# Pickup

The pickup operation allows an application to answer a session that is alerting at another address. The application identifies the target of the pickup and is returned a session identifier for the picked-up call.

There are several ways to identify the target of the pickup request. First, the application may specify the address of the alerting party. Second, if no address is specified and the switch allows it, the application can pick up any alerting session in its pickup group. Third, some switches allow pickup of a session alerting in a different pickup group if the group identifier is specified.

Some key telephone systems support a *transfer through hold* capability on bridged-exclusive call appearances. In this scheme, a particular phone owns a call exclusively when the call is active, but when the call is on hold, any phone that has an appearance of the line can pick up the call.

**TAPI 2.x:** An application can use a pickup operation with a **NULL** target address for this purpose, similar to how the function is used to pick up a call waiting call on an analog line. LINEADDRFEATURE\_PICKUPHELD indicates the existence of the capability.

If LINEADDRCAPFLAGS\_PICKUPCALLWAIT is **TRUE**, a session can be picked up for which the user has audibly detected the call-waiting signal but for which the service provider is unable to perform the detection. This gives the user a mechanism to "answer" a waiting call even though the service provider was unable to detect the call-waiting signal. Both the destination address and the group ID must be **NULL** to pick up a call-waiting call.

When a session has been picked up successfully, the application receives a state change notification with the [reason](reason-ovr.md) set to LINECALLREASON\_PICKUP.

Not all service providers support use of this operation.

**TAPI 2.x:** See [**linePickup**](/windows/win32/api/tapi/nf-tapi-linepickup).

**TAPI 3.x:** See [**ITBasicCallControl::Pickup**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-pickup).

 

 
