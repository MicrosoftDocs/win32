---
title: Searching the Global Catalog
description: Active Directory Domain Services also have a global catalog (GC), which contains a partial replica of all objects in the directory.
ms.assetid: 83970563-1a56-4671-b264-56e29939e369
ms.tgt_platform: multiple
keywords:
- searching the global catalog Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Searching the Global Catalog

Active Directory Domain Services also have a global catalog (GC), which contains a partial replica of all objects in the directory. It also contains partial replicas of the schema and configuration containers. One or more domain controllers in a domain can hold a copy of the global catalog. For more information about binding to a global catalog, see [Binding to the Global Catalog](binding-to-the-global-catalog.md).

The global catalog holds a replica of every object in Active Directory Domain Services, but with only a small number of their attributes. The attributes in the global catalog are those most frequently used in search operations, such as a user's first and last names, login names, and so on. The global catalog attributes also include those required to locate a full replica of the object. The global catalog allows users to quickly find objects of interest without knowing what domain holds them and without requiring a contiguous extended namespace in the enterprise; that is, you can search the entire forest.

So, if you bind to an object in the global catalog, you will search that object and the entire hierarchy below it — without having to go to any other server. However, the search can only use a query filter containing properties in the global catalog and can retrieve only properties in the global catalog.

Searching the global catalog has the following benefits:

-   Global catalog enables you to search the entire forest or any part of the forest as well as the schema and configuration containers.
-   Global catalog enables you to perform a complete search on a single server. No referrals or referral chasing is required.

Searching the global catalog has the following disadvantages:

-   Global catalog contains a small subset of the properties on each object. If your query filter includes properties that are not in the global catalog, the query will evaluate the expressions containing those properties as false. If you specify non-global catalog properties in the list of properties to return, those properties are not retrieved.
-   To search the global catalog, a domain controller that contains a global catalog must be available. If one is not available, you cannot perform a global catalog search.
-   The global catalog is read-only. This means you cannot bind to an object in the global catalog to create, modify, or delete objects.

 

 




