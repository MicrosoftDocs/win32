---
description: Changes the security permissions for the logical file specified in the object path.
ms.assetid: a3caa717-ad37-4e4f-9f4e-f37aed382fa4
ms.tgt_platform: multiple
title: ChangeSecurityPermissions method of the CIM_LogicalFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CIM_LogicalFile.ChangeSecurityPermissions
api_type:
- COM
api_location:
- CIMWin32.dll
---

# ChangeSecurityPermissions method of the CIM\_LogicalFile class

The **ChangeSecurityPermissions** method changes the security permissions for the logical file specified in the object path. If the logical file is a directory, then **ChangeSecurityPermissions** will act recursively, changing the security permissions for all of the files and sub-directories that the directory contains.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ChangeSecurityPermissions(
  [in] Win32_SecurityDescriptor SecurityDescriptor,
  [in] uint32                   Option
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

Specifies security information.

> [!Note]  
> A **NULL** access control list (ACL) in the [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) grants unlimited access.

 

</dd> <dt>

*Option* \[in\]
</dt> <dd>

Security privilege to modify. For example, to change the owner and DACL security, use:

`Option = 1 + 4`

or

`Option = CHANGE_OWNER_SECURITY_INFORMATION | CHANGE_DACL_SECURITY_INFORMATION`

<dt>

<span id="Change_Owner_Security_Information"></span><span id="change_owner_security_information"></span><span id="CHANGE_OWNER_SECURITY_INFORMATION"></span>

<span id="Change_Owner_Security_Information"></span><span id="change_owner_security_information"></span><span id="CHANGE_OWNER_SECURITY_INFORMATION"></span>**Change\_Owner\_Security\_Information** (1)


</dt> <dd>

Change the owner of the logical file.

</dd> <dt>

<span id="Change_Group_Security_Information"></span><span id="change_group_security_information"></span><span id="CHANGE_GROUP_SECURITY_INFORMATION"></span>

<span id="Change_Group_Security_Information"></span><span id="change_group_security_information"></span><span id="CHANGE_GROUP_SECURITY_INFORMATION"></span>**Change\_Group\_Security\_Information** (2)


</dt> <dd>

Change the group of the logical file.

</dd> <dt>

<span id="Change_Dacl_Security_Information"></span><span id="change_dacl_security_information"></span><span id="CHANGE_DACL_SECURITY_INFORMATION"></span>

<span id="Change_Dacl_Security_Information"></span><span id="change_dacl_security_information"></span><span id="CHANGE_DACL_SECURITY_INFORMATION"></span>**Change\_Dacl\_Security\_Information** (4)


</dt> <dd>

Change the ACL of the logical file.

</dd> <dt>

<span id="Change_Sacl_Security_Information"></span><span id="change_sacl_security_information"></span><span id="CHANGE_SACL_SECURITY_INFORMATION"></span>

<span id="Change_Sacl_Security_Information"></span><span id="change_sacl_security_information"></span><span id="CHANGE_SACL_SECURITY_INFORMATION"></span>**Change\_Sacl\_Security\_Information** (8)


</dt> <dd>

Change the system ACL of the logical file.

</dd> </dl> </dd> </dl>

## Return value

Returns a value of 0 on success, and any other number to indicate an error.

<dl> <dt>

**Success**
</dt> <dd>

0

Success.

</dd> <dt>

**Access Denied**
</dt> <dd>

2

Access denied.

</dd> <dt>

**Unspecified failure**
</dt> <dd>

8

Unspecified failure.

</dd> <dt>

**Invalid object**
</dt> <dd>

9

Invalid object.

</dd> <dt>

**Object already exists**
</dt> <dd>

10

Object already exists.

</dd> <dt>

**File system not NTFS**
</dt> <dd>

11

File system not NTFS.

</dd> <dt>

**Platform not NT/Windows 2000**
</dt> <dd>

12

Platform not Windows.

</dd> <dt>

**Drive not the same**
</dt> <dd>

13

Drive not the same.

</dd> <dt>

**Directory not empty**
</dt> <dd>

14

Directory not empty.

</dd> <dt>

**Sharing violation**
</dt> <dd>

15

Sharing violation.

</dd> <dt>

**Invalid start file**
</dt> <dd>

16

Invalid start file.

</dd> <dt>

**Privilege not held**
</dt> <dd>

17

Privilege not held.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

Invalid parameter.

</dd> </dl>

## Remarks

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_LogicalFile**](changesecuritypermissions-method-in-class-cim-logicalfile.md)
</dt> <dt>

[**CIM\_LogicalFile**](cim-logicalfile.md)
</dt> </dl>

 

