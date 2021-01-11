---
description: Is an abstract base class that serves as the parent class for all intrinsic and extrinsic events.
ms.assetid: 4d2e4715-041c-49e9-b948-a148dfe85483
ms.tgt_platform: multiple
title: '__Event class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __Event
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_Event class

The **\_\_Event** system class is an abstract base class that serves as the parent class for all intrinsic and extrinsic events. All new event types must ultimately derive from **\_\_Event**. Intrinsic events derive directly from this class. User-defined extrinsic events derive from a subclass of this class called [**\_\_ExtrinsicEvent**](--extrinsicevent.md).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract]
class __Event : __IndicationRelated
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_Event** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_Event** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine which users can receive the event. For more information, see [WMI Security Constants](wmi-security-constants.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time the event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format.

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_Event** class is derived from [**\_\_IndicationRelated**](--indicationrelated.md), which has no properties.

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

[Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md)
</dt> <dt>

[**\_\_ClassOperationEvent**](--classoperationevent.md)
</dt> <dt>

[**\_\_InstanceOperationEvent**](--instanceoperationevent.md)
</dt> <dt>

[**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md)
</dt> </dl>

 

