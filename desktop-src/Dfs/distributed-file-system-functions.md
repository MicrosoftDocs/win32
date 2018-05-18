---
title: Distributed File System Functions
description: The following are the Distributed File System (DFS) functions.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8f86b717-fe26-4550-8b71-8f7df5ca6022'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-distributed-file-system-(dfs)'
ms.tgt_platform: multiple
---

# Distributed File System Functions

The following are the Distributed File System (DFS) functions.

## In this section

<dl> <dt>

[**NetDfsAdd**](netdfsadd.md)
</dt> <dd>

Creates a new Distributed File System (DFS) link or adds targets to an existing link in a DFS namespace.

</dd> <dt>

[**NetDfsAddFtRoot**](netdfsaddftroot.md)
</dt> <dd>

Creates a new domain-based Distributed File System (DFS) namespace. If the namespace already exists, the function adds the specified root target to it.

</dd> <dt>

[**NetDfsAddRootTarget**](netdfsaddroottarget.md)
</dt> <dd>

Creates a domain-based or stand-alone DFS namespace or adds a new root target to an existing domain-based namespace.

</dd> <dt>

[**NetDfsAddStdRoot**](netdfsaddstdroot.md)
</dt> <dd>

Creates a new stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsEnum**](netdfsenum.md)
</dt> <dd>

Enumerates the Distributed File System (DFS) namespaces hosted on a server or DFS links of a namespace hosted by a server.

</dd> <dt>

[**NetDfsGetClientInfo**](netdfsgetclientinfo.md)
</dt> <dd>

Retrieves information about a Distributed File System (DFS) root or link from the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsGetFtContainerSecurity**](netdfsgetftcontainersecurity.md)
</dt> <dd>

Retrieves the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsGetInfo**](netdfsgetinfo.md)
</dt> <dd>

Retrieves information about a specified Distributed File System (DFS) root or link in a DFS namespace.

</dd> <dt>

[**NetDfsGetSecurity**](netdfsgetsecurity.md)
</dt> <dd>

Retrieves the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsGetStdContainerSecurity**](netdfsgetstdcontainersecurity.md)
</dt> <dd>

Retrieves the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> <dt>

[**NetDfsGetSupportedNamespaceVersion**](netdfsgetsupportednamespaceversion.md)
</dt> <dd>

Determines the supported metadata version number.

</dd> <dt>

[**NetDfsMove**](netdfsmove.md)
</dt> <dd>

Renames or moves a DFS link.

</dd> <dt>

[**NetDfsRemove**](netdfsremove.md)
</dt> <dd>

Removes a Distributed File System (DFS) link or a specific link target of a DFS link in a DFS namespace. When removing a specific link target, the link itself is removed if the last link target of the link is removed.

</dd> <dt>

[**NetDfsRemoveFtRoot**](netdfsremoveftroot.md)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

</dd> <dt>

[**NetDfsRemoveFtRootForced**](netdfsremoveftrootforced.md)
</dt> <dd>

Removes the specified root target from a domain-based Distributed File System (DFS) namespace, even if the root target server is offline. If the last root target of the DFS namespace is being removed, the function also deletes the DFS namespace. A DFS namespace can be deleted without first deleting all the links in it.

> [!Note]  
> The [**NetDfsRemoveFtRootForced**](netdfsremoveftrootforced.md) function does not update the registry on the DFS root target server. For more information, see the Remarks section.

 

</dd> <dt>

[**NetDfsRemoveRootTarget**](netdfsremoveroottarget.md)
</dt> <dd>

Removes a DFS root target from a domain-based DFS namespace. If the root target is the last root target in the DFS namespace, this function removes the DFS namespace. This function can also be used to remove a stand-alone DFS namespace.

</dd> <dt>

[**NetDfsRemoveStdRoot**](netdfsremovestdroot.md)
</dt> <dd>

Deletes a stand-alone Distributed File System (DFS) namespace.

</dd> <dt>

[**NetDfsSetClientInfo**](netdfssetclientinfo.md)
</dt> <dd>

Modifies information about a Distributed File System (DFS) root or link in the cache maintained by the DFS client.

</dd> <dt>

[**NetDfsSetFtContainerSecurity**](netdfssetftcontainersecurity.md)
</dt> <dd>

Sets the security descriptor of the container object for the domain-based DFS namespaces in the specified Active Directory domain.

</dd> <dt>

[**NetDfsSetInfo**](netdfssetinfo.md)
</dt> <dd>

Sets or modifies information about a specific Distributed File System (DFS) root, root target, link, or link target.

</dd> <dt>

[**NetDfsSetSecurity**](netdfssetsecurity.md)
</dt> <dd>

Sets the security descriptor for the root object of the specified DFS namespace.

</dd> <dt>

[**NetDfsSetStdContainerSecurity**](netdfssetstdcontainersecurity.md)
</dt> <dd>

Sets the security descriptor for the container object of the specified stand-alone DFS namespace.

</dd> </dl>

Note that an application invoking any of the functions may indirectly cause the local DFS Namespace server servicing the function call to perform a full synchronization of the related namespace metadata from the PDC emulator master for that domain. This full synchronization could happen even when root scalability mode is configured for that namespace.

 

 




