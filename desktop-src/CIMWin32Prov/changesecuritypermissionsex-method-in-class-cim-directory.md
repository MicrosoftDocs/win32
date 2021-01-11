---
description: Changes the security permissions for the logical directory entry file specified in the object path (this method is an extended version of the ChangeSecurityPermissions method and is inherited from CIM\_LogicalFile).
ms.assetid: 5c1f66ba-9aa1-47ca-8fcf-7663782544cd
ms.tgt_platform: multiple
title: ChangeSecurityPermissionsEx method of the CIM_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CIM_Directory.ChangeSecurityPermissionsEx
api_type:
- COM
api_location:
- CIMWin32.dll
---

# ChangeSecurityPermissionsEx method of the CIM\_Directory class

The **ChangeSecurityPermissionsEx** method changes the security permissions for the logical directory entry file specified in the object path (this method is an extended version of the [**ChangeSecurityPermissions**](changesecuritypermissions-method-in-class-cim-directory.md) method and is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md)). If the logical file is a directory, then this method will act recursively, changing the security permissions for all of the files and sub-directories that the directory contains.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 ChangeSecurityPermissionsEx(
  [in]           Win32_SecurityDescriptor SecurityDescriptor,
  [in]           uint32                   Option,
  [out]          string                   StopFileName,
  [in, optional] string                   StartFileName,
  [in, optional] boolean                  Recursive
);
```



## Parameters

<dl> <dt>

*SecurityDescriptor* \[in\]
</dt> <dd>

Specifies security information.

> [!Note]  
> A **NULL** ACL in the [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) structure grants unlimited access.

 

</dd> <dt>

*Option* \[in\]
</dt> <dd>

Security privilege to modify. For example, to change the owner and DACL security, use

`Option = 1 + 4`

or

`Option = CHANGE_OWNER_SECURITY_INFORMATION | CHANGE_DACL_SECURITY_INFORMATION`

<dt>

<span id="CHANGE_OWNER_SECURITY_INFORMATION"></span><span id="change_owner_security_information"></span>

<span id="CHANGE_OWNER_SECURITY_INFORMATION"></span><span id="change_owner_security_information"></span>**CHANGE\_OWNER\_SECURITY\_INFORMATION** (1)


</dt> <dd>

Change the owner of the logical file.

</dd> <dt>

<span id="CHANGE_GROUP_SECURITY_INFORMATION"></span><span id="change_group_security_information"></span>

<span id="CHANGE_GROUP_SECURITY_INFORMATION"></span><span id="change_group_security_information"></span>**CHANGE\_GROUP\_SECURITY\_INFORMATION** (2)


</dt> <dd>

Change the group of the logical file.

</dd> <dt>

<span id="CHANGE_DACL_SECURITY_INFORMATION"></span><span id="change_dacl_security_information"></span>

<span id="CHANGE_DACL_SECURITY_INFORMATION"></span><span id="change_dacl_security_information"></span>**CHANGE\_DACL\_SECURITY\_INFORMATION** (4)


</dt> <dd>

Change the ACL of the logical file.

</dd> <dt>

<span id="CHANGE_SACL_SECURITY_INFORMATION"></span><span id="change_sacl_security_information"></span>

<span id="CHANGE_SACL_SECURITY_INFORMATION"></span><span id="change_sacl_security_information"></span>**CHANGE\_SACL\_SECURITY\_INFORMATION** (8)


</dt> <dd>

Change the system ACL of the logical file.

</dd> </dl> </dd> <dt>

*StopFileName* \[out\]
</dt> <dd>

String that represents the name of the file (or directory) where the method failed. This parameter has a value of **null** if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

String that represents the child file (or directory) to use as a starting point for this method. Typically, the *StartFileName* parameter is the *StopFileName* parameter specifying the file (or directory) at which an error occurred from the previous method call. If the parameter value is **null**, the operation is performed on the file or directory specified in the [**ExecMethod**](/windows/desktop/WmiSdk/swbemservices-execmethod) call.

</dd> <dt>

*Recursive* \[in, optional\]
</dt> <dd>

If **TRUE**, the method is also applied recursively to files and directories within the directory specified by the [**CIM\_Directory**](cim-directory.md) instance. For file instances, this parameter is ignored.

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error.

<dl> <dt>


</dt> <dd>

0

Success.

</dd> <dt>


</dt> <dd>

2

Access denied.

</dd> <dt>


</dt> <dd>

8

Unspecified failure.

</dd> <dt>


</dt> <dd>

9

Invalid object.

</dd> <dt>


</dt> <dd>

10

Object already exists.

</dd> <dt>


</dt> <dd>

11

File system not NTFS.

</dd> <dt>


</dt> <dd>

12

Platform not Windows.

</dd> <dt>


</dt> <dd>

13

Drive not the same.

</dd> <dt>


</dt> <dd>

14

Directory not empty.

</dd> <dt>


</dt> <dd>

15

Sharing violation.

</dd> <dt>


</dt> <dd>

16

Invalid start file.

</dd> <dt>


</dt> <dd>

17

Privilege not held.

</dd> <dt>


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

[CIM\_Directory](changesecuritypermissionsex-method-in-class-cim-directory.md)
</dt> <dt>

[**CIM\_Directory**](cim-directory.md)
</dt> </dl>

 

