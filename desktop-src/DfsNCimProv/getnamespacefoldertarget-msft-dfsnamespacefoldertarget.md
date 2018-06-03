---
title: GetNamespaceFolderTarget method of the MSFT\_DfsNamespaceFolderTarget class
description: Retrieves the properties of the target of a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f3f3291-ffc8-486f-83a6-5ace7d2c83de
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetNamespaceFolderTarget method
- GetNamespaceFolderTarget method, MSFT_DfsNamespaceFolderTarget class
- MSFT_DfsNamespaceFolderTarget class, GetNamespaceFolderTarget method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolderTarget.GetNamespaceFolderTarget
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetNamespaceFolderTarget method of the MSFT\_DfsNamespaceFolderTarget class

Retrieves the properties of the target of a DFS folder. If no target is specified, the properties of all targets of a DFS folder are retrieved.

## Syntax


```mof
uint32 GetNamespaceFolderTarget(
  [in]  string                        NamespacePath,
  [in]  string                        TargetPath,
  [out] MSFT_DfsNamespaceFolderTarget cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder that has a target with properties to be retrieved.

</dd> <dt>

*TargetPath* \[in\]
</dt> <dd>

The UNC path of the target of a DFS folder. If this parameter is empty, the method retrieves the properties of all folder targets for the specified DFS folder.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, contains an array that represents output from the **Get-DFSNamespaceFolderTarget** cmdlet. This parameter is passed uninitialized.

</dd> </dl>

## Remarks

The *NamespacePath* and *TargetPath* parameters have a format of \\\\HostName\\SharedName\[\\ObjectName\]\*, where:

-   The HostName component represents either the host name of a server or the domain name of a domain that hosts resources.
-   The SharedName component represents the share name or the name of the resource that is being accessed.
-   Each ObjectName component represents the name of a directory on the resource that is being accessed.

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

[**MSFT\_DfsNamespaceFolderTarget**](msft-dfsnamespacefoldertarget.md)
</dt> </dl>

 

 





