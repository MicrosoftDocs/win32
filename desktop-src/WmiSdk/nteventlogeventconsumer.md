---
description: The NTEventLogEventConsumer class logs a specific message to the operating system event log when an event is delivered to it.
ms.assetid: cf986812-f09a-4f32-ba76-db76a23e2e4c
ms.tgt_platform: multiple
title: NTEventLogEventConsumer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NTEventLogEventConsumer
- NTEventLogEventConsumer.CreatorSID
- NTEventLogEventConsumer.MachineName
- NTEventLogEventConsumer.MaximumQueueSize
- NTEventLogEventConsumer.Category
- NTEventLogEventConsumer.NameOfRawDataProperty
- NTEventLogEventConsumer.EventID
- NTEventLogEventConsumer.EventType
- NTEventLogEventConsumer.InsertionStringTemplates
- NTEventLogEventConsumer.Name
- NTEventLogEventConsumer.NumberOfInsertionStrings
- NTEventLogEventConsumer.NameOfUserSidProperty
- NTEventLogEventConsumer.SourceName
- NTEventLogEventConsumer.UNCServerName
api_type: 
- DllExport
api_location: 
- Wbemcons.dll
---

# NTEventLogEventConsumer class

The **NTEventLogEventConsumer** class logs a specific message to the operating system event log when an event is delivered to it. This class is one of the standard event consumers that WMI provides. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

## Syntax

``` syntax
[AMENDMENT]
class NTEventLogEventConsumer : __EventConsumer
{
  uint8  CreatorSID[];
  string MachineName;
  uint32 MaximumQueueSize;
  uint16 Category;
  string NameOfRawDataProperty;
  uint32 EventID;
  uint32 EventType = 1;
  string InsertionStringTemplates[] = {""};
  string Name;
  uint32 NumberOfInsertionStrings = 0;
  string NameOfUserSidProperty;
  string SourceName;
  string UNCServerName;
};
```

## Members

The **NTEventLogEventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **NTEventLogEventConsumer** class has these properties.

<dl> <dt>

**Category**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event category. This is source-specific information and can have any value.

</dd> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier (SID) that uniquely identifies the user who creates a filter. WMI stores the SID of the user who creates an instance of [**\_\_EventConsumer**](--eventconsumer.md) or the Administrator SID, depending on the operating system. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md) and [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**EventID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Event message in the message DLL. This property cannot be **NULL**.

</dd> <dt>

**EventType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of event. This parameter can have one of the values listed in the following list, which are defined in Winnt.h.

<dt>

<span id="EVENTLOG_SUCCESS"></span><span id="eventlog_success"></span>

<span id="EVENTLOG_SUCCESS"></span><span id="eventlog_success"></span>**EVENTLOG\_SUCCESS** (0 (0x0))


</dt> <dd>

Successful event

</dd> <dt>

<span id="EVENTLOG_ERROR_TPYE"></span><span id="eventlog_error_tpye"></span>

<span id="EVENTLOG_ERROR_TPYE"></span><span id="eventlog_error_tpye"></span>**EVENTLOG\_ERROR\_TPYE** (1 (0x1))


</dt> <dd>

Error event

</dd> <dt>

<span id="EVENTLOG_WARNING_TYPE"></span><span id="eventlog_warning_type"></span>

<span id="EVENTLOG_WARNING_TYPE"></span><span id="eventlog_warning_type"></span>**EVENTLOG\_WARNING\_TYPE** (2 (0x2))


</dt> <dd>

Warning event

</dd> <dt>

<span id="EVENTLOG_INFORMATION_TYPE"></span><span id="eventlog_information_type"></span>

<span id="EVENTLOG_INFORMATION_TYPE"></span><span id="eventlog_information_type"></span>**EVENTLOG\_INFORMATION\_TYPE** (4 (0x4))


</dt> <dd>

Information event

</dd> <dt>

<span id="EVENTLOG_AUDIT_SUCCESS"></span><span id="eventlog_audit_success"></span>

<span id="EVENTLOG_AUDIT_SUCCESS"></span><span id="eventlog_audit_success"></span>**EVENTLOG\_AUDIT\_SUCCESS** (8 (0x8))


</dt> <dd>

Success audit type

</dd> <dt>

<span id="EVENTLOG_AUDIT_FAILURE"></span><span id="eventlog_audit_failure"></span>

<span id="EVENTLOG_AUDIT_FAILURE"></span><span id="eventlog_audit_failure"></span>**EVENTLOG\_AUDIT\_FAILURE** (16 (0x10))


</dt> <dd>

Failure audit type

</dd> </dl>

</dd> <dt>

**InsertionStringTemplates**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of standard string templates that is used as the insertion string for an event log record.

</dd> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer to which Windows Management Instrumentation (WMI) sends events.

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**MaximumQueueSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum queue for a specific consumer, in bytes.

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](key-qualifier.md)
</dt> </dl>

Unique name of a consumer.

</dd> <dt>

**NameOfRawDataProperty**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the event property that contains data to be passed to the [**ReportEvent**](/windows/desktop/api/winbase/nf-winbase-reporteventa) function *lpRawData* parameter.

</dd> <dt>

**NameOfUserSidProperty**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the event property that contains a security identifier (SID) to be passed to the [**ReportEvent**](/windows/desktop/api/winbase/nf-winbase-reporteventa) function *lpUserSid* parameter. The property must be either an array of bytes (**uint8**) or a string. If it is an array of bytes, it is assumed to be a SID. If it is a string, it is a string SID that is converted into a SID.

</dd> <dt>

**NumberOfInsertionStrings**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of elements in the **InsertionStringTemplates** array.

</dd> <dt>

**SourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Source name where a message is located. The customer is assumed to have registered a DLL with the necessary messages.

> [!Note]  
> The value of this parameter must not include a colon (:) character.

 

</dd> <dt>

**UNCServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer on which to log an event, or **NULL** if the event is to be logged on a local server.

Authenticated users cannot, by default, log events to the Application log on a remote computer. As a result, using this property to specify a remote computer will not work. To learn how to change event log security, consult this [KB article](https://support.microsoft.com/kb/323076).

</dd> </dl>

## Remarks

The **NTEventLogEventConsumer** class is derived from the [**\_\_EventConsumer**](--eventconsumer.md) abstract class.

## Examples

For an example of using **NTEventLogEventConsumer** to create a consumer, see [Logging to NT Event Log Based on an Event](logging-to-nt-event-log-based-on-an-event.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\subscription<br/>                                                           |
| MOF<br/>                      | <dl> <dt>Wbemcons.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemcons.dll</dt> </dl> |



## See also

<dl> <dt>

[Standard Consumer Classes](standard-consumer-classes.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> </dl>

 

