---
description: The CallHub object represents a third-party view of a multiparty call.
ms.assetid: ea23ae25-2fbb-4060-8273-cd7921d49e52
title: CallHub Object
ms.topic: article
ms.date: 05/31/2018
---

# CallHub Object

The CallHub object represents a third-party view of a multiparty call. The associated interfaces and methods get and set information concerning the hub, such as whether it is active. Using the CallHub object, a user with the required security can discover and potentially control other participants in a call.

A CallHub object cannot be created directly by an application. A CallHub object is created indirectly when an incoming call is received through TAPI 3.

TAPI 3 relies on TAPI service providers to provide the necessary information about calls to implement using the CallHub object. Because not all service providers provide this information, and not all hardware supports call hub tracking, the information available about the other users in the connection may be limited or nonexistent.

The [Create a Simple Conference](create-a-simple-conference.md) code example illustrates use of a CallHub object.

See [CallHub Object Interfaces](callhub-object-interfaces.md) for a list of all interfaces associated with the CallHub object.

 

 



