---
Description: The Volume Shadow Copy Service (VSS) provides the system infrastructure for running VSS applications on Windows-based systems.
ms.assetid: 654c67e8-2f17-4d93-aabd-fabd71c4c852
title: The Volume Shadow Copy Service
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Volume Shadow Copy Service

The Volume Shadow Copy Service (VSS) provides the system infrastructure for running VSS applications on Windows-based systems.

Though largely transparent to user and developer, VSS does the following:

-   Coordinates activities of providers, writers, and requesters in the creation and use of shadow copies
-   Furnishes the default system provider
-   Implements low-level driver functionality necessary for any provider to work

The VSS service starts on demand; therefore, for VSS operations to be successful, this service must be enabled.

 

 



