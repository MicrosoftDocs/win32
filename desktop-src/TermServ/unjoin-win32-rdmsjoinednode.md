---
title: Unjoin method of the Win32\_RDMSJoinedNode class
description: Removes a node from Remote Desktop Management Services (RDMS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 37c462f4-a19d-4b85-8fac-2735deb7c04f
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Unjoin method Remote Desktop Services
- Unjoin method Remote Desktop Services , Win32_RDMSJoinedNode class
- Win32_RDMSJoinedNode class Remote Desktop Services , Unjoin method
topic_type:
- apiref
api_name:
- Win32_RDMSJoinedNode.Unjoin
api_location:
- RDMS.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Unjoin method of the Win32\_RDMSJoinedNode class

Removes a node from Remote Desktop Management Services (RDMS).

## Syntax


```mof
uint32 Unjoin();
```



## Parameters

This method has no parameters.

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
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

 

 





