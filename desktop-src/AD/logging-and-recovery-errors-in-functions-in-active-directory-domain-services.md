---
title: Logging and Recovery Errors in Functions in Active Directory Domain Services
description: This topics lists logging and recovery error return values for functions in Active Directory Domain Services.
ms.assetid: b927073a-8bbc-45d4-b9d3-25f3aa6c6f53
ms.tgt_platform: multiple
keywords:
- Active Directory Logging and Recovery Errors AD
ms.topic: article
ms.date: 05/31/2018
---

# Logging and Recovery Errors in Functions in Active Directory Domain Services

This topics lists logging and recovery error return values for functions in Active Directory Domain Services.



| Value                                | Description                                                                                                                      |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| **hrLogFileCorrupt**                 | The log file is damaged.                                                                                                         |
| **hrNoBackupDirectory**              | No backup directory was given.                                                                                                   |
| **hrBackupDirectoryNotEmpty**        | The backup directory is not empty.                                                                                               |
| **hrBackupInProgress**               | Backup is active.                                                                                                                |
| **hrMissingPreviousLogFile**         | A log file for the checkpoint is missing.                                                                                        |
| **hrLogWriteFail**                   | Unable to write to the log file.                                                                                                 |
| **hrBadLogVersion**                  | The version of the log file is not compatible with the version of the Windows NT/Windows 2000 Directory Service database (NTDS). |
| **hrInvalidLogSequence**             | The time stamp in the next log does not match what was expected.                                                                 |
| **hrLoggingDisabled**                | The log is not active.                                                                                                           |
| **hrLogBufferTooSmall**              | The log buffer is too small to be recovered.                                                                                     |
| **hrLogSequenceEnd**                 | The maximum number of log files has been exceeded.                                                                               |
| **hrNoBackup**                       | There is no backup in progress.                                                                                                  |
| **hrInvalidBackupSequence**          | The backup call is out of sequence.                                                                                              |
| **hrBackupNotAllowedYet**            | Unable to perform a backup now.                                                                                                  |
| **hrDeleteBackupFileFail**           | Unable to delete the backup file.                                                                                                |
| **hrMakeBackupDirectoryFail**        | Unable to make a backup temporary directory.                                                                                     |
| **hrInvalidBackup**                  | An incremental backup cannot be performed when circular logging is enabled.                                                      |
| **hrRecoveredWithErrors**            | Errors were encountered during the repair process.                                                                               |
| **hrMissingLogFile**                 | The current log file is missing.                                                                                                 |
| **hrLogDiskFull**                    | The log disk is full.                                                                                                            |
| **hrBadLogSignature**                | A log file is damaged.                                                                                                           |
| **hrBadDbSignature**                 | A database file is damaged.                                                                                                      |
| **hrBadCheckpointSignature**         | A checkpoint file is damaged.                                                                                                    |
| **hrCheckpointCorrupt**              | A checkpoint file either could not be found or is damaged.                                                                       |
| **hrDatabaseInconsistent**           | The database is damaged.                                                                                                         |
| **hrConsistentTimeMismatch**         | There is a mismatch in the database's last consistent time.                                                                      |
| **hrPatchFileMismatch**              | The patch file is not generated from this backup.                                                                                |
| **hrRestoreLogTooLow**               | The starting log number is too low for the restore.                                                                              |
| **hrRestoreLogTooHigh**              | The starting log number is too high for the restore.                                                                             |
| **hrGivenLogFileHasBadSignature**    | The log file downloaded from the tape is damaged.                                                                                |
| **hrGivenLogFileIsNotContiguous**    | Unable to find a mandatory log file after the tape was downloaded.                                                               |
| **hrMissingRestoreLogFiles**         | The data is not fully restored because some log files are missing.                                                               |
| **hrExistingLogFileHasBadSignature** | The log file in the log file path is damaged.                                                                                    |
| **hrExistingLogFileIsNotContiguous** | Unable to find a mandatory log file in the log file path.                                                                        |
| **hrMissingFullBackup**              | The database missed a previous full backup before the incremental backup.                                                        |
| **hrBadBackupDatabaseSize**          | The backup database size must be a multiple of 4000 (4096 bytes).                                                                |
| **hrTermInProgress**                 | The database is being shut down.                                                                                                 |
| **hrFeatureNotAvailable**            | The feature is not available.                                                                                                    |
| **hrInvalidName**                    | The name is invalid.                                                                                                             |
| **hrInvalidParameter**               | The parameter is invalid.                                                                                                        |
| **hrColumnNull**                     | The value of the column is null.                                                                                                 |
| **hrBufferTruncated**                | The buffer is too small for data.                                                                                                |
| **hrDatabaseAttached**               | The database is already attached.                                                                                                |
| **hrInvalidDatabaseId**              | The database ID is invalid.                                                                                                      |
| **hrOutOfMemory**                    | The computer is out of memory.                                                                                                   |
| **hrOutOfDatabaseSpace**             | The database has reached the maximum size of 16 GB.                                                                              |
| **hrOutOfCursors**                   | Out of table cursors.                                                                                                            |
| **hrOutOfBuffers**                   | Out of database page buffers.                                                                                                    |
| **hrTooManyIndexes**                 | There are too many indexes.                                                                                                      |
| **hrTooManyKeys**                    | There are too many columns in an index.                                                                                          |
| **hrRecordDeleted**                  | The record has been deleted.                                                                                                     |
| **hrReadVerifyFailure**              | A read verification error occurred.                                                                                              |
| **hrOutOfFileHandles**               | Out of file handles.                                                                                                             |
| **hrDiskIO**                         | A disk I/O error occurred.                                                                                                       |
| **hrInvalidPath**                    | The path to the file is invalid.                                                                                                 |
| **hrRecordTooBig**                   | The record has exceeded the maximum size.                                                                                        |
| **hrTooManyOpenDatabases**           | There are too many open databases.                                                                                               |
| **hrInvalidDatabase**                | The file is not a database file.                                                                                                 |
| **hrNotInitialized**                 | The database was not yet called.                                                                                                 |
| **hrAlreadyInitialized**             | The database was already called.                                                                                                 |
| **hrFileAccessDenied**               | Unable to access the file.                                                                                                       |
| **hrBufferTooSmall**                 | The buffer is too small.                                                                                                         |
| **hrSeekNotEqual**                   | Either SeekLE or SeekGE cannot find an exact match.                                                                              |
| **hrTooManyColumns**                 | There are too many columns defined.                                                                                              |
| **hrContainerNotEmpty**              | The container is not empty.                                                                                                      |
| **hrInvalidFilename**                | The filename is invalid.                                                                                                         |
| **hrInvalidBookmark**                | The bookmark is invalid.                                                                                                         |
| **hrColumnInUse**                    | The column is used in an index.                                                                                                  |
| **hrInvalidBufferSize**              | The data buffer does not match the column size.                                                                                  |
| **hrColumnNotUpdatable**             | Unable to set the column value.                                                                                                  |
| **hrIndexInUse**                     | The index is in use.                                                                                                             |
| **hrNullKeyDisallowed**              | Null keys are not allowed on an index.                                                                                           |
| **hrNotInTransaction**               | The operation must be within a transaction.                                                                                      |
| **hrNoIdleActivity**                 | No idle activity occurred.                                                                                                       |
| **hrTooManyActiveUsers**             | There are too many active database users.                                                                                        |
| **hrInvalidCountry**                 | The country or region code is either not known or is invalid.                                                                    |
| **hrInvalidLanguageId**              | The language ID is either not known or is invalid.                                                                               |
| **hrInvalidCodePage**                | The code page is either not known or is invalid.                                                                                 |
| **hrNoWriteLock**                    | There is no write lock at transaction level 0.                                                                                   |
| **hrColumnSetNull**                  | The column value is set to null.                                                                                                 |
| **hrVersionStoreOutOfMemory**        | The lMaxVerPages exceeded (XJET only).                                                                                           |
| **hrCurrencyStackOutOfMemory**       | Out of cursors.                                                                                                                  |
| **hrOutOfSessions**                  | Out of sessions.                                                                                                                 |
| **hrWriteConflict**                  | The write lock failed due to an outstanding write lock.                                                                          |
| **hrTransTooDeep**                   | The transactions are nested too deeply.                                                                                          |
| **hrInvalidSesid**                   | The session handle is invalid.                                                                                                   |
| **hrSessionWriteConflict**           | Another session has a private version of the page.                                                                               |
| **hrInTransaction**                  | The operation is not allowed within a transaction.                                                                               |
| **hrDatabaseDuplicate**              | The database already exists.                                                                                                     |
| **hrDatabaseInUse**                  | The database is in use.                                                                                                          |
| **hrDatabaseNotFound**               | The database does not exist.                                                                                                     |
| **hrDatabaseInvalidName**            | The database name is invalid.                                                                                                    |
| **hrDatabaseInvalidPages**           | The number of pages is invalid.                                                                                                  |
| **hrDatabaseCorrupted**              | The database file is either damaged or cannot be found.                                                                          |
| **hrDatabaseLocked**                 | The database is locked.                                                                                                          |
| **hrTableEmpty**                     | An empty table was opened.                                                                                                       |
| **hrTableLocked**                    | The table is locked.                                                                                                             |
| **hrTableDuplicate**                 | The table already exists.                                                                                                        |
| **hrTableInUse**                     | Unable to lock the table because it is already in use.                                                                           |
| **hrObjectNotFound**                 | The table or object does not exist.                                                                                              |
| **hrCannotRename**                   | Unable to rename the temporary file.                                                                                             |
| **hrDensityInvalid**                 | The file/index density is invalid.                                                                                               |
| **hrTableNotEmpty**                  | Unable to define the clustered index.                                                                                            |
| **hrInvalidTableId**                 | The table ID is invalid.                                                                                                         |
| **hrTooManyOpenTables**              | Unable to open any more tables.                                                                                                  |
| **hrIllegalOperation**               | The operation is not supported on tables.                                                                                        |
| **hrObjectDuplicate**                | The table or object name is already being used.                                                                                  |
| **hrInvalidObject**                  | The object is invalid for operation.                                                                                             |
| **hrIndexCantBuild**                 | Unable to build a clustered index.                                                                                               |
| **hrIndexHasPrimary**                | The primary index is already defined.                                                                                            |
| **hrIndexDuplicate**                 | The index is already defined.                                                                                                    |
| **hrIndexNotFound**                  | The index does not exist.                                                                                                        |
| **hrIndexMustStay**                  | Unable to delete a clustered index.                                                                                              |
| **hrIndexInvalidDef**                | The index definition is illegal.                                                                                                 |
| **hrIndexHasClustered**              | The clustered index is already defined.                                                                                          |
| **hrCreateIndexFailed**              | Unable to create the index because an error occurred while creating a table.                                                     |
| **hrTooManyOpenIndexes**             | Out of index description blocks.                                                                                                 |
| **hrColumnLong**                     | The column value is too long.                                                                                                    |
| **hrColumnDoesNotFit**               | The field will not fit in the record.                                                                                            |
| **hrNullInvalid**                    | The value cannot be null.                                                                                                        |
| **hrColumnIndexed**                  | Unable to delete because the column is indexed.                                                                                  |
| **hrColumnTooBig**                   | The length of the field exceeds the maximum length of 255 bytes.                                                                 |
| **hrColumnNotFound**                 | Unable to find the column.                                                                                                       |
| **hrColumnDuplicate**                | The field is already defined.                                                                                                    |
| **hrColumn2ndSysMaint**              | Only one auto-increment or version column is allowed per table.                                                                  |
| **hrInvalidColumnType**              | The column data type is invalid.                                                                                                 |
| **hrColumnMaxTruncated**             | The column was truncated because it exceeded the maximum length of 255 bytes.                                                    |
| **hrColumnCannotIndex**              | Unable to index a long value column.                                                                                             |
| **hrTaggedNotNULL**                  | Tagged columns cannot be null.                                                                                                   |
| **hrNoCurrentIndex**                 | The entry is invalid without a current index.                                                                                    |
| **hrKeyIsMade**                      | The key is complete.                                                                                                             |
| **hrBadColumnId**                    | The column ID is incorrect.                                                                                                      |
| **hrBadItagSequence**                | There is a bad instance identifier for a multivalued column.                                                                     |
| **hrCannotBeTagged**                 | AutoIncrement and Version cannot be multivalued.                                                                                 |
| **hrRecordNotFound**                 | Unable to find the key.                                                                                                          |
| **hrNoCurrentRecord**                | The currency is not on a record.                                                                                                 |
| **hrRecordClusteredChanged**         | A clustered key cannot be changed.                                                                                               |
| **hrKeyDuplicate**                   | The key already exists.                                                                                                          |
| **hrAlreadyPrepared**                | The current entry has already been copied or cleared.                                                                            |
| **hrKeyNotMade**                     | No key was made.                                                                                                                 |
| **hrUpdateNotPrepared**              | Update was not prepared.                                                                                                         |
| **hrwrnDataHasChanged**              | Data has changed.                                                                                                                |
| **hrerrDataHasChanged**              | The operation was abandoned because data has changed.                                                                            |
| **hrKeyChanged**                     | Moved to a new key.                                                                                                              |
| **hrTooManySorts**                   | There are too many sort processes.                                                                                               |
| **hrInvalidOnSort**                  | An operation that is invalid occurred in the sort.                                                                               |
| **hrTempFileOpenError**              | Unable to open the temporary file.                                                                                               |
| **hrTooManyAttachedDatabases**       | There are too many databases open.                                                                                               |
| **hrDiskFull**                       | The disk is full.                                                                                                                |
| **hrPermissionDenied**               | Permission is denied.                                                                                                            |
| **hrFileNotFound**                   | Unable to find the file.                                                                                                         |
| **hrFileOpenReadOnly**               | The database file is read-only.                                                                                                  |
| **hrAfterInitialization**            | Unable to restore after initialization.                                                                                          |
| **hrLogCorrupted**                   | The database log files are damaged.                                                                                              |
| **hrInvalidOperation**               | The operation is invalid.                                                                                                        |
| **hrAccessDenied**                   | Access is denied.                                                                                                                |



 

## Related topics

<dl> <dt>

[Success](success.md)
</dt> <dt>

[Backup Errors in Active Directory Domain Services](backup-errors-in-active-directory-domain-services.md)
</dt> <dt>

[System Errors in Active Directory Domain Services](system-errors-in-active-directory-domain-services.md)
</dt> <dt>

[Directory Manager Errors](directory-manager-errors.md)
</dt> <dt>

[Return Values for Functions in Active Directory Domain Services](return-values-for-functions-in-active-directory-domain-services.md)
</dt> </dl>

 

 




