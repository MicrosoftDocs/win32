---
title: StopService method of the Win32\_ApplicationService class
description: Places the service represented by the Win32\_ApplicationService in the stopped state.
ms.assetid: '4ea65bc9-9a2c-4f7d-8d03-1c724b249f85'
keywords: ["StopService method", "StopService method, Win32_ApplicationService class", "Win32_ApplicationService class, StopService method"]
topic_type:
- apiref
api_name:
- Win32_ApplicationService.StopService
api_location:
- MsiProv.dll
api_type:
- COM
---

# StopService method of the Win32\_ApplicationService class

The **StopService** [WMI class](https://msdn.microsoft.com/library/aa393244) method places the service represented by the [**Win32\_ApplicationService**](win32-applicationservice.md) in the stopped state.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| Header<br/>                   | <dl> <dt>Sdoias.h</dt> </dl>    |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_ApplicationService**](win32-applicationservice.md)
</dt> </dl>

 

 





