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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Distributed File System Functions

The following are the Distributed File System (DFS) functions.

## In this section

<dl> <dt>

[**NetDfsAdd**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsadd?branch=master)
</dt> <dd>

Creates a new Distributed File System (DFS) link or adds targets to an existing link in a DFS namespace.

</dd> <dt>

[**NetDfsAddFtRoot**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsaddftroot?branch=master)
</dt> <dd>

Creates a new domain-based Distributed File System (DFS) namespace. If the namespace already exists, the function adds the specified root target to it.

</dd> <dt>

[**NetDfsAddRootTarget**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsaddroottarget?branch=master)
</dt> <dd>

Creates a domain-based or stand-alone DFS namespace or adds a new root target to an existing domain-based namespace.

</dd> <dt>

[**NetDfsAddStdRoot**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsaddstdroot?branch=master)
</dt> <dd>

Creates a new stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsEnum**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsenum?branch=master)
</dt> <dd>

Enumerates the Distributed File System (DFS) namespaces hosted on a server or DFS links of a namespace hosted by a server.

</dd> <dt>

[**NetDfsGetClientInfo**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetclientinfo?branch=master)
</dt> <dd>

Retrieves information about a Distributed File System (DFS) root or link from the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsGetFtContainerSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetftcontainersecurity?branch=master)
</dt> <dd>

Retrieves the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsGetInfo**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetinfo?branch=master)
</dt> <dd>

Retrieves information about a specified Distributed File System (DFS) root or link in a DFS namespace.

</dd> <dt>

[**NetDfsGetSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetsecurity?branch=master)
</dt> <dd>

Retrieves the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsGetStdContainerSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetstdcontainersecurity?branch=master)
</dt> <dd>

Retrieves the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> <dt>

[**NetDfsGetSupportedNamespaceVersion**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsgetsupportednamespaceversion?branch=master)
</dt> <dd>

Determines the supported metadata version number.

</dd> <dt>

[**NetDfsMove**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsmove?branch=master)
</dt> <dd>

Renames or moves a DFS link.

</dd> <dt>

[**NetDfsRemove**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremove?branch=master)
</dt> <dd>

Removes a Distributed File System (DFS) link or a specific link target of a DFS link in a DFS namespace. When removing a specific link target, the link itself is removed if the last link target of the link is removed.

</dd> <dt>

[**NetDfsRemoveFtRoot**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremoveftroot?branch=master)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

</dd> <dt>

[**NetDfsRemoveFtRootForced**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremoveftrootforced?branch=master)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace, even if the root target server is offline. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

> [!Note]  
> The [**NetDfsRemoveFtRootForced**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremoveftrootforced?branch=master) function does not update the registry on the DFS root target server. For more information, see the Remarks section.

 

</dd> <dt>

[**NetDfsRemoveRootTarget**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremoveroottarget?branch=master)
</dt> <dd>

Removes a DFS root target from a domain-based DFS namespace. If the root target is the last root target in the DFS namespace, this function removes the DFS namespace. This function can also be used to remove a stand-alone DFS namespace.

</dd> <dt>

[**NetDfsRemoveStdRoot**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfsremovestdroot?branch=master)
</dt> <dd>

Deletes a stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsSetClientInfo**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfssetclientinfo?branch=master)
</dt> <dd>

Modifies information about a Distributed File System (DFS) root or link in the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsSetFtContainerSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfssetftcontainersecurity?branch=master)
</dt> <dd>

Sets the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsSetInfo**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfssetinfo?branch=master)
</dt> <dd>

Sets or modifies information about a specific Distributed File System (DFS) root, root target, link, or link target.

</dd> <dt>

[**NetDfsSetSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfssetsecurity?branch=master)
</dt> <dd>

Sets the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsSetStdContainerSecurity**](/windows/previous-versions/LmDfs/nf-lmdfs-netdfssetstdcontainersecurity?branch=master)
</dt> <dd>

Sets the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> </dl>

Note that an application invoking any of the functions may indirectly cause the local DFS Namespace server servicing the function call to perform a full synchronization of the related namespace metadata from the PDC emulator master for that domain. This full synchronization could happen even when root scalability mode is configured for that namespace.

 

 




