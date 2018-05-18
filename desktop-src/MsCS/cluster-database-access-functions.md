---
title: Cluster Database Access Functions
description: The cluster database access functions are called by Resource DLLs to create and initialize private properties and perform other configuration tasks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e2b2e01b-b2b9-4f4d-b43b-020a884e01bb'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["cluster database Failover Cluster ,access functions", "resource DLL functions Failover Cluster ,cluster database access functions"]
---

# Cluster Database Access Functions

The [cluster database](cluster-database.md) access functions are called by [Resource DLLs](resource-dlls.md) to create and initialize private properties and perform other configuration tasks.

> [!Note]  
> These functions should primarily be used by resource DLLs, so [*Cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) should avoid these functions whenever possible. For more information, see [standard order of preference](standard-order-of-preference.md).

 

## In this section

<dl> <dt>

[Cluster Registry Access Functions](cluster-registry-access-functions.md)
</dt> <dd>

Cluster registry access functions are called by [Resource DLLs](resource-dlls.md) to directly access and update keys in the [cluster database](cluster-database.md).

</dd> <dt>

[Property Access Utility Functions](property-access-utility-functions.md)
</dt> <dd>

The property access utility functions are called by [resource DLLs](resource-dlls.md) to directly access the [cluster database](cluster-database.md) and move property data between [property lists](property-lists.md), [parameter blocks](parameter-blocks.md), and [property tables](property-tables.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Functions](failover-cluster-functions.md)
</dt> <dt>

[Creating Resource Types](creating-resource-types.md)
</dt> </dl>

 

 




