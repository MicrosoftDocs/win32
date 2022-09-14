---
description: Information about each event is stored in the event log in an event log record. The event log record includes time, type, and category information. For more information, see the EVENTLOGRECORD structure.
ms.assetid: 73731505-97f5-4985-8d00-c6ce8604902d
title: Event Log Records
ms.topic: article
ms.date: 05/31/2018
---

# Event Log Records

Information about each event is stored in the event log in an *event log record*. The event log record includes time, type, and category information. For more information, see the [**EVENTLOGRECORD**](/windows/desktop/api/Winnt/ns-winnt-eventlogrecord) structure.

The **RecordNumber** member of [**EVENTLOGRECORD**](/windows/desktop/api/Winnt/ns-winnt-eventlogrecord) contains the record number for the event log record. The very first record written to an event log is record number 1, and other records are numbered sequentially. If the record number reaches ULONG\_MAX, the next record number will be 0, not 1; however, you use zero to seek to the record.

If the [Retention](eventlog-key.md) registry value is set to zero, the event records are overwritten when the maximum log size is reached. Therefore, the oldest record in an event log may not be record number 1. To identify the oldest record in the log, call the [**GetOldestEventLogRecord**](/windows/desktop/api/Winbase/nf-winbase-getoldesteventlogrecord) function. You can then call the [**GetNumberOfEventLogRecords**](/windows/desktop/api/Winbase/nf-winbase-getnumberofeventlogrecords) function and add the returned value to the oldest record number to determine the newest record.

You can read individual records from the event log using the [**ReadEventLog**](/windows/desktop/api/Winbase/nf-winbase-readeventloga) function. For more information, see [Querying for Event Information](querying-for-event-source-messages.md).

 

 



