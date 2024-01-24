---
description: Instmsi.exe is the redistributable package for installing Windows Installer&\#160;2.0, and earlier versions of Windows Installer. See Windows Installer Redistributables for the redistributables for Windows Installer&\#160;3.0 and later versions.
ms.assetid: 74ea4530-3a73-4169-b0b7-f0272229192d
title: Instmsi.exe
ms.topic: article
ms.date: 05/31/2018
---

# Instmsi.exe

Instmsi.exe is the redistributable package for installing Windows Installer 2.0, and earlier versions of Windows Installer. See [Windows Installer Redistributables](windows-installer-redistributables.md) for the redistributables for Windows Installer 3.0 and later versions.

For more information about which version of the Windows Installer was shipped with your operating system, see [Released Versions of Windows Installer](released-versions-of-windows-installer.md).

Some redistributables should not be run on certain versions of the operating system. The following table describes which Instmsi is compatible on which operating system.



| If Instmsi.exe installs this version of the Windows Installer | Instmsi.exe can be run on these operating systems                    | Instmsi.exe must not be run on these operating systems                                        |
|---------------------------------------------------------------|----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| Windows Installer version 1.0                                 | Windows 95, Windows 98, Windows NT 4.0+SP3                           | Windows Me, Windows 2000, Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008 |
| Windows Installer version 1.1                                 | Windows 95, Windows 98, Windows NT 4.0+SP3                           | Windows Me, Windows 2000, Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008 |
| Windows Installer version 1.2                                 | Windows 95, Windows 98, Windows Me, Windows NT 4.0+SP3               | Windows 2000, Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008             |
| Windows Installer version 2.0                                 | Windows 95, Windows 98, Windows Me, Windows NT 4.0+SP6, Windows 2000 | Windows XP, Windows Server 2003, Windows Vista, Windows Server 2008                           |



 

For example, an application that redistributes Windows Installer version 1.1 should check that the operating system is Windows NT 4.0 SP3 or Windows 98/95 before running the redistributable package. Applications using the redistributable package should also ensure that the ANSI version of the Windows Installer is installed on Windows 98/95, and that the Unicode version is installed on Windows NT or Windows 2000. Note that some applications rename the Unicode version to InstMsiW.

## Syntax

**instmsi** *options*

## Command Line Options

The command line options are case-insensitive.



| Option                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /q                         | For use by applications that redistribute the Windows Installer as part of a bootstrapping application. No UI is presented to the user. The bootstrapping application should check the return code to determine whether a reboot is needed to complete the installation of the Windows Installer.                                                                                                                                                                                                                          |
| /t                         | Used for debugging purposes only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| /c:"msiinst /delayreboot"  | The delayed reboot option. Prevents Instmsi from prompting the user for a reboot even if it had to replace files that were in use during the installation. If Instmsi is invoked with this option, it returns ERROR\_SUCCESS\_REBOOT\_REQUIRED if it had to replace files that were in use. If it did not have to replace files that were in use, it returns ERROR\_SUCCESS. Available with Instmsi for Windows Installer  2.0 or later. See the remarks section for additional information on delayed reboots.<br/> |
| /c:"msiinst /delayrebootq" | The quiet version of the delayed reboot option. It does not present any UI to the user. Otherwise the behavior is identical to the previous option. Available with Instmsi for Windows Installer 2.0 or later. See the remarks section for additional information on delayed reboots.<br/>                                                                                                                                                                                                                           |
| /?                         | Displays help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Remarks

[Bootstrapping](bootstrapping.md) applications that use Instmsi.exe to install the Windows Installer with another application may require an extra system reboot. This is potentially an extra reboot in addition to any reboots that are needed to install the application.

The delayed reboot option is only recommended for setup developers who want to eliminate an extra reboot caused by using Instmsi.exe with a setup application that installs files that are in use.

Developers should do the following in their setup application to use the delayed reboot option. This option is not available with Instmsi.exe versions that install Window Installer versions earlier than version 2.0:

**To use the delayed reboot option**

1.  Call Instmsi.exe with one of the delayed reboot command line options.
2.  Treat the return of either ERROR\_SUCCESS or ERROR\_SUCCESS\_REBOOT\_REQUIRED as meaning success.
3.  Get the path to the folder containing the newly installed Windows Installer binaries from the InstallerLocation value under:

    **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Installer**

    This value is of type **REG\_SZ**.

4.  Set the current directory to the path obtained in step 3.
5.  Invoke Msiexec on the application's package and run other setup code specific to the application. If the setup application uses [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta), then the application must load MSI.DLL from the location obtained in step 3.
    > [!Note]  
    > Applications that call **LoadLibrary** on the new MSI.DLL in the location obtained in step 3 must ensure that an older version of MSI.DLL has not already been loaded within the process. If an older version of MSI.DLL was loaded within the process, it must be unloaded from the process address space prior to the **LoadLibrary** call for the new MSI.DLL.

     

6.  If step (5) does not require a reboot and if Instmsi.exe had returned ERROR\_SUCCESS\_REBOOT\_REQUIRED in step (1), prompt the user for a reboot to complete the setup of the Windows Installer binaries on the system. However, if a reboot occurs in step (5), no additional steps are required.

Instmsi.exe is available in the [Windows SDK Components for Windows Installer Developers](platform-sdk-components-for-windows-installer-developers.md).

## Related topics

<dl> <dt>

[Bootstrapping](bootstrapping.md)
</dt> <dt>

[Internet Download Bootstrapping](internet-download-bootstrapping.md)
</dt> <dt>

[Released Versions, Tools, and Redistributables](released-versions-tools-and-redistributables.md)
</dt> <dt>

[Windows Installer Development Tools](windows-installer-development-tools.md)
</dt> </dl>

 

 




