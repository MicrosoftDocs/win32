---
title: What's New in DFS in Windows Server 2008
description: Windows Server 2008 includes the following new and updated programming elements for the Distributed File System (DFS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '54948cdc-3b58-4bfd-b58a-b137668a4297'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-distributed-file-system-(dfs)'
ms.tgt_platform: multiple
keywords: ["Distributed File System Files , what's new in Windows Server 2008"]
---

# What's New in DFS in Windows Server 2008

Windows Server 2008 includes the following new and updated programming elements for the Distributed File System (DFS).

## New Enumerations

<dl> <dt>

<span id="DFS_NAMESPACE_VERSION_ORIGIN"></span><span id="dfs_namespace_version_origin"></span>[**DFS\_NAMESPACE\_VERSION\_ORIGIN**](dfs-namespace-version-origin.md)
</dt> <dd>

Identifies the origin of DFS namespace version information.

</dd> </dl>

## New Functions

<dl> <dt>

<span id="NetDfsAddRootTarget"></span><span id="netdfsaddroottarget"></span><span id="NETDFSADDROOTTARGET"></span>[**NetDfsAddRootTarget**](netdfsaddroottarget.md)
</dt> <dd>

Creates a domain-based or stand-alone DFS namespace. If the namespace already exists, the function adds the specified root target to it.

</dd> <dt>

<span id="NetDfsGetSupportedNamespaceVersion"></span><span id="netdfsgetsupportednamespaceversion"></span><span id="NETDFSGETSUPPORTEDNAMESPACEVERSION"></span>[**NetDfsGetSupportedNamespaceVersion**](netdfsgetsupportednamespaceversion.md)
</dt> <dd>

Determines the version of the DFS namespace that can be created for a server or Active Directory Domain Services (AD DS) domain by using the [**NetDfsAddRootTarget**](netdfsaddroottarget.md) function.

</dd> <dt>

<span id="NetDfsRemoveRootTarget"></span><span id="netdfsremoveroottarget"></span><span id="NETDFSREMOVEROOTTARGET"></span>[**NetDfsRemoveRootTarget**](netdfsremoveroottarget.md)
</dt> <dd>

Removes a DFS root target from a domain-based DFS namespace. If the root target is the last root target in the DFS namespace, this function removes the DFS namespace. This function can also be used to remove a stand-alone DFS namespace.

</dd> </dl>

## New Structures

<dl> <dt>

<span id="DFS_INFO_8"></span><span id="dfs_info_8"></span>[**DFS\_INFO\_8**](dfs-info-8.md)
</dt> <dd>

Contains the name, status, GUID, time-out, property flags, metadata size, DFS target information, and link reparse point security descriptor for a root or link.

</dd> <dt>

<span id="DFS_INFO_9"></span><span id="dfs_info_9"></span>[**DFS\_INFO\_9**](dfs-info-9.md)
</dt> <dd>

Contains the name, status, GUID, time-out, property flags, metadata size, DFS target information, link reparse point security descriptor, and a list of DFS targets for a root or link.

</dd> <dt>

<span id="DFS_INFO_50"></span><span id="dfs_info_50"></span>[**DFS\_INFO\_50**](dfs-info-50.md)
</dt> <dd>

Contains the DFS metadata version and capabilities of an existing DFS namespace.

</dd> <dt>

<span id="DFS_INFO_107"></span><span id="dfs_info_107"></span>[**DFS\_INFO\_107**](dfs-info-107.md)
</dt> <dd>

Contains information about a DFS root or link, including the comment, state, time-out, property flags, and the link reparse point security descriptor.

</dd> <dt>

<span id="DFS_INFO_150"></span><span id="dfs_info_150"></span>[**DFS\_INFO\_150**](dfs-info-150.md)
</dt> <dd>

Contains the security descriptor for a DFS link's reparse point.

</dd> <dt>

<span id="DFS_SUPPORTED_NAMESPACE_VERSION_INFO"></span><span id="dfs_supported_namespace_version_info"></span>[**DFS\_SUPPORTED\_NAMESPACE\_VERSION\_INFO**](dfs-supported-namespace-version-info.md)
</dt> <dd>

Contains version information for a DFS namespace.

</dd> </dl>

 

 




