---
description: Serves as a parent class for all user-defined event types, also known as extrinsic events.
ms.assetid: 8fddbcd1-7393-4a3b-8a10-a8b620efc19f
ms.tgt_platform: multiple
title: '__ExtrinsicEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ExtrinsicEvent
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_ExtrinsicEvent class

The **\_\_ExtrinsicEvent** system class is an abstract base class that serves as a parent class for all user-defined event types, also known as [extrinsic events](determining-the-type-of-event-to-receive.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __ExtrinsicEvent : __Event
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_ExtrinsicEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ExtrinsicEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md). For more information about constants used to set this security descriptor, see [WMI Security Constants](wmi-security-constants.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_ExtrinsicEvent** class is derived from [**\_\_Event**](--event.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_Event**](/windows/desktop/WmiSdk/--event)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

