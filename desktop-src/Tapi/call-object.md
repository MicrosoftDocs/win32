---
description: The Call object represents an addresss connection between the local address and one or more other addresses.
ms.assetid: 67c063ba-8b12-40d6-9011-923bdee8b214
title: Call Object
ms.topic: article
ms.date: 05/31/2018
---

# Call Object

The Call object represents an address's connection between the local address and one or more other addresses. All call control is done through the Call object. [**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol) and [**ITCallInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallinfo) are the most frequently used interfaces on the call object. These interfaces implement a variety of operations and queries, such as acquiring interface pointers for media streams or getting the caller ID. See the main overview sections on [Session Operations](session-operations-ovr.md) and [Session Information](session-information-ovr.md) for reviews of those supported by TAPI.

A media service provider can implement [provider-specific interfaces](provider-specific-interfaces.md), which are aggregated on a call object by TAPI. For detailed information on what a provider has implemented, see the service provider's documentation.

The [Make a Call](make-a-call.md) and [Receive a Call](receive-a-call.md) code examples show some illustrations of using a Call object.

See [Call Object Interfaces](call-object-interfaces.md) for a list of all interfaces associated with the Call object.

 

 



