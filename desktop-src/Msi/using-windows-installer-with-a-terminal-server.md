---
description: The following may affect Windows Installer installations when using a terminal server. Setup developers should always test that their Windows Installer package installs as expected when users are also using a terminal server.
ms.assetid: deda9efa-a0fc-4b4e-a531-650ac201fd84
title: Using Windows Installer with a Terminal Server
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Installer with a Terminal Server

The following may affect Windows Installer installations when using a terminal server. Setup developers should always test that their Windows Installer package installs as expected when users are also using a terminal server.

-   On operating systems earlier than Windows Server 2008 and Windows Vista, the [EnableAdminTSRemote](enableadmintsremote.md) system policy must be set to enable administrators to perform installations in the client session. Beginning with Windows Server 2008 and Windows Vista, the EnableAdminTSRemote policy no longer has any effect. Regardless of its setting, administrators and non-administrators can perform an installation in the client session or the console session. Administrators and non-administrators can always perform Windows Installer installations in the console session.
-   The Windows Installer prevents installation in the per-user [installation context](installation-context.md) if the [DisableUserInstalls](disableuserinstalls.md)[system policy](system-policy.md) is set to 1. In this case, the installer ignores all applications registered as per-user and searches only for applications registered as per-machine.
-   When an administrator performs an installation in a client session of a terminal server that is hosted in Windows 2000, the installation must use a UNC path and not a mapped drive letter.

Developers should adhere to the following guidelines when developing a Windows Installer component that may be used with a terminal server.

-   Write all **HKCU** registry information in the **HKCU**\\**Software** part of the registry.
-   Storing configuration information in INI files is not recommended.
-   Write per-user information to the registry when the application is run for the first time and not at installation time. If you must write per-user information to the registry at installation time, separate the per-user and per-machine information into different Windows Installer components. Author the package such that the installer does not attempt to validate and repair the components containing per-user information when the application is installed.
-   A package used for only per-machine installations should write environment variables to the computer's environment by including \* in the Name column of the [Environment Table](environment-table.md). If the package can be used for per-user installations or per-machine installations, use two components. Include the per-user component in the [Component Table](condition-table.md) and enter the user settings in the Environment Table. Include the per-machine component in the Component Table and enter the computer settings in the Environment Table. Control which component gets installed by using conditional statements based upon the [**ALLUSERS**](allusers.md) property in the Condition field of the Component Table.
-   When performing per-machine installations from a terminal server, the installer writes per-user environment variables to **HKCU**\\**.Default**\\**Environment**. Because the terminal server does not replicate this section of the registry, the installation does not set the per-user environment variables.
-   Because a server may be configured to prevent users from repairing applications, your application should handle the case of missing registry keys gracefully.

The following applies when a Windows Installer package that uses DLL, EXE, or Script [custom actions](custom-actions.md) is installed in the per-machine installation context on a terminal server. In this case, the installer sets the [**TerminalServer**](terminalserver.md) property.

-   Deferred custom actions run in the context of the local system unless the action has the **msidbCustomActionTypeTSAware** attribute. This is true even if the custom action impersonates the user on a system that is not a terminal server. Note that if a custom action having the **msidbCustomActionTypeTSAware** attribute changes the user's registry, the installer does not automatically ensure that those changes are also made in the registry of every user on the computer.
-   Any registry operations in a deferred custom action that read from the **HKCU** registry hive sees the system's default registry hive and not the current user's registry hive.
-   Any registry operations in a deferred custom action that write to **HKCU**\\**Software** are detected by the installer and copied to every user of the computer at the next logon of the user.
-   Any registry operations in a deferred custom action that write to **HKCU**, but are not under the **HKCU**\\**Software** registry key, are not detected by the installer or copied.

For more information, see [Terminal Services](../termserv/terminal-services-portal.md) in the Microsoft Windows Software Development Kit (SDK).

## Related topics

<dl> <dt>

[EnableAdminTSRemote](enableadmintsremote.md)
</dt> <dt>

[**TerminalServer property**](terminalserver.md)
</dt> <dt>

[**RemoteAdminTS property**](remoteadmints.md)
</dt> <dt>

[Terminal Services](../termserv/terminal-services-portal.md)
</dt> </dl>

 

 
