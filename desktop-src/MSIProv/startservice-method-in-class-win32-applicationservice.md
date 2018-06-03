---
title: StartService method of the Win32\_ApplicationService class
description: The StartService method places the service in the started state.Note For more information about support or requirements for installation on a specific operating system, see Operating System Availability of WMI Components.
ms.assetid: dea14f4f-faa4-45c5-9bd2-786cfda4438b
keywords:
- StartService method
- StartService method, Win32_ApplicationService class
- Win32_ApplicationService class, StartService method
topic_type:
- apiref
api_name:
- Win32_ApplicationService.StartService
api_location:
- MsiProv.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StartService method of the Win32\_ApplicationService class

The **StartService** method places the service in the started state.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>MsiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_ApplicationService**](win32-applicationservice.md)
</dt> </dl>

 

 





