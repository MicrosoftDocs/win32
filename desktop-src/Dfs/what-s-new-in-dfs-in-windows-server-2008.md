---
title: Whats New in DFS in Windows Server 2008
description: Windows Server 2008 includes the following new and updated programming elements for the Distributed File System (DFS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 54948cdc-3b58-4bfd-b58a-b137668a4297
ms.prod: windows-server-dev
ms.technology: windows-distributed-file-system-(dfs)
ms.tgt_platform: multiple
keywords:
- Distributed File System Files , whats new in Windows Server 2008
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# What's New in DFS in Windows Server 2008

Windows Server 2008 includes the following new and updated programming elements for the Distributed File System (DFS).

## New Enumerations

<dl> <dt>

<span id="DFS_NAMESPACE_VERSION_ORIGIN"></span><span id="dfs_namespace_version_origin"></span>[**DFS\_NAMESPACE\_VERSION\_ORIGIN**](/windows/previous-versions/LmDfs/ne-lmdfs-dfs_namespace_version_origin?branch=master)
</dt> <dd>

Identifies the origin of DFS namespace version information.

</dd> </dl>

## New Functions

<dl> <dt>

<span id="NetDfsAddRootTarget"></span><span id="netdfsaddroottarget"></span><span id="NETDFSADDROOTTARGET"></span>[**NetDfsAddRootTarget**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsaddroottarget?branch=master)
</dt> <dd>

Creates a domain-based or stand-alone DFS namespace. If the namespace already exists, the function adds the specified root target to it.

</dd> <dt>

<span id="NetDfsGetSupportedNamespaceVersion"></span><span id="netdfsgetsupportednamespaceversion"></span><span id="NETDFSGETSUPPORTEDNAMESPACEVERSION"></span>[**NetDfsGetSupportedNamespaceVersion**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetsupportednamespaceversion?branch=master)
</dt> <dd>

Determines the version of the DFS namespace that can be created for a server or Active Directory Domain Services (AD DS) domain by using the [**NetDfsAddRootTarget**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsaddroottarget?branch=master) function.

</dd> <dt>

<span id="NetDfsRemoveRootTarget"></span><span id="netdfsremoveroottarget"></span><span id="NETDFSREMOVEROOTTARGET"></span>[**NetDfsRemoveRootTarget**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremoveroottarget?branch=master)
</dt> <dd>

Removes a DFS root target from a domain-based DFS namespace. If the root target is the last root target in the DFS namespace, this function removes the DFS namespace. This function can also be used to remove a stand-alone DFS namespace.

</dd> </dl>

## New Structures

<dl> <dt>

<span id="DFS_INFO_8"></span><span id="dfs_info_8"></span>[**DFS\_INFO\_8**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_info_8?branch=master)
</dt> <dd>

Contains the name, status, GUID, time-out, property flags, metadata size, DFS target information, and link reparse point security descriptor for a root or link.

</dd> <dt>

<span id="DFS_INFO_9"></span><span id="dfs_info_9"></span>[**DFS\_INFO\_9**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_info_9?branch=master)
</dt> <dd>

Contains the name, status, GUID, time-out, property flags, metadata size, DFS target information, link reparse point security descriptor, and a list of DFS targets for a root or link.

</dd> <dt>

<span id="DFS_INFO_50"></span><span id="dfs_info_50"></span>[**DFS\_INFO\_50**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_info_50?branch=master)
</dt> <dd>

Contains the DFS metadata version and capabilities of an existing DFS namespace.

</dd> <dt>

<span id="DFS_INFO_107"></span><span id="dfs_info_107"></span>[**DFS\_INFO\_107**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_info_107?branch=master)
</dt> <dd>

Contains information about a DFS root or link, including the comment, state, time-out, property flags, and the link reparse point security descriptor.

</dd> <dt>

<span id="DFS_INFO_150"></span><span id="dfs_info_150"></span>[**DFS\_INFO\_150**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_info_150?branch=master)
</dt> <dd>

Contains the security descriptor for a DFS link's reparse point.

</dd> <dt>

<span id="DFS_SUPPORTED_NAMESPACE_VERSION_INFO"></span><span id="dfs_supported_namespace_version_info"></span>[**DFS\_SUPPORTED\_NAMESPACE\_VERSION\_INFO**](/windows/previous-versions/LmDfs/ns-lmdfs-_dfs_supported_namespace_version_info?branch=master)
</dt> <dd>

Contains version information for a DFS namespace.

</dd> </dl>

 

 




