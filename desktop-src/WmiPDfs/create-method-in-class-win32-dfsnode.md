---
title: Create method of the Win32\_DFSNode class
description: The Create method creates a new instance of the Win32\_DFSNode class. This instance can represent the root of a new Distributed file system (DFS) structure or a connection to one or more shared folders or targets.
audience: developer
author: REDMOND\\martinek
manager: REDMOND\\martinek
ms.assetid: d6338d53-5ca1-4907-8aa7-d0894d7d9913
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Create method
- Create method, Win32_DFSNode class
- Win32_DFSNode class, Create method
topic_type:
- apiref
api_name:
- Win32_DFSNode.Create
api_location:
- Wmipdfs.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Create method of the Win32\_DFSNode class

The **Create** method creates a new instance of the [**Win32\_DFSNode**](win32-dfsnode.md) class. This instance can represent the root of a new Distributed file system (DFS) structure or a connection to one or more shared folders or targets.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Create(
  [in]           string DFSEntryPath,
  [in]           string ServerName,
  [in]           string Sharename,
  [in, optional] string Description
);
```



## Parameters

<dl> <dt>

*DFSEntryPath* \[in\]
</dt> <dd>

Path of the DFS root.

</dd> <dt>

*ServerName* \[in\]
</dt> <dd>

Name of the server that hosts the share to which the node is associated. For example, to create a link associated to a share \\"\\\\\\\\myserver\\myshare\\", the parameter should be set to \\"\\\\\\\\myserver\\".

</dd> <dt>

*Sharename* \[in\]
</dt> <dd>

Name of the share to which the node is associated. For example, to create a link associated to a share \\"\\\\\\\\myserver\\myshare\\", the parameter should be set to \\"myshare\\".

</dd> <dt>

*Description* \[in, optional\]
</dt> <dd>

A comment that describes the node.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the service was successfully modified, 1 (one) if the request is not supported, and any other number to indicate an error. For more information about returned error codes, see [WMI Error Constants](https://msdn.microsoft.com/library/aa394559) for C++ or [WbemErrorEnum](https://msdn.microsoft.com/library/aa393978) for scripting error codes.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1 4294967295)
</dt> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Wmipdfs.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdfs.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_DFSNode**](win32-dfsnode.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 





