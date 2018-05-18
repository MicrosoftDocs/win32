---
Description: 'The Win32\_NTLogEvent&\#32;WMI class is used to translate instances from the Windows event log. An application must have SeSecurityPrivilege to receive events from the security event log, otherwise &\#0034;Access Denied&\#0034; is returned to the application.'
ms.assetid: 'd2c96eef-3680-42f8-bdf1-f987a3e94257'
title: 'Win32\_NTLogEvent class'
---

# Win32\_NTLogEvent class

The **Win32\_NTLogEvent** [WMI class](https://msdn.microsoft.com/library/aa393244) is used to translate instances from the Windows event log. An application must have **SeSecurityPrivilege** to receive events from the security event log, otherwise "Access Denied" is returned to the application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_NTLogEvent
{
  uint16   Category;
  string   CategoryString;
  string   ComputerName;
  uint8    Data[];
  uint16   EventCode;
  uint32   EventIdentifier;
  uint8    EventType;
  string   InsertionStrings[];
  string   Logfile;
  string   Message;
  uint32   RecordNumber;
  string   SourceName;
  datetime TimeGenerated;
  datetime TimeWritten;
  string   Type;
  string   User;
};
```

## Members

The **Win32\_NTLogEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_NTLogEvent** class has these properties.

<dl> <dt>

**Category**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Classification of the event as determined by the source. This subcategory is source-specific.

Although primarily used when recording Security events, this property is available in other event logs as well. Common Security categories include Logon/Logoff, Account Management, and System Event.

</dd> <dt>

**CategoryString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Translation of the subcategory. The translation is source-specific.

</dd> <dt>

**ComputerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer that generated this event.

</dd> <dt>

**Data**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of the binary data that accompanied the report of the Windows event.

</dd> <dt>

**EventCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Value of the lower 16-bits of the **EventIdentifier** property. It is present to match the value displayed in the Windows [Event Viewer](https://msdn.microsoft.com/library/aa390436#wmi-downloads).

> [!Note]  
> Two events from the same source may have the same value for this property but may have different severity and **EventIdentifier** values. For example, a successful logoff is recorded in the Security log with the Event ID 538. However, Event IDs are not necessarily unique. It is possible that, when retrieving Event ID 538, you can get other kinds of events with ID 538. If this happens, you might need to filter by the source as well as ID.

 

</dd> <dt>

**EventIdentifier**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifier of the event. This is specific to the source that generated the event log entry and is used, together with **SourceName**, to uniquely identify a Windows event type.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of event.



| Value                                                                                                | Meaning                           |
|------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Error<br/>                  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Warning<br/>                |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Information<br/>            |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Security Audit Success<br/> |
| <span id="5"></span><dl> <dt>**5**</dt> </dl> | Security Audit Failure<br/> |



 

</dd> <dt>

**InsertionStrings**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of the insertion strings that accompanied the report of the Windows event.

</dd> <dt>

**Logfile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Name of Windows event log file. Together with **RecordNumber**, this is used to uniquely identify an instance of this class.

</dd> <dt>

**Message**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event message as it appears in the Windows event log. This is a standard message with zero or more insertion strings supplied by the source of the Windows event. The insertion strings are inserted into the standard message in a predefined format. If there are no insertion strings or there is a problem inserting the insertion strings, only the standard message will be present in this field.

</dd> <dt>

**RecordNumber**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Identifies the event within the Windows event log file. This is specific to the log file and is used together with the log file name to uniquely identify an instance of this class.

Record numbers are always unique; they are not reset to 1 when an event log is cleared. As a result, the highest record number also indicates the number of records that have been written to the event log since the operating system was installed

</dd> <dt>

**SourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the source (application, service, driver, or subsystem) that generated the entry. It is used, together with **EventIdentifier** to uniquely identify a Windows event type.

</dd> <dt>

**TimeGenerated**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the event is generated.

</dd> <dt>

**TimeWritten**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the event is written to the log file.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of event. This is an enumerated string. It is preferable to use the **EventType** property rather than the **Type** property.



| Value                                                                                                  | Meaning                           |
|--------------------------------------------------------------------------------------------------------|-----------------------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Error<br/>                  |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Warning<br/>                |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Information<br/>            |
| <span id="8"></span><dl> <dt>**8**</dt> </dl>   | Security Audit Success<br/> |
| <span id="16"></span><dl> <dt>**16**</dt> </dl> | Security Audit Failure<br/> |



 

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User name of the logged-on user when the event occurred. If the user name cannot be determined, this will be **NULL**.

</dd> </dl>

## Remarks

**Optimizing Search Queries**

The way an event log query is constructed can have a huge impact on how long it takes WMI to process the query and return the requested information. This is not necessarily true of other managed objects. For example, a query that returns all the properties for all the installed services on a typical Windows 2000-based computer takes about 2 seconds to complete. A filtered query that returns the properties of a single service takes about 1 second to complete, a difference of only 1 second.

However, query times for different types of event log queries can vary widely. The relative query times for several different types of event log queries run on a Windows 2000 Server-based test computer are listed in Table 12.5. The test computer had a total of 13,743 events recorded in its event logs, with 669 of these in the System event log. Retrieving all the events from all the event logs required over 2 hours to complete. When the query was modified so that it retrieved events from only the System event log, the process took just 4 minutes.

Event log queries can also return a very large amount of information compared with queries for other WMI classes, such as Win32\_Service. Retrieving the properties for all the services on the test computer and saving them to a text file resulted in a file that was less than 13 KB. Performing the same task with the event logs resulted in a text file of nearly 1 MB. Attempting to retrieve events from large event logs over the network could cause a script to take hours to run and might generate a huge amount of network traffic.

Because of the length of time it can take an event log query to run and the large amount of information that can be returned, it is important that you carefully design your queries for retrieving data from the event logs. Unless you need to return all the events from all the event logs on a computer, write your queries so that they do one or more of the following:

-   **Specify a single event log.** If events are recorded in only one event log, there is no need to search the other logs for these records. For example, computer startup and shutdown events are recorded only in the System event log. If you are querying for these records, there is no reason to search the Application or DNS event logs.
-   **Return only a subset of events.** When analyzing event logs, you rarely need to examine every event. The vast majority of records in a typical event log report the success of a particular operation. If you are interested only in operations that failed, there is no reason to examine hundreds of records that report operations that succeeded. Instead, you can focus on a subset of events: those records reporting an operation that failed.
-   **Return only events that occurred on a particular day.** For most computers, this kind of query returns only a few hundred records, compared with thousands of records stored in a large event log. If you need to view only the event records for last Tuesday, construct your query so that only the records from that day are returned.
-   **Asynchronouly return event records.** If a dataset is large, asynchronous queries will usually run faster than semi-synchronous queries.
-   **Copy events to a database.** Unlike databases, event logs are not optimized for data retrieval and analysis. If you need to perform a number of queries on your event logs, or if you need to combine events from multiple event logs, you should copy those events to a database and then use the database and its tools to analyze the records. In addition to the speed differential, databases typically provide more sophisticated tools for analyzing data and calculating statistics than do event logs.

You can greatly speed up data queries by limiting your searches to a specific event log. It is very rare for events of a certain type, or events generated by a specific application, to be written to multiple event logs. Instead, operating system events are invariably written to the System event log, events generated by an application such as Microsoft Office are written to the Application event log, and so forth.

For example, if you are interested in the activities of the DNS service, any such events will be written to the DNS server event log. There is no reason to search the other event logs. A nonoptimized query that searches all the event logs instead of limiting the search to the DNS service log might search tens of thousands of events in the Security event log, even though no DNS service events will be recorded there.

In addition, querying an event log for a specific set of events can greatly increase the speed and efficiency of your query.

**Tracking Stop Events**

Tracking stop events and the details about those stop events can help you determine whether a particular problem is endemic to one computer or if it is occurring on other computers in your organization. Because stop events are recorded in the System Event log, you can create a script that periodically queries the System Event log on a computer or set of computers and checks to see whether any stop events have occurred.

Each time a stop event occurs, a record is saved with the following parameters:

-   EventType = Information
-   EventCode = 1001
-   SourceName = Save Dump

The event description will look similar to the following:

`opy     The computer has rebooted from a bugcheck. The bugcheck was: 0x000000e2  (0x00000000, 0x00000000, 0x00000000, 0x00000000). Microsoft Windows 2000 [v15.2195].   A dump was saved in: C:\Windows\MEMORY.DMP.`

You can use the **Win32\_NTLogEvent** class to periodically query the System Event Log and retrieve the details of each stop event.

## Examples

The [Using WMI scripts to locate fault or error](http://gallery.technet.microsoft.com/Using-WMI-to-locate-fault-5a865f75) VBScript code sample on TechNet Gallery uses **Win32\_NTLogEvent** to read all event log errors generated since last time this script was run.

The [PS- Get Event Log information from multiple computers using WMI](http://gallery.technet.microsoft.com/479d4a4e-b06b-4464-94b2-5a61af14d82b) PowerShell code sample on TechNet Gallery uses **Win32\_NTLogEvent** to query multiple remote computers for a specified event.

The following VBScript sample queries a specific event log and echoes the properties of all the records in that log.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\Root\CIMv2")
Set colLoggedEvents = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_NTLogEvent WHERE Logfile = 'System'")
For Each objEvent in colLoggedEvents
 Wscript.Echo "Category: " & objEvent.Category
 Wscript.Echo "Computer Name: " & objEvent.ComputerName
 Wscript.Echo "Event Code: " & objEvent.EventCode
 Wscript.Echo "Message: " & objEvent.Message
 Wscript.Echo "Record Number: " & objEvent.RecordNumber
 Wscript.Echo "Source Name: " & objEvent.SourceName
 Wscript.Echo "Time Written: " & objEvent.TimeWritten
 Wscript.Echo "Event Type: " & objEvent.Type
 Wscript.Echo "User: " & objEvent.User
Next
```



The following VBScript queries an event log and tallies all instances of a specific Event ID. s


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\Root\CIMv2")
Set colLoggedEvents = objWMIService.ExecQuery("SELECT * FROM Win32_NTLogEvent WHERE Logfile = 'System' AND " _
 & "EventCode = '6008'")
Wscript.Echo "Improper shutdowns: " & colLoggedEvents.Count
```



The following VBScript sample demonstrates how to retrieve the events of a particular type (Event code) from the **Win32\_NTLogEvent** class.


```VB
Set EventSet = GetObject("winmgmts:").ExecQuery("select * from Win32_NTLogEvent where EventCode=4097")

if (EventSet.Count = 0) then WScript.Echo "No Events"

for each LogEvent in EventSet
 WScript.Echo "Event Number: " & LogEvent.RecordNumber
 WScript.Echo "Log File: " & LogEvent.LogFile
 WScript.Echo "Type: " & LogEvent.Type 
 WScript.Echo "Message: " & LogEvent.Message
 WScript.Echo "Time: " & LogEvent.TimeGenerated
 WScript.Echo ""
next
```



The following Perl sample demonstrates how to retrieve the events of a particular type (Event code) from the **Win32\_NTLogEvent** class.


```Perl
use strict;
use Win32::OLE;

my ( $EventSet, $LogEvent );

eval { $EventSet = Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\Root\\CIMv2")->
     ExecQuery("SELECT * FROM Win32_NTLogEvent WHERE EventCode=4097"); };
unless( $@ )
{
 print "\n";
 if ( $EventSet->{Count} == 0 )
 {
  print "No Events\n";
 }
 else
 {
  foreach $LogEvent ( in $EventSet )
  {
   print "Event Number: ", $LogEvent->{RecordNumber}, "\n";
   print "Log File: ", $LogEvent->{LogFile}, "\n";
   print "Type: ", $LogEvent->{Type}, "\n"; 
   print "Message: ", $LogEvent->{Message}, "\n";
   print "Time: ", $LogEvent->{TimeGenerated}, "\n";
   print "\n";
  }
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
}
```



The following VBScript example demonstrates how to display NT events using a notification query.


```VB
on error resume next
set locator = CreateObject("WbemScripting.SWbemLocator")

'Access to the NT event log requires the security privilege
locator.Security_.Privileges.AddAsString "SeSecurityPrivilege"

set events = locator.ConnectServer().ExecNotificationQuery _ 
 ("select * from __instancecreationevent where targetinstance isa 'Win32_NTLogEvent'")      

if err <> 0 then
 WScript.Echo Err.Description, Err.Number, Err.Source
end if 

' Note this next call will wait indefinitely - a timeout can be specified 

WScript.Echo "Waiting for NT Events..."
WScript.Echo ""

do 
 set NTEvent = events.nextevent 
 if err <> 0 then
  WScript.Echo Err.Number, Err.Description, Err.Source
  Exit Do
 elseif  NTEvent.TargetInstance.Message <> Empty then  
  WScript.Echo NTEvent.TargetInstance.Message
 else
  Wscript.Echo "Event received, but it did not contain a message."
 end if
loop

WScript.Echo "finished"
```



## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




