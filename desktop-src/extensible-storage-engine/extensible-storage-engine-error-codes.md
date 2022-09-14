---
description: "Learn more about: Extensible Storage Engine Error Codes"
title: Extensible Storage Engine Error Codes
TOCTitle: Extensible Storage Engine Error Codes
ms:assetid: 7534370d-aed6-4980-b1ca-c3d063507e31
ms:mtpsurl: https://msdn.microsoft.com/library/Gg269297(v=EXCHG.10)
ms:contentKeyID: 32765589
ms.date: 09/22/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Extensible Storage Engine Error Codes


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine Error Codes

The following error codes (flags) are used by functions in the Extensible Storage Engine API.

A [JET_ERR](./jet-err.md) value of zero should be interpreted as success.


| <p>Success</p> | <p>Description</p> | 
|----------------|--------------------|
| <p>JET_errSuccess 0</p> | <p>The function succeeded.</p> | 



A [JET_ERR](./jet-err.md) value that is greater than zero should be interpreted as a warning.


| <p>Warnings</p> | <p>Description</p> | 
|-----------------|--------------------|
| <p>JET_wrnRemainingVersions<br />321</p> | <p>The version store is still active. This error is returned by the directory manager.</p> | 
| <p>JET_wrnUniqueKey<br />345</p> | <p>A seek on a non-unique index yielded a unique key. This error is returned by the directory manager.</p> | 
| <p>JET_wrnSeparateLongValue<br />406</p> | <p>A database column is a separated long value. This error is returned by the record manager.</p> | 
| <p>JET_wrnExistingLogFileHasBadSignature<br />558</p> | <p>The existing log file has a bad signature.</p> | 
| <p>JET_wrnExistingLogFileIsNotContiguous<br />559</p> | <p>The existing log file is not contiguous.</p> | 
| <p>JET_wrnSkipThisRecord<br />564</p> | <p>This error is for internal use only.</p> | 
| <p>JET_wrnTargetInstanceRunning<br />578</p> | <p>The TargetInstance specified for the restore is running.</p> | 
| <p>JET_wrnDatabaseRepaired<br />595</p> | <p>The database corruption has been repaired.</p> | 
| <p>JET_wrnColumnNull<br />1004</p> | <p>The column has a <strong>NULL</strong> value.</p> | 
| <p>JET_wrnBufferTruncated<br />1006</p> | <p>The buffer is too small for the data.</p> | 
| <p>JET_wrnDatabaseAttached<br />1007</p> | <p>The database is already attached.</p> | 
| <p>JET_wrnSortOverflow<br />1009</p> | <p>The sort that is being attempted does not have enough memory to complete.</p> | 
| <p>JET_wrnSeekNotEqual<br />1039</p> | <p>An exact match was not found during a seek.</p> | 
| <p>JET_wrnRecordFoundGreater<br />JET_wrnSeekNotEqual</p> | <p>An exact match was not found during a seek. This error is returned by the record manager.</p> | 
| <p>JET_wrnRecordFoundLess<br />JET_wrnSeekNotEqual</p> | <p>An exact match was not found during a seek. This error is returned by the record manager.</p> | 
| <p>JET_wrnNoErrorInfo<br />1055</p> | <p>There is no extended error information.</p> | 
| <p>JET_wrnNoIdleActivity<br />1058</p> | <p>No idle activity occurred.</p> | 
| <p>JET_wrnNoWriteLock<br />1067</p> | <p>There is a no write lock at transaction level 0.</p> | 
| <p>JET_wrnColumnSetNull<br />1068</p> | <p>The column is set to a <strong>NULL</strong> value.</p> | 
| <p>JET_wrnTableEmpty<br />1301</p> | <p>An empty table was opened.</p> | 
| <p>JET_wrnTableInUseBySystem<br />1327</p> | <p>The system cleanup has a cursor open on the table.</p> | 
| <p>JET_wrnCorruptIndexDeleted<br />1415</p> | <p>The out-of-date index must be removed.</p> | 
| <p>JET_wrnColumnMaxTruncated<br />1512</p> | <p>The Max length is too large and has been truncated.</p> | 
| <p>JET_wrnCopyLongValue<br />1520</p> | <p>A BLOB value has been moved from the record into a separate storage of large BLOBs.</p><p><strong>Note</strong> This error is for internal use only.</p> | 
| <p>JET_wrnColumnSkipped<br />1531</p> | <p>The column values were not returned because the corresponding column ID or <em>itagSequence</em> member from the <a href="gg294052(v=exchg.10).md">JET_ENUMCOLUMNVALUE</a> structure that was requested for enumeration was null.</p> | 
| <p>JET_wrnColumnNotLocal<br />1532</p> | <p>The column values were not returned because they could not be reconstructed from the existing data.</p> | 
| <p>JET_wrnColumnMoreTags<br />1533</p> | <p>The existing column values were not requested for enumeration.</p> | 
| <p>JET_wrnColumnTruncated<br />1534</p> | <p>The column value was truncated at the requested size limit during enumeration.</p> | 
| <p>JET_wrnColumnPresent<br />1535</p> | <p>The column values exist but were not returned by the request.</p> | 
| <p>JET_wrnColumnSingleValue<br />1536</p> | <p>The column value was returned in JET_COLUMNENUM as a result of the JET_bitEnumerateCompressOutput being set.</p> | 
| <p>JET_wrnColumnDefault<br />1537</p> | <p>The column value is set to the default value of the column.</p> | 
| <p>JET_wrnDataHasChanged<br />1610</p> | <p>The data has changed.</p> | 
| <p>JET_wrnKeyChanged<br />1618</p> | <p>A new key is being used.</p> | 
| <p>JET_wrnFileOpenReadOnly<br />1813</p> | <p>The database file is read only.</p> | 
| <p>JET_wrnIdleFull<br />1908</p> | <p>The idle registry is full.</p> | 
| <p>JET_wrnDefragAlreadyRunning<br />2000</p> | <p>There was an online defragmentation already running on the specified database.</p> | 
| <p>JET_wrnDefragNotRunning<br />2001</p> | <p>An online defragmentation is not running on the specified database.</p> | 
| <p>JET_wrnCallbackNotRegistered<br />2100</p> | <p>A non-existent callback function was unregistered.</p> | 



A [JET_ERR](./jet-err.md) value that is less than zero should be interpreted as an error.


| <p>Errors</p> | <p>Description</p> | 
|---------------|--------------------|
| <p>JET_wrnNyi<br />-1</p> | <p>The function is not yet implemented.</p> | 
| <p>JET_errRfsFailure<br />-100</p> | <p>The Resource Failure Simulator failed.</p> | 
| <p>JET_errRfsNotArmed<br />-101</p> | <p>The Resource Failure Simulator has not been initialized.</p> | 
| <p>JET_errFileClose<br />-102</p> | <p>The file could not be closed.</p> | 
| <p>JET_errOutOfThreads<br />-103</p> | <p>The thread could not be started.</p> | 
| <p>JET_errTooManyIO<br />-105</p> | <p>The system is busy due to too many IOs.</p> | 
| <p>JET_errTaskDropped<br />-106</p> | <p>The requested asynchronous task could not be executed.</p> | 
| <p>JET_errInternalError<br />-107</p> | <p>There was a fatal internal error.</p> | 
| <p>JET_errDatabaseBufferDependenciesCorrupted<br />-255</p> | <p>The buffer dependencies were set improperly and there was a recovery failure.</p> | 
| <p>JET_errPreviousVersion<br />-322</p> | <p>The version already existed and there was a recovery failure. This error is returned by the directory manager.</p> | 
| <p>JET_errPageBoundary<br />-323</p> | <p>The page boundary has been reached. This error is returned by the directory manager.</p> | 
| <p>JET_errKeyBoundary<br />-324</p> | <p>The key boundary has been reached. This error is returned by the directory manager.</p> | 
| <p>JET_errBadPageLink<br />-327</p> | <p>The database is corrupt. This error is returned by the directory manager.</p> | 
| <p>JET_errBadBookmark<br />-328</p> | <p>The bookmark has no corresponding address in the database. This error is returned by the directory manager.</p> | 
| <p>JET_errNTSystemCallFailed<br />-334</p> | <p>The call to the operating system failed. This error is returned by the directory manager.</p> | 
| <p>JET_errBadParentPageLink<br />-338</p> | <p>A parent database is corrupt. This error is returned by the directory manager.</p> | 
| <p>JET_errSPAvailExtCacheOutOfSync<br />-340</p> | <p>The AvailExt cache does not match the B+ tree. This error is returned by the directory manager.</p> | 
| <p>JET_errSPAvailExtCorrupted<br />-341</p> | <p>The AllAvailExt space tree is corrupt. This error is returned by the directory manager.</p> | 
| <p>JET_errSPAvailExtCacheOutOfMemory<br />-342</p> | <p>An out of memory error occurred while allocating an AvailExt cache node. This error is returned by the directory manager.</p> | 
| <p>JET_errSPOwnExtCorrupted<br />-343</p> | <p>The OwnExt space tree is corrupt. This error is returned by the directory manager.</p> | 
| <p>JET_errDbTimeCorrupted<br />-344</p> | <p>The Dbtime on the current page is greater than the global database dbtime. This error is returned by the directory manager.</p> | 
| <p>JET_errKeyTruncated<br />-346</p> | <p>An attempt to create a key for an index entry failed because the key would have been truncated and the index definition disallows key truncation.</p> | 
| <p>JET_errKeyTooBig<br />-408</p> | <p>The key is too large. This error is returned by the record manager.</p> | 
| <p>JET_errInvalidLoggedOperation<br />-500</p> | <p>The logged operation cannot be redone.</p> | 
| <p>JET_errLogFileCorrupt<br />-501</p> | <p>The log file is corrupt.</p> | 
| <p>JET_errNoBackupDirectory<br />-503</p> | <p>A backup directory was not given.</p> | 
| <p>JET_errBackupDirectoryNotEmpty<br />-504</p> | <p>The backup directory is not empty.</p> | 
| <p>JET_errBackupInProgress<br />-505</p> | <p>The backup is active already.</p> | 
| <p>JET_errRestoreInProgress<br />-506</p> | <p>A restore is in progress.</p> | 
| <p>JET_errMissingPreviousLogFile<br />-509</p> | <p>The log file is missing for the check point.</p> | 
| <p>JET_errLogWriteFail<br />-510</p> | <p>There was a failure writing to the log file.</p> | 
| <p>JET_errLogDisabledDueToRecoveryFailure<br />-511</p> | <p>The attempt to write to the log after recovery failed.</p> | 
| <p>JET_errCannotLogDuringRecoveryRedo<br />-512</p> | <p>The attempt to write to the log during the recovery redo failed.</p> | 
| <p>JET_errLogGenerationMismatch<br />-513</p> | <p>The name of of the log file does not match the internal generation number.</p> | 
| <p>JET_errBadLogVersion<br />-514</p> | <p>The version of the log file is not compatible with the ESE version.</p> | 
| <p>JET_errInvalidLogSequence<br />-515</p> | <p>The timestamp in the next log does not match the expected timestamp.</p> | 
| <p>JET_errLoggingDisabled<br />-516</p> | <p>The log is not active.</p> | 
| <p>JET_errLogBufferTooSmall<br />-517</p> | <p>The log buffer is too small for recovery.</p> | 
| <p>JET_errLogSequenceEnd<br />-519</p> | <p>The maximum log file number has been exceeded.</p> | 
| <p>JET_errNoBackup<br />-520</p> | <p>There is no backup in progress.</p> | 
| <p>JET_errInvalidBackupSequence<br />-521</p> | <p>The backup call is out of sequence.</p> | 
| <p>JET_errBackupNotAllowedYet<br />-523</p> | <p>A backup cannot be done at this time.</p> | 
| <p>JET_errDeleteBackupFileFail<br />-524</p> | <p>A backup file could not be deleted.</p> | 
| <p>JET_errMakeBackupDirectoryFail<br />-525</p> | <p>The backup temporary directory could not be created.</p> | 
| <p>JET_errInvalidBackup<br />-526</p> | <p>Circular logging is enabled; an incremental backup cannot be performed.</p> | 
| <p>JET_errRecoveredWithErrors<br />-527</p> | <p>The data was restored with errors.</p> | 
| <p>JET_errMissingLogFile<br />-528</p> | <p>The current log file is missing.</p> | 
| <p>JET_errLogDiskFull<br />-529</p> | <p>The log disk is full.</p> | 
| <p>JET_errBadLogSignature<br />-530</p> | <p>There is a bad signature for a log file.</p> | 
| <p>JET_errBadDbSignature<br />-531</p> | <p>There is a bad signature for a database file.</p> | 
| <p>JET_errBadCheckpointSignature<br />-532</p> | <p>There is a bad signature for a checkpoint file.</p> | 
| <p>JET_errCheckpointCorrupt<br />-533</p> | <p>The checkpoint file was not found or was corrupt.</p> | 
| <p>JET_errMissingPatchPage<br />-534</p> | <p>The database patch file page was not found during recovery.</p> | 
| <p>JET_errBadPatchPage<br />-535</p> | <p>The database patch file page is not valid.</p> | 
| <p>JET_errRedoAbruptEnded<br />-536</p> | <p>The redo abruptly ended due to a sudden failure while reading logs from the log file.</p> | 
| <p>JET_errBadSLVSignature<br />-537</p> | <p>This flag is reserved.</p> | 
| <p>JET_errPatchFileMissing<br />-538</p> | <p>The hard restore detected that a database patch file is missing from the backup set.</p> | 
| <p>JET_errDatabaseLogSetMismatch<br />-539</p> | <p>The database does not belong with the current set of log files.</p> | 
| <p>JET_errDatabaseStreamingFileMismatch<br />-540</p> | <p>This flag is reserved.</p> | 
| <p>JET_errLogFileSizeMismatch<br />-541</p> | <p>The actual log file size does not match <a href="gg269235(v=exchg.10).md">JET_paramLogFileSize</a>.</p> | 
| <p>JET_errCheckpointFileNotFound<br />-542</p> | <p>The checkpoint file could not be located.</p> | 
| <p>JET_errRequiredLogFilesMissing<br />-543</p> | <p>The required log files for recovery are missing.</p> | 
| <p>JET_errSoftRecoveryOnBackupDatabase<br />-544</p> | <p>A soft recovery is about to be used on a backup database when a restore should be used instead.</p> | 
| <p>JET_errLogFileSizeMismatchDatabasesConsistent<br />-545</p> | <p>The databases have been recovered, but the log file size used during recovery does not match <a href="gg269235(v=exchg.10).md">JET_paramLogFileSize</a>.</p> | 
| <p>JET_errLogSectorSizeMismatch<br />-546</p> | <p>The log file sector size does not match the sector size of the current volume.</p> | 
| <p>JET_errLogSectorSizeMismatchDatabasesConsistent<br />-547</p> | <p>The databases have been recovered, but the log file sector size (used during recovery) does not match the sector size of the current volume.</p> | 
| <p>JET_errLogSequenceEndDatabasesConsistent<br />-548</p> | <p>The databases have been recovered, but all possible log generations in the current sequence have been used. All log files and the checkpoint file must be deleted and databases must be backed up before continuing.</p> | 
| <p>JET_errStreamingDataNotLogged<br />-549</p> | <p>There was an illegal attempt to replay a streaming file operation where the data was not logged. This is probably caused by an attempt to rollforward with circular logging enabled.</p> | 
| <p>JET_errDatabaseDirtyShutdown<br />-550</p> | <p>The database was not shutdown cleanly. A recovery must first be run to properly complete database operations for the previous shutdown.</p> | 
| <p>JET_errDatabaseInconsistent<br />JET_errDatabaseDirtyShutdown</p> | <p>This error is obsolete and has been replaced by JET_errDatabaseDirtyShutdown.</p> | 
| <p>JET_errConsistentTimeMismatch<br />-551</p> | <p>The last consistent time for the database has not been matched.</p> | 
| <p>JET_errDatabasePatchFileMismatch<br />-552</p> | <p>The database patch file is not generated from this backup.</p> | 
| <p>JET_errEndingRestoreLogTooLow<br />-553</p> | <p>The starting log number is too low for the restore.</p> | 
| <p>JET_errStartingRestoreLogTooHigh<br />-554</p> | <p>The starting log number is too high for the restore.</p> | 
| <p>JET_errGivenLogFileHasBadSignature<br />-555</p> | <p>The restore log file has a bad signature.</p> | 
| <p>JET_errGivenLogFileIsNotContiguous<br />-556</p> | <p>The restore log file is not contiguous.</p> | 
| <p>JET_errMissingRestoreLogFiles<br />-557</p> | <p>Some restore log files are missing.</p> | 
| <p>JET_errMissingFullBackup<br />-560</p> | <p>The database missed a previous full backup before attempting to perform an incremental backup.</p> | 
| <p>JET_errBadBackupDatabaseSize<br />-561</p> | <p>The backup database size is not a multiple of the database page size.</p> | 
| <p>JET_errDatabaseAlreadyUpgraded<br />-562</p> | <p>The current attempt to upgrade a database has been stopped because the database is already current.</p> | 
| <p>JET_errDatabaseIncompleteUpgrade<br />-563</p> | <p>The database was only partially converted to the current format. The database must be restored from backup.</p> | 
| <p>JET_errMissingCurrentLogFiles<br />-565</p> | <p>Some current log files are missing for continuous restore.</p> | 
| <p>JET_errDbTimeTooOld<br />-566</p> | <p>The dbtime on a page is smaller than the dbtimeBefore that is in the record.</p> | 
| <p>JET_errDbTimeTooNew<br />-567</p> | <p>The dbtime on a page is in advance of the dbtimeBefore that is in the record.</p> | 
| <p>JET_errMissingFileToBackup<br />-569</p> | <p>Some log or database patch files were missing during the backup.</p> | 
| <p>JET_errLogTornWriteDuringHardRestore<br />-570</p> | <p>A torn write was detected in a backup that was set during a hard restore.</p> | 
| <p>JET_errLogTornWriteDuringHardRecovery<br />-571</p> | <p>A torn write was detected during a hard recovery (the log was not part of a backup set).</p> | 
| <p>JET_errLogCorruptDuringHardRestore<br />-573</p> | <p>Corruption was detected in a backup set during a hard restore.</p> | 
| <p>JET_errLogCorruptDuringHardRecovery<br />-574</p> | <p>Corruption was detected during hard recovery (the log was not part of a backup set).</p> | 
| <p>JET_errMustDisableLoggingForDbUpgrade<br />-575</p> | <p>Logging cannot be enabled while attempting to upgrade a database.</p> | 
| <p>JET_errBadRestoreTargetInstance<br />-577</p> | <p>Either the TargetInstance that was specified for restore has not been found or the log files do not match.</p> | 
| <p>JET_errRecoveredWithoutUndo<br />-579</p> | <p>The database engine successfully replayed all operations in the transaction log to perform a crash recovery but the caller elected to stop recovery without rolling back uncommitted updates.</p> | 
| <p>JET_errDatabasesNotFromSameSnapshot<br />-580</p> | <p>The databases to be restored are not from the same shadow copy backup.</p> | 
| <p>JET_errSoftRecoveryOnSnapshot<br />-581</p> | <p>There is a soft recovery on a database from a shadow copy backup set.</p> | 
| <p>JET_errUnicodeTranslationBufferTooSmall<br />-601</p> | <p>The Unicode translation buffer is too small.</p> | 
| <p>JET_errUnicodeTranslationFail<br />-602</p> | <p>The Unicode normalization failed.</p> | 
| <p>JET_errUnicodeNormalizationNotSupported<br />-603</p> | <p>The operating system does not provide support for Unicode normalization and a normalization callback was not specified.</p> | 
| <p>JET_errExistingLogFileHasBadSignature<br />-610</p> | <p>The existing log file has a bad signature.</p> | 
| <p>JET_errExistingLogFileIsNotContiguous<br />-611</p> | <p>An existing log file is not contiguous.</p> | 
| <p>JET_errLogReadVerifyFailure<br />-612</p> | <p>A checksum error was found in the log file during backup.</p> | 
| <p>JET_errSLVReadVerifyFailure<br />-613</p> | <p>This flag is reserved.</p> | 
| <p>JET_errCheckpointDepthTooDeep<br />-614</p> | <p>There are too many outstanding generations between the checkpoint and the current generation.</p> | 
| <p>JET_errRestoreOfNonBackupDatabase<br />-615</p> | <p>A hard recovery was attempted on a database that was not a backup database.</p> | 
| <p>JET_errInvalidGrbit<br />-900</p> | <p>There is an invalid grbit parameter.</p> | 
| <p>JET_errTermInProgress<br />-1000</p> | <p>Termination is in progress.</p> | 
| <p>JET_errFeatureNotAvailable<br />-1001</p> | <p>This API element is not supported.</p> | 
| <p>JET_errInvalidName<br />-1002</p> | <p>An invalid name is being used.</p> | 
| <p>JET_errInvalidParameter<br />-1003</p> | <p>An invalid API parameter is being used.</p> | 
| <p>JET_errDatabaseFileReadOnly<br />-1008</p> | <p>There was an attempt to attach to a read-only database file for read/write operations.</p> | 
| <p>JET_errInvalidDatabaseId<br />-1010</p> | <p>There is an invalid database ID.</p> | 
| <p>JET_errOutOfMemory<br />-1011</p> | <p>The system is out of memory.</p> | 
| <p>JET_errOutOfDatabaseSpace<br />-1012</p> | <p>The maximum database size has been reached.</p> | 
| <p>JET_errOutOfCursors<br />-1013</p> | <p>The table is out of cursors.</p> | 
| <p>JET_errOutOfBuffers<br />-1014</p> | <p>The database is out of page buffers.</p> | 
| <p>JET_errTooManyIndexes<br />-1015</p> | <p>There are too many indexes.</p> | 
| <p>JET_errTooManyKeys<br />-1016</p> | <p>There are too many columns in an index.</p> | 
| <p>JET_errRecordDeleted<br />-1017</p> | <p>The record has been deleted.</p> | 
| <p>JET_errReadVerifyFailure<br />-1018</p> | <p>There is a checksum error on a database page.</p> | 
| <p>JET_errPageNotInitialized<br />-1019</p> | <p>There is a blank database page.</p> | 
| <p>JET_errOutOfFileHandles<br />-1020</p> | <p>There are no file handles.</p> | 
| <p>JET_errDiskIO<br />-1022</p> | <p>There is a disk IO error.</p> | 
| <p>JET_errInvalidPath<br />-1023</p> | <p>There is an invalid file path.</p> | 
| <p>JET_errInvalidSystemPath<br />-1024</p> | <p>There is an invalid system path.</p> | 
| <p>JET_errInvalidLogDirectory<br />-1025</p> | <p>There is an invalid log directory.</p> | 
| <p>JET_errRecordTooBig<br />-1026</p> | <p>The record is larger than maximum size.</p> | 
| <p>JET_errTooManyOpenDatabases<br />-1027</p> | <p>There are too many open databases.</p> | 
| <p>JET_errInvalidDatabase<br />-1028</p> | <p>This is not a database file.</p> | 
| <p>JET_errNotInitialized<br />-1029</p> | <p>The database engine has not been initialized.</p> | 
| <p>JET_errAlreadyInitialized<br />-1030</p> | <p>The database engine is already initialized.</p> | 
| <p>JET_errInitInProgress<br />-1031</p> | <p>The database engine is being initialized.</p> | 
| <p>JET_errFileAccessDenied<br />-1032</p> | <p>The file cannot be accessed because the file is locked or in use.</p> | 
| <p>JET_errBufferTooSmall<br />-1038</p> | <p>The buffer is too small.</p> | 
| <p>JET_errTooManyColumns<br />-1040</p> | <p>Too many columns are defined.</p> | 
| <p>JET_errContainerNotEmpty<br />-1043</p> | <p>The container is not empty.</p> | 
| <p>JET_errInvalidFilename<br />-1044</p> | <p>The filename is invalid.</p> | 
| <p>JET_errInvalidBookmark<br />-1045</p> | <p>There is an invalid bookmark.</p> | 
| <p>JET_errColumnInUse<br />-1046</p> | <p>The column used is in an index.</p> | 
| <p>JET_errInvalidBufferSize<br />-1047</p> | <p>The data buffer does not match the column size.</p> | 
| <p>JET_errColumnNotUpdatable<br />-1048</p> | <p>The column value cannot be set.</p> | 
| <p>JET_errIndexInUse<br />-1051</p> | <p>The index is in use.</p> | 
| <p>JET_errLinkNotSupported<br />-1052</p> | <p>The link support is unavailable.</p> | 
| <p>JET_errNullKeyDisallowed<br />-1053</p> | <p>Null keys are not allowed on an index.</p> | 
| <p>JET_errNotInTransaction<br />-1054</p> | <p>The operation must occur within a transaction.</p> | 
| <p>JET_errTooManyActiveUsers<br />-1059</p> | <p>There are too many active database users</p> | 
| <p>JET_errInvalidCountry<br />-1061</p> | <p>There is an invalid or unknown country code.</p> | 
| <p>JET_errInvalidLanguageId<br />-1062</p> | <p>There is an invalid or unknown language ID.</p> | 
| <p>JET_errInvalidCodePage<br />-1063</p> | <p>There is an invalid or unknown code page.</p> | 
| <p>JET_errInvalidLCMapStringFlags<br />-1064</p> | <p>There are invalid flags being used for <a href="/windows/win32/api/winnls/nf-winnls-lcmapstringa">LCMapString</a>.</p> | 
| <p>JET_errVersionStoreEntryTooBig<br />-1065</p> | <p>There was an attempt to create a version store entry (RCE) that was larger than a version bucket.</p> | 
| <p>JET_errVersionStoreOutOfMemoryAndCleanupTimedOut<br />-1066</p> | <p>The version store is out of memory and the cleanup attempt failed to complete.</p> | 
| <p>JET_errVersionStoreOutOfMemory<br />-1069</p> | <p>The version store is out of memory and a cleanup was already attempted).</p> | 
| <p>JET_errCannotIndex<br />-1071</p> | <p>The escrow and SLV columns cannot be indexed.</p> | 
| <p>JET_errRecordNotDeleted<br />-1072</p> | <p>The record has not been deleted.</p> | 
| <p>JET_errTooManyMempoolEntries<br />-1073</p> | <p>Too many mempool entries have been requested.</p> | 
| <p>JET_errOutOfObjectIDs<br />-1074</p> | <p>The database is out of B+ tree ObjectIDs so an offline defragmentation must be performed to reclaim freed or unused ObjectIds.</p> | 
| <p>JET_errOutOfLongValueIDs<br />-1075</p> | <p>The Long-value ID counter has reached the maximum value. An offline defragmentation must be performed to reclaim free or unused LongValueIDs.</p> | 
| <p>JET_errOutOfAutoincrementValues<br />-1076</p> | <p>The auto-increment counter has reached the maximum value. An offline defragmentation will not be able to reclaim free or unused auto-increment values).</p> | 
| <p>JET_errOutOfDbtimeValues<br />-1077</p> | <p>The Dbtime counter has reached the maximum value. An offline defragmentation must be performed to reclaim free or unused Dbtime values.</p> | 
| <p>JET_errOutOfSequentialIndexValues<br />-1078</p> | <p>A sequential index counter has reached the maximum value. An offline defragmentation must be performed to reclaim free or unused SequentialIndex values.</p> | 
| <p>JET_errRunningInOneInstanceMode<br />-1080</p> | <p>This multi-instance call has the single-instance mode enabled.</p> | 
| <p>JET_errRunningInMultiInstanceMode<br />-1081</p> | <p>This single-instance call has the multi-instance mode enabled.</p> | 
| <p>JET_errSystemParamsAlreadySet<br />-1082</p> | <p>The global system parameters have already been set.</p> | 
| <p>JET_errSystemPathInUse<br />-1083</p> | <p>The system path is already being used by another database instance.</p> | 
| <p>JET_errLogFilePathInUse<br />-1084</p> | <p>The log file path is already being used by another database instance.</p> | 
| <p>JET_errTempPathInUse<br />-1085</p> | <p>The path to the temporary database is already being used by another database instance.</p> | 
| <p>JET_errInstanceNameInUse<br />-1086</p> | <p>The instance name is already in use.</p> | 
| <p>JET_errInstanceUnavailable<br />-1090</p> | <p>This instance cannot be used because it encountered a fatal error.</p> | 
| <p>JET_errDatabaseUnavailable<br />-1091</p> | <p>This database cannot be used because it encountered a fatal error.</p> | 
| <p>JET_errInstanceUnavailableDueToFatalLogDiskFull<br />-1092</p> | <p>This instance cannot be used because it encountered a log-disk-full error while performing an operation (such as a transaction rollback) that could not tolerate failure.</p> | 
| <p>JET_errOutOfSessions<br />-1101</p> | <p>The database is out of sessions.</p> | 
| <p>JET_errWriteConflict<br />-1102</p> | <p>The write lock failed due to the existence of an outstanding write lock.</p> | 
| <p>JET_errTransTooDeep<br />-1103</p> | <p>The transactions are nested too deeply.</p> | 
| <p>JET_errInvalidSesid<br />-1104</p> | <p>There is an invalid session handle.</p> | 
| <p>JET_errWriteConflictPrimaryIndex<br />-1105</p> | <p>An update was attempted on an uncommitted primary index.</p> | 
| <p>JET_errInTransaction<br />-1108</p> | <p>The operation is not allowed within a transaction.</p> | 
| <p>JET_errRollbackRequired<br />-1109</p> | <p>The current transaction must be rolled back. It cannot be committed and a new one cannot be started.</p> | 
| <p>JET_errTransReadOnly<br />-1110</p> | <p>A read-only transaction tried to modify the database.</p> | 
| <p>JET_errSessionWriteConflict<br />-1111</p> | <p>There was an attempt to replace the same record by two different cursors in the same session.</p> | 
| <p>JET_errRecordTooBigForBackwardCompatibility<br />-1112</p> | <p>The record would be too big if represented in a database format from a previous version of Jet.</p> | 
| <p>JET_errCannotMaterializeForwardOnlySort<br />-1113</p> | <p>The temporary table could not be created due to parameters that conflict with JET_bitTTForwardOnly.</p> | 
| <p>JET_errSesidTableIdMismatch<br />-1114</p> | <p>The session handle cannot be used with the table id because it was not used to create it.</p> | 
| <p>JET_errInvalidInstance<br />-1115</p> | <p>The instance handle is invalid or refers to an instance that has been shut down.</p> | 
| <p>JET_errReadLostFlushVerifyFailure<br />-1119</p> | <p>The database page read from disk had a previous write not represented on the page. Available on Windows 8 and later for client, and Windows Server 2012 and later for server.</p> | 
| <p>JET_errDatabaseDuplicate<br />-1201</p> | <p>The database already exists.</p> | 
| <p>JET_errDatabaseInUse<br />-1202</p> | <p>The database in use.</p> | 
| <p>JET_errDatabaseNotFound<br />-1203</p> | <p>There is no such database.</p> | 
| <p>JET_errDatabaseInvalidName<br />-1204</p> | <p>The database name is invalid.</p> | 
| <p>JET_errDatabaseInvalidPages<br />-1205</p> | <p>There are an invalid number of pages.</p> | 
| <p>JET_errDatabaseCorrupted<br />-1206</p> | <p>There is a non-database file or corrupt database.</p> | 
| <p>JET_errDatabaseLocked<br />-1207</p> | <p>The database is exclusively locked.</p> | 
| <p>JET_errCannotDisableVersioning<br />-1208</p> | <p>The versioning for this database cannot be disabled.</p> | 
| <p>JET_errInvalidDatabaseVersion<br />-1209</p> | <p>The database engine is incompatible with the database.</p> | 
| <p>JET_errDatabase200Format<br />-1210</p> | <p>The database is in an older (200) format. This error is returned by <a href="gg294068(v=exchg.10).md">JetInit</a> if <a href="gg269337(v=exchg.10).md">JET_paramCheckFormatWhenOpenFail</a> is set. Windows NT client only.</p> | 
| <p>JET_errDatabase400Format<br />-1211</p> | <p>The database is in an older (400) format. This error is returned by <a href="gg294068(v=exchg.10).md">JetInit</a> if <a href="gg269337(v=exchg.10).md">JET_paramCheckFormatWhenOpenFail</a> is set. Windows NT client only.</p> | 
| <p>JET_errDatabase500Format<br />-1212</p> | <p>The database is in an older (500) format. This error is returned by <a href="gg294068(v=exchg.10).md">JetInit</a> if <a href="gg269337(v=exchg.10).md">JET_paramCheckFormatWhenOpenFail</a> is set. Windows NT client only.</p> | 
| <p>JET_errPageSizeMismatch<br />-1213</p> | <p>The database page size does not match the engine.</p> | 
| <p>JET_errTooManyInstances<br />-1214</p> | <p>No more database instances can be started.</p> | 
| <p>JET_errDatabaseSharingViolation<br />-1215</p> | <p>A different database instance is using this database.</p> | 
| <p>JET_errAttachedDatabaseMismatch<br />-1216</p> | <p>An outstanding database attachment has been detected at the start or end of the recovery, but the database is missing or does not match attachment info.</p> | 
| <p>JET_errDatabaseInvalidPath<br />-1217</p> | <p>The specified path to the database file is illegal.</p> | 
| <p>JET_errDatabaseIdInUse<br />-1218</p> | <p>A database is being assigned an ID that is already in use.</p> | 
| <p>JET_errForceDetachNotAllowed<br />-1219</p> | <p>The force detach is allowed only after the normal detach was stopped due to an error.</p> | 
| <p>JET_errCatalogCorrupted<br />-1220</p> | <p>Corruption was detected in the catalog.</p> | 
| <p>JET_errPartiallyAttachedDB<br />-1221</p> | <p>The database is only partially attached and the attach operation cannot be completed.</p> | 
| <p>JET_errDatabaseSignInUse<br />-1222</p> | <p>The database with the same signature is already in use.</p> | 
| <p>JET_errDatabaseCorruptedNoRepair<br />-1224</p> | <p>The database is corrupted but a repair is not allowed.</p> | 
| <p>JET_errInvalidCreateDbVersion<br />-1225</p> | <p>The database engine attempted to replay a Create Database operation from the transaction log but failed due to an incompatible version of that operation.</p> | 
| <p>JET_errTableLocked<br />-1302</p> | <p>The table is exclusively locked.</p> | 
| <p>JET_errTableDuplicate<br />-1303</p> | <p>The table already exists.</p> | 
| <p>JET_errTableInUse<br />-1304</p> | <p>The table is in use and cannot be locked.</p> | 
| <p>JET_errObjectNotFound<br />-1305</p> | <p>There is no such table or object.</p> | 
| <p>JET_errDensityInvalid<br />-1307</p> | <p>There is a bad file or index density.</p> | 
| <p>JET_errTableNotEmpty<br />-1308</p> | <p>The table is not empty.</p> | 
| <p>JET_errInvalidTableId<br />-1310</p> | <p>The table ID is invalid.</p> | 
| <p>JET_errTooManyOpenTables<br />-1311</p> | <p>No more tables can be opened, even after the internal cleanup task has run.</p> | 
| <p>JET_errIllegalOperation<br />-1312</p> | <p>The operation is not supported on the table.</p> | 
| <p>JET_errTooManyOpenTablesAndCleanupTimedOut<br />-1313</p> | <p>No more tables can be opened because the cleanup attempt failed to complete.</p> | 
| <p>JET_errObjectDuplicate<br />-1314</p> | <p>The table or object name is in use.</p> | 
| <p>JET_errInvalidObject<br />-1316</p> | <p>The object is invalid for operation.</p> | 
| <p>JET_errCannotDeleteTempTable<br />-1317</p> | <p><a href="gg294087(v=exchg.10).md">JetCloseTable</a> must be used instead of <a href="gg294128(v=exchg.10).md">JetDeleteTable</a> to delete a temporary table.</p> | 
| <p>JET_errCannotDeleteSystemTable<br />-1318</p> | <p>There was an illegal attempt to delete a system table.</p> | 
| <p>JET_errCannotDeleteTemplateTable<br />-1319</p> | <p>There was an illegal attempt to delete a template table.</p> | 
| <p>JET_errExclusiveTableLockRequired<br />-1322</p> | <p>There must be an exclusive lock on the table.</p> | 
| <p>JET_errFixedDDL<br />-1323</p> | <p>DDL operations are prohibited on this table.</p> | 
| <p>JET_errFixedInheritedDDL<br />-1324</p> | <p>On a derived table, DDL operations are prohibited on the inherited portion of the DDL.</p> | 
| <p>JET_errCannotNestDDL<br />-1325</p> | <p>Nesting the hierarchical DDL is not currently supported.</p> | 
| <p>JET_errDDLNotInheritable<br />-1326</p> | <p>There was an attempt to inherit a DDL from a table that is not marked as a template table.</p> | 
| <p>JET_errInvalidSettings<br />-1328</p> | <p>The system parameters were set improperly.</p> | 
| <p>JET_errClientRequestToStopJetService<br />-1329</p> | <p>The client has requested that the service be stopped.</p> | 
| <p>JET_errCannotAddFixedVarColumnToDerivedTable<br />-1330</p> | <p>The Template table was created with the NoFixedVarColumnsInDerivedTables flag set.</p> | 
| <p>JET_errIndexCantBuild<br />-1401</p> | <p>The index build failed.</p> | 
| <p>JET_errIndexHasPrimary<br />-1402</p> | <p>The primary index is already defined.</p> | 
| <p>JET_errIndexDuplicate<br />-1403</p> | <p>The index is already defined.</p> | 
| <p>JET_errIndexNotFound<br />-1404</p> | <p>There is no such index.</p> | 
| <p>JET_errIndexMustStay<br />-1405</p> | <p>The clustered index cannot be deleted.</p> | 
| <p>JET_errIndexInvalidDef<br />-1406</p> | <p>The index definition is invalid.</p> | 
| <p>JET_errInvalidCreateIndex<br />-1409</p> | <p>The creation of the index description was invalid.</p> | 
| <p>JET_errTooManyOpenIndexes<br />-1410</p> | <p>The database is out of index description blocks.</p> | 
| <p>JET_errMultiValuedIndexViolation<br />-1411</p> | <p>Non-unique inter-record index keys have been generated for a multi-valued index.</p> | 
| <p>JET_errIndexBuildCorrupted<br />-1412</p> | <p>A secondary index that properly reflects the primary index failed to build.</p> | 
| <p>JET_errPrimaryIndexCorrupted<br />-1413</p> | <p>The primary index is corrupt and the database must be defragmented.</p> | 
| <p>JET_errSecondaryIndexCorrupted<br />-1414</p> | <p>The secondary index is corrupt and the database must be defragmented.</p> | 
| <p>JET_errInvalidIndexId<br />-1416</p> | <p>The index ID is invalid.</p> | 
| <p>JET_errIndexTuplesSecondaryIndexOnly<br />-1430</p> | <p>The tuple index can only be set on a secondary index.</p> | 
| <p>JET_errIndexTuplesTooManyColumns<br />-1431</p> | <p>The index definition for the tuple index contains more key columns that the database engine can support.</p><p><strong>Note  </strong>The JET_errIndexTuplesOneColumnOnly error is obsolete and has been replaced by JET_errIndexTuplesTooManyColumns.</p> | 
| <p>JET_errIndexTuplesNonUniqueOnly<br />-1432</p> | <p>The tuple index must be a non-unique index.</p> | 
| <p>JET_errIndexTuplesTextBinaryColumnsOnly<br />-1433</p> | <p>A tuple index definition can only contain key columns that have text or binary column types.</p><p><strong>Note  </strong>The JET_errIndexTuplesTextColumnsOnly error is obsolete and has been replaced by JET_errIndexTuplesTextBinaryColumnsOnly.</p> | 
| <p>JET_errIndexTuplesVarSegMacNotAllowed<br />-1434</p> | <p>The tuple index does not allow setting cbVarSegMac.</p> | 
| <p>JET_errIndexTuplesInvalidLimits<br />-1435</p> | <p>The minimum/maximum tuple length or the maximum number of characters that are specified for an index are invalid.</p> | 
| <p>JET_errIndexTuplesCannotRetrieveFromIndex<br />-1436</p> | <p><a href="gg269198(v=exchg.10).md">JetRetrieveColumn</a> cannot be called with the JET_bitRetrieveFromIndex flag set while retrieving a column on a tuple index.</p> | 
| <p>JET_errIndexTuplesKeyTooSmall<br />-1437</p> | <p>The specified key does not meet the minimum tuple length.</p> | 
| <p>JET_errColumnLong<br />-1501</p> | <p>The column value is long.</p> | 
| <p>JET_errColumnNoChunk<br />-1502</p> | <p>There is no such chunk in a long value.</p> | 
| <p>JET_errColumnDoesNotFit<br />-1503</p> | <p>The field will not fit in the record.</p> | 
| <p>JET_errNullInvalid<br />-1504</p> | <p>Null is not valid.</p> | 
| <p>JET_errColumnIllegalNull<br />JET_errNullInvalid</p> | <p>Null is not valid. This error is returned by the record manager.</p> | 
| <p>JET_errColumnIndexed -1505</p> | <p>The column is indexed and cannot be deleted.</p> | 
| <p>JET_errColumnTooBig -1506</p> | <p>The field length is greater than maximum allowed length.</p> | 
| <p>JET_errColumnNotFound -1507</p> | <p>There is no such column.</p> | 
| <p>JET_errColumnDuplicate -1508</p> | <p>This field is already defined.</p> | 
| <p>JET_errMultiValuedColumnMustBeTagged -1509</p> | <p>An attempt was made to create a multi-valued column, but the column was not tagged.</p> | 
| <p>JET_errColumnRedundant -1510</p> | <p>There was a second auto-increment or version column.</p> | 
| <p>JET_errInvalidColumnType -1511</p> | <p>The column data type is invalid.</p> | 
| <p>JET_errTaggedNotNULL -1514</p> | <p>There are no non-NULL tagged columns.</p> | 
| <p>JET_errNoCurrentIndex -1515</p> | <p>The database is invalid because it does not contain a current index.</p> | 
| <p>JET_errKeyIsMade -1516</p> | <p>The key is completely made.</p> | 
| <p>JET_errBadColumnId -1517</p> | <p>The column ID is incorrect.</p> | 
| <p>JET_errBadItagSequence -1518</p> | <p>There is a bad itagSequence for the tagged column.</p> | 
| <p>JET_errColumnInRelationship -1519</p> | <p>A column cannot be deleted because it is part of a relationship.</p> | 
| <p>JET_errCannotBeTagged -1521</p> | <p>The auto increment and version cannot be tagged.</p> | 
| <p>JET_errDefaultValueTooBig -1524</p> | <p>The default value exceeds the maximum size.</p> | 
| <p>JET_errMultiValuedDuplicate -1525</p> | <p>A duplicate value was detected on a unique multi-valued column.</p> | 
| <p>JET_errLVCorrupted -1526</p> | <p>Corruption was encountered in a long-value tree.</p> | 
| <p>JET_errMultiValuedDuplicateAfterTruncation -1528</p> | <p>A duplicate value was detected on a unique multi-valued column after the data was normalized, and it is normalizing truncated the data before comparison.</p> | 
| <p>JET_errDerivedColumnCorruption -1529</p> | <p>There is an invalid column in derived table.</p> | 
| <p>JET_errInvalidPlaceholderColumn -1530</p> | <p>An attempt was made to convert a column to a primary index placeholder, but the column does not meet the necessary criteria.</p> | 
| <p>JET_errRecordNotFound -1601</p> | <p>The key was not found.</p> | 
| <p>JET_errRecordNoCopy -1602</p> | <p>There is no working buffer.</p> | 
| <p>JET_errNoCurrentRecord -1603</p> | <p>There is no current record.</p> | 
| <p>JET_errRecordPrimaryChanged -1604</p> | <p>The primary key might not change.</p> | 
| <p>JET_errKeyDuplicate -1605</p> | <p>There is an illegal duplicate key.</p> | 
| <p>JET_errAlreadyPrepared -1607</p> | <p>An attempt was made to update a record while a record update was already in progress.</p> | 
| <p>JET_errKeyNotMade -1608</p> | <p>A call was not made to <a href="gg269329(v=exchg.10).md">JetMakeKey</a>.</p> | 
| <p>JET_errUpdateNotPrepared -1609</p> | <p>A call was not made to <a href="gg269339(v=exchg.10).md">JetPrepareUpdate</a>.</p> | 
| <p>JET_errDataHasChanged -1611</p> | <p>The data has changed and the operation was aborted.</p> | 
| <p>JET_errLanguageNotSupported -1619</p> | <p>This Windows installation does not support the selected language.</p> | 
| <p>JET_errTooManySorts -1701</p> | <p>There are too many sort processes.</p> | 
| <p>JET_errInvalidOnSort -1702</p> | <p>An invalid operation occurred during a sort.</p> | 
| <p>JET_errTempFileOpenError -1803</p> | <p>The temporary file could not be opened.</p> | 
| <p>JET_errTooManyAttachedDatabases -1805</p> | <p>Too many databases are open.</p> | 
| <p>JET_errDiskFull -1808</p> | <p>There is no space left on disk.</p> | 
| <p>JET_errPermissionDenied -1809</p> | <p>Permission is denied.</p> | 
| <p>JET_errFileNotFound -1811</p> | <p>The file was not found.</p> | 
| <p>JET_errFileInvalidType -1812</p> | <p>The file type is invalid.</p> | 
| <p>JET_errAfterInitialization -1850</p> | <p>A restore cannot be started after initialization.</p> | 
| <p>JET_errLogCorrupted -1852</p> | <p>The logs could not be interpreted.</p> | 
| <p>JET_errInvalidOperation -1906</p> | <p>The operation is invalid.</p> | 
| <p>JET_errAccessDenied -1907</p> | <p>Access is denied.</p> | 
| <p>JET_errTooManySplits -1909</p> | <p>An infinite split.</p> | 
| <p>JET_errSessionSharingViolation -1910</p> | <p>Multiple threads are using the same session.</p> | 
| <p>JET_errEntryPointNotFound -1911</p> | <p>An entry point in a required DLL could not be found.</p> | 
| <p>JET_errSessionContextAlreadySet -1912</p> | <p>The specified session already has a session context set.</p> | 
| <p>JET_errSessionContextNotSetByThisThread -1913</p> | <p>An attempt was made to reset the session context, but the current thread was not the original one that set the session context.</p> | 
| <p>JET_errSessionInUse -1914</p> | <p>An attempt was made to terminate the session currently in use.</p> | 
| <p>JET_errRecordFormatConversionFailed -1915</p> | <p>An internal error occurred during a dynamic record format conversion.</p> | 
| <p>JET_errOneDatabasePerSession -1916</p> | <p>Only one open user database per session is allowed (as indicated by setting the <a href="gg269337(v=exchg.10).md">JET_paramOneDatabasePerSession</a> flag during database creation).</p> | 
| <p>JET_errRollbackError -1917</p> | <p>There was an error during rollback.</p> | 
| <p>JET_errCallbackFailed -2101</p> | <p>A callback function call failed.</p> | 
| <p>JET_errCallbackNotResolved -2102</p> | <p>A callback function could not be found.</p> | 
| <p>JET_errOSSnapshotInvalidSequence -2401</p> | <p>The operating system shadow copy API was used in an invalid sequence.</p> | 
| <p>JET_errOSSnapshotTimeOut -2402</p> | <p>The operating system shadow copy ended with a time-out.</p> | 
| <p>JET_errOSSnapshotNotAllowed -2403</p> | <p>The operating system shadow copy is not allowed because a backup or recovery in is progress.</p> | 
| <p>JET_errOSSnapshotInvalidSnapId -2404</p> | <p>The operation failed because the specified operating system shadow copy handle was invalid.</p> | 
| <p>JET_errLSCallbackNotSpecified -3000</p> | <p>An attempt was made to use local storage without a callback function being specified.</p> | 
| <p>JET_errLSAlreadySet -3001</p> | <p>An attempt was made to set the local storage for an object which already had it set.</p> | 
| <p>JET_errLSNotSet -3002</p> | <p>An attempt was made to retrieve local storage from an object which did not have it set.</p> | 
| <p>JET_errFileIOSparse -4000</p> | <p>An I/O operation failed because it was attempted against an unallocated region of a file.</p> | 
| <p>JET_errFileIOBeyondEOF -4001</p> | <p>A read was issued to a location beyond the EOF (writes will expand the file).</p> | 
| <p>JET_errFileIOAbort -4002</p> | <p>This flag instructs the JET_ABORTRETRYFAILCALLBACK caller to abort the specified I/O.</p> | 
| <p>JET_errFileIORetry -4003</p> | <p>This flag instructs the JET_ABORTRETRYFAILCALLBACK caller to retry the specified I/O.</p> | 
| <p>JET_errFileIOFail -4004</p> | <p>This flag instructs the JET_ABORTRETRYFAILCALLBACK caller to fail the specified I/O.</p> | 
| <p>JET_errFileCompressed -4005</p> | <p>Read/write access is not supported on compressed files.</p> | 



### Remarks

In general, a value that is greater than zero should be interpreted as a warning, a value of zero should be interpreted as success, and a value that is less than zero should be interpreted as an error. No other patterns in these values, such as ranges of values, should be relied upon by an application.

### Requirements


| Requirement | Value |
|------------|----------|
| <p><strong>Client</strong></p> | <p>Requires Windows Vista, Windows XP, or Windows 2000 Professional.</p> | 
| <p><strong>Server</strong></p> | <p>Requires Windows Server 2008, Windows Server 2003, or Windows 2000 Server.</p> | 
| <p><strong>Header</strong></p> | <p>Declared in Esent.h.</p> | 



### See Also

[Error Handling Parameters](./error-handling-parameters.md)  
[Extensible Storage Engine Errors](./extensible-storage-engine-errors.md)  
[Extensible Storage Engine Files](./extensible-storage-engine-files.md)
