---
description: A smart card interface consists of a predefined set of services available within a smart card, the protocols necessary to invoke the services, and any assumptions regarding the context of the services.
ms.assetid: 4f9c13da-8fe3-43e7-875f-04850495edf3
title: Smart Card Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Smart Card Interfaces

A [*smart card*](../secgloss/s-gly.md) interface consists of a predefined set of services available within a *smart card*, the protocols necessary to invoke the services, and any assumptions regarding the context of the services.

With respect to smart cards, the term "interface" is similar to how it is used in COM, which in turn is similar in concept to the ISO 7816/5 application identifier but with a different scope.

Each smart card interface is identified by a GUID. For example, an interface might be defined that provides biorhythm information to its holder. If a given smart card supports this service, then it may claim to support that interface GUID. Using the interface GUIDs, an application may search for a particular set of interfaces, locating any card that supports that set, to complete a task.

Although an interface has one GUID, it might be implemented differently on different cards. For example, the biorhythm interface mentioned above can have several different implementations, yet all are referenced using the same GUID. The different implementations would not change the interaction between the application and the smart card; however, the interaction between the [*service provider*](../secgloss/c-gly.md) and the smart cards may differ depending on the interface's implementation.

The set of interfaces supported by a smart card is defined during smart card introduction (see [Introducing Smart Cards to the System](introducing-smart-cards-to-the-system.md)).

 

 
