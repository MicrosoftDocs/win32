---
description: Controls remote access to unsupported versions of Windows.
ms.assetid: eb326bba-a011-4b9c-b4ee-fc08ae364f6f
ms.tgt_platform: multiple
title: '__NTLMUser9X class'
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- __NTLMUser9X
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

# \_\_NTLMUser9X class

The **\_\_NTLMUser9X** system class controls remote access to unsupported versions of Windows. The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class __NTLMUser9X : __SecurityRelatedClass
{
  string Authority;
  sint32 Flags;
  sint32 Mask;
  string Name;
  sint32 Type;
};
```

## Members

The **\_\_NTLMUser9X** class has these types of members:

-   [Properties](#properties)

### Properties

The **\_\_NTLMUser9X** class has these properties.

<dl> <dt>

**Authority**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Domain to which a user name applies.

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Inheritance flags.

<dt>

0
</dt> <dd>

No inheritance.

</dd> <dt>

2
</dt> <dd>

Apply to child namespaces, in addition to the current one.

</dd> </dl>

</dd> <dt>

**Mask**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Bitmask that specifies access rights to the namespace in the Windows Management Instrumentation (WMI) repository. For bit values, see [**Namespace Access Rights Constants**](namespace-access-rights-constants.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

User name.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Access allowed.

<dt>

0
</dt> <dd>

Access allowed.

</dd> <dt>

2
</dt> <dd>

Access denied.

</dd> </dl>

</dd> </dl>

## Remarks

The **\_\_NTLMUser9X** class is used as an input parameter for the [**\_\_SystemSecurity::Get9XUserList**](--systemsecurity-get9xuserlist.md) and [**\_\_SystemSecurity::Set9XUserList**](--systemsecurity-set9xuserlist.md) methods.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>       |
| Minimum supported server<br/> | Windows Server 2008<br/> |
| Namespace<br/>                | All WMI namespaces<br/>  |



## See also

<dl> <dt>

[**\_\_SecurityRelatedClass**](/windows/desktop/WmiSdk/--securityrelatedclass)
</dt> <dt>

[WMI System Classes](wmi-system-classes.md)
</dt> <dt>

[**\_\_SystemSecurity**](--systemsecurity.md)
</dt> </dl>

 

