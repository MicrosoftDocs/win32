---
title: GrantNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class
description: Grants access permissions for a DFS folder to the specified users or groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '99680f5f-28a7-4abb-bf21-6cd10ad91c2a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GrantNamespaceAccessRights method", "GrantNamespaceAccessRights method, MSFT_DfsNamespaceAccess class", "MSFT_DfsNamespaceAccess class, GrantNamespaceAccessRights method"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceAccess.GrantNamespaceAccessRights
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# GrantNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class

Grants access permissions for a DFS folder to the specified users or groups.

## Syntax


```mof
uint32 GrantNamespaceAccessRights(
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

The Universal Naming Convention (UNC) path of the DFS folder for which access is to be granted. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*AccessType* \[in\]
</dt> <dd>

The type of access to be granted for the users or groups on a DFS folder.

<dt>

<span id="enumerate"></span><span id="ENUMERATE"></span>

<span id="enumerate"></span><span id="ENUMERATE"></span>**enumerate** (0)


</dt> <dd>

The right to view and enumerate the contents of a DFS folder.

</dd> </dl> </dd> <dt>

*AccountName* \[in\]
</dt> <dd>

An array that contains the names of users or groups to be granted access.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Grant-DFSNamespaceAccess** cmdlet. This parameter is passed uninitialized.

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

 

 





