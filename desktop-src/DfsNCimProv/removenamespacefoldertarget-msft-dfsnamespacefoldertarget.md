---
title: RemoveNamespaceFolderTarget method of the MSFT\_DfsNamespaceFolderTarget class
description: Removes a target of a DFS folder.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 85a7664e-e913-40b8-b968-a71d05893543
ms.prod: windows-server-dev
ms.technology:
- distributed-file-system-namespace
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveNamespaceFolderTarget method
- RemoveNamespaceFolderTarget method, MSFT_DfsNamespaceFolderTarget class
- MSFT_DfsNamespaceFolderTarget class, RemoveNamespaceFolderTarget method
topic_type:
- apiref
api_name:
- MSFT_DfsNamespaceFolderTarget.RemoveNamespaceFolderTarget
api_location:
- DfsNCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveNamespaceFolderTarget method of the MSFT\_DfsNamespaceFolderTarget class

Removes a target of a DFS folder. If the target being removed is the last target of the DFS folder, the user is notified.

## Syntax


```mof
uint32 RemoveNamespaceFolderTarget(
  [in] string NamespacePath,
  [in] string TargetPath
);
```



## Parameters

<dl> <dt>

*NamespacePath* \[in\]
</dt> <dd>

The Universal Naming Convention (UNC) path of the DFS folder that has a target to be removed.

</dd> <dt>

*TargetPath* \[in\]
</dt> <dd>

The UNC path of the target of a DFS folder.

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

 

 





