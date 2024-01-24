---
description: The FASTOEM property is designed to enable OEMs to reduce the time it takes to install Windows Installer applications for a specific scenario.
ms.assetid: 4c0af524-eb2e-4d64-bb25-3dae488d236d
title: FASTOEM property
ms.topic: reference
ms.date: 05/31/2018
---

# FASTOEM property

The **FASTOEM** property is designed to enable OEMs to reduce the time it takes to install Windows Installer applications for a specific scenario. Do not author the **FASTOEM** property into the [Property Table](property-table.md).

The **FASTOEM** property is only applicable if all of these conditions are true:

-   The application is being installed on the same volume as the folder containing the source files.
-   The source files are deleted after the installation.
-   No user interface is displayed during the installation. The [user interface level](user-interface-levels.md) is none.
-   The installation is performed in the per-machine [installation context](installation-context.md).
-   There is enough space on the computer for a successful installation.
-   This is first time installation. The installation is not advertising, reinstalling, removing, or doing an administrative installation.
-   No features are installed to run from source.
-   The installation package contains no [isolated components](isolated-components.md). Because isolated components require source files to remain located at the source, the **FASTOEM** property cannot currently be used with isolated components.

If all of the previous conditions are true, setting the **FASTOEM** property enables Windows Installer to improve performance by doing the following:

-   Move rather than copy files on the same volume. This does not guarantee that all files are moved rather than copied. Note that if the computer has multiple hard drives, you must initialize the [**ROOTDRIVE**](rootdrive.md) property on the command line to the same drive containing the installation source.
-   Omit this source from the application's source list so that subsequent reinstallation or maintenance installations default to the CD-ROM sources specified in the [Media Table](media-table.md).
-   Streamline [file costing](file-costing.md).
-   Suppress progress messages sent from Windows Installer to the client.

## Remarks

Because no progress messages are sent when **FASTOEM** is set, it is recommended that authors manually write a value of 1800 for Timeout into the key

**HKLM**\\**SoftWare**\\**Policies**\\**Microsoft**\\**Windows**\\**Installer**\\**Timeout**

Timeout is a **REG\_DWORD** type.

To display the size of the application in Add or Remove Programs in the Windows 2000 Control Panel, you must manually write the value of EstimatedSize into the key

**HKLM**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Uninstall**\\**<*Product Code*>**

This is a **REG\_DWORD** type and equals to the size of the application in Kbytes. The installer does not automatically write this value.

Use the following example command line if the CD-ROM shipped to end users stores the application's installation package at the root of the CD-ROM. Note that the volume label in the [Media Table](media-table.md) of the .msi file must match the volume label of the CD-ROM.

**Msiexec /I C:\\TempImage\\package.msi /qn /le logfile.txt ALLUSERS=1 FASTOEM=1 DISABLEROLLBACK=1 ROOTDRIVE=C:\\**

Use the following example command line if the installation package is not located at the root of the CD-ROM shipped to end users. You must set the [**MEDIAPACKAGEPATH**](mediapackagepath.md) property in this case to the path to the installation package. The volume label in the [Media Table](media-table.md) of the .msi file must match the volume label of the CD-ROM. In this case follow this example.

**Msiexec /I C:\\TempImage\\package.msi /qn /le logfile.txt ALLUSERS=1 FASTOEM=1 DISABLEROLLBACK=1 MEDIAPACKAGEPATH=C:\\TempImage\\package.msi ROOTDRIVE=C:\\**

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Windows Installer 5.0 on Windows Server 2012, Windows 8, Windows Server 2008 R2 or Windows 7. Windows Installer 4.0 or Windows Installer 4.5 on Windows Server 2008 or Windows Vista. Windows Installer on Windows Server 2003 or Windows XP. See the [Windows Installer Run-Time Requirements](windows-installer-portal.md) for information about the minimum Windows service pack that is required by a Windows Installer version.<br/> |



## See also

<dl> <dt>

[Properties](properties.md)
</dt> </dl>

 

 




