---
Description: The following procedure identifies how to read log records by using the Common Log File System (CLFS).
ms.assetid: c7e5a038-9a97-4580-84d9-57972b103d0c
title: Reading Records from a Log
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Reading Records from a Log

The following procedure identifies how to read log records by using the Common Log File System (CLFS).

**To read records from a log**

1.  Open an existing log by calling the [**CreateLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogfile) function.

    The reader receives an open handle that can be used to read records from the log stream. For more information about creating a new log, see [Create a Log File](creating-a-log-file.md).

2.  Create a marshaling area by calling the [**CreateLogMarshallingArea**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogmarshallingarea) function.

    This call only succeeds if there is at least one container in the log. The marshaling area is a set of log-block buffers that are allocated to contain application records that the reader can read from the log. The reader has the option to specify callback functions to control how the memory associated with the marshaling area is allocated and freed. The maximum number of read and write buffers and the size of each buffer must be specified, and all buffers that are allocated from the same marshaling area are of the same size.

    > [!Note]  
    > Marshaling contexts are thread-safe.

     

    CLFS allocates log-block buffers as required, which depends on the maximum number specified. You must ensure that the buffer size is large enough to accommodate the largest log block in the log.

3.  Read from the log by calling the [**ReadLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrecord) function.

    To read a log record, the reader application must specify a marshaling context, the starting LSN to read from, and one of three modes in which records are to be read. The modes are: **ClfsContextPrevious**, **ClfsContextUndoNext**, and **ClfsContextForward**.

    When marshaling contexts are created successfully, the reader application can start reading log records, and receives a read context with the first record is read. This context must be specified in read-next operations, and is updated on every CLFS read.

    > [!Note]  
    > Each read context maintains a cursor into the log-block buffers. As a result, read contexts are not thread-safe, and support only one asynchronous operation at a time. Therefore, the reader application is responsible for ensuring synchronization before it invokes the log services module with a shared read context.

     

4.  Optionally, continue reading log records by calling the [**ReadNextLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readnextlogrecord) function.
5.  Free the context that the [**ReadLogRecord**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogrecord) function returns by calling the [**TerminateReadLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-terminatereadlog) function.

    This ensures that there are no memory leaks associated with the read context.

6.  Close the handle that the [**CreateLogFile**](/windows/desktop/api/Clfsw32/nf-clfsw32-createlogfile) function returns by calling the [**CloseHandle**](https://msdn.microsoft.com/windows/desktop/9b84891d-62ca-4ddc-97b7-c4c79482abd9) function.

 

 



