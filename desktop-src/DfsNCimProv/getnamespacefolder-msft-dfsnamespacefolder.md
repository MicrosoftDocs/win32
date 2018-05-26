---
title: GetNamespaceFolder method of the MSFT\_DfsNamespaceFolder class
description: Retrieves the properties of a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e953f4f7-81e6-4b82-bc53-120370284004
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNamespaceFolder method
- GetNamespaceFolder method, MSFT_DfsNamespaceFolder class
- MSFT_DfsNamespaceFolder class, GetNamespaceFolder method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolder.GetNamespaceFolder
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetNamespaceFolder method of the MSFT\_DfsNamespaceFolder class

Retrieves the properties of a DFS folder.

## Syntax


```mof
uint32 GetNamespaceFolder(
  [in]  string                  NamespacePath,
  [out] MSFT_DfsNamespaceFolder cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder that contains the properties to be retrieved. The UNC path has a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Get-DFSNamespaceFolder** cmdlet. This parameter is passed uninitialized.

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

 

 





