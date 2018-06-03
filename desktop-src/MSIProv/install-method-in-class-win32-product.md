---
title: Install method of the Win32\_Product class
description: Installs an associated Win32\_Product instance using the installation package provided through the PackageLocation parameter, and any supplied command line options.
ms.assetid: bbbecbf7-2374-4628-a230-0a49fa00fecf
keywords:
- Install method
- Install method, Win32_Product class
- Win32_Product class, Install method
topic_type:
- apiref
api_name:
- Win32_Product.Install
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

# Install method of the Win32\_Product class

The static **Install** [WMI class](https://msdn.microsoft.com/library/aa393244) method installs an associated [**Win32\_Product**](win32-product.md) instance using the installation package provided through the *PackageLocation* parameter, and any supplied command line options.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Install(
  [in] string PackageLocation,
  [in] string Options,
  [in] boolean AllUsers
);
```



## Parameters

<dl> <dt>

*PackageLocation* \[in\]
</dt> <dd>

Path to the Installer package, which is relative to the computer on which the software is being installed and which can be referenced using a Universal Naming Convention (UNC) path.

</dd> <dt>

*Options* \[in\]
</dt> <dd>

Command-line options required for installing the software. Format as *property***=***setting*. If no options are required, this parameter should be left blank.

</dd> <dt>

*AllUsers* \[in\]
</dt> <dd>

Boolean value that indicates whether the software should be available to all the users on a computer or just the currently logged-on user. If True, the software will be installed under the All Users profile. If set to False, the software will be installed under the profile of the user whose credentials are being used to run the script. For example, if the script is running under the Administrator account, the software will be installed under the Administrator profile and thus will not be accessible to other users.

</dd> </dl>

## Return value



| Return code                                                                               | Description                                                                                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl>          | Successful completion<br/>                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**13**</dt> </dl>         | The data is invalid. <br/>                                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**87** </dt> </dl>        | One of the parameters was invalid. <br/>                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**120** </dt> </dl>       | This value is returned when a custom action attempts to call a function that cannot be called from custom actions. The function returns the value ERROR\_CALL\_NOT\_IMPLEMENTED. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                    |
| <dl> <dt>**1259** </dt> </dl>      | This error code only occurs when using Windows Installer version 2.0 and Windows XP. If Windows Installer determines a product may be incompatible with the current operating system, it displays a dialog box informing the user and asking whether to try to install anyway. This error code is returned if the user chooses not to try the installation. <br/> |
| <dl> <dt>**1601** </dt> </dl>      | The Windows Installer service could not be accessed. Contact your support personnel to verify that the Windows Installer service is properly registered. <br/>                                                                                                                                                                                                    |
| <dl> <dt>**1602** </dt> </dl>      | The user cancels the installation. <br/>                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**1603** </dt> </dl>      | A fatal error occurred during the installation. <br/>                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**1604** </dt> </dl>      | Installation suspended, incomplete. <br/>                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**1605** </dt> </dl>      | This action is only valid for products that are currently installed. <br/>                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**1606** </dt> </dl>      | The feature identifier is not registered. <br/>                                                                                                                                                                                                                                                                                                                   |
| <dl> <dt>**1607** </dt> </dl>      | The component identifier is not registered. <br/>                                                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**1608** </dt> </dl>      | This is an unknown property. <br/>                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**1609** </dt> </dl>      | The handle is in an invalid state. <br/>                                                                                                                                                                                                                                                                                                                          |
| <dl> <dt>**1610** </dt> </dl>      | The configuration data for this product is corrupt. Contact your support personnel. <br/>                                                                                                                                                                                                                                                                         |
| <dl> <dt>**1611** </dt> </dl>      | The component qualifier is not present. <br/>                                                                                                                                                                                                                                                                                                                     |
| <dl> <dt>**1612** </dt> </dl>      | The installation source for this product is not available. Verify that the source exists and that you can access it. <br/>                                                                                                                                                                                                                                        |
| <dl> <dt>**1613** </dt> </dl>      | This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service. <br/>                                                                                                                                                                     |
| <dl> <dt>**1614** </dt> </dl>      | The product is un-installed. <br/>                                                                                                                                                                                                                                                                                                                                |
| <dl> <dt>**1615** </dt> </dl>      | The SQL query syntax is invalid or unsupported. <br/>                                                                                                                                                                                                                                                                                                             |
| <dl> <dt>**1616** </dt> </dl>      | The record field does not exist. <br/>                                                                                                                                                                                                                                                                                                                            |
| <dl> <dt>**1618** </dt> </dl>      | Another installation is already in progress. Complete that installation before proceeding with this install. <br/>                                                                                                                                                                                                                                                |
| <dl> <dt>**1619** </dt> </dl>      | This installation package could not be opened. Verify that the package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer package. <br/>                                                                                                                                                                |
| <dl> <dt>**1620** </dt> </dl>      | This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package. <br/>                                                                                                                                                                                                                     |
| <dl> <dt>**1621** </dt> </dl>      | There was an error when starting the Windows Installer service user interface. Contact your support personnel. <br/>                                                                                                                                                                                                                                              |
| <dl> <dt>**1622** </dt> </dl>      | There was an error opening installation log file. Verify that the specified log file location exists and is writable. <br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**1623** </dt> </dl>      | This language of this installation package is not supported by your system. <br/>                                                                                                                                                                                                                                                                                 |
| <dl> <dt>**1624** </dt> </dl>      | There was an error applying transforms. Verify that the specified transform paths are valid. <br/>                                                                                                                                                                                                                                                                |
| <dl> <dt>**1625** </dt> </dl>      | This installation is forbidden by system policy. Contact your system administrator. <br/>                                                                                                                                                                                                                                                                         |
| <dl> <dt>**1626** </dt> </dl>      | The function could not be executed. <br/>                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**1627** </dt> </dl>      | The function failed during execution. <br/>                                                                                                                                                                                                                                                                                                                       |
| <dl> <dt>**1628** </dt> </dl>      | An invalid or unknown table was specified. <br/>                                                                                                                                                                                                                                                                                                                  |
| <dl> <dt>**1629** </dt> </dl>      | The data supplied is the wrong type. <br/>                                                                                                                                                                                                                                                                                                                        |
| <dl> <dt>**1630** </dt> </dl>      | Data of this type is not supported. <br/>                                                                                                                                                                                                                                                                                                                         |
| <dl> <dt>**1631** </dt> </dl>      | The Windows Installer service failed to start. Contact your support personnel. <br/>                                                                                                                                                                                                                                                                              |
| <dl> <dt>**1632** </dt> </dl>      | The Temp folder is either full or inaccessible. Verify that the Temp folder exists and that you can write to it. <br/>                                                                                                                                                                                                                                            |
| <dl> <dt>**1633** </dt> </dl>      | This installation package is not supported on this platform. Contact your application vendor. <br/>                                                                                                                                                                                                                                                               |
| <dl> <dt>**1634** </dt> </dl>      | Component is not used on this machine. <br/>                                                                                                                                                                                                                                                                                                                      |
| <dl> <dt>**1635** </dt> </dl>      | This patch package could not be opened. Verify that the patch package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer patch package. <br/>                                                                                                                                                           |
| <dl> <dt>**1636** </dt> </dl>      | This patch package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer patch package. <br/>                                                                                                                                                                                                                      |
| <dl> <dt>**1637** </dt> </dl>      | This patch package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service. <br/>                                                                                                                                                                            |
| <dl> <dt>**1638** </dt> </dl>      | Another version of this product is already installed. Installation of this version cannot continue. <br/>                                                                                                                                                                                                                                                         |
| <dl> <dt>**1639** </dt> </dl>      | Invalid command line argument. Consult the Windows Installer SDK for detailed command-line help. <br/>                                                                                                                                                                                                                                                            |
| <dl> <dt>**1640** </dt> </dl>      | Installation from a Terminal Server client session is not permitted for the current user. <br/>                                                                                                                                                                                                                                                                   |
| <dl> <dt>**1641** </dt> </dl>      | The installer has initiated a restart. This message is indicative of a success. This error code is not available on Windows Installer version 1.0. <br/>                                                                                                                                                                                                          |
| <dl> <dt>**1642** </dt> </dl>      | The installer cannot install the upgrade patch because the program being upgraded may be missing or the upgrade patch updates a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch. This error code is not available on Windows Installer version 1.0. <br/>            |
| <dl> <dt>**1643** </dt> </dl>      | The patch package is not permitted by system policy. This error code is available with Windows Installer version 2.0. <br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**1644** </dt> </dl>      | One or more customizations are not permitted by system policy. This error code is available with Windows Installer version 2.0. <br/>                                                                                                                                                                                                                             |
| <dl> <dt>**1645** </dt> </dl>      | Windows Installer does not permit installation from a Remote Desktop Connection. Available beginning with Windows Installer version 2.0 for Windows Server 2003. <br/>                                                                                                                                                                                            |
| <dl> <dt>**1646** </dt> </dl>      | The patch package is not a removable patch package. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                                                                                                 |
| <dl> <dt>**1647** </dt> </dl>      | The patch is not applied to this product. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                                                                                                           |
| <dl> <dt>**1648** </dt> </dl>      | No valid sequence could be found for the set of patches. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                                                                                            |
| <dl> <dt>**1649** </dt> </dl>      | Patch removal was disallowed by policy. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                                                                                                             |
| <dl> <dt>**1650** </dt> </dl>      | The XML patch data is invalid. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                                                                                                                      |
| <dl> <dt>**1651** </dt> </dl>      | Administrative user failed to apply patch for a per-user managed or a per-machine application that is in advertise state. Available beginning with Windows Installer version 3.0. <br/>                                                                                                                                                                           |
| <dl> <dt>**3010** </dt> </dl>      | A restart is required to complete the install. This message is indicative of a success. This does not include installs where the ForceReboot action is run. This error code is not available on Windows Installer version 1.0. <br/>                                                                                                                              |
| <dl> <dt>**2147549445**</dt> </dl> | RPC Server Fault Error<br/>                                                                                                                                                                                                                                                                                                                                       |



 

## Remarks

The ability to install software without using Group Policy can be an enormous boon to administrators; this allows you to install software without requiring user interaction and without requiring the user to log off and log on or the computer to restart. In addition, a WMI script can help ensure a successful installation by doing such things as checking for available memory or available disk space before beginning the installation process. If there is not enough memory or disk space on the target computer, your script can terminate without installing the software. This prevents any problems that can occur from attempting to install software on computers not capable of running that software.

The install method of [**Win32\_Product**](win32-product.md) can be used to install software on the local or remote computer.

## Examples

The following VBScript sample installs software for all users on a local computer.


```VB
Const ALL_USERS = True
Set objService = GetObject("winmgmts:")
Set objSoftware = objService.Get("Win32_Product")
errReturn = objSoftware.Install("c:\scripts\database.msi", , ALL_USERS)
```



The following VBScript sample installs software for all users on a remote computer.


```VB
strComputer = "atl-dc-02"
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set objSoftware = objWMIService.Get("Win32_Product")
errReturn = objSoftware.Install("c:\scripts\database.msi",,True)
Wscript.Echo errReturn
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

 

 





