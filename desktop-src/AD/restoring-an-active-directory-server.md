---
title: Restoring an Active Directory Server
description: Active Directory servers must be restored offline.
ms.assetid: 91fbbdc1-0e84-4b89-8a38-4c8d0268992b
ms.tgt_platform: multiple
keywords:
- Restoring Active Directory Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Restoring an Active Directory Server

Active Directory servers must be restored offline. The system must be restarted in Directory Services Restore mode. In this mode, the operating system is running without Active Directory Domain Services and all user validation occurs through the Security Accounts Manager (SAM) in the registry. To restore Active Directory Domain Services, use the credentials of a local administrator on the domain controller that is restored.

The caller of the restore functions must have the **SE\_RESTORE\_NAME** access privilege. Use the [**DsSetAuthIdentity**](dssetauthidentity.md) function to set the security context under which the directory backup and restore functions are called.

Be aware that when you restore Active Directory Domain Services, you must also restore the other system state components.

**To restore Active Directory Domain Services**

1.  Call the [**DsIsNTDSOnline**](dsisntdsonline.md) function to determine if Active Directory Domain Services are running.
2.  If Active Directory Domain Services are not running, the [**DsRestorePrepare**](dsrestoreprepare.md) function is called to initialize the restore operation and obtain a backup context handle. If Active Directory Domain Services are running, it cannot be restored and the restore application must fail the restore operation. The **DsRestorePrepare** function requires that the expiry token be obtained from the [**DsBackupPrepare**](dsbackupprepare.md) function during the backup operation.
3.  Call the [**DsRestoreGetDatabaseLocations**](dsrestoregetdatabaselocations.md) function to determine the directories where the files are to be restored. If this function fails, restore the data back to the original backup source directory; that is the directory from which the data was backed up.
4.  Call the [**DsRestoreRegister**](dsrestoreregister.md) function to prepare the Active Directory server for the restore operation and lock the restore directories.
5.  Use standard Win32 functions to restore the files. First, delete all files in the destination directory; then copy the backup files to the destination directory.
6.  Call the [**DsRestoreRegisterComplete**](dsrestoreregistercomplete.md) function to indicate that the restore has completed.
7.  Call the [**DsRestoreEnd**](dsrestoreend.md) function to release any resources associated with the context.

After a restore in Directory Services Restore mode, the domain controller should be restarted in normal mode. When the directory service starts, the domain controller will perform the normal consistency check and the restored directory will then be online.

Be aware that restoring an Active Directory server is always a two-part operation. First, restore the database to a time when the backup was taken. Second, replicate the directory, where the newly restored DSA replicates post-backup updates from other DSAs in the domain and enterprise forest.

A computer running on Windows 2000 or Windows Server 2003, that contains a replica of the directory service, is a domain controller.

The [**DsRestoreRegister**](dsrestoreregister.md) function adds data to the registry that must survive the registry restoration process for the restoration to work correctly. To ensure this registry data is preserved, restore Active Directory Domain Services with the **DsRestore\*** functions prior to restarting the computer after the [**RegReplaceKey**](/windows/desktop/api/winreg/nf-winreg-regreplacekeya) function is called. This process works because **RegReplaceKey** does not actually replace the registry hive until the computer is restarted and the registry data added by the **DsRestoreRegister** function is specifically excluded from being replaced during a registry restore operation.

 

 