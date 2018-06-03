---
Description: Returns a uint32 bitmap with the access rights to the share held by the user or group on whose behalf the instance is returned.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1f656c63-f5ee-4b14-845a-0eb34a0e7a64
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: GetAccessMask method of the Win32\_ClusterShare class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetAccessMask method of the Win32\_ClusterShare class

Returns a **uint32** bitmap with the access rights to the share held by the user or group on whose behalf the instance is returned.

## Syntax


```mof
uint32 GetAccessMask();
```



## Parameters

This method has no parameters.

## Return value

Access rights to the share held by the user or group.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ClusterShare**](win32-clustershare.md)
</dt> </dl>

 

 




