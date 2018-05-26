---
Description: An event viewer application uses the OpenEventLog function to open the event log for an event source.
ms.assetid: f10ea874-66a6-446a-a18a-0c008c2da64f
title: Reading from the Event Log
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Reading from the Event Log

An event viewer application uses the [**OpenEventLog**](/windows/win32/Winbase/nf-winbase-openeventloga?branch=master) function to open the event log for an event source. The event viewer can then use the [**ReadEventLog**](/windows/win32/Winbase/nf-winbase-readeventloga?branch=master) function to read event records from the log. **ReadEventLog** returns a buffer containing an [**EVENTLOGRECORD**](/windows/win32/Winnt/ns-winnt-_eventlogrecord?branch=master) structure and additional information that describes a logged event. The following diagram illustrates this process.

![reading from the event log](images/readlog.png)

For example code, see [Querying for Event Information](querying-for-event-source-messages.md).

 

 



