---
Description: The following functions are used to manage logs.
ms.assetid: a3059828-d291-493d-a4fe-13d06e49ed12
title: Common Log File System Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Common Log File System Functions

The following functions are used to manage logs.



| Function                                                         | Description                                                                                                                                                                                                                                                                                      |
|------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AlignReservedLog**](/windows/win32/Clfsw32/nf-clfsw32-alignreservedlog?branch=master)                     | Calculates the sector-aligned reservation size for a set of records.                                                                                                                                                                                                                             |
| [**AllocReservedLog**](/windows/win32/Clfsw32/nf-clfsw32-allocreservedlog?branch=master)                     | Allocates sector-aligned space for a set of reserved records.                                                                                                                                                                                                                                    |
| [**CloseAndResetLogFile**](/windows/win32/Clfsw32/nf-clfsw32-closeandresetlogfile?branch=master)             | Resets the log file and then shuts the log.                                                                                                                                                                                                                                                      |
| [**CreateLogFile**](/windows/win32/Clfsw32/nf-clfsw32-createlogfile?branch=master)                           | Creates or opens a log.                                                                                                                                                                                                                                                                          |
| [**DeleteLogByHandle**](/windows/win32/Clfsw32/nf-clfsw32-deletelogbyhandle?branch=master)                   | Marks the specified log for deletion.                                                                                                                                                                                                                                                            |
| [**DeleteLogFile**](/windows/win32/Clfsw32/nf-clfsw32-deletelogfile?branch=master)                           | Marks a log for deletion.                                                                                                                                                                                                                                                                        |
| [**DumpLogRecords**](/windows/win32/Clfsw32/nf-clfsw32-dumplogrecords?branch=master)                         | Scans a specified log, filters log records based on record type, and places the records in an output file stream that the caller opens.                                                                                                                                                          |
| [**FlushLogBuffers**](/windows/win32/Clfsw32/nf-clfsw32-flushlogbuffers?branch=master)                       | Forces all records that are appended to this marshaling area to be flushed to disk.                                                                                                                                                                                                              |
| [**FlushLogToLsn**](/windows/win32/Clfsw32/nf-clfsw32-flushlogtolsn?branch=master)                           | Forces all records that are appended to this marshaling area up to the record with the specified log sequence number (LSN) to be flushed to the disk.                                                                                                                                            |
| [**FreeReservedLog**](/windows/win32/Clfsw32/nf-clfsw32-freereservedlog?branch=master)                       | Reduces the number of reserved log records in a marshaling area made by calling [**ReserveAndAppendLog**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlog?branch=master), [**ReserveAndAppendLogAligned**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlogaligned?branch=master), or [**AllocReservedLog**](/windows/win32/Clfsw32/nf-clfsw32-allocreservedlog?branch=master).                                           |
| [**GetLogFileInformation**](/windows/win32/Clfsw32/nf-clfsw32-getlogfileinformation?branch=master)           | Returns a buffer that contains metadata about a specified log and its current state, as defined by the [**CLFS\_INFORMATION**](/windows/win32/Clfs/ns-clfs-_cls_information?branch=master) structure.                                                                                                                                  |
| [**GetLogIoStatistics**](/windows/win32/Clfsw32/nf-clfsw32-getlogiostatistics?branch=master)                 | Retrieves log I/O statistics for a dedicated or multiplexed log that is associated with the specified handle.                                                                                                                                                                                    |
| [**ReadLogRecord**](/windows/win32/Clfsw32/nf-clfsw32-readlogrecord?branch=master)                           | Initiates a sequence of reads from a specified log sequence number (LSN) in one of three modes, and returns the first of the specified log records and a read context.                                                                                                                           |
| [**ReadNextLogRecord**](/windows/win32/Clfsw32/nf-clfsw32-readnextlogrecord?branch=master)                   | Reads the next record in a sequence that is initiated by a call to [**ReadLogRecord**](/windows/win32/Clfsw32/nf-clfsw32-readlogrecord?branch=master) or [**ReadLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-readlogrestartarea?branch=master).                                                                                                                                   |
| [**ReserveAndAppendLog**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlog?branch=master)               | Reserves space for log buffers, appends a log record to the log, or does both.                                                                                                                                                                                                                   |
| [**ReserveAndAppendLogAligned**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlogaligned?branch=master) | Reserves space for log buffers, appends a log record to the log, or both. This function is like [**ReserveAndAppendLog**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlog?branch=master), but [**ReserveAndAppendLogAligned**](/windows/win32/Clfsw32/nf-clfsw32-reserveandappendlogaligned?branch=master) aligns the write entries of the record to the specified byte alignment. |
| [**SetEndOfLog**](/windows/win32/Clfsw32/nf-clfsw32-setendoflog?branch=master)                               | This function has been deprecated. Use [**TruncateLog**](/windows/win32/Clfsw32/nf-clfsw32-truncatelog?branch=master) instead.                                                                                                                                                                                                               |
| [**TerminateReadLog**](/windows/win32/Clfsw32/nf-clfsw32-terminatereadlog?branch=master)                     | Terminates a read context. This function frees system-allocated resources that are associated with the specified read context.                                                                                                                                                                   |
| [**TruncateLog**](/windows/win32/Clfsw32/nf-clfsw32-truncatelog?branch=master)                               | Truncates the log.                                                                                                                                                                                                                                                                               |



 

The following functions are used to manage containers.



| Function                                                               | Description                                                                                                                                                                                                     |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddLogContainer**](/windows/win32/Clfsw32/nf-clfsw32-addlogcontainer?branch=master)                             | Adds a container to the physical log that is associated with the log handle, if the calling process has write access to the .blf file and the ability to create files in the target directory of the container. |
| [**AddLogContainerSet**](/windows/win32/Clfsw32/nf-clfsw32-addlogcontainerset?branch=master)                       | Adds multiple log containers to the physical log that is associated with the log handle, if the calling process has access to the log handle.                                                                   |
| [**CreateLogContainerScanContext**](/windows/win32/Clfsw32/nf-clfsw32-createlogcontainerscancontext?branch=master) | Creates a scan context to use with [**ScanLogContainers**](/windows/win32/Clfsw32/nf-clfsw32-scanlogcontainers?branch=master) to enumerate all log containers that are associated with a log, and performs the first scan.                                  |
| [**GetLogContainerName**](/windows/win32/Clfsw32/nf-clfsw32-getlogcontainername?branch=master)                     | Retrieves the full path name of a container when given its container identifier.                                                                                                                                |
| [**RemoveLogContainer**](/windows/win32/Clfsw32/nf-clfsw32-removelogcontainer?branch=master)                       | Removes a single container from a log that is associated with a dedicated or multiplexed log handle.                                                                                                            |
| [**RemoveLogContainerSet**](/windows/win32/Clfsw32/nf-clfsw32-removelogcontainerset?branch=master)                 | Removes multiple containers from a log that is associated with a dedicated or multiplexed log handle.                                                                                                           |
| [**ScanLogContainers**](/windows/win32/Clfsw32/nf-clfsw32-scanlogcontainers?branch=master)                         | Enumerates log containers. Call this function repeatedly to iterate over all log containers.                                                                                                                    |



 

The following functions are used for crash restart.



| Function                                                         | Description                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvanceLogBase**](/windows/win32/Clfsw32/nf-clfsw32-advancelogbase?branch=master)                         | Advances the base log sequence number (LSN) of a log stream to the specified LSN.                                                                                                                                                                                                                        |
| [**ReadLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-readlogrestartarea?branch=master)                 | Returns the last restart area that was written successfully to the log associated with the marshaling area of [**WriteLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-writelogrestartarea?branch=master). The function also returns a read context that allows the caller to cursor backward or forward through the log from the restart record. |
| [**ReadPreviousLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-readpreviouslogrestartarea?branch=master) | Reads the previous log restart area that is relative to the current restart record specified in the read context.                                                                                                                                                                                        |
| [**WriteLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-writelogrestartarea?branch=master)               | Appends a new client restart area to a log and optionally advances the base log sequence number (LSN) of the log.                                                                                                                                                                                        |



 

The following functions are used for archiving.



| Function                                                   | Description                                                                                                                             |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNextLogArchiveExtent**](/windows/win32/Clfsw32/nf-clfsw32-getnextlogarchiveextent?branch=master) | Retrieves the next set of archive extents in a log archive context.                                                                     |
| [**PrepareLogArchive**](/windows/win32/Clfsw32/nf-clfsw32-preparelogarchive?branch=master)             | Prepares a physical log for archiving.                                                                                                  |
| [**ReadLogArchiveMetadata**](/windows/win32/Clfsw32/nf-clfsw32-readlogarchivemetadata?branch=master)   | Copies a range of the archive view of the metadata to the specified buffer.                                                             |
| [**SetLogArchiveMode**](/windows/win32/ClfsW32/nf-clfsw32-setlogarchivemode?branch=master)             | Enables or disables log archive support for a specified log.                                                                            |
| [**SetLogArchiveTail**](/windows/win32/Clfsw32/nf-clfsw32-setlogarchivetail?branch=master)             | Sets the last archived log sequence number (LSN) or *archive tail* of an archivable log.                                                |
| [**TerminateLogArchive**](/windows/win32/Clfsw32/nf-clfsw32-terminatelogarchive?branch=master)         | Deallocates system resources that are allocated originally for a log archive context by [**PrepareLogArchive**](/windows/win32/Clfsw32/nf-clfsw32-preparelogarchive?branch=master). |
| [**ValidateLog**](/windows/win32/Clfsw32/nf-clfsw32-validatelog?branch=master)                  | Validates the consistency of the log metadata and data before log archive and after log restore.                                        |



 

The following functions are used for marshaling.



| Function                                                     | Description                                                                                                                     |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**CreateLogMarshallingArea**](/windows/win32/Clfsw32/nf-clfsw32-createlogmarshallingarea?branch=master) | Creates a marshaling area for a log, and when successful it returns a marshaling context.                                       |
| [**DeleteLogMarshallingArea**](/windows/win32/Clfsw32/nf-clfsw32-deletelogmarshallingarea?branch=master) | Deletes a marshaling area that is created by a successful call to [**CreateLogMarshallingArea**](/windows/win32/Clfsw32/nf-clfsw32-createlogmarshallingarea?branch=master). |



 

The following functions are used to work with LSNs.



| Function                                       | Description                                                                                              |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**LsnBlockOffset**](/windows/win32/Clfsw32/nf-clfsw32-lsnblockoffset?branch=master)       | Returns the sector-aligned block offset that is contained in the specified LSN.                          |
| [**LsnContainer**](/windows/win32/Clfsw32/nf-clfsw32-lsncontainer?branch=master)           | Retrieves the logical container ID that is contained in a specified LSN.                                 |
| [**LsnCreate**](/windows/win32/Clfsw32/nf-clfsw32-lsncreate?branch=master)                 | Creates a log sequence number (LSN), given a container ID, a block offset, and a record sequence number. |
| [**LsnEqual**](/windows/win32/Clfs/nf-clfs-clfslsnequal?branch=master)                   | Determines whether two LSNs from the same stream are equal.                                              |
| [**LsnGreater**](/windows/win32/Clfs/nf-clfs-clfslsngreater?branch=master)               | Determines whether one LSN is greater than another LSN. The two LSNs must be from the same stream.       |
| [**LsnLess**](/windows/win32/Clfs/nf-clfs-clfslsnless?branch=master)                     | Determines whether one LSN is less than another LSN. The two LSNs must be from the same stream.          |
| [**LsnNull**](/windows/win32/Clfs/nf-clfs-clfslsnnull?branch=master)                     | Determines whether a specified LSN is equal to the smallest possible LSN, which is CLFS\_LSN\_NULL.      |
| [**LsnRecordSequence**](/windows/win32/Clfsw32/nf-clfsw32-lsnrecordsequence?branch=master) | Retrieves the record sequence number that is contained in a specified LSN.                               |



 

 

 



