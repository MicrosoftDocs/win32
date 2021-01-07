---
description: The Windows Installer can determine when a reboot of the system is necessary and automatically prompt the user to reboot at the end of the installation.
ms.assetid: 10117d2c-c2c8-456f-9fce-a89c2d69d3c1
title: System Reboots
ms.topic: article
ms.date: 05/31/2018
---

# System Reboots

The Windows Installer can determine when a reboot of the system is necessary and automatically prompt the user to reboot at the end of the installation. For example, the installer automatically prompts for a reboot if it needs to replace any files that are in use during the installation.

Applications that use [Windows Installer](windows-installer-portal.md) version 4.0 or later for installation and servicing automatically use the [Restart Manager](../rstmgr/restart-manager-portal.md) to reduce system restarts. Windows Installer version 4.0 or later has properties and policies that enable the package author and administrators to control the interaction of Windows Installer with the Restart Manager. For more information, see [Using Windows Installer with Restart Manager](using-windows-installer-with-restart-manager.md).

Installation package authors can schedule and suppress reboots by using standard actions in the sequence tables and by setting properties. The following actions and properties are used to handle system reboots.



| Action, dialog box, or property                                                | Brief description                                                                                                                                             |
|--------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [ForceReboot Action](forcereboot-action.md)                                   | Prompts the user for a reboot during the installation.                                                                                                        |
| [ScheduleReboot Action](schedulereboot-action.md)                             | Prompts the user for a reboot at the end of the installation.                                                                                                 |
| [**REBOOT Property**](reboot.md)                                              | Forces or suppresses certain automatic prompts for a system reboot.                                                                                           |
| [**REBOOTPROMPT Property**](rebootprompt.md)                                  | Suppresses the display of prompts for reboots to the user. Any needed reboots happen automatically.                                                           |
| [**AFTERREBOOT Property**](afterreboot.md)                                    | Commonly used in a condition imposed on the ForceReboot Action.                                                                                               |
| [InstallValidate Action](installvalidate-action.md)                           | Displays the FilesInUse Dialog, if necessary, giving users the opportunity to shut down processes and avoid some system reboots.                              |
| [FilesInUse Dialog](filesinuse-dialog.md)                                     | Gives users the opportunity to shut down processes to avoid some system reboots.                                                                              |
| [MsiRMFilesInUse Dialog](msirmfilesinuse-dialog.md)                           | Gives users the option to use the [Restart Manager](../rstmgr/restart-manager-portal.md) to close and restart applications. Available beginning with Windows Installer version 4.0. |
| [**ReplacedInUseFiles Property**](replacedinusefiles.md)                      | Set if the installer installs over a file in use. This property is used by custom actions to detect that a reboot is required.                                |
| [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md)                   | Property to disable Windows Installer interaction with the [Restart Manager](../rstmgr/restart-manager-portal.md). Available beginning with Windows Installer version 4.0.          |
| [**MSIDISABLERMRESTART**](msidisablermrestart.md)                             | Specifies how the [Restart Manager](../rstmgr/restart-manager-portal.md) closes and restarts applications. Available beginning with Windows Installer version 4.0.                  |
| [**MSIRMSHUTDOWN**](msirmshutdown.md)                                         | Specifies how the [Restart Manager](../rstmgr/restart-manager-portal.md) closes and restarts applications. Available beginning with Windows Installer version 4.0.                  |
| [**MsiSystemRebootPending**](msisystemrebootpending.md)                       | Installer sets this property if a restart of the operating system is pending. Available beginning with Windows Installer version 4.0.                         |
| [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md) | Policy to disable Windows Installer interaction with [Restart Manager](../rstmgr/restart-manager-portal.md). Available beginning with Windows Installer version 4.0.                |



 

ERROR\_INSTALL\_SUSPEND means the installation did not complete or rollback. The installation must resume before it is completed. The system may need to be rebooted before the installation can resume.

The Windows Installer returns the error code ERROR\_INSTALL\_SUSPEND when the [ForceReboot action](forcereboot-action.md) is run. It returns ERROR\_SUCCESS\_REBOOT\_REQUIRED if a reboot is required before running the application, and it returns ERROR\_SUCCESS\_REBOOT\_INITIATED if the installer has actually started a reboot. Note that because reboots are asynchronous, the reboot may actually occur before the error code is returned. For more information, see [Error Codes](error-codes.md).

Custom actions can force a prompt for reboot at the end of an installation by calling [**MsiSetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msisetmode). Custom actions can also check for a pending reboot prompt by calling [**MsiGetMode**](/windows/desktop/api/Msiquery/nf-msiquery-msigetmode).

## FilesInUse Dialog

The installer can determine when a reboot of the system is necessary and prompt the user with a request to reboot. Commonly, a system reboot is required because the installer is attempting to install a file that is currently being used. If the [InstallValidate action](installvalidate-action.md) detects the installation of a file in use it displays the [FilesInUse Dialog](filesinuse-dialog.md).

If you expect the installer to display a FilesInUseDialog, but it does not, this may be due to one of the following reasons:

-   The files in use are not executables.
-   The installer is not actually trying to install those files.
-   The process holding those files is the process invoking the installation.
-   The process holding those files is one that does not have a window with a title associated with it.

For more information, see [Logging of Reboot Requests](logging-of-reboot-requests.md).

 

 
