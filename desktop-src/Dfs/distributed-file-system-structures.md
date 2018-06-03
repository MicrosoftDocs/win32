---
title: Distributed File System Structures
description: The following are the Distributed File System (DFS) structures
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f55ad3c0-0457-4d5a-a7d3-8eff744d573d
ms.prod: windows-server-dev
ms.technology: windows-distributed-file-system-(dfs)
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System Structures

The following are the Distributed File System (DFS) structures:

## In this section

<dl> <dt>

[**DFS\_GET\_PKT\_ENTRY\_STATE\_ARG**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-dfs_get_pkt_entry_state_arg)
</dt> <dd>

Input buffer used with the [**FSCTL\_DFS\_GET\_PKT\_ENTRY\_STATE**](/previous-versions/windows/desktop/api/LmDfs/) control code

</dd> <dt>

[**DFS\_INFO\_1**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_1)
</dt> <dd>

Contains the name of a Distributed File System (DFS) root or link.

</dd> <dt>

[**DFS\_INFO\_2**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_2)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, and number of DFS targets for the root or link.

</dd> <dt>

[**DFS\_INFO\_3**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_3)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, number of DFS targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_4**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_4)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, number of targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_5**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_5)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, and number of targets for the root or link.

</dd> <dt>

[**DFS\_INFO\_6**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_6)
</dt> <dd>

Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, number of targets, and information about each target of the root or link.

</dd> <dt>

[**DFS\_INFO\_7**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_7)
</dt> <dd>

Contains information about a DFS namespace. This structure contains the version **GUID** for the metadata for the namespace.

</dd> <dt>

[**DFS\_INFO\_8**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_8)
</dt> <dd>

Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, and link reparse point security descriptor for a root or link.

</dd> <dt>

[**DFS\_INFO\_9**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_9)
</dt> <dd>

Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, link reparse point security descriptor, and a list of DFS targets for a root or link.

</dd> <dt>

[**DFS\_INFO\_50**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_50)
</dt> <dd>

Contains the DFS metadata version and capabilities of an existing DFS namespace.

</dd> <dt>

[**DFS\_INFO\_100**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_100)
</dt> <dd>

Contains a comment associated with a Distributed File System (DFS) root or link.

</dd> <dt>

[**DFS\_INFO\_101**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_101)
</dt> <dd>

Describes the state of storage on a DFS root, link, root target, or link target.

</dd> <dt>

[**DFS\_INFO\_102**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_102)
</dt> <dd>

Contains a time-out value to associate with a Distributed File System (DFS) root or a link in a named DFS root.

</dd> <dt>

[**DFS\_INFO\_103**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_103)
</dt> <dd>

Contains properties that set specific behaviors for a DFS root or link.

</dd> <dt>

[**DFS\_INFO\_104**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_104)
</dt> <dd>

Contains the priority of a DFS root target or link target.

</dd> <dt>

[**DFS\_INFO\_105**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_105)
</dt> <dd>

Contains information about a DFS root or link, including comment, state, time-out, and DFS behaviors specified by property flags.

</dd> <dt>

[**DFS\_INFO\_106**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_106)
</dt> <dd>

Contains the storage state and priority for a DFS root target or link target. This structure is only for use with the [**NetDfsSetInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetinfo) function.

</dd> <dt>

[**DFS\_INFO\_107**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_107)
</dt> <dd>

Contains information about a DFS root or link, including the comment, state, time-out, property flags, and link reparse point security descriptor.

</dd> <dt>

[**DFS\_INFO\_150**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_150)
</dt> <dd>

Contains the security descriptor for a DFS link's reparse point.

</dd> <dt>

[**DFS\_INFO\_200**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_200)
</dt> <dd>

Contains the name of a domain-based Distributed File System (DFS) namespace.

</dd> <dt>

[**DFS\_INFO\_300**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_info_300)
</dt> <dd>

Contains the name and type (domain-based or stand-alone) of a DFS namespace.

</dd> <dt>

[**DFS\_STORAGE\_INFO**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_storage_info)
</dt> <dd>

Contains information about a DFS root or link target in a DFS namespace or from the cache maintained by the DFS client.

</dd> <dt>

[**DFS\_STORAGE\_INFO\_1**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_storage_info_1)
</dt> <dd>

Contains information about a DFS target, including the DFS target server name and share name as well as the target's state and priority.

</dd> <dt>

[**DFS\_SUPPORTED\_NAMESPACE\_VERSION\_INFO**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_supported_namespace_version_info)
</dt> <dd>

Contains version information for a DFS namespace.

</dd> <dt>

[**DFS\_TARGET\_PRIORITY**](/previous-versions/windows/desktop/api/LmDfs/ns-lmdfs-_dfs_target_priority)
</dt> <dd>

Contains the priority class and rank of a specific DFS target.

</dd> </dl>

 

 




