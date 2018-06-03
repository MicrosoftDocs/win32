---
Description: The following functions are used to manage logs.
ms.assetid: a3059828-d291-493d-a4fe-13d06e49ed12
title: Common Log File System Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Common Log File System Functions

The following functions are used to manage logs.



| Function                                                         | Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AlignReservedLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-alignreservedlog)                     | Calculates the sector-aligned reservation size for a set of records.                                                                                                                                                                                                                             |
| [**AllocReservedLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-allocreservedlog)                     | Allocates sector-aligned space for a set of reserved records.                                                                                                                                                                                                                                    |
| [**CloseAndResetLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-closeandresetlogfile)             | Resets the log file and then shuts the log.                                                                                                                                                                                                                                                      |
| [**CreateLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogfile)                           | Creates or opens a log.                                                                                                                                                                                                                                                                          |
| [**DeleteLogByHandle**](/windows/desktop/api/Clfsw32/nf-clfsw32-deletelogbyhandle)                   | Marks the specified log for deletion.                                                                                                                                                                                                                                                            |
| [**DeleteLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-deletelogfile)                           | Marks a log for deletion.                                                                                                                                                                                                                                                                        |
| [**DumpLogRecords**](/windows/desktop/api/Clfsw32/nf-clfsw32-dumplogrecords)                         | Scans a specified log, filters log records based on record type, and places the records in an output file stream that the caller opens.                                                                                                                                                          |
| [**FlushLogBuffers**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogbuffers)                       | Forces all records that are appended to this marshaling area to be flushed to disk.                                                                                                                                                                                                              |
| [**FlushLogToLsn**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogtolsn)                           | Forces all records that are appended to this marshaling area up to the record with the specified log sequence number (LSN) to be flushed to the disk.                                                                                                                                            |
| [**FreeReservedLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-freereservedlog)                       | Reduces the number of reserved log records in a marshaling area made by calling [**ReserveAndAppendLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlog), [**ReserveAndAppendLogAligned**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlogaligned), or [**AllocReservedLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-allocreservedlog).                                           |
| [**GetLogFileInformation**](/windows/desktop/api/Clfsw32/nf-clfsw32-getlogfileinformation)           | Returns a buffer that contains metadata about a specified log and its current state, as defined by the [**CLFS\_INFORMATION**](/windows/desktop/api/Clfs/ns-clfs-_cls_information) structure.                                                                                                                                  |
| [**GetLogIoStatistics**](/windows/desktop/api/Clfsw32/nf-clfsw32-getlogiostatistics)                 | Retrieves log I/O statistics for a dedicated or multiplexed log that is associated with the specified handle.                                                                                                                                                                                    |
| [**ReadLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrecord)                           | Initiates a sequence of reads from a specified log sequence number (LSN) in one of three modes, and returns the first of the specified log records and a read context.                                                                                                                           |
| [**ReadNextLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readnextlogrecord)                   | Reads the next record in a sequence that is initiated by a call to [**ReadLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrecord) or [**ReadLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrestartarea).                                                                                                                                   |
| [**ReserveAndAppendLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlog)               | Reserves space for log buffers, appends a log record to the log, or does both.                                                                                                                                                                                                                   |
| [**ReserveAndAppendLogAligned**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlogaligned) | Reserves space for log buffers, appends a log record to the log, or both. This function is like [**ReserveAndAppendLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlog), but [**ReserveAndAppendLogAligned**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlogaligned) aligns the write entries of the record to the specified byte alignment. |
| [**SetEndOfLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-setendoflog)                               | This function has been deprecated. Use [**TruncateLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-truncatelog) instead.                                                                                                                                                                                                               |
| [**TerminateReadLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-terminatereadlog)                     | Terminates a read context. This function frees system-allocated resources that are associated with the specified read context.                                                                                                                                                                   |
| [**TruncateLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-truncatelog)                               | Truncates the log.                                                                                                                                                                                                                                                                               |



 

The following functions are used to manage containers.



| Function                                                               | Description                                                                                                                                                                                                     |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddLogContainer**](/windows/desktop/api/Clfsw32/nf-clfsw32-addlogcontainer)                             | Adds a container to the physical log that is associated with the log handle, if the calling process has write access to the .blf file and the ability to create files in the target directory of the container. |
| [**AddLogContainerSet**](/windows/desktop/api/Clfsw32/nf-clfsw32-addlogcontainerset)                       | Adds multiple log containers to the physical log that is associated with the log handle, if the calling process has access to the log handle.                                                                   |
| [**CreateLogContainerScanContext**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogcontainerscancontext) | Creates a scan context to use with [**ScanLogContainers**](/windows/desktop/api/Clfsw32/nf-clfsw32-scanlogcontainers) to enumerate all log containers that are associated with a log, and performs the first scan.                                  |
| [**GetLogContainerName**](/windows/desktop/api/Clfsw32/nf-clfsw32-getlogcontainername)                     | Retrieves the full path name of a container when given its container identifier.                                                                                                                                |
| [**RemoveLogContainer**](/windows/desktop/api/Clfsw32/nf-clfsw32-removelogcontainer)                       | Removes a single container from a log that is associated with a dedicated or multiplexed log handle.                                                                                                            |
| [**RemoveLogContainerSet**](/windows/desktop/api/Clfsw32/nf-clfsw32-removelogcontainerset)                 | Removes multiple containers from a log that is associated with a dedicated or multiplexed log handle.                                                                                                           |
| [**ScanLogContainers**](/windows/desktop/api/Clfsw32/nf-clfsw32-scanlogcontainers)                         | Enumerates log containers. Call this function repeatedly to iterate over all log containers.                                                                                                                    |



 

The following functions are used for crash restart.



| Function                                                         | Description                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvanceLogBase**](/windows/desktop/api/Clfsw32/nf-clfsw32-advancelogbase)                         | Advances the base log sequence number (LSN) of a log stream to the specified LSN.                                                                                                                                                                                                                        |
| [**ReadLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrestartarea)                 | Returns the last restart area that was written successfully to the log associated with the marshaling area of [**WriteLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-writelogrestartarea). The function also returns a read context that allows the caller to cursor backward or forward through the log from the restart record. |
| [**ReadPreviousLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-readpreviouslogrestartarea) | Reads the previous log restart area that is relative to the current restart record specified in the read context.                                                                                                                                                                                        |
| [**WriteLogRestartArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-writelogrestartarea)               | Appends a new client restart area to a log and optionally advances the base log sequence number (LSN) of the log.                                                                                                                                                                                        |



 

The following functions are used for archiving.



| Function                                                   | Description                                                                                                                             |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNextLogArchiveExtent**](/windows/desktop/api/Clfsw32/nf-clfsw32-getnextlogarchiveextent) | Retrieves the next set of archive extents in a log archive context.                                                                     |
| [**PrepareLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-preparelogarchive)             | Prepares a physical log for archiving.                                                                                                  |
| [**ReadLogArchiveMetadata**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogarchivemetadata)   | Copies a range of the archive view of the metadata to the specified buffer.                                                             |
| [**SetLogArchiveMode**](/windows/desktop/api/ClfsW32/nf-clfsw32-setlogarchivemode)             | Enables or disables log archive support for a specified log.                                                                            |
| [**SetLogArchiveTail**](/windows/desktop/api/Clfsw32/nf-clfsw32-setlogarchivetail)             | Sets the last archived log sequence number (LSN) or *archive tail* of an archivable log.                                                |
| [**TerminateLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-terminatelogarchive)         | Deallocates system resources that are allocated originally for a log archive context by [**PrepareLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-preparelogarchive). |
| [**ValidateLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-validatelog)                  | Validates the consistency of the log metadata and data before log archive and after log restore.                                        |



 

The following functions are used for marshaling.



| Function                                                     | Description                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLogMarshallingArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogmarshallingarea) | Creates a marshaling area for a log, and when successful it returns a marshaling context.                                       |
| [**DeleteLogMarshallingArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-deletelogmarshallingarea) | Deletes a marshaling area that is created by a successful call to [**CreateLogMarshallingArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogmarshallingarea). |



 

The following functions are used to work with LSNs.



| Function                                       | Description                                                                                              |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**LsnBlockOffset**](/windows/desktop/api/Clfsw32/nf-clfsw32-lsnblockoffset)       | Returns the sector-aligned block offset that is contained in the specified LSN.                          |
| [**LsnContainer**](/windows/desktop/api/Clfsw32/nf-clfsw32-lsncontainer)           | Retrieves the logical container ID that is contained in a specified LSN.                                 |
| [**LsnCreate**](/windows/desktop/api/Clfsw32/nf-clfsw32-lsncreate)                 | Creates a log sequence number (LSN), given a container ID, a block offset, and a record sequence number. |
| [**LsnEqual**](/windows/desktop/api/Clfs/nf-clfs-clfslsnequal)                   | Determines whether two LSNs from the same stream are equal.                                              |
| [**LsnGreater**](/windows/desktop/api/Clfs/nf-clfs-clfslsngreater)               | Determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream.       |
| [**LsnLess**](/windows/desktop/api/Clfs/nf-clfs-clfslsnless)                     | Determines whether one LSN is less than another LSN. The two LSNs must be from the same stream.          |
| [**LsnNull**](/windows/desktop/api/Clfs/nf-clfs-clfslsnnull)                     | Determines whether a specified LSN is equal to the smallest possible LSN, which is CLFS\_LSN\_NULL.      |
| [**LsnRecordSequence**](/windows/desktop/api/Clfsw32/nf-clfsw32-lsnrecordsequence) | Retrieves the record sequence number that is contained in a specified LSN.                               |



 

 

 



