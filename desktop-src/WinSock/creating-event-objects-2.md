---
description: The Ws2\_32.dll provides facilities for event object creation to both applications and service providers, although in most instances event objects will be created by applications.
ms.assetid: 86da30ad-80bc-4982-9306-bbe29b1bab19
title: Creating Event Objects
ms.topic: article
ms.date: 05/31/2018
---

# Creating Event Objects

The Ws2\_32.dll provides facilities for event object creation to both applications and service providers, although in most instances event objects will be created by applications. Event object services are made available to Windows Sockets service providers through [**WPUCreateEvent**](/windows/desktop/api/Ws2spi/nf-ws2spi-wpucreateevent) simply as a convenience mechanism for any internal processing that may benefit from same. Note that the event object handle is only valid in the context of the calling process. In Windows environments the realization of event objects is through the native event services provided by the operating system.

 

 



