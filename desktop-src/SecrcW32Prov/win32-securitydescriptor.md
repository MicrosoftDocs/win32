---
Description: 'The Win32\_SecurityDescriptor abstract WMI class represents a SECURITY\_DESCRIPTOR structure. A security descriptor contains the security information for a securable object.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '1045d6e2-64bb-404f-80f2-3b5b46717892'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_SecurityDescriptor class'
---

# Win32\_SecurityDescriptor class

The **Win32\_SecurityDescriptor** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) represents a [**SECURITY\_DESCRIPTOR**](https://msdn.microsoft.com/library/windows/desktop/aa379561) structure. A security descriptor contains the security information for a securable object. The **Owner** and **Group** properties identify the owner and primary group for the object. It can also contain a [*discretionary access control list (DACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) that controls access to the object and a [*system access control list (SACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) that controls the logging of attempts to access the object.

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

``` syntax
[abstract, UUID("{8502C58B-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SecurityDescriptor : __SecurityDescriptor
{
  uint64        TIME_CREATED;
  uint32        ControlFlags;
  Win32_ACE     DACL[];
  Win32_Trustee Group;
  Win32_Trustee Owner;
  Win32_ACE     SACL[];
};
```

## Members

The **Win32\_SecurityDescriptor** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SecurityDescriptor** class has these properties.

<dl> <dt>

**ControlFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (ControlFlags), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Control bits that qualify the meaning of a security descriptor (SD) or its individual members. See the Remarks section of this topic for information about setting the **ControlFlags** value. The following list lists the flags in **ControlFlags**. For more information, see [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566).

<dt>

<span id="SE_OWNER_DEFAULTED"></span><span id="se_owner_defaulted"></span>

<span id="SE_OWNER_DEFAULTED"></span><span id="se_owner_defaulted"></span>**SE\_OWNER\_DEFAULTED** (1 (0x1))


</dt> <dd>

Indicates an SD with a default owner security identifier (SID). Use this bit to find all of the objects that have default owner permissions set.

</dd> <dt>

<span id="SE_GROUP_DEFAULTED"></span><span id="se_group_defaulted"></span>

<span id="SE_GROUP_DEFAULTED"></span><span id="se_group_defaulted"></span>**SE\_GROUP\_DEFAULTED** (2 (0x2))


</dt> <dd>

Indicates an SD with a default group SID. Use this bit to find all of the objects that have default group permissions set.

</dd> <dt>

<span id="SE_DACL_PRESENT"></span><span id="se_dacl_present"></span>

<span id="SE_DACL_PRESENT"></span><span id="se_dacl_present"></span>**SE\_DACL\_PRESENT** (4 (0x4))


</dt> <dd>

Indicates an SD that has a DACL. If this flag is not set, or if this flag is set and the DACL is **NULL**, the SD allows full access to everyone.

</dd> <dt>

<span id="SE_DACL_DEFAULTED"></span><span id="se_dacl_defaulted"></span>

<span id="SE_DACL_DEFAULTED"></span><span id="se_dacl_defaulted"></span>**SE\_DACL\_DEFAULTED** (8 (0x8))


</dt> <dd>

Indicates an SD with a default DACL. For example, if an object creator does not specify a DACL, the object receives the default DACL from the access token of the creator. This flag can affect how the system treats the DACL, with respect to access control entry (ACE) inheritance. The system ignores this flag if the **SE\_DACL\_PRESENT** flag is not set.

</dd> <dt>

<span id="SE_SACL_PRESENT"></span><span id="se_sacl_present"></span>

<span id="SE_SACL_PRESENT"></span><span id="se_sacl_present"></span>**SE\_SACL\_PRESENT** (16 (0x10))


</dt> <dd>

Indicates an SD that has a system access control list (SACL).

</dd> <dt>

<span id="SE_SACL_DEFAULTED"></span><span id="se_sacl_defaulted"></span>

<span id="SE_SACL_DEFAULTED"></span><span id="se_sacl_defaulted"></span>**SE\_SACL\_DEFAULTED** (32 (0x20))


</dt> <dd>

Indicates an SD with a default SACL. For example, if an object creator does not specify an SACL, the object receives the default SACL from the access token of the creator. This flag can affect how the system treats the SACL, with respect to ACE inheritance. The system ignores this flag if the **SE\_SACL\_PRESENT** flag is not set.

</dd> <dt>

<span id="SE_DACL_AUTO_INHERIT_REQ"></span><span id="se_dacl_auto_inherit_req"></span>

<span id="SE_DACL_AUTO_INHERIT_REQ"></span><span id="se_dacl_auto_inherit_req"></span>**SE\_DACL\_AUTO\_INHERIT\_REQ** (256 (0x100))


</dt> <dd>

Requests that the provider for the object protected by the SD automatically propagate the DACL to existing child objects. If the provider supports automatic inheritance, the DACL is propagated to any existing child objects, and the **SE\_DACL\_AUTO\_INHERITED** bit in the SD of the parent and child objects is set.

</dd> <dt>

<span id="SE_SACL_AUTO_INHERIT_REQ"></span><span id="se_sacl_auto_inherit_req"></span>

<span id="SE_SACL_AUTO_INHERIT_REQ"></span><span id="se_sacl_auto_inherit_req"></span>**SE\_SACL\_AUTO\_INHERIT\_REQ** (512 (0x200))


</dt> <dd>

Requests that the provider for the object protected by the SD automatically propagate the SACL to existing child objects. If the provider supports automatic inheritance, the SACL is propagated to any existing child objects, and the **SE\_SACL\_AUTO\_INHERITED** bit in the SDs of the parent object and child objects is set.

</dd> <dt>

<span id="SE_DACL_AUTO_INHERITED"></span><span id="se_dacl_auto_inherited"></span>

<span id="SE_DACL_AUTO_INHERITED"></span><span id="se_dacl_auto_inherited"></span>**SE\_DACL\_AUTO\_INHERITED** (1024 (0x400))


</dt> <dd>

Indicates an SD in which the DACL is set up to support automatic propagation of inheritable ACEs to existing child objects. The system sets this bit when it performs the automatic inheritance algorithm for the object and its existing child objects.

</dd> <dt>

<span id="SE_SACL_AUTO_INHERITED"></span><span id="se_sacl_auto_inherited"></span>

<span id="SE_SACL_AUTO_INHERITED"></span><span id="se_sacl_auto_inherited"></span>**SE\_SACL\_AUTO\_INHERITED** (2048 (0x800))


</dt> <dd>

Indicates an SD in which the SACL is set up to support automatic propagation of inheritable ACEs to existing child objects. The system sets this bit when it performs the automatic inheritance algorithm for the object and its existing child objects.

</dd> <dt>

<span id="SE_DACL_PROTECTED"></span><span id="se_dacl_protected"></span>

<span id="SE_DACL_PROTECTED"></span><span id="se_dacl_protected"></span>**SE\_DACL\_PROTECTED** (4096 (0x1000))


</dt> <dd>

Prevents the DACL of an SD from being modified by inheritable ACEs.

</dd> <dt>

<span id="SE_SACL_PROTECTED"></span><span id="se_sacl_protected"></span>

<span id="SE_SACL_PROTECTED"></span><span id="se_sacl_protected"></span>**SE\_SACL\_PROTECTED** (8192 (0x2000))


</dt> <dd>

Prevents the SACL of an SD from being modified by inheritable ACEs.

</dd> <dt>

<span id="SE_SELF_RELATIVE"></span><span id="se_self_relative"></span>

<span id="SE_SELF_RELATIVE"></span><span id="se_self_relative"></span>**SE\_SELF\_RELATIVE** (32768 (0x8000))


</dt> <dd>

Indicates an SD in self-relative format with all the security information in a contiguous block of memory. If this flag is not set, the SD is in absolute format. For more information, see [Absolute and Self-Relative Security Descriptors](https://msdn.microsoft.com/library/windows/desktop/aa374807).

</dd> </dl>

</dd> <dt>

**DACL**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ACE** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (DACL), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Each array entry defines the type of object access that the system grants to a specific user or group. For more information about security for access control lists (ACL), see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872) and [Creating a DACL](https://msdn.microsoft.com/library/windows/desktop/ms717798).

</dd> <dt>

**Group**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Trustee**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Group), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Group that owns this object.

</dd> <dt>

**Owner**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Trustee**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Owner), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Owner of an object.

</dd> <dt>

**SACL**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ACE** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (SACL), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Each array entry defines the type of access attempts that generate audit records for a specific user or group.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time in the [CIM\_DATETIME](https://msdn.microsoft.com/library/aa387237) format when the security descriptor was created.

This property is inherited from [**\_\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394673).

</dd> </dl>

## Remarks

The **Win32\_SecurityDescriptor** class is derived from [**Win32\_MethodParameterClass**](https://msdn.microsoft.com/library/aa394200).

The values in **ControlFlags** affect the elements of the descriptor that WMI writes to a new SD in methods such as [**Win32\_SecuritySetting.SetSecurityDescriptor**](setsecuritydescriptor-method-in-class-win32-securitysetting.md). Some of the flags, such as **SE\_GROUP\_DEFAULTED** or **SE\_SACL\_DEFAULTED** indicate that a part of the SD is a default value. For example, Active Directory may have default SDs for all types of objects. When a new object is created, the default owner, group, DACL, and SACL are applied. If a system-wide change must be made to the defaults, the system administrator can find all of the objects with defaults by locating the objects that have the default flags set.

If the **SE\_DACL\_PRESENT** bit is specified and a DACL entry is also present in the call to **SetSecurityDescriptor**, then an empty DACL is written to the new security descriptor. To provide better security, WMI does not write a **NULL** DACL when **SE\_DACL\_PRESENT** is set but a parameter is not supplied, because a **NULL** DACL gives everyone full access to the object. For more information, see [Creating a DACL](https://msdn.microsoft.com/library/windows/desktop/ms717798).

The **ControlFlags** property contains individual bit positions, which indicate that specific flags are set. You can combine these flags by adding the associated values. For example, to specify both **SE\_DACL\_PRESENT** and **SE\_DACL\_AUTO\_INHERITED** you add the associated values 4 and 1024 to make the value of the **ControlFlags** property 1028.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394673)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> </dl>

 

 




