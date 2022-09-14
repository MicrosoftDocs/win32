---
title: SetActiveServer method of the Win32_RDMSEnvironment class
description: Sets the FQDN of the Remote Desktop Management Services (RDMS) environment to the current node.
ms.assetid: ed7b71cf-c3a4-4d2f-856a-31332f94fac9
ms.tgt_platform: multiple
keywords:
- SetActiveServer method Remote Desktop Services
- SetActiveServer method Remote Desktop Services , Win32_RDMSEnvironment class
- Win32_RDMSEnvironment class Remote Desktop Services , SetActiveServer method
topic_type:
- apiref
api_name:
- Win32_RDMSEnvironment.SetActiveServer
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetActiveServer method of the Win32\_RDMSEnvironment class

Sets the FQDN of the Remote Desktop Management Services (RDMS) environment to the current node.

## Syntax


```mof
uint32 SetActiveServer();
```



## Parameters

This method has no parameters.

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

[**Win32\_RDMSEnvironment**](win32-rdmsenvironment.md)
</dt> </dl>

 

 





