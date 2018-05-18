---
Description: 'How you can use the Certificate Services backup functions to back up a Certificate Services database and its associated files.'
ms.assetid: 'f5c9c9f9-5211-4151-b8e0-3351d462c71b'
title: Backing Up Certificate Services
---

# Backing Up Certificate Services

The following is a scenario showing how you can use the Certificate Services backup functions to back up a Certificate Services database and its associated files.

1.  Load the Certadm.dll library into memory (by calling [**LoadLibrary**](base.loadlibrary)).
2.  Retrieve the address of each of the necessary functions in Certadm.dll (by means of [**GetProcAddress**](base.getprocaddress)). Use these addresses when calling the functions in the remaining steps.
3.  Call [**CertSrvIsServerOnline**](certsrvisserveronline.md) to determine whether Certificate Services is online. Certificate Services must be online for the backup operations to be successful.
4.  Call [**CertSrvBackupPrepare**](certsrvbackupprepare.md) to start a backup session. The resulting Certificate Services backup context handle will be used by many of the other backup functions.
5.  Call [**CertSrvRestoreGetDatabaseLocations**](certsrvrestoregetdatabaselocations.md) to determine the restore map. The restore map contains the paths to be used when restoring the backup. Save the information retrieved by **CertSrvRestoreGetDatabaseLocations** to an application-specific location.
6.  Call [**CertSrvBackupGetDatabaseNames**](certsrvbackupgetdatabasenames.md) to determine the names of the database files to backup. For each of these files, execute steps 7 through 9.
7.  Call [**CertSrvBackupOpenFile**](certsrvbackupopenfile.md) to open the file for backup.
8.  Call [**CertSrvBackupRead**](certsrvbackupread.md) to read a portion of bytes from the file, then call an application-specific routine to store the bytes on a backup medium. Repeat this step until all of the bytes in the file are backed up.
9.  Call [**CertSrvBackupClose**](certsrvbackupclose.md) to close the file.
10. Call [**CertSrvBackupGetBackupLogs**](certsrvbackupgetbackuplogs.md) to determine the names of the log files to backup. For each of these files, execute steps 7 through 9.
11. Call [**CertSrvBackupTruncateLogs**](certsrvbackuptruncatelogs.md) to truncate the log files which were backed up in steps 6 and 10. This step is optional; however, call **CertSrvBackupTruncateLogs** only if all files returned by [**CertSrvBackupGetDatabaseNames**](certsrvbackupgetdatabasenames.md) and [**CertSrvBackupGetBackupLogs**](certsrvbackupgetbackuplogs.md) have been backed up (otherwise, the restore operation will fail). Consult the **CertSrvBackupTruncateLogs** reference page for details.
12. Call [**CertSrvBackupGetDynamicFileList**](certsrvbackupgetdynamicfilelist.md) to determine the names of the non-database files to backup. These files are only identified by the function, and must be backed up by some other means.
13. Backup the dynamic files identified in step 12, using routines separate from Certadm.dll.
14. Call [**CertSrvBackupEnd**](certsrvbackupend.md) to end the backup session.
15. Call [**CertSrvBackupFree**](certsrvbackupfree.md) as needed to release buffers allocated by certain Certificate Services backup functions. Calls to [**CertSrvBackupGetBackupLogs**](certsrvbackupgetbackuplogs.md), [**CertSrvBackupGetDatabaseNames**](certsrvbackupgetdatabasenames.md), and [**CertSrvBackupGetDynamicFileList**](certsrvbackupgetdynamicfilelist.md) will allocate buffers that can be freed by a call to **CertSrvBackupFree**.
16. Release the Certadm.dll resources by calling [**FreeLibrary**](base.freelibrary).

For information about the privileges required to back up the Certificate Services database and associated files, see [Setting the Backup and Restore Privileges](setting-the-backup-and-restore-privileges.md).

 

 



