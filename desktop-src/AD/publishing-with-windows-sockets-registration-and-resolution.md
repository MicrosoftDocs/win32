---
title: Publishing with Windows Sockets Registration & Resolution
description: Windows Sockets services can use the Registration and Resolution (RnR) APIs to publish services and look up services published with RnR.
ms.assetid: 95c16d0b-abbc-4407-ac31-d7de0b25bd74
ms.tgt_platform: multiple
keywords:
- Windows Sockets Registration and Resolution AD ,Publishing
ms.topic: article
ms.date: 05/31/2018
---

# Publishing with Windows Sockets Registration & Resolution

Windows Sockets services can use the Registration and Resolution (RnR) APIs to publish services and look up services published with RnR. RnR publication occurs in two steps. The first step installs a service class that associates a GUID with a name for the service. The service class can hold service-specific configuration data. Services can then publish themselves as instances of the service class. When published, clients can query the directory service for instances of a given class using the RnR APIs and select an instance to bind to. When a class is no longer required, it can be removed.

 

 




