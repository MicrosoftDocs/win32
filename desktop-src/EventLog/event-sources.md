---
description: Each log in the Eventlog key contains subkeys called event sources. The event source is the name of the software that logs the event.
ms.assetid: bc7fdc74-be41-4d17-997c-27171ef73f0f
title: Event Sources
ms.topic: article
ms.date: 05/31/2018
---

# Event Sources

Each log in the [Eventlog key](eventlog-key.md) contains subkeys called *event sources*. The event source is the name of the software that logs the event. It is often the name of the application or the name of a subcomponent of the application if the application is large. You can add a maximum of 16,384 event sources to the registry. The **Security** log is for system use only. Device drivers should add their names to the **System** log. Applications and services should add their names to the **Application** log or create a custom log.

The structure of the event sources is as follows:

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         Services
            EventLog
               Application
                  AppName
               Security
               System
                  DriverName
               CustomLog
                  AppName
```

You cannot use a source name that has already been used as a log name. In addition, source names cannot be hierarchical; that is, they cannot contain the backslash character ("\\").

Each event source contains information (such as a [message file](message-files.md)) specific to the software that will be logging the events, as shown in the following table.



<table>
<thead>
<tr class="header">
<th>Registry Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CategoryCount</strong></td>
<td>Number of event categories supported. This value is of type <strong>REG_DWORD</strong>.</td>
</tr>
<tr class="even">
<td><strong>CategoryMessageFile</strong></td>
<td>Path to the category message file. A category message file contains language-dependent strings that describe the categories. This value can be of type <strong>REG_SZ</strong> or <strong>REG_EXPAND_SZ</strong>.</td>
</tr>
<tr class="odd">
<td><strong>EventMessageFile</strong></td>
<td>Path to one or more event message files; use a semicolon to delimit multiple files. An event message file contains language-dependent strings that describe the events. This value can be of type <strong>REG_SZ</strong> or <strong>REG_EXPAND_SZ</strong>.</td>
</tr>
<tr class="even">
<td><strong>ParameterMessageFile</strong></td>
<td>Path to the parameter message file. A parameter message file contains language-independent strings that are to be inserted into the event description strings. This value can be of type <strong>REG_SZ</strong> or <strong>REG_EXPAND_SZ</strong>.</td>
</tr>
<tr class="odd">
<td><strong>TypesSupported</strong></td>
<td>Bitmask of supported types. This value is of type <strong>REG_DWORD</strong>. It can be one or more of the following values: <dl> <strong>EVENTLOG_AUDIT_FAILURE</strong> (0x0010)<br />
<strong>EVENTLOG_AUDIT_SUCCESS</strong> (0x0008)<br />
<strong>EVENTLOG_ERROR_TYPE</strong> (0x0001)<br />
<strong>EVENTLOG_INFORMATION_TYPE</strong> (0x0004)<br />
<strong>EVENTLOG_WARNING_TYPE</strong> (0x0002)<br />
</dl></td>
</tr>
</tbody>
</table>



 

When an application uses the [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea) or [**OpenEventLog**](/windows/desktop/api/Winbase/nf-winbase-openeventloga) function to get a handle to an event log, the event logging service searches for the specified event source in the registry. For example, the **Application** log might contain event sources for Microsoft SQL Server and Microsoft Excel. If an application uses [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea) or **OpenEventLog** with a source name of Application, SQL, or Excel, the event logging service returns a handle to the **Application** log.

An application can use the **Application** log without adding a new event source to the registry. If the application calls [**RegisterEventSource**](/windows/desktop/api/Winbase/nf-winbase-registereventsourcea) and passes a source name that cannot be found in the registry, the event-logging service uses the **Application** log by default. However, because there are no message files, the Event Viewer cannot map any event identifiers or event categories to a description string, and will display an error. For this reason, you should add a unique event source to the registry for your application and specify a message file.

 

 



