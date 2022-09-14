---
title: Indexed Attributes (AD DS)
description: Attributes may be indexed. Indexing an attribute can improve the performance of queries for that attribute.
ms.assetid: 20e10fc9-d767-4d82-9ed6-b9f384e77b12
ms.tgt_platform: multiple
keywords:
- Indexed Attributes AD
- Attributes AD , indexed
ms.topic: article
ms.date: 05/31/2018
---

# Indexed Attributes (AD DS)

Attributes may be indexed. Indexing an attribute can improve the performance of queries for that attribute.

An attributes is indexed when the [**searchFlags**](/windows/desktop/ADSchema/a-searchflags) attribute in the attribute's schema definition has the least significant bit set to 1. Setting the least significant bit of the **searchFlags** attribute schema definition to 1 will dynamically build an index. Setting the least significant bit of the **searchFlags** attribute schema definition to 0 will cause the index for the attribute to be removed. The index will be built automatically by a background thread on the domain controller.

Ideally, indexed attributes should be single valued with highly unique values evenly distributed across the set of instances. The less unique the values of an attribute are, the less effective the index will be.

Multi-valued attributes can also be indexed, but the cost to build the index for a multi-valued attribute is larger in terms of storage, update, and search time. The uniqueness requirement for a multi-valued property is the same as that for a single-valued property—the more unique the values are the more effective the index.

The more indexed attributes a class has, the more time is required to create new instances of the class.

Indexes apply to attributes, not to classes. That is, when an attribute is marked as indexed, all instances of the attribute are added to the index, not just the instances that are members of a particular class.

To verify that a server is using an index to process a query, set the following registry value on a domain controller to 4. Then perform a query on that domain controller and look in the directory event log for data about the indexes, if any, used to process the query.

```
HKEY_LOCAL_MACHINE
   SYSTEM
      Current Control Set
         Services
            NTDS
               Diagnostics
                  9 Internal Processing
```

For more information about other bits in the [**searchFlags**](/windows/desktop/ADSchema/a-searchflags) property, see [Characteristics of Attributes](characteristics-of-attributes.md).

 

 