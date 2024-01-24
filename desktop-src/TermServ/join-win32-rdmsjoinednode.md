---
title: Join method of the Win32_RDMSJoinedNode class
description: Adds a node to Remote Desktop Management Services (RDMS).
ms.assetid: 7451d12a-ace2-4564-bf6d-fb0169be967f
ms.tgt_platform: multiple
keywords:
- Join method Remote Desktop Services
- Join method Remote Desktop Services , Win32_RDMSJoinedNode class
- Win32_RDMSJoinedNode class Remote Desktop Services , Join method
topic_type:
- apiref
api_name:
- Win32_RDMSJoinedNode.Join
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Join method of the Win32\_RDMSJoinedNode class

Adds a node to Remote Desktop Management Services (RDMS).

## Syntax


```mof
uint32 Join(
  [in] string NodeFQDN,
  [in] string NodeSID
);
```



## Parameters

<dl> <dt>

*NodeFQDN* \[in\]
</dt> <dd>

The fully qualified domain name of the node.

</dd> <dt>

*NodeSID* \[in\]
</dt> <dd>

The security identifier (SID) of the node.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSJoinedNode**](win32-rdmsjoinednode.md)
</dt> </dl>

 

 





