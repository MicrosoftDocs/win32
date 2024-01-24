---
description: Shows how the Certificate Services backup functions can be used to restore and recover a Certificate Services database and its associated files.
ms.assetid: f4914f45-629d-4f24-8328-d7f27e8a0062
title: Restoring Certificate Services from Backup
ms.topic: article
ms.date: 05/31/2018
---

# Restoring Certificate Services from Backup

The following scenario shows how the Certificate Services backup functions can be used to restore and recover a Certificate Services database and its associated files. The restoration process involves writing the files contained in a backup set to disk. You may restore multiple backup sets (one full backup plus zero or more incremental backups), but all restores must be complete prior to beginning the recovery process. The recovery process involves Certificate Services replaying log files to ensure database and log file consistency, thereby ensuring database integrity. The scenario illustrates the function calls to restore the backup sets and inform Certificate Services of the recovery parameters.

An existing full backup of the Certificate Services database must exist before implementing this scenario.

1.  Load the Certadm.dll library into memory (by calling [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya)).
2.  Retrieve the address of each of the necessary functions in Certadm.dll (by means of [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress)). Use these addresses when calling the functions in the remaining steps.
3.  Call [**CertSrvIsServerOnline**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvisserveronlinew) to determine whether Certificate Services is online. If Certificate Services is running, shut it down before proceeding. Certificate Services must not be online for the restore operations to be successful.
4.  Call [**CertSrvRestorePrepare**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestorepreparew) to begin a restore session. The resulting Certificate Services backup context handle will be used by several of the other functions.
5.  Determine the path for the database location. During a backup scenario, this value would have been available from a call to [**CertSrvRestoreGetDatabaseLocations**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoregetdatabaselocationsw); this value should have been stored as part of the backup.
6.  Create a restore map specifying the name of the restored database. A Certificate Services database restore map structure (CSEDB\_RSTMAPW) is used to specify a restore map. Set the CSEDB\_RSTMAPW's **pwszDatabaseName** member and the CSEDB\_RSTMAPW's **pwszNewDatabaseName** member to the database location determined in step 5. Optionally, if the restored database is to have a different name than the backup database, set the CSEDB\_RSTMAPW's **pwszNewDatabaseName** member to the new database name.
7.  If you want to ensure that modifications made to the database after the backup was performed are not reapplied after database restore is complete (as part of database recovery performed during the next Certificate Services startup), delete files from the target server's active database and log directories.
8.  Copy the files contained in the full backup to the target server's active database and log directories.
9.  Call [**CertSrvRestoreRegister**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregisterw) to register a restore operation for the full backup. **CertSrvRestoreRegister** uses the restore map specified in step 6. **CertSrvRestoreRegister** also specifies the location of the backup database and logs. Calling **CertSrvRestoreRegister** will force Certificate Services to attempt a restore operation the next time it is started. It also prevents Certificate Services from processing Certificate Requests until the restoration is complete.
10. Call [**CertSrvRestoreRegisterComplete**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregistercomplete), thereby finishing the registration activity that started in step 8. Note that the registration of a restore operation is an instruction for Certificate Services to follow when it is started; the actual recovery will take place only after Certificate Services is started.
11. For each incremental backup to be restored, copy the files contained in the incremental backup to the target server's active log directory, then call [**CertSrvRestoreRegister**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregisterw), followed by a call to [**CertSrvRestoreRegisterComplete**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreregistercomplete). The registration of the incremental backups for restoration can occur in any order, but only the set of files for one incremental backup should be copied to the server before each call to **CertSrvRestoreRegister**.
12. Copy the Certificate Services dynamic files to the target server. The dynamic files would have been identified during the backup when [**CertSrvBackupGetDynamicFileList**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvbackupgetdynamicfilelistw) was called. It may be necessary to stop the World Wide Web Publishing Service to allow overwriting the dynamic files.
13. Call [**CertSrvRestoreEnd**](/windows/desktop/api/Certbcli/nf-certbcli-certsrvrestoreend) to end the restore session.
14. Start the Certificate Services application manually (or wait until the next restart for it to start automatically). When Certificate Services starts, it will determine whether a restore operation has been registered; if a restore operation has been registered, Certificate Services will begin the recovery. Certificate Services will not process any certificate requests until the recovery operation is completed.

> [!Note]  
> When a recovery is complete, it is important that you make a new full backup of the Certificate Services database. This is necessary to truncate the restored log files and to establish a base backup set for future restores. Backups performed after a restore cannot be mixed with backups (full or incremental) taken before the restore; that is, after a certificate services database is restored and has progressed to a subsequent state, you cannot use the pre-restoration backups to restore the database to that subsequent state.

 

 

 
