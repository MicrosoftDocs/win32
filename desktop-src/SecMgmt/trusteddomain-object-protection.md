---
description: When a TrustedDomain object is created, it is assigned a standard protection.
ms.assetid: cc554630-7be7-4657-90f2-ce5fa81731b2
title: TrustedDomain Object Protection
ms.topic: article
ms.date: 05/31/2018
---

# TrustedDomain Object Protection

When a [**TrustedDomain**](trusteddomain-object.md) object is created, it is assigned a standard protection as follows:

-   The WORLD local group is granted GENERIC\_EXECUTE access.
-   The LOCAL\_ADMIN local group is granted DELETE, GENERIC\_READ, GENERIC\_WRITE, and GENERIC\_EXECUTE access.
-   The LOCAL\_ADMIN local group is assigned as owner and primary group of the object.

 

 



