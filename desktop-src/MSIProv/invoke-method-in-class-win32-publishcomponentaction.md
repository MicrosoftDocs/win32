---
title: Invoke method of the Win32\_PublishComponentAction class
description: The Invoke WMI class method of the Win32\_PublishComponentAction class takes a particular action. The details of how the method performs the action are implementation-specific. The results of the method are based on the return value.
ms.assetid: 7ed36f5c-328a-4b70-82cd-d10156a54721
keywords:
- Invoke method
- Invoke method, Win32_PublishComponentAction class
- Win32_PublishComponentAction class, Invoke method
topic_type:
- apiref
api_name:
- Win32_PublishComponentAction.Invoke
api_location:
- Msiprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Invoke method of the Win32\_PublishComponentAction class

The **Invoke** [WMI class](https://msdn.microsoft.com/library/aa393244) method of the [**Win32\_PublishComponentAction**](win32-publishcomponentaction.md) class takes a particular action. The details of how the method performs the action are implementation-specific. The results of the method are based on the return value.

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
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_PublishComponentAction**](win32-publishcomponentaction.md)
</dt> </dl>

 

 





