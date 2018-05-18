---
title: Invoke method of the Win32\_EnvironmentSpecification class
description: The Invoke WMI class method of the Win32\_EnvironmentSpecification class evaluates a particular check.
ms.assetid: '372d6396-4a95-4680-b10f-e9dad73e9dda'
keywords: ["Invoke method", "Invoke method, Win32_EnvironmentSpecification class", "Win32_EnvironmentSpecification class, Invoke method"]
topic_type:
- apiref
api_name:
- Win32_EnvironmentSpecification.Invoke
api_location:
- Msiprov.dll
api_type:
- COM
---

# Invoke method of the Win32\_EnvironmentSpecification class

The **Invoke** [WMI class](https://msdn.microsoft.com/library/aa393244) method of the [**Win32\_EnvironmentSpecification**](win32-environmentspecification.md) class evaluates a particular check. The details of how the method evaluates a particular check in a CIM context are described by the non-abstract [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) subclasses. The results of the method are based on the return value.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Invoke();
```



## Parameters

This method has no parameters.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_EnvironmentSpecification**](win32-environmentspecification.md)
</dt> </dl>

 

 





