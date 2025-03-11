---
description: The Windows Installer redistributable is a software update package.
ms.assetid: 8491dfa6-b9be-4e37-8a61-a405c8eb0ab0
title: Windows Installer Redistributables
ms.topic: reference
ms.date: 01/08/2024
---

# Windows Installer Redistributables

Windows Installer 4.5 and earlier is available as a redistributable software update package. See the section [Released Versions of Windows Installer](released-versions-of-windows-installer.md) to determine which products shipped versions of the Windows Installer. The redistributable update package for a version is made available after the release of the product that ships with a specific Windows Installer version.

> [!NOTE]
> There is no redistributable for Windows Installer 5.0. This version is included with the OS in Windows 7, Windows Server 2008 R2, and later client and server releases (including Windows 10).

## Obtaining the Windows Installer Redistributable (4.5 and earlier)
You can find all the available Windows Installer redistributables at the [Microsoft Download Center](https://www.microsoft.com/Downloads/).

### Windows Installer 4.5 Redistributable
[Windows Installer 4.5 redistributable package](https://support.microsoft.com/kb/942288) is available here: [https://go.microsoft.com/fwlink/p/?LinkID=101159](https://go.microsoft.com/fwlink/p/?LinkID=101159).

| File Name | OS Version | Architecture |
| --- | --- | --- |
| Windows6.0-KB942288-v2-x86.MSU | Windows Vista <br>Windows Vista with Service Pack 1 (SP1)<br> Windows Server 2008 | x86 (32 bit)|
| Windows6.0-KB942288-v2-x64.MSU | Windows Vista <br>Windows Vista with Service Pack 1 (SP1) <br>Windows Server 2008 | x86-64 (64 bit) |
| Windows6.0-KB942288-v2-ia64.MSU | Windows Vista <br>Windows Vista with Service Pack 1 (SP1) <br>Windows Server 2008 | Itanium (64 bit) |
| WindowsXP-KB942288-v3-x86.exe | Windows XP with Service Pack 2 (SP2) <br>Windows XP with Service Pack 3 (SP3) | x86 (32 bit) |
| WindowsServer2003-KB942288-v4-x86.exe | Windows Server 2003 with Service Pack 1 (SP1) <br>Windows Server 2003 with Service Pack 2 (SP2) | x86 (32 bit) |
| WindowsServer2003-KB942288-v4-x64.exe | Windows Server 2003 with Service Pack 1 (SP1) <br>Windows Server 2003 with Service Pack 2 (SP2) | x86-64 (64 bit) |
| WindowsServer2003-KB942288-v4-ia64.exe | Windows Server 2003 with Sevice Pack 1 (SP1) <br>Windows Server 2003 with Service Pack 2 (SP2) | Itanium (64 bit) |

### Windows Installer 4.0 Redistributable
- There is no redistributable that installs Windows Installer 4.0. This version of the Windows Installer ships with Windows Vista.

### Windows Installer 3.1 Redistributable

-   Windows Installer 3.1 Redistributable (v2) is available here: [https://www.catalog.update.microsoft.com/Search.aspx?q=893803](https://www.catalog.update.microsoft.com/Search.aspx?q=893803).
    > [!Note]  
    > If you upgraded to Windows Installer 3.1 by installing Windows Server 2003 with SP1, or an earlier version of this redistributable, you may also need to install the [Update for Windows Server 2003 Service Pack 1 (KB898715)](https://www.microsoft.com/es-es/download/details.aspx?id=5344) to obtain all the updates available in [Windows Installer 3.1 Redistributable (v2)](https://www.catalog.update.microsoft.com/Search.aspx?q=893803).

### Windows Installer 3.0 Redistributable
-   Windows Installer 3.0 Redistributable is available here: [WindowsInstaller-KB884016-v2-x86.exe](https://archive.org/download/windows-installer-3.0/WindowsInstaller-KB884016-v2-x86.exe).

### Windows Installer 2.0 Redistributable
-   Windows Installer 2.0 Redistributable for Windows NT 4.0 and Windows 2000 is available here: [instmsi.exe](https://archive.org/details/instmsi2-nt-2k).
    > [!Note]
    > The Windows Installer 2.0 used a previous naming convention for the redistributable: [Instmsi.exe](instmsi-exe.md). The redistributable for installing or upgrading to Windows Installer 2.0 on Windows 2000 should not be used to install or upgrade Windows Installer 2.0 on Windows Server 2003 and Windows XP.


## Installing the Windows Installer Redistributable (4.5 and earlier)

The Windows Installer 4.5 resdistributable is provided for Windows Vista and Windows Server 2008 operating systems as a .msu file and should be installed using the [Windows Update Stand-alone Installer](https://support.microsoft.com/kb/934307/) (Wusa.exe.)

The Windows Installer 4.5 redistributable for Windows XP and Windows Server 2003 operating systems can be installed using the following command line syntax and options.

The Windows Installer 3.1 and Windows Installer 3.0 redistributables can be installed using the following command line syntax and options.

### Syntax

Use the following syntax to install the redistributables for Windows Installer 4.5 on Windows XP and Windows Server 2003.

```CMD
<Name of the Redistributable>\[<options>\]*
```

### Command-Line Options

The Windows Installer redistributable software update packages use the following case-insensitive command-line options.



| Option     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /norestart | Prevents the redistributable package from asking the user to reboot even if it had to replace files that were in use during the installation. If the update package is invoked with this option, it returns **ERROR\_SUCCESS\_REBOOT\_REQUIRED** if it had to replace files that were in use.<br/> If it did not have to replace files that were in use, it returns **ERROR\_SUCCESS**. See the remarks section for additional information on delayed reboots.<br/> |
| /quiet     | For use by applications that redistribute the Windows Installer as part of a bootstrapping application. A user interface (UI) is not presented to the user. The bootstrapping application should check the return code to determine whether a reboot is needed to complete the installation of the Windows Installer.<br/>                                                                                                                                                |
| /help      | Displays help on all the available options.                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Delayed Restart on Windows Vista and Windows Server 2008

The /norestart command-line option prevents wusa.exe from restarting the computer. However, if a file being updated by the MSU package is in use, then the package is not applied to the computer until the user restarts the computer. This means that applications that use the Windows Installer 4.5 redistributable for Windows Vista and Windows Server 2008 cannot use the Windows Installer 4.5 functionality until the computer is restarted.

### Delayed Restart on Windows XP and Windows Server 2003

It is recommended that the Windows Installer service be stopped when using the update package. When the package is run in full UI mode it detects if the Windows Installer service is running and requests the user to stop the service. If the user continues without stopping the service, the update replaces Windows Installer.

[Bootstrapping](bootstrapping.md) applications that use the redistributable package to install the Windows Installer with another application can require an extra system reboot in addition to reboots needed to install the application. The delayed reboot option is only recommended for cases where it is necessary to eliminate an extra reboot caused by installing files that are in use. Developers should do the following in their setup application to use the delayed reboot option.

-   Call the redistributable package with the /norestart command-line option.
-   Treat the return of either **ERROR\_SUCCESS** or **ERROR\_SUCCESS\_REBOOT\_REQUIRED** as meaning success.
-   Invoke Msiexec on the application's package and run other setup code specific to the application. If the setup application uses [**MsiInstallProduct**](/windows/desktop/api/Msi/nf-msi-msiinstallproducta), then the application must load MSI.DLL from the system directory. If no reboot occurs and if the redistributable returned **ERROR\_SUCCESS\_REBOOT\_REQUIRED**, then prompt the user for a reboot to complete the setup of the Windows Installer binaries. If a reboot occurs, no additional steps are required.
    > [!Note]  
    > Applications that call [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) on the new MSI.DLL after the redistributable package returns success must ensure that an older version of MSI.DLL has not already been loaded within the process. If an older version of MSI.DLL was loaded, it must be unloaded from the process address space prior to calling **LoadLibrary** for the new MSI.DLL.

     

For more information, see [Windows Installer Bootstrapping](windows-installer-bootstrapping.md).

 

 
