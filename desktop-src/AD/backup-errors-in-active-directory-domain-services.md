---
title: Backup Errors in Active Directory Domain Services
description: This topic lists backup error return values for functions in Active Directory Domain Services.
ms.assetid: d042f189-1b86-42ca-bdb4-a8aaa96c9c65
ms.tgt_platform: multiple
keywords:
- Active Directory Backup Errors
- Active Directory Domain Service Backup Errors
ms.topic: article
ms.date: 05/31/2018
---

# Backup Errors in Active Directory Domain Services

This topic lists backup error return values for functions in Active Directory Domain Services.



| Value                                      | Description                                                                                                                                                                                  |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **hrNyi**<br/>                       | The function is not implemented.<br/>                                                                                                                                                  |
| **hrInvalidParam**<br/>              | The parameter is not valid.<br/>                                                                                                                                                       |
| **hrError**<br/>                     | An internal error occurred.<br/>                                                                                                                                                       |
| **hrInvalidHandle**<br/>             | The handle is not valid.<br/>                                                                                                                                                          |
| **hrRestoreInProgress**<br/>         | The restore process is in progress.<br/>                                                                                                                                               |
| **hrAlreadyOpen**<br/>               | The specified file is open.<br/>                                                                                                                                                       |
| **hrInvalidRecips**<br/>             | The recipients are not valid. <br/>                                                                                                                                                    |
| **hrCouldNotConnect**<br/>           | Unable to backup. A connection to the specified backup server was not detected or the service you are attempting to back up is not running.<br/>                                       |
| **hrRestoreMapExists**<br/>          | A restore map exists for the specified component. A restore map can be specified when performing a full restore.<br/>                                                                  |
| **hrIncrementalBackupDisabled**<br/> | Another application has modified the specified Windows NT/Windows 2000 Directory Service database such that any subsequent backups will fail. To fix this, perform a full backup.<br/> |
| **hrLogFileNotFound**<br/>           | Unable to perform an incremental backup because a required Windows NT/Windows 2000 Directory Service database log file could not be found.<br/>                                        |
| **hrCircularLogging**<br/>           | The Windows NT/Windows 2000 Directory Service component specified is configured to use circular database logs. It cannot be backed up incrementally. Perform a full backup.<br/>       |
| **hrNoFullRestore**<br/>             | The databases have not been restored to this computer. You cannot restore an incremental backup until a full backup has been restored.<br/>                                            |
| **hrCommunicationError**<br/>        | A communications error occurred while attempting to perform a local backup.<br/>                                                                                                       |
| **hrFullBackupNotTaken**<br/>        | You must perform a full backup before you can perform an incremental backup.<br/>                                                                                                      |
| **hrMissingExpiryToken**<br/>        | Expiry token is missing. Cannot restore without the expiry data.<br/>                                                                                                                  |
| **hrUnknownExpiryTokenFormat**<br/>  | Expiry token is in an unrecognizable format.<br/>                                                                                                                                      |
| **hrContentsExpired**<br/>           | DS Contents in the backup are out of date. Restore with a recent copy.<br/>                                                                                                            |



 

## See Also

[Success](success.md), [System Errors in Active Directory Domain Services](system-errors-in-active-directory-domain-services.md), [Directory Manager Errors](directory-manager-errors.md), [Logging and Recovery Errors in Functions in Active Directory Domain Services](logging-and-recovery-errors-in-functions-in-active-directory-domain-services.md), [Return Values for Functions in Active Directory Domain Services](return-values-for-functions-in-active-directory-domain-services.md)


 

 





