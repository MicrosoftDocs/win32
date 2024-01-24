---
description: Reports a namespace creation event, which is a type of intrinsic event generated when a new namespace is added to the current namespace.
ms.assetid: 50b9860a-d6e8-4dab-a7d0-09da9dd37b6b
ms.tgt_platform: multiple
title: '__NamespaceCreationEvent class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __NamespaceCreationEvent
- All
- All
- All
api_type: 
- Schema
api_location: 
- All
---

# \_\_NamespaceCreationEvent class

The **\_\_NamespaceCreationEvent** system class reports a namespace creation event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) generated when a new namespace is added to the current namespace.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __NamespaceCreationEvent : __NamespaceOperationEvent
{
  uint8       SECURITY_DESCRIPTOR[];
  __Namespace TargetNamespace;
  uint64      TIME_CREATED;
};
```

## Members

The **\_\_NamespaceCreationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NamespaceCreationEvent** class has these properties.

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

Copy of the [**\_\_Namespace**](--namespace.md) instance that was created. The **Name** property of the **\_\_Namespace** instance indicates which namespace was created. This property is inherited from [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_NamespaceCreationEvent** class is derived from [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

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

 

