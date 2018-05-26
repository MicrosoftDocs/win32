---
title: Disconnect method of the Win32\_VirtualDesktopSession class
description: Disconnects the virtual desktop session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9dbb256c-c416-4749-87be-05a906070560
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Disconnect method Remote Desktop Services
- Disconnect method Remote Desktop Services , Win32_VirtualDesktopSession class
- Win32_VirtualDesktopSession class Remote Desktop Services , Disconnect method
topic_type:
- apiref
api_name:
- Win32_VirtualDesktopSession.Disconnect
api_location:
- RDMS.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Disconnect method of the Win32\_VirtualDesktopSession class

Disconnects the virtual desktop session.

## Syntax


```mof
uint32 Disconnect();
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

[**Win32\_VirtualDesktopSession**](win32-virtualdesktopsession.md)
</dt> </dl>

 

 





