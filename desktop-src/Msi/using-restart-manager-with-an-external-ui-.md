---
description: Windows Installer developers can prepare their installation package to work with Restart Manager by following the guidelines described in Using Windows Installer with Restart Manager.
ms.assetid: 777f8864-b3d2-43c7-9296-1118f3595d7b
title: Using Restart Manager with an External UI
ms.topic: article
ms.date: 05/31/2018
---

# Using Restart Manager with an External UI

Windows Installer developers can prepare their installation package to work with [Restart Manager](../rstmgr/restart-manager-portal.md) by following the guidelines described in [Using Windows Installer with Restart Manager](using-windows-installer-with-restart-manager.md).

Specify the INSTALLLOGMODE\_RMFILESINUSE message type when calling the [**MsiSetExternalUI**](/windows/desktop/api/Msi/nf-msi-msisetexternaluia) or [**MsiSetExternalUIRecord**](/windows/desktop/api/Msi/nf-msi-msisetexternaluirecord) function to enable the external user-interface handler. Windows Installer then sends an INSTALLMESSAGE\_RMFILESINUSE message for use by external user-interface handlers that support the [Restart Manager](../rstmgr/restart-manager-portal.md).

Your external user-interface handler should handle the information contained in INSTALLMESSAGE\_RMFILESINUSE messages. If no registered or internal user-interface handles the INSTALLMESSAGE\_RMFILESINUSE message, Windows Installer sends an INSTALLMESSAGE\_FILESINUSE message for use by existing external handlers that support INSTALLMESSAGE\_FILESINUSE messages and the [FilesInUse](filesinuse-dialog.md) dialog box.

The external user interface can return the values listed in the following table.



| External UI return value | Action taken by Windows Installer                                                                                                                                                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IDOK                     | The **OK** button was pressed by the user. The Windows Installer will request that the [Restart Manager](../rstmgr/restart-manager-portal.md) shut down and restart the applications that hold files currently in use.                                                                                                                                               |
| IDCANCEL                 | The **CANCEL** button was pressed. Cancel the installation.                                                                                                                                                                                                                                                                                    |
| IDIGNORE                 | The **IGNORE** button was pressed. Ignore and continue the installation. A restart will be required at the end of the installation.                                                                                                                                                                                                            |
| IDNO                     | The **NO** button was pressed. If the package has an [MsiRMFilesInUse](msirmfilesinuse-dialog.md) dialog box, send a 1610 message. For more information, see [Windows Installer Error Messages](windows-installer-error-messages.md). If the package does not have a MsiRMFilesInUse dialog box, send an INSTALLMESSAGE\_FILESINUSE message. |
| IDRETRY                  | The **RETRY** button was pressed. Send the INSTALLMESSAGE\_FILESINUSE message.                                                                                                                                                                                                                                                                 |
| -1                       | An error. End the installation.                                                                                                                                                                                                                                                                                                                |



 

 

 
