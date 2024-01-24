---
description: The SMTPEventConsumer class sends an email message by using Simple Mail Transfer Protocol (SMTP) each time an event is delivered to it.
ms.assetid: 42178360-9e22-4cd1-9b72-5f6b0d7e6c9c
ms.tgt_platform: multiple
title: SMTPEventConsumer class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SMTPEventConsumer
- SMTPEventConsumer.CreatorSID
- SMTPEventConsumer.MachineName
- SMTPEventConsumer.MaximumQueueSize
- SMTPEventConsumer.BccLine
- SMTPEventConsumer.CcLine
- SMTPEventConsumer.FromLine
- SMTPEventConsumer.HeaderFields
- SMTPEventConsumer.Message
- SMTPEventConsumer.Name
- SMTPEventConsumer.ReplyToLine
- SMTPEventConsumer.SMTPServer
- SMTPEventConsumer.Subject
- SMTPEventConsumer.ToLine
api_type: 
- DllExport
api_location: 
- Smtpcons.dll
---

# SMTPEventConsumer class

The **SMTPEventConsumer** class sends an email message by using Simple Mail Transfer Protocol (SMTP) each time an event is delivered to it. An SMTP server must exist on the network. The SMTPEventConsumer class does not support attachments. The encoding of the email message must be US-ASCII.

This class is one of the standard event consumers that WMI provides. For an example of using **SMTPEventConsumer** to create a consumer, see [Sending Email Based on an Event](sending-e-mail-based-on-an-event.md). For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class SMTPEventConsumer : __EventConsumer
{
  uint8  CreatorSID[];
  string MachineName;
  uint32 MaximumQueueSize;
  string BccLine;
  string CcLine;
  string FromLine;
  string HeaderFields[];
  string Message;
  string Name;
  string ReplyToLine;
  string SMTPServer;
  string Subject;
  string ToLine;
};
```

## Members

The **SMTPEventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **SMTPEventConsumer** class has these properties.

<dl> <dt>

**BccLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of addresses, separated by a comma or semicolon, in the format of a standard string template to which the message is sent as a blind carbon copy. For more information, see the Remarks section of this topic.

</dd> <dt>

**CcLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of addresses, separated by a comma or semicolon, in the format of a standard string template to which the message is sent as a carbon copy. For more information, see the Remarks section of this topic.

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

**FromLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

From line of an email message in the format of a standard string template. If **NULL**, a From line is constructed in the form of "WinMgmt@*MachineName*".

</dd> <dt>

**HeaderFields**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of header fields that are inserted into an email message without interpretation.

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

**Message**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Standard string template that contains the body of an email message.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](key-qualifier.md)
</dt> </dl>

Unique identifier for the event consumer.

</dd> <dt>

**ReplyToLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reply-to line of an email message in the format of a standard string template. If **NULL**, no Reply-to line is used.

</dd> <dt>

**SMTPServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the SMTP server through which an email is sent. Permissible names are an IP address, or a DNS or NetBIOS name. This property cannot be **NULL**.

</dd> <dt>

**Subject**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Standard string template that contains the subject of an email message.

</dd> <dt>

**ToLine**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A list of addresses, separated by a comma or semicolon, in the format of a standard string template that identifies where the message is to be sent. For more information, see the Remarks section of this topic.

</dd> </dl>

## Remarks

The SMTPEventConsumer class is derived from the [**\_\_EventConsumer**](--eventconsumer.md) abstract class.

Some of the **ToLine**, **CcLine**, or **BccLine** properties can be **NULL**, but they cannot all be **NULL**.

Receiving an error return code from the SMTP service is considered a failure.

## Examples

For an example of using **SMTPEventConsumer** to create a consumer, see [Sending Email Based on an Event](sending-e-mail-based-on-an-event.md). For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\subscription<br/>                                                           |
| MOF<br/>                      | <dl> <dt>Smtpcons.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Smtpcons.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> <dt>

[Standard Consumer Classes](standard-consumer-classes.md)
</dt> <dt>

[Sending Email Based on an Event](sending-e-mail-based-on-an-event.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> </dl>

 

 




