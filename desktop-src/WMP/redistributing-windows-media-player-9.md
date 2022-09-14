---
title: Redistributing Windows Media Player 9 Series
description: Redistributing Windows Media Player 9 Series
ms.assetid: 812e3fc7-e23d-489c-a486-62c7602cf46e
ms.topic: article
ms.date: 05/31/2018
---

# Redistributing Windows Media Player 9 Series

You can install Windows Media Player 9 Series on Windows XP by using one of the following setup programs.

-   MPSetupXP.exe
-   MPSetup.exe

> [!Note]  
> MPSetup.exe is a superset of the MPSetupXP.exe setup program. It contains files that are needed by operating systems released before Windows XP. MPSetup.exe is functionally equivalent to MPSetupXP.exe when run on Windows XP, but the setup program file size is larger because it has not been optimized for installation on Windows XP operating systems.

 

You can install Windows Media Player 9 Series on Windows 98 Second Edition, Windows Millennium Edition or Windows 2000 by using the following setup program.

-   MPSetup.exe

Here is an example of a command line for installation with no UI and no restart or restart prompt.


```
MPSetup.exe /q:A /c:"setup_wm.exe /Q /R:N /P:#e"
```



> [!Note]  
> The /P:\#e parameter specifies that the Windows Media Player installation package should be cached during Windows Media Player setup. This command is used to handle future upgrades of the operating system. This command should be omitted only by corporate IT administrators. The only case where /P:\#e should not be included on the command line is when you own the target system and know that the target system will never be upgraded to a later operating system. For example, if you are installing Windows Media Player 9 Series on Windows 2000 and the computer may someday be upgraded to Windows XP, you must use /P:\#e on the command line. Otherwise, after the Windows XP installation, the Windows Media Player files will be overwritten with the files for Windows Media Player for Windows XP.

 

The following table shows additional parameters that you can use with the Windows Media Player 9 Series setup program.



| Parameter              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /NoMigrate             | Prevent library migration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| /NestedRestore         | Create a nested system restore point. Use this if your application creates a system restore point to nest the Windows Media Player restore point within your application restore point.                                                                                                                                                                                                                                                                                                                             |
| /DisallowSystemRestore | Disallow the creation of a system restore point. This flag will disable the creation of a system restore point. Under most circumstances this flag should not be used for general software redistribution. This should be used only when you can make an explicit choice on behalf of the end user not to support the rollback of the Windows Media Player files to an earlier version of the Player. This flag should be used only for corporate deployment or original equipment manufacturer (OEM) installation. |



 

## Notes

-   The command-line parameters are case-sensitive.
-   When suppressing the restart prompt, you must check the InstallResult registry key and handle restart notification in the calling setup application.
-   Windows Media Player 9 Series also installs the Windows Media Format runtime, so there is no need to include both the Windows Media Player distribution package and the Windows Media Format runtime distribution package in the same software redistribution package. Therefore, if you include MPSetup.exe or MPSetupXP.exe in your installation, you do not need to include WMFdist.exe.

## Related topics

<dl> <dt>

[**Redistributing Windows Media Player Software**](redistributing-windows-media-player-software.md)
</dt> </dl>

 

 




