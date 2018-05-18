---
title: Implementing Instance Management
description: Requirements for managing resource instances using the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '477485af-d593-4ccf-bca5-4ecc83df423e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["resource DLLS Failover Cluster ,implementing resource instance management"]
---

# Implementing Instance Management

You can create any system for managing instances in your [resource DLL](resource-dlls.md) as long as you meet the following requirements.

-   Each instance is assigned a unique [resource identifier](resource-identifiers.md).
-   The resource identifier is associated with the required [instance data](instance-data.md).
-   When the [Cluster service](cluster-service.md) passes a resource identifier to an entry point function, the resource DLL can use the identifier to locate the correct instance and its associated data.

The Cluster Resource Wizard automatically generates code that meets these requirements. In the implementation of [**Open**](open.md) created by the Cluster Resource Wizard, a new [resource structure](resource-structures.md) is allocated for each new instance. The address of this structure becomes the resource identifier. The resource identifier is stored as the first member of the resource structure. This is used for validation as well as for identification. The address of the structure points to the first member of the structure, whose value is also the address of the structure. Thus the resource identifier acts as an index into the "table" of resource structures maintained by the DLL.

## Example

See [Resource DLL Examples](https://msdn.microsoft.com/library/aa370474).

 

 




