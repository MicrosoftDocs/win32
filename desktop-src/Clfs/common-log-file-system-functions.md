---
Description: 'The following functions are used to manage logs.'
ms.assetid: 'a3059828-d291-493d-a4fe-13d06e49ed12'
title: Common Log File System Functions
---

# Common Log File System Functions

The following functions are used to manage logs.



| Function                                                         | Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AlignReservedLog**](alignreservedlog.md)                     | Calculates the sector-aligned reservation size for a set of records.                                                                                                                                                                                                                             |
| [**AllocReservedLog**](allocreservedlog.md)                     | Allocates sector-aligned space for a set of reserved records.                                                                                                                                                                                                                                    |
| [**CloseAndResetLogFile**](closeandresetlogfile.md)             | Resets the log file and then shuts the log.                                                                                                                                                                                                                                                      |
| [**CreateLogFile**](createlogfile.md)                           | Creates or opens a log.                                                                                                                                                                                                                                                                          |
| [**DeleteLogByHandle**](deletelogbyhandle.md)                   | Marks the specified log for deletion.                                                                                                                                                                                                                                                            |
| [**DeleteLogFile**](deletelogfile.md)                           | Marks a log for deletion.                                                                                                                                                                                                                                                                        |
| [**DumpLogRecords**](dumplogrecords.md)                         | Scans a specified log, filters log records based on record type, and places the records in an output file stream that the caller opens.                                                                                                                                                          |
| [**FlushLogBuffers**](flushlogbuffers.md)                       | Forces all records that are appended to this marshaling area to be flushed to disk.                                                                                                                                                                                                              |
| [**FlushLogToLsn**](flushlogtolsn.md)                           | Forces all records that are appended to this marshaling area up to the record with the specified log sequence number (LSN) to be flushed to the disk.                                                                                                                                            |
| [**FreeReservedLog**](freereservedlog.md)                       | Reduces the number of reserved log records in a marshaling area made by calling [**ReserveAndAppendLog**](reserveandappendlog.md), [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md), or [**AllocReservedLog**](allocreservedlog.md).                                           |
| [**GetLogFileInformation**](getlogfileinformation.md)           | Returns a buffer that contains metadata about a specified log and its current state, as defined by the [**CLFS\_INFORMATION**](clfs-information.md) structure.                                                                                                                                  |
| [**GetLogIoStatistics**](getlogiostatistics.md)                 | Retrieves log I/O statistics for a dedicated or multiplexed log that is associated with the specified handle.                                                                                                                                                                                    |
| [**ReadLogRecord**](readlogrecord.md)                           | Initiates a sequence of reads from a specified log sequence number (LSN) in one of three modes, and returns the first of the specified log records and a read context.                                                                                                                           |
| [**ReadNextLogRecord**](readnextlogrecord.md)                   | Reads the next record in a sequence that is initiated by a call to [**ReadLogRecord**](readlogrecord.md) or [**ReadLogRestartArea**](readlogrestartarea.md).                                                                                                                                   |
| [**ReserveAndAppendLog**](reserveandappendlog.md)               | Reserves space for log buffers, appends a log record to the log, or does both.                                                                                                                                                                                                                   |
| [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) | Reserves space for log buffers, appends a log record to the log, or both. This function is like [**ReserveAndAppendLog**](reserveandappendlog.md), but [**ReserveAndAppendLogAligned**](reserveandappendlogaligned.md) aligns the write entries of the record to the specified byte alignment. |
| [**SetEndOfLog**](setendoflog.md)                               | This function has been deprecated. Use [**TruncateLog**](truncatelog.md) instead.                                                                                                                                                                                                               |
| [**TerminateReadLog**](terminatereadlog.md)                     | Terminates a read context. This function frees system-allocated resources that are associated with the specified read context.                                                                                                                                                                   |
| [**TruncateLog**](truncatelog.md)                               | Truncates the log.                                                                                                                                                                                                                                                                               |



 

The following functions are used to manage containers.



| Function                                                               | Description                                                                                                                                                                                                     |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddLogContainer**](addlogcontainer.md)                             | Adds a container to the physical log that is associated with the log handle, if the calling process has write access to the .blf file and the ability to create files in the target directory of the container. |
| [**AddLogContainerSet**](addlogcontainerset.md)                       | Adds multiple log containers to the physical log that is associated with the log handle, if the calling process has access to the log handle.                                                                   |
| [**CreateLogContainerScanContext**](createlogcontainerscancontext.md) | Creates a scan context to use with [**ScanLogContainers**](scanlogcontainers.md) to enumerate all log containers that are associated with a log, and performs the first scan.                                  |
| [**GetLogContainerName**](getlogcontainername.md)                     | Retrieves the full path name of a container when given its container identifier.                                                                                                                                |
| [**RemoveLogContainer**](removelogcontainer.md)                       | Removes a single container from a log that is associated with a dedicated or multiplexed log handle.                                                                                                            |
| [**RemoveLogContainerSet**](removelogcontainerset.md)                 | Removes multiple containers from a log that is associated with a dedicated or multiplexed log handle.                                                                                                           |
| [**ScanLogContainers**](scanlogcontainers.md)                         | Enumerates log containers. Call this function repeatedly to iterate over all log containers.                                                                                                                    |



 

The following functions are used for crash restart.



| Function                                                         | Description                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvanceLogBase**](advancelogbase.md)                         | Advances the base log sequence number (LSN) of a log stream to the specified LSN.                                                                                                                                                                                                                        |
| [**ReadLogRestartArea**](readlogrestartarea.md)                 | Returns the last restart area that was written successfully to the log associated with the marshaling area of [**WriteLogRestartArea**](writelogrestartarea.md). The function also returns a read context that allows the caller to cursor backward or forward through the log from the restart record. |
| [**ReadPreviousLogRestartArea**](readpreviouslogrestartarea.md) | Reads the previous log restart area that is relative to the current restart record specified in the read context.                                                                                                                                                                                        |
| [**WriteLogRestartArea**](writelogrestartarea.md)               | Appends a new client restart area to a log and optionally advances the base log sequence number (LSN) of the log.                                                                                                                                                                                        |



 

The following functions are used for archiving.



| Function                                                   | Description                                                                                                                             |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNextLogArchiveExtent**](getnextlogarchiveextent.md) | Retrieves the next set of archive extents in a log archive context.                                                                     |
| [**PrepareLogArchive**](preparelogarchive.md)             | Prepares a physical log for archiving.                                                                                                  |
| [**ReadLogArchiveMetadata**](readlogarchivemetadata.md)   | Copies a range of the archive view of the metadata to the specified buffer.                                                             |
| [**SetLogArchiveMode**](setlogarchivemode.md)             | Enables or disables log archive support for a specified log.                                                                            |
| [**SetLogArchiveTail**](setlogarchivetail.md)             | Sets the last archived log sequence number (LSN) or *archive tail* of an archivable log.                                                |
| [**TerminateLogArchive**](terminatelogarchive.md)         | Deallocates system resources that are allocated originally for a log archive context by [**PrepareLogArchive**](preparelogarchive.md). |
| [**ValidateLog**](validatelogrestore.md)                  | Validates the consistency of the log metadata and data before log archive and after log restore.                                        |



 

The following functions are used for marshaling.



| Function                                                     | Description                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLogMarshallingArea**](createlogmarshallingarea.md) | Creates a marshaling area for a log, and when successful it returns a marshaling context.                                       |
| [**DeleteLogMarshallingArea**](deletelogmarshallingarea.md) | Deletes a marshaling area that is created by a successful call to [**CreateLogMarshallingArea**](createlogmarshallingarea.md). |



 

The following functions are used to work with LSNs.



| Function                                       | Description                                                                                              |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**LsnBlockOffset**](lsnblockoffset.md)       | Returns the sector-aligned block offset that is contained in the specified LSN.                          |
| [**LsnContainer**](lsncontainer.md)           | Retrieves the logical container ID that is contained in a specified LSN.                                 |
| [**LsnCreate**](lsncreate.md)                 | Creates a log sequence number (LSN), given a container ID, a block offset, and a record sequence number. |
| [**LsnEqual**](lsnequal.md)                   | Determines whether two LSNs from the same stream are equal.                                              |
| [**LsnGreater**](lsngreater.md)               | Determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream.       |
| [**LsnLess**](lsnless.md)                     | Determines whether one LSN is less than another LSN. The two LSNs must be from the same stream.          |
| [**LsnNull**](lsnnull.md)                     | Determines whether a specified LSN is equal to the smallest possible LSN, which is CLFS\_LSN\_NULL.      |
| [**LsnRecordSequence**](lsnrecordsequence.md) | Retrieves the record sequence number that is contained in a specified LSN.                               |



 

 

 



