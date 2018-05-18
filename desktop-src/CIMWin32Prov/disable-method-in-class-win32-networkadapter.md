---
Description: 'Disables the network adapter.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '6b328d7c-a9ef-4c9b-bc32-13fa2e0f65eb'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Disable method of the Win32\_NetworkAdapter class'
---

# Disable method of the Win32\_NetworkAdapter class

The **Disable** method disables the network adapter.

## Syntax


```mof
uint32 Disable();
```



## Parameters

This method has no parameters.

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_NetworkAdapter**](win32-networkadapter.md)
</dt> <dt>

[WMI Tasks: Networking](https://msdn.microsoft.com/library/aa394595)
</dt> <dt>

[IPv6 and IPv4 Support in WMI](https://msdn.microsoft.com/library/aa822883)
</dt> </dl>

 

 




