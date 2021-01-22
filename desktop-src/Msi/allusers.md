---
Description: The ALLUSERS property configures the installation context of the package.
ms.assetid: 942e7764-a80f-4880-9559-72174f1827f7
title: ALLUSERS property
ms.topic: reference
ms.custom: snippet-project
ms.date: 07/27/2020
---

# ALLUSERS property

The **ALLUSERS** property configures the installation context of the package. The Windows Installer performs a per-user installation or per-machine installation depending on the access privileges of the user, whether elevated privileges are required to install the application, the value of the **ALLUSERS** property, the value of the [**MSIINSTALLPERUSER**](msiinstallperuser.md) property and the version of the operating system.

The value of the **ALLUSERS** property, at installation time, determines the [installation context](installation-context.md).

-   An **ALLUSERS** property value of 1 specifies the per-machine installation context.
-   An **ALLUSERS** property value of an empty string ("") specifies the per-user installation context.
-   If the value of the **ALLUSERS** property is set to 2, the Windows Installer always resets the value of the **ALLUSERS** property to 1 and performs a per-machine installation or it resets the value of the **ALLUSERS** property to an empty string ("") and performs a per-user installation. The value ALLUSERS=2 enables the system to reset the value of **ALLUSERS**, and the installation context, dependent upon the user's privileges and the version of Windows.

    **Windows 7:** Set the **ALLUSERS** property to 2 to use the [**MSIINSTALLPERUSER**](msiinstallperuser.md) property to specify the installation context. Set the **MSIINSTALLPERUSER** property to an empty string ("") for a per-machine installation. Set the **MSIINSTALLPERUSER** property to 1 for a per-user installation. If the package has been written following the development guidelines described in [Single Package Authoring](single-package-authoring.md), users having user access can install into the per-user context without having to provide UAC credentials. If the user has user access privileges, the installer performs a per-machine installation only if Admin credentials are provided to the UAC dialog box.

    **Windows Vista:** Set the **ALLUSERS** property to 2 and Windows Installer complies with [*User Account Control*](u-gly.md) (UAC). If the user has user access privileges, and ALLUSERS=2, the installer performs a per-machine installation only if Admin credentials are provided to the UAC dialog box. If UAC is enabled and the correct Admin credentials are not provided, the installation fails with an error stating that administrator privileges are required. If UAC is disabled by the registry key, group policy, or the control panel, the UAC dialog box is not displayed and the installation fails with an error stating that administrator privileges are required.

    **Windows XP:** Set the **ALLUSERS** property to 2 and Windows Installer performs a per-user installation if the user has user access privileges.

-   If the value of the **ALLUSERS** property does not equal 2, the Windows Installer ignores the value of the [**MSIINSTALLPERUSER**](msiinstallperuser.md) property.

## Example

```xml
  <!-- Disallow user from installing for all users -->
    <Property Id="ALLUSERS" Secure="yes"/>
    <Condition Message="Setting the ALLUSERS property is not allowed because [ProductName] is a per-user application. Setup will now exit.">
      NOT ALLUSERS
    </Condition>
```

Example from [Windows Classic Samples](https://github.com/microsoft/Windows-classic-samples/blob/1d363ff4bd17d8e20415b92e2ee989d615cc0d91/Samples/DesktopToasts/CPP/Product.wxs) on GitHub.

## Default Value

The recommended default installation context is per-user. If **ALLUSERS** is not set, the installer does a per-user installation. You can ensure the **ALLUSERS** property has not been set by setting its value to an empty string (""), ALLUSERS="".

## Remarks

The [installation context](installation-context.md) determines the values of the [**DesktopFolder**](desktopfolder.md), [**ProgramMenuFolder**](programmenufolder.md), [**StartMenuFolder**](startmenufolder.md), [**StartupFolder**](startupfolder.md), [**TemplateFolder**](templatefolder.md), [**AdminToolsFolder**](admintoolsfolder.md), [**ProgramFilesFolder**](programfilesfolder.md), [**CommonFilesFolder**](commonfilesfolder.md), [**ProgramFiles64Folder**](programfiles64folder.md), and [**CommonFiles64Folder**](commonfiles64folder.md) properties. The installation context determines the parts of the registry where entries in the [Registry table](registry-table.md) and [RemoveRegistry table](removeregistry-table.md), with -1 in the Root column, are written or removed.

## Requirements



|                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> <dt>

[**MSIINSTALLPERUSER**](msiinstallperuser.md)
</dt> <dt>

[Installation Context](installation-context.md)
</dt> <dt>

[Single Package Authoring](single-package-authoring.md)
</dt> </dl>

 

 




