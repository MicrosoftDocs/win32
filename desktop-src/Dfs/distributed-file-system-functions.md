---
title: Distributed File System Functions
description: The following are the Distributed File System (DFS) functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8f86b717-fe26-4550-8b71-8f7df5ca6022
ms.prod: windows-server-dev
ms.technology: windows-distributed-file-system-(dfs)
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Distributed File System Functions

The following are the Distributed File System (DFS) functions.

## In this section

<dl> <dt>

[**NetDfsAdd**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsadd)
</dt> <dd>

Creates a new Distributed File System (DFS) link or adds targets to an existing link in a DFS namespace.

</dd> <dt>

[**NetDfsAddFtRoot**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsaddftroot)
</dt> <dd>

Creates a new domain-based Distributed File System (DFS) namespace. If the namespace already exists, the function adds the specified root target to it.

</dd> <dt>

[**NetDfsAddRootTarget**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsaddroottarget)
</dt> <dd>

Creates a domain-based or stand-alone DFS namespace or adds a new root target to an existing domain-based namespace.

</dd> <dt>

[**NetDfsAddStdRoot**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsaddstdroot)
</dt> <dd>

Creates a new stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsEnum**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsenum)
</dt> <dd>

Enumerates the Distributed File System (DFS) namespaces hosted on a server or DFS links of a namespace hosted by a server.

</dd> <dt>

[**NetDfsGetClientInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetclientinfo)
</dt> <dd>

Retrieves information about a Distributed File System (DFS) root or link from the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsGetFtContainerSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetftcontainersecurity)
</dt> <dd>

Retrieves the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsGetInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetinfo)
</dt> <dd>

Retrieves information about a specified Distributed File System (DFS) root or link in a DFS namespace.

</dd> <dt>

[**NetDfsGetSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetsecurity)
</dt> <dd>

Retrieves the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsGetStdContainerSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetstdcontainersecurity)
</dt> <dd>

Retrieves the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> <dt>

[**NetDfsGetSupportedNamespaceVersion**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsgetsupportednamespaceversion)
</dt> <dd>

Determines the supported metadata version number.

</dd> <dt>

[**NetDfsMove**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsmove)
</dt> <dd>

Renames or moves a DFS link.

</dd> <dt>

[**NetDfsRemove**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremove)
</dt> <dd>

Removes a Distributed File System (DFS) link or a specific link target of a DFS link in a DFS namespace. When removing a specific link target, the link itself is removed if the last link target of the link is removed.

</dd> <dt>

[**NetDfsRemoveFtRoot**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremoveftroot)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

</dd> <dt>

[**NetDfsRemoveFtRootForced**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremoveftrootforced)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace, even if the root target server is offline. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

> [!Note]  
> The [**NetDfsRemoveFtRootForced**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremoveftrootforced) function does not update the registry on the DFS root target server. For more information, see the Remarks section.

 

</dd> <dt>

[**NetDfsRemoveRootTarget**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremoveroottarget)
</dt> <dd>

Removes a DFS root target from a domain-based DFS namespace. If the root target is the last root target in the DFS namespace, this function removes the DFS namespace. This function can also be used to remove a stand-alone DFS namespace.

</dd> <dt>

[**NetDfsRemoveStdRoot**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfsremovestdroot)
</dt> <dd>

Deletes a stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsSetClientInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetclientinfo)
</dt> <dd>

Modifies information about a Distributed File System (DFS) root or link in the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsSetFtContainerSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetftcontainersecurity)
</dt> <dd>

Sets the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsSetInfo**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetinfo)
</dt> <dd>

Sets or modifies information about a specific Distributed File System (DFS) root, root target, link, or link target.

</dd> <dt>

[**NetDfsSetSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetsecurity)
</dt> <dd>

Sets the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsSetStdContainerSecurity**](/previous-versions/windows/desktop/api/LmDfs/nf-lmdfs-netdfssetstdcontainersecurity)
</dt> <dd>

Sets the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> </dl>

Note that an application invoking any of the functions may indirectly cause the local DFS Namespace server servicing the function call to perform a full synchronization of the related namespace metadata from the PDC emulator master for that domain. This full synchronization could happen even when root scalability mode is configured for that namespace.

 

 




