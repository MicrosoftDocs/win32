---
title: Backing Up an Active Directory Server
description: An Active Directory server backup requires you to back up the database and the transaction logs. This topic provides a walkthrough of how a backup application backs up the Active Directory directory service.
ms.assetid: 250b2f40-6d43-4aa5-a588-b0cd4839828d
ms.tgt_platform: multiple
keywords:
- backing up Active Directory
ms.topic: article
ms.date: 05/31/2018
---

# Backing Up an Active Directory Server

An Active Directory server backup requires you to back up the database and the transaction logs. This topic provides a walkthrough of how a backup application backs up the Active Directory directory service.

The caller of these backup functions must have the **SE\_BACKUP\_NAME** privilege. You can use the [**DsSetAuthIdentity**](dssetauthidentity.md) function to set the security context under which the directory backup/restore functions are called.

**To backup an Active Directory server, perform the following steps**

1.  Call the [**DsIsNTDSOnline**](dsisntdsonline.md) function to determine if Active Directory Domain Services are running.
2.  If Active Directory Domain Services are running, call the [**DsBackupPrepare**](dsbackupprepare.md) function to initialize a backup context handle. If Active Directory Domain Services are not running, it cannot be backed up and the backup application must fail the backup operation.
3.  Call the [**DsBackupGetDatabaseNames**](dsbackupgetdatabasenames.md) function to get a list of files to back up. To release the memory returned by this function, call the [**DsBackupFree**](dsbackupfree.md) function.
4.  For each name in the returned list of files, call the [**DsBackupOpenFile**](dsbackupopenfile.md) function followed by repeated calls to the [**DsBackupRead**](dsbackupread.md) function until the entire file has been read. When you have finished reading the file, call the [**DsBackupClose**](dsbackupclose.md) function to close it.
5.  After all database files are backed up, call the [**DsBackupGetBackupLogs**](dsbackupgetbackuplogs.md) function to get a list of transaction logs. This list is handled just like the list of database files.
6.  When you have finished backing up the transaction log, call the [**DsBackupTruncateLogs**](dsbackuptruncatelogs.md) function to delete all committed transaction logs that were backed up.
7.  Save the contents of the expiry token provided by the [**DsBackupPrepare**](dsbackupprepare.md) function. This can be saved in a file or some other persistent memory. This token must be passed to the [**DsRestorePrepare**](dsrestoreprepare.md) function to initiate a restore operation.
8.  Free the memory for the expiry token by passing the token pointer to the [**DsBackupFree**](dsbackupfree.md) function.
9.  Finally, call the [**DsBackupEnd**](dsbackupend.md) function to release all resources associated with the backup context handle.

 

 




