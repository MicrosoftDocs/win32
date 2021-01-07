---
description: Reports a namespace deletion event, which is a type of intrinsic event that is generated when a sub-namespace is removed from the current namespace.
ms.assetid: f7160a90-562d-40d9-9189-32aaabcd81d0
ms.tgt_platform: multiple
title: '__NamespaceDeletionEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __NamespaceDeletionEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_NamespaceDeletionEvent class

The **\_\_NamespaceDeletionEvent** system class reports a namespace deletion event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) that is generated when a sub-namespace is removed from the current namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __NamespaceDeletionEvent : __NamespaceOperationEvent
{
  uint8       SECURITY_DESCRIPTOR[];
  __Namespace TargetNamespace;
  uint64      TIME_CREATED;
};
```

## Members

The **\_\_NamespaceDeletionEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NamespaceDeletionEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine the users that can receive an event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**TargetNamespace**
</dt> <dd> <dl> <dt>

Data type: **\_\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of the [**\_\_Namespace**](--namespace.md) instance that is deleted. The **Name** property of the **\_\_Namespace** instance identifies the namespace that is deleted. This property is inherited from [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time an event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_NamespaceDeletionEvent** class is derived from [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_NamespaceOperationEvent**](/windows/desktop/WmiSdk/--namespaceoperationevent)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> </dl>

 

