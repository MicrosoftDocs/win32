---
title: Admin method of the Win32\_Product class
description: Performs an administrative install of an associated Win32\_Product using the installation package provided through the PackageLocation parameter, and any supplied command line options.
ms.assetid: 'b2c60a2b-6aaf-43e3-9cb8-9cb49027a8bb'
keywords: ["Admin method", "Admin method, Win32_Product class", "Win32_Product class, Admin method"]
topic_type:
- apiref
api_name:
- Win32_Product.Admin
api_location:
- Msiprov.dll
api_type:
- COM
---

# Admin method of the Win32\_Product class

The **Admin** [WMI class](https://msdn.microsoft.com/library/aa393244) method performs an administrative install of an associated [**Win32\_Product**](win32-product.md) using the installation package provided through the *PackageLocation* parameter, and any supplied command line options.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Admin(
  [in] string PackageLocation,
  [in] string TargetLocation,
  [in] string Options
);
```



## Parameters

<dl> <dt>

*PackageLocation* \[in\]
</dt> <dd>

Path to the package to be administered.

</dd> <dt>

*TargetLocation* \[in\]
</dt> <dd>

Location for the administrative image to be installed.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Command line options for the upgrade. These should be in the form of *property***=***setting*.

</dd> </dl>

## Return value



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/> |



 

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

[**Win32\_Product**](win32-product.md)
</dt> <dt>

[WMI Tasks: Computer Software](https://msdn.microsoft.com/library/aa394588)
</dt> </dl>

 

 





