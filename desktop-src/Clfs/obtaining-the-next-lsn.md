---
Description: If you are trying to advance the base log sequence number (LSN) of a log, or trying to read records from a log, typically you need to specify an LSN to a valid record in the log.
ms.assetid: 2e47a5c9-a0bd-4cd1-ba30-9ebde6df0f91
title: Obtaining the Next LSN
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining the Next LSN

If you are trying to advance the base log sequence number (LSN) of a log, or trying to read records from a log, typically you need to specify an LSN to a valid record in the log. There are two ways to obtain the next LSN, and the way you use depends on whether you want the last LSN in the log, or the LSN that will be assigned to the next record added.

The following list identifies the two ways to obtain the next LSN:

-   Reading records sequentially by using the [**ReadNextLogRecord**](/windows/win32/Clfsw32/nf-clfsw32-readnextlogrecord?branch=master) function always return valid log records. The last valid log record is the last record that is read before encountering the end-of-file marker.
-   Querying the log metadata by using the [**GetLogFileInformation**](/windows/win32/Clfsw32/nf-clfsw32-getlogfileinformation?branch=master) function returns the next available LSN in the **LastLsn** member of the [**CLFS\_INFORMATION**](/windows/win32/Clfs/ns-clfs-_cls_information?branch=master) structure. Then you can use the [**AdvanceLogBase**](/windows/win32/Clfsw32/nf-clfsw32-advancelogbase?branch=master) function to advance the base LSN beyond the last record in the log.

For example, if you are using the [**AdvanceLogBase**](/windows/win32/Clfsw32/nf-clfsw32-advancelogbase?branch=master) or [**WriteLogRestartArea**](/windows/win32/Clfsw32/nf-clfsw32-writelogrestartarea?branch=master) function, you can advance the base LSN beyond the last record of the log by using the **LastLsn** member that is returned from the [**GetLogFileInformation**](/windows/win32/Clfsw32/nf-clfsw32-getlogfileinformation?branch=master) function.

 

 



