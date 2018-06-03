---
title: GetNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class
description: Retrieves access permissions for the specified DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b60e3bd6-67ce-4de4-9041-11699fc400c6
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNamespaceAccessRights method
- GetNamespaceAccessRights method, MSFT_DfsNamespaceAccess class
- MSFT_DfsNamespaceAccess class, GetNamespaceAccessRights method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceAccess.GetNamespaceAccessRights
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetNamespaceAccessRights method of the MSFT\_DfsNamespaceAccess class

Retrieves access permissions for the specified DFS folder.

## Syntax


```mof
uint32 GetNamespaceAccessRights(
  [in]  string                  NamespacePath,
  [out] MSFT_DfsNamespaceAccess cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder for which to retrieve the currently granted access permissions are to be retrieved. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Get-DFSNamespaceAccess** cmdlet. This parameter is passed uninitialized.

</dd> </dl>

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\dfsn<br/>                                                  |
| MOF<br/>                      | <dl> <dt>DfsNCimProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DfsNCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DfsNamespaceAccess**](msft-dfsnamespaceaccess.md)
</dt> </dl>

 

 





