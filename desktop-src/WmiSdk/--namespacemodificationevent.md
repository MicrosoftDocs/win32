---
description: Reports a namespace modification event, which is a type of intrinsic event that is generated when a namespace is modified.
ms.assetid: 168505d7-4677-4f41-935e-149f22de2cb5
ms.tgt_platform: multiple
title: __NamespaceModificationEvent class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- __NamespaceModificationEvent
- All
- All
- All
- All
- All
api_type:
- Schema
api_location:
- All
---

# \_\_NamespaceModificationEvent class

The **\_\_NamespaceModificationEvent** system class reports a namespace modification event, which is a type of [intrinsic event](determining-the-type-of-event-to-receive.md) that is generated when a namespace is modified.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __NamespaceModificationEvent : __NamespaceOperationEvent
{
  uint8       SECURITY_DESCRIPTOR[];
  __Namespace PreviousNamespace;
  uint8       SECURITY_DESCRIPTOR [];
  __Namespace TargetNamespace;
  uint64      TIME_CREATED;
};
```

## Members

The **\_\_NamespaceModificationEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NamespaceModificationEvent** class has these properties.

<dl> <dt>

**PreviousNamespace**
</dt> <dd> <dl> <dt>

Data type: **\_\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of the original version of a [**\_\_Namespace**](--namespace.md) instance. The **Name** property of this instance identifies the namespace that is modified.

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](--event.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR** 
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor that the event provider uses to determine the users that can receive an event. This property is inherited from [**\_\_Event**](--event.md).

> [!Note]  
> A **NULL** access control list (ACL) in the [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) grants unlimited access to everyone all the time. For more information, see [Creating a Security Descriptor for a New Object](/windows/desktop/SecAuthZ/creating-a-security-descriptor-for-a-new-object-in-c--).

 

</dd> <dt>

**TargetNamespace**
</dt> <dd> <dl> <dt>

Data type: **\_\_Namespace**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Copy of the [**\_\_Namespace**](--namespace.md) instance that is modified. The **Name** property of the **\_\_Namespace** instance indicates the namespace that is modified. This property is inherited from class [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time that an event is generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Time (UTC) format. This property is inherited from [**\_\_Event**](--event.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> </dl>

## Remarks

The **\_\_NamespaceModificationEvent** class is derived from [**\_\_NamespaceOperationEvent**](--namespaceoperationevent.md).

The only differences between the target namespace and the previous namespace is the qualifiers and properties except [**Name**](--namespace.md).

Note that the [**Name**](--namespace.md) property of a **\_\_Namespace** instance cannot change because namespaces cannot be renamed. To modify the name of a namespace, the **\_\_Namespace** instance must be deleted and re-created with a new name. Therefore, namespace modification events are generated when a change occurs to qualifiers and properties other than **Name**. A namespace modification event is not generated when any kind of change occurs within the namespace. A namespace modification event is generated only when a namespace instance is modified.

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

 

