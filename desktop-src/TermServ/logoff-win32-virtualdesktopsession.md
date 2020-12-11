---
title: Logoff method of the Win32_VirtualDesktopSession class (Sensevts.h)
description: Logs off the user from the virtual desktop session.
ms.assetid: a9c90ace-324c-4eec-86e1-30ce35307e52
ms.tgt_platform: multiple
keywords:
- Logoff method Remote Desktop Services
- Logoff method Remote Desktop Services , Win32_VirtualDesktopSession class
- Win32_VirtualDesktopSession class Remote Desktop Services , Logoff method
topic_type:
- apiref
api_name:
- Win32_VirtualDesktopSession.Logoff
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Logoff method of the Win32\_VirtualDesktopSession class

Logs off the user from the virtual desktop session.

## Syntax


```mof
uint32 Logoff();
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
| Header<br/>                   | <dl> <dt>Sensevts.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_VirtualDesktopSession**](win32-virtualdesktopsession.md)
</dt> </dl>

 

 





