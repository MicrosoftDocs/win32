---
description: Is an abstract base class that is used in the registration of a permanent event consumer.
ms.assetid: c1dc9a91-76f9-4527-ad69-0323a9aef28a
ms.tgt_platform: multiple
title: '__EventConsumer class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __EventConsumer
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_EventConsumer class

The **\_\_EventConsumer** system class is an abstract base class that is used in the registration of a permanent event consumer. You can derive a new event consumer class from**\_\_EventConsumer**.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __EventConsumer : __IndicationRelated
{
  uint8  CreatorSID[];
  string MachineName;
  uint32 MaximumQueueSize;
};
```

## Members

The **\_\_EventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_EventConsumer** class has these properties.

<dl> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier (SID) that uniquely identifies the user who creates a filter. WMI stores the SID of the user who creates an instance of **\_\_EventConsumer** or the Administrator SID, depending on the operating system. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md) and [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

</dd> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer to which Windows Management Instrumentation (WMI) sends events.

</dd> <dt>

**MaximumQueueSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum queue for a specific consumer, in bytes.

</dd> </dl>

## Remarks

The **\_\_EventConsumer** class is derived from [**\_\_IndicationRelated**](--indicationrelated.md), which does not have properties.

Permanent consumers define new consumer classes to describe an action to take and data to be processed when consumers receive event notifications. Permanent consumers have special security concerns. For more information, see [Securing WMI Events](securing-wmi-events.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_IndicationRelated**](/windows/desktop/WmiSdk/--indicationrelated)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[Receiving Events at All Times](receiving-events-at-all-times.md)
</dt> <dt>

[Creating a New Permanent Event Consumer Class](creating-a-new-permanent-event-consumer-class.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Securing WMI Events](securing-wmi-events.md)
</dt> </dl>

 

