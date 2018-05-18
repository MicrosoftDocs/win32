---
title: RemoveNamespaceFolder method of the MSFT\_DfsNamespaceFolder class
description: Removes a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'cfd24f34-b6e4-403b-8020-26313cd50398'
ms.prod: 'windows-server-dev'
ms.technology:
- 'distributed-file-system-namespace'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoveNamespaceFolder method", "RemoveNamespaceFolder method, MSFT_DfsNamespaceFolder class", "MSFT_DfsNamespaceFolder class, RemoveNamespaceFolder method"]
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder.RemoveNamespaceFolder
api_location:
- DfsNCimProv.dll
api_type:
- COM
---

# RemoveNamespaceFolder method of the MSFT\_DfsNamespaceFolder class

Removes a DFS folder.

## Syntax


```mof
uint32 RemoveNamespaceFolder(
  [in] string NamespacePath
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder to delete. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

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

[**MSFT\_DfsNamespaceFolder**](msft-dfsnamespacefolder.md)
</dt> </dl>

 

 





