---
description: Learn about error codes that are returned by the Windows Installer functions MsiExec.exe and InstMsi.exe.
ms.assetid: 9ea81ef3-a5b5-4d13-b0b8-3da6e919315e
title: MsiExec.exe and InstMsi.exe error messages (for developers)
ms.topic: article
ms.date: 02/08/2023
---

# MsiExec.exe and InstMsi.exe error messages (for developers)

> [!NOTE]  
> This article is intended for software developers who use Windows Installer to build installer packages for their applications. If you're a user experiencing difficulty with your computer either during or after installing or uninstalling an application, you should contact customer support for the software you're trying to install or remove. If you need support for a Microsoft product, please go to our [technical support site](https://support.microsoft.com).

These error codes are returned by the Windows Installer functions *MsiExec.exe* and *InstMsi.exe*. Note that any error in *Winerror.h* (such as ERROR\_INVALID\_DATA) can be returned as well. For more error codes returned by the Windows Installer, see [Windows Installer error messages](windows-installer-error-messages.md).
 
The error codes ERROR\_SUCCESS, ERROR\_SUCCESS\_REBOOT\_INITIATED, and ERROR\_SUCCESS\_REBOOT\_REQUIRED indicate success. If ERROR\_SUCCESS\_REBOOT\_REQUIRED is returned, the installation completed successfully but a reboot is required to complete the installation operation.

| Error code                                 | Value | Description                           |
|--------------------------------------------|-------|---------------------------------------|
| ERROR\_SUCCESS                             | 0     | The action completed successfully.    |
| ERROR\_INVALID\_DATA                       | 13    | The data is invalid.                  |
| ERROR\_INVALID\_PARAMETER                  | 87    | One of the parameters was invalid.    |
| ERROR\_CALL\_NOT\_IMPLEMENTED              | 120   | This value is returned when a custom action attempts to call a function that can't be called from custom actions. The function returns the value ERROR\_CALL\_NOT\_IMPLEMENTED.     |
| ERROR\_APPHELP\_BLOCK                      | 1259  | If Windows Installer determines a product might be incompatible with the current operating system, it displays a dialog box informing the user and asking whether to try to install anyway. This error code is returned if the user chooses not to try the installation.        |
| ERROR\_INSTALL\_SERVICE\_FAILURE           | 1601  | The Windows Installer service couldn't be accessed. Contact your support personnel to verify that the Windows Installer service is properly registered.     |
| ERROR\_INSTALL\_USEREXIT                   | 1602  | The user canceled installation.   |
| ERROR\_INSTALL\_FAILURE                    | 1603  | A fatal error occurred during installation.    |
| ERROR\_INSTALL\_SUSPEND                    | 1604  | Installation suspended, incomplete.      |
| ERROR\_UNKNOWN\_PRODUCT                    | 1605  | This action is only valid for products that are currently installed.   |
| ERROR\_UNKNOWN\_FEATURE                    | 1606  | The feature identifier isn't registered.      |
| ERROR\_UNKNOWN\_COMPONENT                  | 1607  | The component identifier isn't registered.        |
| ERROR\_UNKNOWN\_PROPERTY                   | 1608  | This is an unknown property.     |
| ERROR\_INVALID\_HANDLE\_STATE              | 1609  | The handle is in an invalid state.      |
| ERROR\_BAD\_CONFIGURATION                  | 1610  | The configuration data for this product is corrupt. Contact your support personnel.     |
| ERROR\_INDEX\_ABSENT                       | 1611  | The component qualifier not present.    |
| ERROR\_INSTALL\_SOURCE\_ABSENT             | 1612  | The installation source for this product isn't available. Verify that the source exists and that you can access it.     |
| ERROR\_INSTALL\_PACKAGE\_VERSION           | 1613  | This installation package can't be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.    |
| ERROR\_PRODUCT\_UNINSTALLED                | 1614  | The product is uninstalled.   |
| ERROR\_BAD\_QUERY\_SYNTAX                  | 1615  | The SQL query syntax is invalid or unsupported.    |
| ERROR\_INVALID\_FIELD                      | 1616  | The record field does not exist.    |
| ERROR\_INSTALL\_ALREADY\_RUNNING           | 1618  | Another installation is already in progress. Complete that installation before proceeding with this install. For information about the mutex, see [\_MSIExecute Mutex](-msiexecute-mutex.md).    |
| ERROR\_INSTALL\_PACKAGE\_OPEN\_FAILED      | 1619  | This installation package couldn't be opened. Verify that the package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer package.           |
| ERROR\_INSTALL\_PACKAGE\_INVALID           | 1620  | This installation package couldn't be opened. Contact the application vendor to verify that this is a valid Windows Installer package.  |
| ERROR\_INSTALL\_UI\_FAILURE                | 1621  | There was an error starting the Windows Installer service user interface. Contact your support personnel.   |
| ERROR\_INSTALL\_LOG\_FAILURE               | 1622  | There was an error opening installation log file. Verify that the specified log file location exists and is writable.    |
| ERROR\_INSTALL\_LANGUAGE\_UNSUPPORTED      | 1623  | This language of this installation package isn't supported by your system.   |
| ERROR\_INSTALL\_TRANSFORM\_FAILURE         | 1624  | There was an error applying transforms. Verify that the specified transform paths are valid.    |
| ERROR\_INSTALL\_PACKAGE\_REJECTED          | 1625  | This installation is forbidden by system policy. Contact your system administrator.    |
| ERROR\_FUNCTION\_NOT\_CALLED               | 1626  | The function couldn't be executed.     |
| ERROR\_FUNCTION\_FAILED                    | 1627  | The function failed during execution.     |
| ERROR\_INVALID\_TABLE                      | 1628  | An invalid or unknown table was specified.   |
| ERROR\_DATATYPE\_MISMATCH                  | 1629  | The data supplied is the wrong type.    |
| ERROR\_UNSUPPORTED\_TYPE                   | 1630  | Data of this type isn't supported.     |
| ERROR\_CREATE\_FAILED                      | 1631  | The Windows Installer service failed to start. Contact your support personnel.    |
| ERROR\_INSTALL\_TEMP\_UNWRITABLE           | 1632  | The Temp folder is either full or inaccessible. Verify that the *Temp* folder exists and that you can write to it.    |
| ERROR\_INSTALL\_PLATFORM\_UNSUPPORTED      | 1633  | This installation package isn't supported on this platform. Contact your application vendor.     |
| ERROR\_INSTALL\_NOTUSED                    | 1634  | Component isn't used on this machine.                    |
| ERROR\_PATCH\_PACKAGE\_OPEN\_FAILED        | 1635  | This patch package couldn't be opened. Verify that the patch package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer patch package.    |
| ERROR\_PATCH\_PACKAGE\_INVALID             | 1636  | This patch package couldn't be opened. Contact the application vendor to verify that this is a valid Windows Installer patch package.         |
| ERROR\_PATCH\_PACKAGE\_UNSUPPORTED         | 1637  | This patch package can't be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.    |
| ERROR\_PRODUCT\_VERSION                    | 1638  | Another version of this product is already installed. Installation of this version can't continue. To configure or remove the existing version of this product, use **Add/Remove Programs** in **Control Panel**.     |
| ERROR\_INVALID\_COMMAND\_LINE              | 1639  | Invalid command line argument. Consult the Windows Installer SDK for detailed command-line help.    |
| ERROR\_INSTALL\_REMOTE\_DISALLOWED         | 1640  | The current user isn't permitted to perform installations from a client session of a server running the Terminal Server role service.     |
| ERROR\_SUCCESS\_REBOOT\_INITIATED          | 1641  | The installer has initiated a restart. This message indicates success.   |
| ERROR\_PATCH\_TARGET\_NOT\_FOUND           | 1642  | The installer can't install the upgrade patch because the program being upgraded may be missing or the upgrade patch updates a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch. |
| ERROR\_PATCH\_PACKAGE\_REJECTED            | 1643  | The patch package isn't permitted by system policy.             |
| ERROR\_INSTALL\_TRANSFORM\_REJECTED        | 1644  | One or more customizations aren't permitted by system policy.   |
| ERROR\_INSTALL\_REMOTE\_PROHIBITED         | 1645  | Windows Installer doesn't permit installation from a Remote Desktop Connection.    |
| ERROR\_PATCH\_REMOVAL\_UNSUPPORTED         | 1646  | The patch package isn't a removable patch package.      |
| ERROR\_UNKNOWN\_PATCH                      | 1647  | The patch isn't applied to this product.        |
| ERROR\_PATCH\_NO\_SEQUENCE                 | 1648  | No valid sequence could be found for the set of patches.      |
| ERROR\_PATCH\_REMOVAL\_DISALLOWED          | 1649  | Patch removal was disallowed by policy.       |
| ERROR\_INVALID\_PATCH\_XML                 | 1650  | The XML patch data is invalid.     |
| ERROR\_PATCH\_MANAGED\_ADVERTISED\_PRODUCT | 1651  | Administrative user failed to apply patch for a per-user managed or a per-machine application that'is in advertised state.     |
| ERROR\_INSTALL\_SERVICE\_SAFEBOOT          | 1652  | Windows Installer isn't accessible when the computer is in *Safe Mode*. Exit Safe Mode and try again or try using [system restore](/windows/desktop/sr/system-restore-portal) to return your computer to a previous state. Available beginning with Windows Installer version 4.0.          |
| ERROR\_ROLLBACK\_DISABLED                  | 1653  | Couldn't perform a multiple-package transaction because rollback has been disabled. [Multiple-package installations](multiple-package-installations.md) can't run if rollback is disabled. Available beginning with Windows Installer version 4.5.   |
| ERROR\_INSTALL\_REJECTED                   | 1654  | The app that you're trying to run isn't supported on this version of Windows. A Windows Installer package, patch, or transform that has not been signed by Microsoft can't be installed on an ARM computer.    |
| ERROR\_SUCCESS\_REBOOT\_REQUIRED           | 3010  | A restart is required to complete the install. This message indicates success. This does not include installs where the [ForceReboot](forcereboot-action.md) action is run.     |


