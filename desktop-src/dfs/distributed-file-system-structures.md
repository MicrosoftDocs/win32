---
description: The following are the Distributed File System DFS structures
ms.assetid: f55ad3c0-0457-4d5a-a7d3-8eff744d573d
title: Distributed File System Structures
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System Structures

The following are the Distributed File System (DFS) structures:

## In this section

<dl> <dt>

[**DFS_GET_PKT_ENTRY_STATE_ARG**](/windows/win32/api/lmdfs/ns-lmdfs-dfs_get_pkt_entry_state_arg)
</dt> <dd>

Input buffer used with the [**FSCTL_DFS_GET_PKT_ENTRY_STATE**](fsctl-dfs-get-pkt-entry-state.md) control code
</dd> <dt>

[_DFS_INFO_1 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_1)
</dt> <dd>
Contains the name of a Distributed File System (DFS) root or link.

</dd> <dt>

[_DFS_INFO_2 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_2)
</dt> <dd>
Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, and number of DFS targets for the root or link.

</dd> <dt>

[_DFS_INFO_3 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_3)
</dt> <dd>
Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, number of DFS targets, and information about each target of the root or link.

</dd> <dt>

[_DFS_INFO_4 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_4)
</dt> <dd>
Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, number of targets, and information about each target of the root or link.

</dd> <dt>

[_DFS_INFO_5 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_5)
</dt> <dd>
Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, and number of targets for the root or link.

</dd> <dt>

[_DFS_INFO_6 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_6)
</dt> <dd>
Contains information about a Distributed File System (DFS) root or link. This structure contains the name, status, **GUID**, time-out, namespace/root/link properties, metadata size, number of targets, and information about each target of the root or link.

</dd> <dt>

[_DFS_INFO_7 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_7)
</dt> <dd>
Contains information about a DFS namespace. This structure contains the version **GUID** for the metadata for the namespace.

</dd> <dt>

[_DFS_INFO_8 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_8)
</dt> <dd>
Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, and link reparse point security descriptor for a root or link.

</dd> <dt>

[_DFS_INFO_9 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_9)
</dt> <dd>
Contains the name, status, **GUID**, time-out, property flags, metadata size, DFS target information, link reparse point security descriptor, and a list of DFS targets for a root or link.

</dd> <dt>

[_DFS_INFO_50 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_50)
</dt> <dd>
Contains the DFS metadata version and capabilities of an existing DFS namespace.

</dd> <dt>

[_DFS_INFO_100 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_100)
</dt> <dd>
Contains a comment associated with a Distributed File System (DFS) root or link.

</dd> <dt>

[_DFS_INFO_101 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_101)
</dt> <dd>
Describes the state of storage on a DFS root, link, root target, or link target.

</dd> <dt>

[_DFS_INFO_102 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_102)
</dt> <dd>
Contains a time-out value to associate with a Distributed File System (DFS) root or a link in a named DFS root.

</dd> <dt>

[_DFS_INFO_103 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_103)
</dt> <dd>
Contains properties that set specific behaviors for a DFS root or link.

</dd> <dt>

[_DFS_INFO_104 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_104)
</dt> <dd>
Contains the priority of a DFS root target or link target.

</dd> <dt>

[_DFS_INFO_105 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_105)
</dt> <dd>
Contains information about a DFS root or link, including comment, state, time-out, and DFS behaviors specified by property flags.

</dd> <dt>

[_DFS_INFO_106 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_106)
</dt> <dd>
Contains the storage state and priority for a DFS root target or link target. This structure is only for use with the [**NetDfsSetInfo**](netdfssetinfo.md) function.

</dd> <dt>

[_DFS_INFO_107 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_107)
</dt> <dd>
Contains information about a DFS root or link, including the comment, state, time-out, property flags, and link reparse point security descriptor.

</dd> <dt>

[_DFS_INFO_150 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_150)
</dt> <dd>
Contains the security descriptor for a DFS link's reparse point.

</dd> <dt>

[_DFS_INFO_200 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_200)
</dt> <dd>
Contains the name of a domain-based Distributed File System (DFS) namespace.

</dd> <dt>

[_DFS_INFO_300 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_info_300)
</dt> <dd>
Contains the name and type (domain-based or stand-alone) of a DFS namespace.

</dd> <dt>

[_DFS_STORAGE_INFO structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_storage_info)
</dt> <dd>
Contains information about a DFS root or link target in a DFS namespace or from the cache maintained by the DFS client.

</dd> <dt>

[_DFS_STORAGE_INFO_1 structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_storage_info_1)
</dt> <dd>
Contains information about a DFS target, including the DFS target server name and share name as well as the target's state and priority.

</dd> <dt>

[_DFS_SUPPORTED_NAMESPACE_VERSION_INFO structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_supported_namespace_version_info)
</dt> <dd>
Contains version information for a DFS namespace.

</dd> <dt>

[_DFS_TARGET_PRIORITY structure](/windows/desktop/api/lmdfs/ns-lmdfs-dfs_target_priority)
</dt> <dd>
Contains the priority class and rank of a specific DFS target.

</dd> </dl>
