---
description: Explains how Account objects are protected.
ms.assetid: a07ef46e-f4b6-4e21-bdd7-72d03e1c88b3
title: Account Object Protection
ms.topic: article
ms.date: 05/31/2018
---

# Account Object Protection

[**Account**](account-object.md) objects are protected in the following fashion:

-   The group **WORLD** has GENERIC\_EXECUTE.
-   The group **LOCAL\_ADMIN** has DELETE, GENERIC\_READ, GENERIC\_WRITE, GENERIC\_EXECUTE, and WRITE\_DACL access.
-   The group **LOCAL\_ADMIN** is assigned as owner and primary group of Account objects.

 

 



