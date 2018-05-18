---
title: Value Lists for Storage Class Resources
description: The CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO and CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS control codes return value lists describing storage class resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '23e56e88-7a98-4c7c-aee9-9674b17e3635'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# Value Lists for Storage Class Resources

The [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md) and [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md) control codes return [value lists](value-lists.md) describing [*storage class resources*](s-gly.md#-wolf-storage-class-resource-gly).

A single storage class resource is described by a value list entry consisting of one or more [data structures](data-structures.md), as follows:

-   The value list entry must always begin with a **CLUSPROP\_SYNTAX\_DISK\_SIGNATURE** value containing a [**CLUSPROP\_DISK\_SIGNATURE**](clusprop-disk-signature.md) structure specifying the signature (for MBR-formatted storage class resources) or **CLUSPROP\_SYNTAX\_DISK\_GUID** value specifying the **GUID** (for GPT-formatted storage class resources.)
-   The value list entry may contain the following structures in any order:

    -   A **CLUSPROP\_SYNTAX\_SCSI\_ADDRESS** value containing a [**CLUSPROP\_SCSI\_ADDRESS**](clusprop-scsi-address.md) structure describing the [*SCSI*](s-gly.md#-wolf-small-computer-system-interface-gly) address of the storage class resource (if applicable).
    -   A **CLUSPROP\_SYNTAX\_DISK\_NUMBER** value containing a [**CLUSPROP\_DISK\_NUMBER**](clusprop-disk-number.md) structure specifying the disk number of the storage class resource (if applicable).
    -   A **CLUSPROP\_SYNTAX\_DISK\_SIZE** value containing a **ULARGE\_INTEGER** specifying the total size, in bytes, of the storage class resource.
    -   One or more **CLUSPROP\_SYNTAX\_PARTITION\_INFO** values, each containing a [**CLUSPROP\_PARTITION\_INFO**](clusprop-partition-info.md) structure for each drive letter or partition assigned to the storage class resource (if applicable).

The value list returned from [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO](clusctl-resource-storage-get-disk-info.md) describes information about a single storage class resource and thus contains only one of these entries terminated by a **CLUSPROP\_SYNTAX\_ENDMARK** value.

The value list returned from [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS](clusctl-resource-type-storage-get-available-disks.md) describes information about a multiple storage class resources as a series of such entries, with the entire series terminated by a **CLUSPROP\_SYNTAX\_ENDMARK** value. Each [**CLUSPROP\_DISK\_SIGNATURE**](clusprop-disk-signature.md) structure marks the start of a new entry and identifies the storage class resource described by the entry. Thus the **CLUSPROP\_DISK\_SIGNATURE** structure acts like an index or key when the list is parsed.

 

 




