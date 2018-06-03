---
title: Configure method of the Win32\_Product class
description: The Configure WMI class method configures the associated instance of Win32\_Product to the specified install state and level.
ms.assetid: 973e3c98-846a-4724-ba4a-59f562513ba9
keywords:
- Configure method
- Configure method, Win32_Product class
- Win32_Product class, Configure method
topic_type:
- apiref
api_name:
- Win32_Product.Configure
api_location:
- Msiprov.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Configure method of the Win32\_Product class

The **Configure** [WMI class](https://msdn.microsoft.com/library/aa393244) method configures the associated instance of [**Win32\_Product**](win32-product.md) to the specified install state and level.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Configure(
  [in] uint32       InstallState,
  [in] uint32       InstallLevel,
  [in] string Options
);
```



## Parameters

<dl> <dt>

*InstallState* \[in\]
</dt> <dd>

Installation state. Can be one of the following values.



| Value                                                                        | Meaning             |
|------------------------------------------------------------------------------|---------------------|
| <dl> <dt>1</dt> </dl> | Default <br/> |
| <dl> <dt>2</dt> </dl> | Local<br/>    |
| <dl> <dt>3</dt> </dl> | Source<br/>   |



 

</dd> <dt>

*InstallLevel* \[in\]
</dt> <dd>

Installation level. Can be one of the following values.



| Value                                                                        | Meaning            |
|------------------------------------------------------------------------------|--------------------|
| <dl> <dt>1</dt> </dl> | Default<br/> |
| <dl> <dt>2</dt> </dl> | Minimum<br/> |
| <dl> <dt>3</dt> </dl> | Maximum<br/> |



 

</dd> <dt>

*Options* \[in\]
</dt> <dd>

The command line options for configure. These should be in the form of *property***=***setting*.

</dd> </dl>

## Return value



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/> |



 

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

[**Win32\_Product**](win32-product.md)
</dt> <dt>

[WMI Tasks: Computer Software](https://msdn.microsoft.com/library/aa394588)
</dt> </dl>

 

 





