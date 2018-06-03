---
Description: CLFS provides you with the information that you need to archive and restore your logs.
ms.assetid: 648850f0-cb65-4a6e-8c31-73d62a387e31
title: Log Archive and Restore
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Log Archive and Restore

CLFS provides you with the information that you need to archive and restore your logs. It does not perform the archive and restore operations itself. You can write an archive and restore application to write your log to a durable medium. To keep an ongoing history of log records, logs must be archived periodically. If archived data must be accessed for legal, technical, or other reasons, log records must be restored.

A non-ephemeral log persists the data until it is archived. An ephemeral log is not archived; older data is discarded to make space for new data.

If your logs are not ephemeral, you must archive it periodically to reclaim space. You can only archive and restore physical logs; you cannot archive an individual log stream.

To track the portions of a log that are archived so that log space can be recycled, CLFS marks the last archived log sequence number (LSN), which is called the *log archive tail*. The log archive tail can be set by using the [**SetLogArchiveTail**](/windows/desktop/api/Clfsw32/nf-clfsw32-setlogarchivetail) function. Then, you can move the tail, freeing up space.

Logs that are created with the **FILE\_ATTRIBUTE\_ARCHIVE** flag are non-ephemeral and require archiving. Logs that are created without the **FILE\_ATTRIBUTE\_ARCHIVE** flag are ephemeral do not require archiving. Calling the [**PrepareLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-preparelogarchive) or [**SetLogArchiveTail**](/windows/desktop/api/Clfsw32/nf-clfsw32-setlogarchivetail) function on an ephemeral log returns the error **ERROR\_LOG\_EPHEMERAL**. The mode of the log can be switched between ephemeral and non-ephemeral.

When you restore a log, you restore it to the point in time at which the archive was written. If you must process all of the data in all the archive sets to be restored, you must process data after each archive has been restored; otherwise, you may overwrite data. For example, if you have a log with 4 containers, you can create an archive set that contains 5 archives. The first archive consists of all 4 containers, and archives 2-5 back up a single container each. If you restore all 5 archives in your archive set, you will never see the data of the first archive (the one with all 4 containers) because it is overwritten by the data in archives 2-5.

If you are logging transactional data for re-do operations, to restore your resource, you must restore the first set of data, apply the re-do information from the log, make note of the last LSN, and repeat these steps for each archive in the set.

The following functions can be used to perform log archiving and restoring.



| Function                                                   | Description                                                                                                                                        |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetNextLogArchiveExtent**](/windows/desktop/api/Clfsw32/nf-clfsw32-getnextlogarchiveextent) | Gets the next set of archive extents in a log archive context.                                                                                     |
| [**PrepareLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-preparelogarchive)             | Used by a log archival client to prepare to archive a log.                                                                                         |
| [**ReadLogArchiveMetadata**](/windows/desktop/api/Clfsw32/nf-clfsw32-readlogarchivemetadata)   | Copies a range of the archive view of the metadata to the specified buffer.                                                                        |
| [**SetLogArchiveMode**](/windows/desktop/api/ClfsW32/nf-clfsw32-setlogarchivemode)             | Enables or disables log archive support for a specified log.                                                                                       |
| [**SetLogArchiveTail**](/windows/desktop/api/Clfsw32/nf-clfsw32-setlogarchivetail)             | Sets the last archived LSN, or *archive tail* of a non-ephemeral log.                                                                              |
| [**TerminateLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-terminatelogarchive)         | Deallocates all system resources that are originally allocated to a valid log archive context with [**PrepareLogArchive**](/windows/desktop/api/Clfsw32/nf-clfsw32-preparelogarchive). |
| [**ValidateLog**](/windows/desktop/api/Clfsw32/nf-clfsw32-validatelog)                  | Validates the consistency of both log metadata and data before archiving and after log restore.                                                    |



 

 

 



