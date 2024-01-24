---
description: Windows-based systems can have multiple instances of the TrustedDomain object type.
ms.assetid: 13efedb5-ebb6-459b-8c4f-06774226278c
title: The TrustedDomain Object Type
ms.topic: article
ms.date: 05/31/2018
---

# The TrustedDomain Object Type

Windows-based systems can have multiple instances of the [**TrustedDomain**](trusteddomain-object.md) object type. **TrustedDomain** objects have two fields that must be unique among all **TrustedDomain** objects:

-   The name of the [**TrustedDomain**](trusteddomain-object.md)
-   The [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) of the [**TrustedDomain**](trusteddomain-object.md).

An attempt to create a new **TrustedDomain** object with either a name or SID that is already in use by another **TrustedDomain** object will be rejected.

 

 
