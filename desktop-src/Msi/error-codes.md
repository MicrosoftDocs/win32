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

These error codes are returned by the Windows Installer functions *MsiExec.exe* and *InstMsi.exe*. Note that any error in *Winerror.h* (such as `ERROR_INVALID_DATA`, included here) can be returned as well. For more error codes returned by the Windows Installer, see [Windows Installer error messages](windows-installer-error-messages.md).
 
The error codes `ERROR_SUCCESS`, `ERROR_SUCCESS_REBOOT_INITIATED`, and `ERROR_SUCCESS_REBOOT_REQUIRED` indicate success. If `ERROR_SUCCESS_REBOOT_REQUIRED` is returned, the installation completed successfully but a reboot is required to complete the installation operation.

| Error code                                 | Value | Description                           |
|--------------------------------------------|-------|---------------------------------------|
| `ERROR_SUCCESS`                            | 0     | The action completed successfully.    |
| `ERROR_INVALID_DATA`                       | 13    | The data is invalid.                  |
| `ERROR_INVALID_PARAMETER`                  | 87    | One of the parameters was invalid.    |
| `ERROR_CALL_NOT_IMPLEMENTED`               | 120   | This value is returned when a custom action attempts to call a function that cannot be called from custom actions. The function returns the value `ERROR_CALL_NOT_IMPLEMENTED`.     |
| `ERROR_APPHELP_BLOCK`                      | 1259  | If Windows Installer determines a product might be incompatible with the current operating system, it displays a dialog box informing the user and asking whether to try to install anyway. This error code is returned if the user chooses not to try the installation.        |
| `ERROR_INSTALL_SERVICE_FAILURE`            | 1601  | The Windows Installer service could not be accessed. Contact your support personnel to verify that the Windows Installer service is properly registered.     |
| `ERROR_INSTALL_USEREXIT`                   | 1602  | The user cancels installation.   |
| `ERROR_INSTALL_FAILURE`                    | 1603  | A fatal error occurred during installation.    |
| `ERROR_INSTALL_SUSPEND`                    | 1604  | Installation suspended, incomplete.      |
| `ERROR_UNKNOWN_PRODUCT`                    | 1605  | This action is only valid for products that are currently installed.   |
| `ERROR_UNKNOWN_FEATURE`                    | 1606  | The feature identifier isn't registered.      |
| `ERROR_UNKNOWN_COMPONENT`                  | 1607  | The component identifier isn't registered.        |
| `ERROR_UNKNOWN_PROPERTY`                   | 1608  | This is an unknown property.     |
| `ERROR_INVALID_HANDLE_STATE`               | 1609  | The handle is in an invalid state.      |
| `ERROR_BAD_CONFIGURATION`                  | 1610  | The configuration data for this product is corrupt. Contact your support personnel.     |
| `ERROR_INDEX_ABSENT`                       | 1611  | The component qualifier not present.    |
| `ERROR_INSTALL_SOURCE_ABSENT`              | 1612  | The installation source for this product isn't available. Verify that the source exists and that you can access it.     |
| `ERROR_INSTALL_PACKAGE_VERSION`            | 1613  | This installation package cannot be installed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.    |
| `ERROR_PRODUCT_UNINSTALLED`                | 1614  | The product is uninstalled.   |
| `ERROR_BAD_QUERY_SYNTAX`                   | 1615  | The SQL query syntax is invalid or unsupported.    |
| `ERROR_INVALID_FIELD`                      | 1616  | The record field does not exist.    |
| `ERROR_INSTALL_ALREADY_RUNNING`            | 1618  | Another installation is already in progress. Complete that installation before proceeding with this install.For information about the mutex, see [\_MSIExecute Mutex](-msiexecute-mutex.md).    |
| `ERROR_INSTALL_PACKAGE_OPEN_FAILED`        | 1619  | This installation package could not be opened. Verify that the package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer package.           |
| `ERROR_INSTALL_PACKAGE_INVALID`            | 1620  | This installation package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer package.  |
| `ERROR_INSTALL_UI_FAILURE`                 | 1621  | There was an error starting the Windows Installer service user interface. Contact your support personnel.   |
| `ERROR_INSTALL_LOG_FAILURE`                | 1622  | There was an error opening installation log file. Verify that the specified log file location exists and is writable.    |
| `ERROR_INSTALL_LANGUAGE_UNSUPPORTED`       | 1623  | This language of this installation package is not supported by your system.   |
| `ERROR_INSTALL_TRANSFORM_FAILURE`          | 1624  | There was an error applying transforms. Verify that the specified transform paths are valid.    |
| `ERROR_INSTALL_PACKAGE_REJECTED`          | 1625  | This installation is forbidden by system policy. Contact your system administrator.    |
| `ERROR_FUNCTION_NOT_CALLED`               | 1626  | The function could not be executed.     |
| `ERROR_FUNCTION_FAILED`                    | 1627  | The function failed during execution.     |
| `ERROR_INVALID_TABLE`                      | 1628  | An invalid or unknown table was specified.   |
| `ERROR_DATATYPE_MISMATCH`                  | 1629  | The data supplied is the wrong type.    |
| `ERROR_UNSUPPORTED_TYPE`                   | 1630  | Data of this type is not supported.     |
| `ERROR_CREATE_FAILED`                      | 1631  | The Windows Installer service failed to start. Contact your support personnel.    |
| `ERROR_INSTALL_TEMP_UNWRITABLE`            | 1632  | The Temp folder is either full or inaccessible. Verify that the *Temp* folder exists and that you can write to it.    |
| `ERROR_INSTALL_PLATFORM_UNSUPPORTED`       | 1633  | This installation package is not supported on this platform. Contact your application vendor.     |
| `ERROR_INSTALL_NOTUSED`                    | 1634  | Component is not used on this machine.                    |
| `ERROR_PATCH_PACKAGE_OPEN_FAILED`          | 1635  | This patch package could not be opened. Verify that the patch package exists and is accessible, or contact the application vendor to verify that this is a valid Windows Installer patch package.    |
| `ERROR_PATCH_PACKAGE_INVALID`              | 1636  | This patch package could not be opened. Contact the application vendor to verify that this is a valid Windows Installer patch package.         |
| `ERROR_PATCH_PACKAGE_UNSUPPORTED`          | 1637  | This patch package cannot be processed by the Windows Installer service. You must install a Windows service pack that contains a newer version of the Windows Installer service.    |
| `ERROR_PRODUCT_VERSION`                    | 1638  | Another version of this product is already installed. Installation of this version cannot continue. To configure or remove the existing version of this product, use **Add/Remove Programs** in **Control Panel**.     |
| `ERROR_INVALID_COMMAND_LINE`               | 1639  | Invalid command line argument. Consult the Windows Installer SDK for detailed command-line help.    |
| `ERROR_INSTALL_REMOTE_DISALLOWED`          | 1640  | The current user isn't permitted to perform installations from a client session of a server running the Terminal Server role service.     |
| `ERROR_SUCCESS_REBOOT_INITIATED`           | 1641  | The installer has initiated a restart. This message is indicative of a success.   |
| `ERROR_PATCH_TARGET_NOT_FOUND`             | 1642  | The installer can't install the upgrade patch because the program being upgraded may be missing or the upgrade patch updates a different version of the program. Verify that the program to be upgraded exists on your computer and that you have the correct upgrade patch. |
| `ERROR_PATCH_PACKAGE_REJECTED`             | 1643  | The patch package isn't permitted by system policy.             |
| `ERROR_INSTALL_TRANSFORM_REJECTED`         | 1644  | One or more customizations aren't permitted by system policy.   |
| `ERROR_INSTALL_REMOTE_PROHIBITED`          | 1645  | Windows Installer doesn't permit installation from a Remote Desktop Connection.    |
| `ERROR_PATCH_REMOVAL_UNSUPPORTED`          | 1646  | The patch package isn't a removable patch package.      |
| `ERROR_UNKNOWN_PATCH`                      | 1647  | The patch isn't applied to this product.        |
| `ERROR_PATCH_NO_SEQUENCE`                  | 1648  | No valid sequence could be found for the set of patches.      |
| `ERROR_PATCH_REMOVAL_DISALLOWED`           | 1649  | Patch removal was disallowed by policy.       |
| `ERROR_INVALID_PATCH_XML`                  | 1650  | The XML patch data is invalid.     |
| `ERROR_PATCH_MANAGED_ADVERTISED_PRODUCT`   | 1651  | Administrative user failed to apply patch for a per-user managed or a per-machine application that'is in advertised state.     |
| `ERROR_INSTALL_SERVICE_SAFEBOOT`           | 1652  | Windows Installer is not accessible when the computer is in Safe Mode. Exit Safe Mode and try again or try using [system restore](/windows/desktop/sr/system-restore-portal) to return your computer to a previous state. Available beginning with Windows Installer version 4.0.          |
| `ERROR_ROLLBACK_DISABLED`                  | 1653  | Couldn't perform a multiple-package transaction because rollback has been disabled. [Multiple-package installations](multiple-package-installations.md) can't run if rollback is disabled. Available beginning with Windows Installer version 4.5.   |
| `ERROR_INSTALL_REJECTED`                   | 1654  | The app that you're trying to run isn't supported on this version of Windows. A Windows Installer package, patch, or transform that has not been signed by Microsoft cannot be installed on an ARM computer.    |
| `ERROR_SUCCESS_REBOOT_REQUIRED`            | 3010  | A restart is required to complete the install. This message is indicative of a success. This does not include installs where the [ForceReboot](forcereboot-action.md) action is run.     |


