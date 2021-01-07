---
description: When the user starts Event Viewer to view the event log entries, it calls the ReadEventLog function to obtain the EVENTLOGRECORD structures.
ms.assetid: 1d5b62cb-cf5b-4f4c-8521-1c783ae3afc7
title: Viewing the Event Log
ms.topic: article
ms.date: 05/31/2018
---

# Viewing the Event Log

When the user starts Event Viewer to view the event log entries, it calls the [**ReadEventLog**](/windows/desktop/api/Winbase/nf-winbase-readeventloga) function to obtain the [**EVENTLOGRECORD**](/windows/desktop/api/Winnt/ns-winnt-eventlogrecord) structures. The Event Viewer uses the event source and event identifier to get message text for each event from the registered message file (indicated by the **EventMessageFile** registry value for the source). The Event Viewer uses the [**LoadLibraryEx**](/windows/desktop/api/libloaderapi/nf-libloaderapi-loadlibraryexa) function to load the message file. The Event Viewer then uses the [**FormatMessage**](/windows/desktop/api/winbase/nf-winbase-formatmessage) function to retrieve the base description string from the loaded module. Finally, the Event Viewer replaces the insertion parameters in the base description string to yield the final message string.

 

 
