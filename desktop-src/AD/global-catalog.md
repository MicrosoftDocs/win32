---
title: Global Catalog
description: A Domain run by Active Directory Domain Services can consist of many partitions or naming contexts.
ms.assetid: eac02c1f-0c37-4eee-822d-07913ea8775a
ms.tgt_platform: multiple
keywords:
- global catalog Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Global Catalog

A Domain run by Active Directory Domain Services can consist of many partitions or naming contexts. The distinguished name (DN) of an object includes enough information to locate a replica of the partition that holds the object. Many times however, the user or application does not know the DN of the target object or which partition might contain the object. The [*global catalog (GC)*](/previous-versions/windows/desktop/legacy/ms681905(v=vs.85)) allows users and applications to find objects in an Active Directory domain tree, given one or more attributes of the target object.

The global catalog contains a partial replica of every naming context in the directory. It contains the schema and configuration naming contexts as well. This means the GC holds a replica of every object in the directory but with only a small number of their attributes. The attributes in the GC are those most frequently used in search operations (such as a user's first and last names or login names) and those required to locate a full replica of the object. The GC allows users to quickly find objects of interest without knowing what domain holds them and without requiring a contiguous extended namespace in the enterprise.

The global catalog is built automatically by the Active Directory Domain Services replication system. The replication topology for the global catalog is generated automatically. The properties replicated into the global catalog include a base set defined by Microsoft. Administrators can specify additional properties to meet the needs of their installation.

 

 