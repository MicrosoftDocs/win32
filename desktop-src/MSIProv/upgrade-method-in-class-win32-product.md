---
title: Upgrade method of the Win32\_Product class
description: The Upgrade WMI class method upgrades the associated Win32\_Product instance using the upgrade package provided through the PackageLocation parameter and any supplied command line options.
ms.assetid: '1e27128f-f7b3-4632-bca6-78de423d256d'
keywords: ["Upgrade method", "Upgrade method, Win32_Product class", "Win32_Product class, Upgrade method"]
topic_type:
- apiref
api_name:
- Win32_Product.Upgrade
api_location:
- Msiprov.dll
api_type:
- COM
---

# Upgrade method of the Win32\_Product class

The **Upgrade** [WMI class](https://msdn.microsoft.com/library/aa393244) method upgrades the associated [**Win32\_Product**](win32-product.md) instance using the upgrade package provided through the *PackageLocation* parameter and any supplied command line options.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Upgrade(
  [in] string PackageLocation,
  [in] string Options
);
```



## Parameters

<dl> <dt>

*PackageLocation* \[in\]
</dt> <dd>

Path to the Windows Installer upgrade package, relative to the computer on which the software is being installed. The path can be referenced using UNC paths or mapped network drives.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Command-line options required for installing the software. If no options are required, this parameter should be left blank. Format as *property***=***setting*.

</dd> </dl>

## Return value



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/> |



 

## Remarks

As new versions of a software package are released, you might need to upgrade existing copies of that software. These upgrades can be carried out using the Win32\_Product Upgrade method. The Upgrade method works only under the following conditions:

-   It is used only with a software upgrade package.

    Upgrade packages are .msi files specifically designed to upgrade a previous version of the software. If you attempt to use a standard Windows Installer package with the Upgrade method, you will receive an error message

    `1636:        Copy     This patch package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer patch package.    `

-   A previous version of the product is already installed.

    The Upgrade method will fail if a previous version of the software is not found. For example, to upgrade a computer from version 1 to version 2 of an application, version 1 must first be installed on that computer. If it is not, the upgrade will fail, and version 2 will not be installed.

If you are upgrading software on a remote computer and the Installer file is located on a third computer, you need to reference the UNC path to the file and use delegation to allow the computer being upgraded to connect over the network and retrieve that file.

## Examples

The following VBS example upgrades an application called Personnel Database on a computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colSoftware = objWMIService.ExecQuery _
 ("SELECT * FROM Win32__Product WHERE Name = 'Personnel Database'")
For Each objSoftware in colSoftware
 errReturn = objSoftware.Upgrade("c:\scripts\database2.msi")
Next
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| Header<br/>                   | <dl> <dt>Netcfgn.h</dt> </dl>   |
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

 

 





