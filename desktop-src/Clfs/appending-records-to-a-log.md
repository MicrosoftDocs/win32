---
Description: Common Log File System (CLFS) is optimized for performance.
ms.assetid: b6f9793e-ac8f-42f2-b3bd-fefa86b1cb84
title: Appending Records to a Log
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Appending Records to a Log

Common Log File System (CLFS) is optimized for performance. When a log client appends records to the log, the records are buffered in the client's marshaling area until they are written to the disk by a flush operation. That reduces the number of transitions between user and kernel mode, and increases the size of physical I/O's to disk.

Data is written to the disk directly from client marshaling buffers without copying. Read operations actively attempt to short-circuit disk accesses by caching recently read or written log records in the system cache and client marshaling buffers, respectively.

The following procedure describes how to append records to a log by using CLFS.

**To append a record to a log**

1.  Create a new log or open an existing log by calling the [**CreateLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogfile) function.

    If the function succeeds, the log client receives an open handle that can be used to write to the log.

    The target log can be a dedicated log or a log stream. When a new log is created, it does not have containers associated with it. In the next step of this procedure, space is added to the log in the form of log containers.

    The log client must have appropriate credentials to create or open the log. If the log client creates a log, the name of the log can contain any characters that are considered valid for file names by the underlying file system.

2.  Allocate disk space to the log by calling the [**AddLogContainer**](/windows/desktop/api/Clfsw32/nf-clfsw32-addlogcontainer) or [**AddLogContainerSet**](/windows/desktop/api/Clfsw32/nf-clfsw32-addlogcontainerset) function.

    To write to a log, the log must have at least two log containers. The log container size must be a multiple of 512 KB, and for multiplexed logs, must be a minimum of 1 MB. Additionally, all log containers that are associated with a log are an equal size. Therefore, a multiplexed log requires a minimum of 2 MB of disk space; otherwise, log-write operations fail. You can increase the capacity of an existing log at any time by adding one or more containers.

3.  Create a marshaling area by calling the [**CreateLogMarshallingArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogmarshallingarea) function.

    You can specify allocation and memory free callback functions to exert more control on the memory that is associated with the marshaling area. The maximum number of buffers and size of each buffer must be specified, and all buffers allocated are the same size.

    CLFS allocates write buffers as required, which depends on the maximum number specified. Ensure that the size of the buffer is large enough to hold the largest log record to be written to the log.

    > [!Note]  
    > marshaling contexts are thread-safe.

     

4.  Append the log by calling the [**ReserveAndAppendLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlog) function with the marshaling area created in the previous step of this procedure.

    Use the [**ReserveAndAppendLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-reserveandappendlog) function as the standard utility function to log records. Reserving log space is not required unless your log client must ensure that "log full" errors are not encountered at inconvenient times.

    For example, log reservation can be used by clients that support transactions. These clients need guaranteed space in the log for logging undo-records while they roll back transactions. These records are not written until the marshaling area is flushed.

5.  (Optional) Flush the appended record by calling the [**FlushLogBuffers**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogbuffers) or [**FlushLogToLsn**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogtolsn) function.

    Occasionally, you may want to flush a log to ensure that log records, up to a specified record, are written to disk. The [**FlushLogToLsn**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogtolsn) function flushes records up to a specified log sequence number (LSN) and the [**FlushLogBuffers**](/windows/desktop/api/Clfsw32/nf-clfsw32-flushlogbuffers) function flushes all records in the marshaling area.

 

 



