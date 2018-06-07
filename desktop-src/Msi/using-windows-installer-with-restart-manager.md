---
Description: Applications that use Windows Installer 4.0 for installation and servicing on Windows Vista automatically use the Restart Manager to reduce system restarts.
ms.assetid: 821739ff-f7a7-4192-ad34-254aa7d74d13
title: Using Windows Installer with Restart Manager
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using Windows Installer with Restart Manager

Applications that use Windows Installer 4.0 for installation and servicing on Windows Vista automatically use the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5) to reduce system restarts. The default behavior on Windows Vista is to shut down applications rather than shut down and restart the operating system whenever possible. In cases where a system restart is unavoidable, installers can use the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5) API to schedule restarts in such a way that it minimizes the disruption of the user's work flow.

Windows Installer developers can perform the following actions to prepare their package to work with the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5).

-   Add the [MsiRMFilesInUse](msirmfilesinuse-dialog.md) dialog box to your package. If the MsiRMFilesInUse dialog box is present in the package, the Windows Vista user running an installation at the Full UI [user interface level](user-interface-levels.md) is given the option to automatically close and restart applications. An installation package can contain information for both the MsiRMFilesInUse dialog box and the [FilesInUse](filesinuse-dialog.md) dialog box . The MsiRMFilesInUse dialog box is only displayed if the package is installed with at least Windows Installer 4.0 on Windows Vista, and is otherwise ignored. Existing packages that do not have the MsiRMFilesInUse dialog box continue to function using the FilesInUse dialog box. A customization transform can be used to add an MsiRMFilesInUse dialog box to existing packages.

    End-users typically run installations at the Full UI [user interface level](user-interface-levels.md). Basic UI or Reduced UI level installations give the user the option of using the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5) to reduce system restarts even if the [MsiRMFilesInUse](msirmfilesinuse-dialog.md) dialog box is not present. Silent UI level installations always shut down applications and services, and on Windows Vista, always use Restart Manager.

-   Register applications for a restart using the [**RegisterApplicationRestart**](f4cd25b3-2aee-460f-9f9f-b45ecded094f) function. Restart Manager can only restart applications that have been registered for restart. Restart Manager restarts registered applications after the installation. If the installation requires a system restart, Restart Manager restarts the registered application after the system restart.
-   Specify INSTALLLOGMODE\_RMFILESINUSE when enabling an external user-interface handler with the [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia) and [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord) functions. Windows Installer will send a INSTALLMESSAGE\_RMFILESINUSE message for external user-interface handlers that support the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5). If no registered or internal user-interface handles the INSTALLMESSAGE\_RMFILESINUSE message, the installer sends a INSTALLMESSAGE\_FILESINUSE message for user-interface handlers that support the [FilesInUse](filesinuse-dialog.md) dialog box. For more information, see [Using Restart Manager with an External UI](using-restart-manager-with-an-external-ui-.md).
-   Custom actions can add resources belonging to a [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5) session. The custom action should be sequenced before the [InstallValidate](installvalidate-action.md) action. Custom actions can use the [**MsiRestartManagerSessionKey**](msirestartmanagersessionkey.md) property to obtain the session key, and should call the [**RmJoinSession**](https://msdn.microsoft.com/f9cb2d81-a2bc-4bb7-920a-1630354ea942) and [**RmEndSession**](https://msdn.microsoft.com/2681cb69-a66f-4aec-a164-98d2d28f9908) functions of the Restart Manager API. Custom actions cannot remove resources belonging to a Restart Manager session. Custom actions should not attempt to shutdown or restart applications using the [**RmShutdown**](https://msdn.microsoft.com/cdbc3bb7-0b3c-4fbc-8023-45a309c65bae), [**RmGetList**](https://msdn.microsoft.com/de4feea4-2b45-4430-a4b3-8ca26c455e42) and [**RmRestart**](https://msdn.microsoft.com/e0939b31-0233-40d2-96cf-bbabe9488a12) functions.
-   Package authors can base a condition in the [LaunchCondition table](launchcondition-table.md) on the [**MsiSystemRebootPending**](msisystemrebootpending.md) property to prevent the installation of their package when a system restart is pending.
-   Package authors and administrators can control the interaction of the Windows Installer and Restart Manager by using the [**MSIRESTARTMANAGERCONTROL**](msirestartmanagercontrol.md), [**MSIDISABLERMRESTART**](msidisablermrestart.md), [**MSIRMSHUTDOWN**](msirmshutdown.md) properties and the [DisableAutomaticApplicationShutdown](disableautomaticapplicationshutdown.md) policy.
-   Applications and services should follow the guidelines described in the [Using Restart Manager](https://msdn.microsoft.com/78448d5e-20f6-45b6-b833-7d7791e5e4c6) section of the [Restart Manager](44b7975a-0093-4c8f-9a14-2a6bfd7a68a5) documentation.

 

 



