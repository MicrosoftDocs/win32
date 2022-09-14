---
description: The LSA stores local security policy information in a set of objects. Your application can query or edit the local security policy by accessing these objects.
ms.assetid: c8ed5cd8-55cf-43e7-92a3-9bd17a1147a9
title: LSA Policy Objects
ms.topic: article
ms.date: 05/31/2018
---

# LSA Policy Objects

The LSA stores local security policy information in a set of objects. Your application can query or edit the local security policy by accessing these objects.

The set consists of the following four objects:

-   [Policy](policy-object.md) contains global policy information.
-   [TrustedDomain](trusteddomain-object.md) contains information about a trusted domain.
-   [Account](account-object.md) contains information about a user, group, or local group account.
-   [Private Data](private-data-object.md) contains protected information, such as server account passwords. This information is stored as encrypted strings.

For more information on how to use the LSA Policy functions to manage the information stored in these objects, see [Using LSA Policy](using-lsa-policy.md).

 

 



