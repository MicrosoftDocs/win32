---
title: GetJoinedNodeCount method of the Win32_RDMSJoinedNode class
description: Get number of servers that have the specified roles installed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ed2ae0b5-5cbc-4c11-a2ad-065f88dd5842
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- GetJoinedNodeCount method Remote Desktop Services
- GetJoinedNodeCount method Remote Desktop Services , Win32_RDMSJoinedNode class
- Win32_RDMSJoinedNode class Remote Desktop Services , GetJoinedNodeCount method
topic_type:
- apiref
api_name:
- Win32_RDMSJoinedNode.GetJoinedNodeCount
api_location:
- RDMS.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetJoinedNodeCount method of the Win32\_RDMSJoinedNode class

Get number of servers that have the specified roles installed.

## Syntax


```mof
uint32 GetJoinedNodeCount(
  [in]  uint32 roleType,
  [out] uint32 Count
);
```



## Parameters

<dl> <dt>

*roleType* \[in\]
</dt> <dd>

A bitfield that specifies the role types.

<dt>

0
</dt> <dd>

All

</dd> <dt>

1
</dt> <dd>

Remote Desktop Connection Broker (RDCB)

</dd> <dt>

2
</dt> <dd>

Remote Desktop Session Host (RDSH)

</dd> <dt>

4
</dt> <dd>

Remote Desktop Virtualization Host (RDVH)

</dd> </dl> </dd> <dt>

*Count* \[out\]
</dt> <dd>

On success, returns the number of servers with the specified roles installed.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSJoinedNode**](win32-rdmsjoinednode.md)
</dt> </dl>

 

 





