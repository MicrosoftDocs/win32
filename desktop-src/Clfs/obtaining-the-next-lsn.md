---
Description: 'If you are trying to advance the base log sequence number (LSN) of a log, or trying to read records from a log, typically you need to specify an LSN to a valid record in the log.'
ms.assetid: '2e47a5c9-a0bd-4cd1-ba30-9ebde6df0f91'
title: Obtaining the Next LSN
---

# Obtaining the Next LSN

If you are trying to advance the base log sequence number (LSN) of a log, or trying to read records from a log, typically you need to specify an LSN to a valid record in the log. There are two ways to obtain the next LSN, and the way you use depends on whether you want the last LSN in the log, or the LSN that will be assigned to the next record added.

The following list identifies the two ways to obtain the next LSN:

-   Reading records sequentially by using the [**ReadNextLogRecord**](readnextlogrecord.md) function always return valid log records. The last valid log record is the last record that is read before encountering the end-of-file marker.
-   Querying the log metadata by using the [**GetLogFileInformation**](getlogfileinformation.md) function returns the next available LSN in the **LastLsn** member of the [**CLFS\_INFORMATION**](clfs-information.md) structure. Then you can use the [**AdvanceLogBase**](advancelogbase.md) function to advance the base LSN beyond the last record in the log.

For example, if you are using the [**AdvanceLogBase**](advancelogbase.md) or [**WriteLogRestartArea**](writelogrestartarea.md) function, you can advance the base LSN beyond the last record of the log by using the **LastLsn** member that is returned from the [**GetLogFileInformation**](getlogfileinformation.md) function.

 

 



