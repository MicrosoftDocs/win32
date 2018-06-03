---
title: MoveNamespaceFolder method of the MSFT\_DfsNamespaceFolder class
description: Moves a DFS folder to another location within the same namespace.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 226c0dac-d424-4492-b5d3-85f661ccfb96
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MoveNamespaceFolder method
- MoveNamespaceFolder method, MSFT_DfsNamespaceFolder class
- MSFT_DfsNamespaceFolder class, MoveNamespaceFolder method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder.MoveNamespaceFolder
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MoveNamespaceFolder method of the MSFT\_DfsNamespaceFolder class

Moves a DFS folder to another location within the same namespace.

## Syntax


```mof
uint32 MoveNamespaceFolder(
  [in] string NamespacePath,
  [in] string NewNamespacePath
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder to move. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*NewNamespacePath* \[in\]
</dt> <dd>

The UNC path of another location in the namespace to move the DFS folder to.

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

[**MSFT\_DfsNamespaceFolder**](msft-dfsnamespacefolder.md)
</dt> </dl>

 

 





