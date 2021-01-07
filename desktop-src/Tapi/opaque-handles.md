---
description: A few types defined by TSPI are opaque handles.
ms.assetid: e52ed691-0479-48da-9e06-c6a0d7a20e10
title: Opaque Handles
ms.topic: article
ms.date: 05/31/2018
---

# Opaque Handles

A few types defined by TSPI are opaque handles. These are used in TSPI as public references to private data structures. This allows type-checking of parameters supplied to the interface procedures while still giving a measure of type protection. Only the owner of the private data structure knows how to interpret the opaque type as a reference to its data structure representation. As an example of how opaque handles are used, consider a phone device. Both TAPI and the service provider typically maintain data structures representing their respective views of the device.

In typical phone data structures maintained by TAPI and a service provider, each contains an opaque handle for the other data structure. These were exchanged at an early initialization step. When TAPI calls a TSPI function, it passes the opaque handle to refer to the device. The service provider knows how to resolve this as a reference (arrow) to its data structure. A similar process occurs when the service provider calls a callback function in TAPI.

 

 



