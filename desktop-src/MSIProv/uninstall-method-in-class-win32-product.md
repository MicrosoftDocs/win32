---
title: Uninstall method of the Win32\_Product class
description: The Uninstall WMI class method uninstalls the associated instance of Win32\_Product.
ms.assetid: b9490fce-b07e-4c16-8164-f29b5a7ca9d2
keywords:
- Uninstall method
- Uninstall method, Win32_Product class
- Win32_Product class, Uninstall method
topic_type:
- apiref
api_name:
- Win32_Product.Uninstall
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

# Uninstall method of the Win32\_Product class

The **Uninstall** [WMI class](https://msdn.microsoft.com/library/aa393244) method uninstalls the associated instance of [**Win32\_Product**](win32-product.md).

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Uninstall();
```



## Parameters

This method has no parameters.

## Return value



| Return code                                                                               | Description                       |
|-------------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>  |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/> |



 

## Remarks

Software installation is rarely permanent; instead, software is typically removed at some point in time, and for any number of reasons:

-   The functionality supplied by the software is no longer needed.
-   The software is being replaced by a competing software package.
-   The software is not licensed for use in the organization.
-   The software is installed on the wrong computer.

The [**Win32\_Product**](win32-product.md) Uninstall method can be used to remove software from a computer.

The Uninstall method can be used either on the local computer or on a remote computer, and without delegation. This is because no multihop security operations are involved. Instead, the software is simply removed from the computer.

Although the Uninstall method can remove software from a computer, it does not override Group Policy. For example, if Microsoft Excel has been installed on a computer, you can use the Uninstall method to remove it. However, if Microsoft Excel is available to the user through Group Policy, the user will be able to reinstall the application.

## Examples

The following VBScript sample deletes software on a computer


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colSoftware = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_Product WHERE Name = 'Personnel database'")
For Each objSoftware in colSoftware
 objSoftware.Uninstall()
Next
```



The following PowerShell code sample describes how to uninstall an application from multiple computers.


```PowerShell
$list = 'host1','host2','host3'   # your hosts go here
$name = 'appname'                 # your application name goes here (as displayed by win32_product instance)
$list | foreach {
    $hostname = $_
    gwmi win32_product -filter "Name = '$name'" -namespace root/cimv2 -comp $_ | foreach {
        if ($_.uninstall().returnvalue -eq 0) { write-host "Successfully uninstalled $name from $($hostname)" }
        else { write-warning "Failed to uninstall $name from $($hostname)." }
    }
}
```



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

 

 





