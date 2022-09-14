---
description: A base class for all intrinsic events that relate to a namespace.
ms.assetid: 168637b1-217e-4b6d-bd07-25127b9e9f6c
ms.tgt_platform: multiple
title: '__NamespaceOperationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __NamespaceOperationEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_NamespaceOperationEvent class

The **\_\_NamespaceOperationEvent** system class is a base class for all intrinsic events that relate to a namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __NamespaceOperationEvent : __Event
{
  uint8       SECURITY_DESCRIPTOR[];
  __Namespace TargetNamespace;
  uint64      TIME_CREATED;
};
```

## Members

The **\_\_NamespaceOperationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NamespaceOperationEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**TargetNamespace**
</dt> <dd> <dl> <dt>

Data type: **\_\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Namespace affected by the event. For creation events, this is the newly created namespace. For modification events, this is the changed namespace. For deletion events, this is the deleted namespace.

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

The **\_\_NamespaceOperationEvent** class is derived from [**\_\_Event**](--event.md).

Instances of this class are not created. WMI creates instances of one of the following classes derived from this class:

[**\_\_NamespaceCreationEvent**](--namespacecreationevent.md)

[**\_\_NamespaceModificationEvent**](--namespacemodificationevent.md)

[**\_\_NamespaceDeletionEvent**](--namespacedeletionevent.md)

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
</dt> <dt>

[Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md)
</dt> </dl>

 

