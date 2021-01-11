---
description: Represents an access control entry (ACE).
ms.assetid: 47daffd0-b9db-4367-b0b8-654a2da30fed
ms.tgt_platform: multiple
title: '__ACE class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __ACE
- All
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

# \_\_ACE class

The **\_\_ACE** abstract system class represents an access control entry ([*ACE*](/windows/desktop/SecGloss/a-gly)).

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class  __ACE : __SecurityRelatedClass
{
            AceFlags;
            AccessMask;
            AceType;
            GuidInheritedObjectType;
            GuidObjectType;
  uint64    TIME_CREATED;
  __Trustee Trustee;
};
```

## Members

The **\_\_ACE** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_ACE** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: 
</dt> <dt>

Access type: Read/write
</dt> </dl>

Bit flags representing rights that are granted or denied to the trustee. For more information and a description of the flags, see **AccessMask** property in the [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace) class.

</dd> <dt>

**AceFlags**
</dt> <dd> <dl> <dt>

Data type: 
</dt> <dt>

Access type: Read/write
</dt> </dl>

Bit flags specifying the inheritance of the ACE. For more information and a description of the flags, see **AceFlags** property in the [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace) class.

</dd> <dt>

**AceType**
</dt> <dd> <dl> <dt>

Data type: 
</dt> <dt>

Access type: Read/write
</dt> </dl>

The type of ACE entry that this instance represents.

</dd> <dt>

**GuidInheritedObjectType**
</dt> <dd> <dl> <dt>

Data type: 
</dt> <dt>

Access type: Read/write
</dt> </dl>

The GUID of the parent of the object to which the access rights in the **AccessMask** property apply.

</dd> <dt>

**GuidObjectType**
</dt> <dd> <dl> <dt>

Data type: 
</dt> <dt>

Access type: Read/write
</dt> </dl>

The GUID that indicates the type of object to which the rights in the **AccessMask** property apply.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time, in the [CIM\_DATETIME](cim-datetime.md) format, when the security descriptor was created.

</dd> <dt>

**Trustee**
</dt> <dd> <dl> <dt>

Data type: **[**\_\_Trustee**](--trustee.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The trustee of the ACE entry represented by this instance of the **\_\_ACE** class.

</dd> </dl>

## Remarks

This class provides the properties that are inherited by the [**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace) class, which is a member of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class. For more information, see [WMI Security Descriptor Objects](wmi-security-descriptor-objects.md) and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md). For more information about ACEs, see [Access Control Components](/windows/desktop/SecAuthZ/access-control-components).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SecurityRelatedClass**](--securityrelatedclass.md)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**Win32\_ACE**](/previous-versions/windows/desktop/secrcw32prov/win32-ace)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

