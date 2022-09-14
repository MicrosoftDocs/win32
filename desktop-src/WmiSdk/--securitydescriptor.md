---
description: Represents a security descriptor.
ms.assetid: 1ade1751-52a2-4ada-8255-323321111663
ms.tgt_platform: multiple
title: '__SecurityDescriptor class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __SecurityDescriptor
- All
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

# \_\_SecurityDescriptor class

The **\_\_SecurityDescriptor** abstract system class represents a [*security descriptor*](/windows/desktop/SecGloss/s-gly).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __SecurityDescriptor
{
  uint32 ControlFlags;
  __ACE  DACL[];
  __ACE  Group;
  __ACE  Owner;
  __ACE  SACL;
  uint64 TIME_CREATED;
};
```

## Members

The **\_\_SecurityDescriptor** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_SecurityDescriptor** class has these properties.

<dl> <dt>

**ControlFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags that provide information about the descriptor's contents and format. See the **ControlFlags** property in the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class for a description of the flags.

</dd> <dt>

**DACL**
</dt> <dd> <dl> <dt>

Data type: **[**\_\_ACE**](--ace.md)** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of [**\_\_ACE**](--ace.md) entries that specify access to the object.

</dd> <dt>

**Group**
</dt> <dd> <dl> <dt>

Data type: **[**\_\_ACE**](--ace.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ACE that identifies the trustee representing the group of the object.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **[**\_\_ACE**](--ace.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ACE that identifies the trustee representing the owner of the object.

</dd> <dt>

**SACL**
</dt> <dd> <dl> <dt>

Data type: **[**\_\_ACE**](--ace.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of [**\_\_ACE**](--ace.md) entries that identifies users and groups for which auditing information is gathered.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in the [CIM\_DATETIME](cim-datetime.md) format when the security descriptor was created.

</dd> </dl>

## Remarks

This class provides properties inherited by [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor). For more information, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md) and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md). For more information about ACEs, see [Access Control Components](/windows/desktop/SecAuthZ/access-control-components).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

