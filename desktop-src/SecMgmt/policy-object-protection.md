---
description: Describes how the Policy object is protected by default.
ms.assetid: e2d65ebf-5fbd-4e25-9862-a8188abb5492
title: Policy Object Protection
ms.topic: article
ms.date: 05/31/2018
---

# Policy Object Protection

The [**Policy**](policy-object.md) object is protected by default with the following settings:

-   The local group WORLD has GENERIC\_EXECUTE access.
-   The well-known ID System is granted POLICY\_ALL\_ACCESS.
-   The local group LOCAL\_ADMIN has GENERIC\_READ, GENERIC\_WRITE, and GENERIC\_EXECUTE access.
-   The group LOCAL\_ADMIN is assigned as owner and primary group of this object.

The [**Policy**](policy-object.md) object cannot be created or destroyed.

 

 



