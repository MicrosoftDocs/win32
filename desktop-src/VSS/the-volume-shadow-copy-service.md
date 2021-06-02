---
description: The Volume Shadow Copy Service (VSS) provides the system infrastructure for running VSS applications on Windows-based systems.
ms.assetid: '237b2729-1e9b-4d0e-9c59-990e047a0360'
title: The Volume Shadow Copy Service
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

 

 



