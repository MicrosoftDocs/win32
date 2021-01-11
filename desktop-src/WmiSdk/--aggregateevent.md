---
description: Represents an aggregate event of several individual intrinsic or extrinsic events.
ms.assetid: 99afa390-01fe-4a13-ba21-27587470f111
ms.tgt_platform: multiple
title: '__AggregateEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __AggregateEvent
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_AggregateEvent class

The **\_\_AggregateEvent** system class represents an aggregate event of several individual intrinsic or extrinsic events. WMI generates an instance of **\_\_AggregateEvent** rather than [**\_\_Event**](--event.md) when consumers register with the [GROUP WITHIN](group-clause.md) clause in their event query.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __AggregateEvent : __IndicationRelated
{
  uint32 NumberOfEvents;
  object Representative;
};
```

## Members

The **\_\_AggregateEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_AggregateEvent** class has these properties.

<dl> <dt>

**NumberOfEvents**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of events combined to produce this single summary event.

</dd> <dt>

**Representative**
</dt> <dd> <dl> <dt>

Data type: **object**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of one of the events delivered within the aggregation interval. For example, if a consumer has registered for registry key change events from the Registry Event provider, **Representative** would hold an instance of the **RegistryKeyChangeEvent** class.

</dd> </dl>

## Remarks

The **\_\_AggregateEvent** class is derived from [**\_\_IndicationRelated**](--indicationrelated.md), which has no properties.

Event providers never generate aggregate events. They must ignore the GROUP WITHIN clause in their processing of event queries.

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

[Querying with WQL](querying-with-wql.md)
</dt> </dl>

 

