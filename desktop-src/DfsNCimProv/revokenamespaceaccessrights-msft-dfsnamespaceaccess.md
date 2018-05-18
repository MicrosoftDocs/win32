---
title: RevokeNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class
description: Revokes access permissions for a DFS folder from the specified users or groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'bb0b5efa-1f05-42ee-8121-70afff3fa3d6'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RevokeNamespaceAccessRights method", "RevokeNamespaceAccessRights method, MSFT_DfsNamespaceAccess class", "MSFT_DfsNamespaceAccess class, RevokeNamespaceAccessRights method"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceAccess.RevokeNamespaceAccessRights
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# RevokeNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class

Revokes access permissions for a DFS folder from the specified users or groups.

## Syntax


```mof
uint32 RevokeNamespaceAccessRights(
  [in]  string                  NamespacePath,
  [in]  uint32                  AccessType,
  [in]  string                  AccountName[],
  [out] MSFT_DfsNamespaceAccess cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder for which access is to be revoked. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*AccessType* \[in\]
</dt> <dd>

The type of access to be revoked for the users or groups on a DFS folder.

<dt>

<span id="enumerate"></span><span id="ENUMERATE"></span>

<span id="enumerate"></span><span id="ENUMERATE"></span>**enumerate** (0)


</dt> <dd>

The right to view and enumerate the contents of a DFS folder.

</dd> </dl> </dd> <dt>

*AccountName* \[in\]
</dt> <dd>

An array that contains the names of users or groups to be revoked access.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Revoke-DFSNamespaceAccess** cmdlet. This parameter is passed uninitialized.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsNamespaceAccess**](msft-dfsnamespaceaccess.md)
</dt> </dl>

 

 





