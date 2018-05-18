---
title: Distributed File System Structures
description: The following are the Distributed File System (DFS) structures
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f55ad3c0-0457-4d5a-a7d3-8eff744d573d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-distributed-file-system-(dfs)'
ms.tgt_platform: multiple
---

# Distributed File System Structures

The following are the Distributed File System (DFS) structures:

## In this section

<dl> <dt>

[**DFS\_GET\_PKT\_ENTRY\_STATE\_ARG**](dfs-get-pkt-entry-state-arg.md)
</dt> <dd>

Input buffer used with the [**FSCTL\_DFS\_GET\_PKT\_ENTRY\_STATE**](fsctl-dfs-get-pkt-entry-state.md) control code

</dd> <dt>

[**DFS\_INFO\_1**](dfs-info-1-str.md)
</dt> <dd>

Contains the name of a Distributed File System (DFS) root or link.

</dd> <dt>

[**DFS\_INFO\_2**](dfs-info-2-str.md)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, and number of DFS targets for the root or link.

</dd> <dt>

[**DFS\_INFO\_3**](dfs-info-3-str.md)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, number of DFS targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_4**](dfs-info-4-str.md)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, number of targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_5**](dfs-info-5.md)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, and number of targets for the root or link.

</dd> <dt>

[**DFS\_INFO\_6**](dfs-info-6.md)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, number of targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_7**](dfs-info-7.md)
</dt> <dd>

Contains information about a DFS namespace. This structure contains the version **GUID** for the metadata for the namespace.

</dd> <dt>

[**DFS\_INFO\_8**](dfs-info-8.md)
</dt> <dd>

Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, and link reparse point security descriptor for a root or link.

</dd> <dt>

[**DFS\_INFO\_9**](dfs-info-9.md)
</dt> <dd>

Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, link reparse point security descriptor, and a list of DFS targets for a root or link.

</dd> <dt>

[**DFS\_INFO\_50**](dfs-info-50.md)
</dt> <dd>

Contains the DFS metadata version and capabilities of an existing DFS namespace.

</dd> <dt>

[**DFS\_INFO\_100**](dfs-info-100-str.md)
</dt> <dd>

Contains a comment associated with a Distributed File System (DFS) root or link.

</dd> <dt>

[**DFS\_INFO\_101**](dfs-info-101-str.md)
</dt> <dd>

Describes the state of storage on a DFS root, link, root target, or link target.

</dd> <dt>

[**DFS\_INFO\_102**](dfs-info-102-str.md)
</dt> <dd>

Contains a time-out value to associate with a Distributed File System (DFS) root or a link in a named DFS root.

</dd> <dt>

[**DFS\_INFO\_103**](dfs-info-103.md)
</dt> <dd>

Contains properties that set specific behaviors for a DFS root or link.

</dd> <dt>

[**DFS\_INFO\_104**](dfs-info-104.md)
</dt> <dd>

Contains the priority of a DFS root target or link target.

</dd> <dt>

[**DFS\_INFO\_105**](dfs-info-105.md)
</dt> <dd>

Contains information about a DFS root or link, including comment, state, time-out, and DFS behaviors specified by property flags.

</dd> <dt>

[**DFS\_INFO\_106**](dfs-info-106.md)
</dt> <dd>

Contains the storage state and priority for a DFS root target or link target. This structure is only for use with the [**NetDfsSetInfo**](netdfssetinfo.md) function.

</dd> <dt>

[**DFS\_INFO\_107**](dfs-info-107.md)
</dt> <dd>

Contains information about a DFS root or link, including the comment, state, time-out, property flags, and link reparse point security descriptor.

</dd> <dt>

[**DFS\_INFO\_150**](dfs-info-150.md)
</dt> <dd>

Contains the security descriptor for a DFS link's reparse point.

</dd> <dt>

[**DFS\_INFO\_200**](dfs-info-200-str.md)
</dt> <dd>

Contains the name of a domain-based Distributed File System (DFS) namespace.

</dd> <dt>

[**DFS\_INFO\_300**](dfs-info-300-str.md)
</dt> <dd>

Contains the name and type (domain-based or stand-alone) of a DFS namespace.

</dd> <dt>

[**DFS\_STORAGE\_INFO**](dfs-storage-info.md)
</dt> <dd>

Contains information about a DFS root or link target in a DFS namespace or from the cache maintained by the DFS client.

</dd> <dt>

[**DFS\_STORAGE\_INFO\_1**](dfs-storage-info-1.md)
</dt> <dd>

Contains information about a DFS target, including the DFS target server name and share name as well as the target's state and priority.

</dd> <dt>

[**DFS\_SUPPORTED\_NAMESPACE\_VERSION\_INFO**](dfs-supported-namespace-version-info.md)
</dt> <dd>

Contains version information for a DFS namespace.

</dd> <dt>

[**DFS\_TARGET\_PRIORITY**](dfs-target-priority.md)
</dt> <dd>

Contains the priority class and rank of a specific DFS target.

</dd> </dl>

 

 




