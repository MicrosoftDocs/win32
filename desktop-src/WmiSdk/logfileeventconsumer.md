---
description: The LogFileEventConsumer class writes customized strings to a text log file when events are delivered to it.
ms.assetid: 8934b60e-3763-4b85-89fd-58fe6136dff6
ms.tgt_platform: multiple
title: LogFileEventConsumer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LogFileEventConsumer
- LogFileEventConsumer.CreatorSID
- LogFileEventConsumer.MachineName
- LogFileEventConsumer.MaximumQueueSize
- LogFileEventConsumer.Filename
- LogFileEventConsumer.IsUnicode
- LogFileEventConsumer.MaximumFileSize
- LogFileEventConsumer.Name
- LogFileEventConsumer.Text
api_type: 
- DllExport
api_location: 
- Wbemcons.dll
---

# LogFileEventConsumer class

The **LogFileEventConsumer** class writes customized strings to a text log file when events are delivered to it. The strings are separated by end-of-line sequences. This class is one of the standard event consumers that WMI provides. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

## Syntax

``` syntax
[AMENDMENT]
class LogFileEventConsumer : __EventConsumer
{
  uint8   CreatorSID[];
  string  MachineName;
  uint32  MaximumQueueSize;
  string  Filename;
  boolean IsUnicode;
  uint64  MaximumFileSize = 65535;
  string  Name;
  string  Text;
};
```

## Members

The **LogFileEventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **LogFileEventConsumer** class has these properties.

<dl> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier (SID) that uniquely identifies the user who creates a filter. WMI stores the SID of the user who creates an instance of [**\_\_EventConsumer**](--eventconsumer.md) or the Administrator SID, depending on the operating system. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md) and [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**Filename**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of a file that includes the path to which the log entries are appended. If the file does not exist, **LogFileEventConsumer** attempts to create it. The consumer fails when the path does not exist, or when the user who creates the consumer does not have write permissions for the file or path.

</dd> <dt>

**IsUnicode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the log file is a Unicode text file. If **FALSE**, the log file is a multibyte code text file. If the file exists, this property is ignored and the current file setting is used. For example, if **IsUnicode** is **FALSE**, but the existing file is a Unicode file, then Unicode is used. If **IsUnicode** is **TRUE**, but the file is multibyte code, then multibyte code is used.

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

**MaximumFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum size of a log file in bytes. If the primary file exceeds its maximum size, the contents are moved to a different file and the primary file is emptied. A value of 0 (zero) means there is no size limit. The default value is 65,535 bytes. The size of the file is checked before a write operation. Therefore, you can have a file that is slightly larger than the specified size limit. The next write operation catches it and starts a new file.

The following list identifies the naming structure for the backup file:

-   If the original filename is 8.3, the extension is replaced by a string in the format of "001", "002", and so on with the smallest number larger than all the previously used and chosen numbers. If "999" is used, then the number chosen is the smallest unused number.
-   If the original filename is not 8.3, a string in the format of "001", "002", and so on is appended to the file name.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

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

Unique name for this consumer.

</dd> <dt>

**Text**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Standard string [template](using-standard-string-templates.md) for the text of a log entry.

</dd> </dl>

## Remarks

> [!Note]  
> The **LogFileEventConsumer** does not secure the log file. Therefore, when you configure the **LogFileEventConsumer**, it is important to specify a directory that is secured to the level that you require.

 

The **LogFileEventConsumer** class is derived from the [**\_\_EventConsumer**](--eventconsumer.md) abstract class.

## Examples

For an example of using **LogFileEventConsumer** to create a consumer, see [Writing to a Log File Based on an Event](writing-to-a-log-file-based-on-an-event.md).

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

[Writing to a Log File Based on an Event](writing-to-a-log-file-based-on-an-event.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> </dl>

 

