---
title: Use of the ProviderSpecific Buffer as a Receiver
description: Use of the ProviderSpecific buffer as a receiver.
ms.assetid: 9b199bc4-8846-4ec0-86ba-a719115433d2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Use of the ProviderSpecific Buffer as a Receiver

Receivers can use the [ProviderSpecific buffer](the-providerspecific-buffer.md) to do the following:

While making QOS requests, receivers can:

-   Specify nondefault RSVP reservation style, flow descriptors, and filter specifications.
-   Request Resv confirmation.
-   Specify one or more policy elements (policy information) to RSVP.

While receiving notification, such as getting additional information from the sender, receivers can:

-   Retrieve policy information
-   Retrieve QOS and RESV\_CONFIRM events.

 

 




