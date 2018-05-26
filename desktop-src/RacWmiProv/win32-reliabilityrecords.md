---
title: Win32\_ReliabilityRecords class
description: The Win32\_ReliabilityRecords WMI class contains information from the Windows Event Log related to system reliability.
ms.assetid: c180ab8a-1794-4db3-89a9-4aa3c0d9c4ae
keywords:
- Win32_ReliabilityRecords class
- Win32_ReliabilityRecords class, described
topic_type:
- apiref
api_name:
- Win32_ReliabilityRecords
- Win32_ReliabilityRecords.ComputerName
- Win32_ReliabilityRecords.EventIdentifier
- Win32_ReliabilityRecords.InsertionStrings
- Win32_ReliabilityRecords.Logfile
- Win32_ReliabilityRecords.Message
- Win32_ReliabilityRecords.ProductName
- Win32_ReliabilityRecords.RecordNumber
- Win32_ReliabilityRecords.SourceName
- Win32_ReliabilityRecords.TimeGenerated
- Win32_ReliabilityRecords.user
api_location:
- RacWmiProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_ReliabilityRecords class

The **Win32\_ReliabilityRecords** [WMI class](https://msdn.microsoft.com/library/aa393244) contains information from the Windows Event Log related to system reliability.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("ReliabilityMetricsProvider"), Dynamic]
class Win32_ReliabilityRecords : Win32_Reliability
{
  string   ComputerName;
  uint32   EventIdentifier;
  string   InsertionStrings[];
  string   Logfile;
  string   Message;
  string   ProductName;
  uint32   RecordNumber;
  string   SourceName;
  datetime TimeGenerated;
  string   user;
};
```

## Members

The **Win32\_ReliabilityRecords** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_ReliabilityRecords** class has these methods.



| Method                                                            | Description                                                                              |
|:------------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**GetRecordCount**](win32-reliabilityrecords-getrecordcount.md) | Retrieves the number of instances in the **Win32\_ReliabilityRecords** class.<br/> |



 

### Properties

The **Win32\_ReliabilityRecords** class has these properties.

<dl> <dt>

ComputerName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the name of the computer that generated this event.

</dd> <dt>

EventIdentifier
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the identifier of the event. This value is specific to the source that generated the event log entry and is used, together with SourceName, to uniquely identify a Windows event type.

</dd> <dt>

InsertionStrings
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Lists the insertion strings that accompanied the report of the Windows event.

</dd> <dt>

Logfile
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Specifies the name of Windows event log file. Together with the RecordNumber and TimeGenerated properties, this property is used to uniquely identify an instance of this class.

</dd> <dt>

Message
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the event message as it appears in the event log. This is a standard message with zero or more insertion strings supplied by the source of the Windows event. The insertion strings are inserted into the standard message in a predefined format. If there are no insertion strings or there is a problem inserting the insertion strings, only the standard message will be present in this field.

</dd> <dt>

ProductName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the product name that is associated with the event if available. If the product name cannot be determined, this property is set to **NULL**.

</dd> <dt>

RecordNumber
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Identifies the event within the Windows event log file. This value is specific to the log file and is used together with the log file name to uniquely identify an instance of this class.

</dd> <dt>

SourceName
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the name of the source (application, service, driver, or subsystem) that generated the entry. It is used, together with the EventIdentifier property, to uniquely identify a Windows event type.

</dd> <dt>

TimeGenerated
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Specifies the UTC time at which the source generated the event. Together with the LogFile and RecordNumber properties, this property is used to uniquely identify an instance of this class.

</dd> <dt>

user
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the user name of the logged-on user when the event occurred. If the user name cannot be determined, this property is set to **NULL**.

</dd> </dl>

## Remarks

The **Win32\_ReliabilityRecords** class is derived from **Win32\_Reliability**. Additional details for a record in **Win32\_ReliabilityRecords** might also be present in [**Win32\_NTLogEvent**](https://msdn.microsoft.com/library/aa394226) if the record still exists. To access information from this WMI class, the group policy Configure Reliability WMI Providers must be enabled. On Windows client systems, the policy is enabled by default. On Windows server systems, the policy is disabled by default. Disabling the policy will clear existing data within one hour. The **Win32\_ReliabilityRecords** class is not available on Itanium-based versions of the Windows operating system or on the Server Core installation option of Windows Server operating systems.

## Examples

The following Windows PowerShell example displays the five most recent reliability records from the local computer.


```PowerShell
get-wmiobject Win32_ReliabilityRecords -computername 127.0.0.1 -property Message | 
  select-object -first 5 Message | format-list *
```



The following Windows PowerShell example displays the number of each combination of the SourceName and EventIdentifier properties for all reliability records.


```PowerShell
get-wmiobject Win32_ReliabilityRecords -property @("SourceName", "EventIdentifier") | 
  group-object -property SourceName,EventIdentifier -noelement | sort-object -descending Count | 
  select-object Count,Name | format-table *
```



## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>RacWmiProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RacWmiProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ReliabilityStabilityMetrics**](win32-reliabilitystabilitymetrics.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[**Win32\_NTLogEvent**](https://msdn.microsoft.com/library/aa394226)
</dt> </dl>

 

 





