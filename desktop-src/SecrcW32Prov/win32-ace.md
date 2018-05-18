---
Description: 'The Win32\_ACE abstract WMI class specifies an access control entry (ACE).'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'dfeea7cd-6e24-486a-99d3-f54597bf6d27'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_ACE class'
---

# Win32\_ACE class

The **Win32\_ACE** abstract [WMI class](https://msdn.microsoft.com/library/aa393244) specifies an access control entry (ACE). An ACE grants permission to execute a restricted operation, such as writing to a file or formatting a disk. An ACE that is specific to WMI allows logon, remote access, method execution, and writing to the WMI repository.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{8502C58A-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_ACE : __ACE
{
  uint64        TIME_CREATED;
  uint32        AccessMask;
  uint32        AceFlags;
  uint32        AceType;
  string        GuidInheritedObjectType;
  string        GuidObjectType;
  Win32_Trustee Trustee;
};
```

## Members

The **Win32\_ACE** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ACE** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (AccessMask), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Bit flags that indicate rights granted or denied to the trustee. For more information, see the Remarks section of this topic.

<dt>

<span id="FILE_READ_DATA__file__or_FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__or_file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__OR_FILE_LIST_DIRECTORY__DIRECTORY_"></span>

<span id="FILE_READ_DATA__file__or_FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__or_file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__OR_FILE_LIST_DIRECTORY__DIRECTORY_"></span>**FILE\_READ\_DATA (file) or FILE\_LIST\_DIRECTORY (directory)** (1 (0x1))


</dt> <dd>

Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.

</dd> <dt>

<span id="FILE_WRITE_DATA__file__or_FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__or_file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__OR_FILE_ADD_FILE__DIRECTORY_"></span>

<span id="FILE_WRITE_DATA__file__or_FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__or_file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__OR_FILE_ADD_FILE__DIRECTORY_"></span>**FILE\_WRITE\_DATA (file) or FILE\_ADD\_FILE (directory)** (2 (0x2))


</dt> <dd>

Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.

</dd> <dt>

<span id="FILE_APPEND_DATA__file__or_FILE_ADD_SUBDIRECTORY__directory_"></span><span id="file_append_data__file__or_file_add_subdirectory__directory_"></span><span id="FILE_APPEND_DATA__FILE__OR_FILE_ADD_SUBDIRECTORY__DIRECTORY_"></span>

<span id="FILE_APPEND_DATA__file__or_FILE_ADD_SUBDIRECTORY__directory_"></span><span id="file_append_data__file__or_file_add_subdirectory__directory_"></span><span id="FILE_APPEND_DATA__FILE__OR_FILE_ADD_SUBDIRECTORY__DIRECTORY_"></span>**FILE\_APPEND\_DATA (file) or FILE\_ADD\_SUBDIRECTORY (directory)** (4 (0x4))


</dt> <dd>

Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.

</dd> <dt>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>**FILE\_READ\_EA** (8 (0x8))


</dt> <dd>

Grants the right to read extended attributes.

</dd> <dt>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>**FILE\_WRITE\_EA** (16 (0x10))


</dt> <dd>

Grants the right to write extended attributes.

</dd> <dt>

<span id="FILE_EXECUTE__file__or_FILE_TRAVERSE__directory_"></span><span id="file_execute__file__or_file_traverse__directory_"></span><span id="FILE_EXECUTE__FILE__OR_FILE_TRAVERSE__DIRECTORY_"></span>

<span id="FILE_EXECUTE__file__or_FILE_TRAVERSE__directory_"></span><span id="file_execute__file__or_file_traverse__directory_"></span><span id="FILE_EXECUTE__FILE__OR_FILE_TRAVERSE__DIRECTORY_"></span>**FILE\_EXECUTE (file) or FILE\_TRAVERSE (directory)** (32 (0x20))


</dt> <dd>

Grants the right to execute a file. For a directory, the directory can be traversed.

</dd> <dt>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>**FILE\_DELETE\_CHILD** (64 (0x40))


</dt> <dd>

Grants the right to delete a directory and all the files it contains (its children), even if the files are read-only.

</dd> <dt>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>**FILE\_READ\_ATTRIBUTES** (128 (0x80))


</dt> <dd>

Grants the right to read file attributes.

</dd> <dt>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>**FILE\_WRITE\_ATTRIBUTES** (256 (0x100))


</dt> <dd>

Grants the right to change file attributes.

</dd> <dt>

<span id="DELETE"></span><span id="delete"></span>

<span id="DELETE"></span><span id="delete"></span>**DELETE** (65536 (0x10000))


</dt> <dd>

Grants delete access.

</dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL** (131072 (0x20000))


</dt> <dd>

Grants read access to the security descriptor and owner.

</dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC** (262144 (0x40000))


</dt> <dd>

Grants write access to the discretionary access control list (ACL).

</dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>**WRITE\_OWNER** (524288 (0x80000))


</dt> <dd>

Assigns the write owner.

</dd> <dt>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>**SYNCHRONIZE** (1048576 (0x100000))


</dt> <dd>

Synchronizes access and allows a process to wait for an object to enter the signaled state.

</dd> </dl>

</dd> <dt>

**AceFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (AceFlags), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Bit flags that specify inheritance of the ACE. The the relevant permission values for **AceFlags** are listed below.

<dt>

<span id="OBJECT_INHERIT_ACE"></span><span id="object_inherit_ace"></span>

<span id="OBJECT_INHERIT_ACE"></span><span id="object_inherit_ace"></span>**OBJECT\_INHERIT\_ACE** (1 (0x1))


</dt> <dd>

Noncontainer child objects inherit the ACE as an effective ACE.

For child objects that are containers, the ACE is inherited as an inherit-only ACE unless the **NO\_PROPAGATE\_INHERIT\_ACE** bit flag is also set.

</dd> <dt>

<span id="CONTAINER_INHERIT_ACE"></span><span id="container_inherit_ace"></span>

<span id="CONTAINER_INHERIT_ACE"></span><span id="container_inherit_ace"></span>**CONTAINER\_INHERIT\_ACE** (2 (0x2))


</dt> <dd>

Child objects that are containers, such as directories, inherit the ACE as an effective ACE. The inherited ACE is inheritable unless the **NO\_PROPAGATE\_INHERIT\_ACE** bit flag is also set.

</dd> <dt>

<span id="NO_PROPAGATE_INHERIT_ACE"></span><span id="no_propagate_inherit_ace"></span>

<span id="NO_PROPAGATE_INHERIT_ACE"></span><span id="no_propagate_inherit_ace"></span>**NO\_PROPAGATE\_INHERIT\_ACE** (4 (0x4))


</dt> <dd>

If the ACE is inherited by a child object, the system clears the **OBJECT\_INHERIT\_ACE** and **CONTAINER\_INHERIT\_ACE** flags in the inherited ACE. This prevents the ACE from being inherited by subsequent generations of objects.

</dd> <dt>

<span id="INHERIT_ONLY_ACE"></span><span id="inherit_only_ace"></span>

<span id="INHERIT_ONLY_ACE"></span><span id="inherit_only_ace"></span>**INHERIT\_ONLY\_ACE** (8 (0x8))


</dt> <dd>

Indicates an inherit-only ACE which does not control access to the object to which it is attached. If this flag is not set, the ACE is an effective ACE which controls access to the object to which it is attached.

Both effective and inherit-only ACEs can be inherited depending on the state of the other inheritance flags.

</dd> <dt>

<span id="INHERITED_ACE"></span><span id="inherited_ace"></span>

<span id="INHERITED_ACE"></span><span id="inherited_ace"></span>**INHERITED\_ACE** (16 (0x10))


</dt> <dd>

The system sets this bit when it propagates an inherited ACE to a child object.

</dd> </dl>

The two possible values for **AceFlags** that pertain only to an ACE contained within a system access control list (SACL) are listed below.

<dt>

<span id="SUCCESSFUL_ACCESS_ACE_FLAG"></span><span id="successful_access_ace_flag"></span>

<span id="SUCCESSFUL_ACCESS_ACE_FLAG"></span><span id="successful_access_ace_flag"></span>**SUCCESSFUL\_ACCESS\_ACE\_FLAG** (64 (0x40))


</dt> <dd>

Used with system-audit ACEs in an SACL to generate audit messages for successful access attempts.

</dd> <dt>

<span id="FAILED_ACCESS_ACE_FLAG"></span><span id="failed_access_ace_flag"></span>

<span id="FAILED_ACCESS_ACE_FLAG"></span><span id="failed_access_ace_flag"></span>**FAILED\_ACCESS\_ACE\_FLAG** (128 (0x80))


</dt> <dd>

Used with system-audit ACEs in an SACL to generate audit messages for failed access attempts.

</dd> </dl>

</dd> <dt>

**AceType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (AceType), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Type of ACE.

<dt>

<span id="Access_Allowed"></span><span id="access_allowed"></span><span id="ACCESS_ALLOWED"></span>

**Access Allowed** (0)


</dt> <dd></dd> <dt>

<span id="Access_Denied"></span><span id="access_denied"></span><span id="ACCESS_DENIED"></span>

**Access Denied** (1)


</dt> <dd></dd> <dt>

<span id="Audit"></span><span id="audit"></span><span id="AUDIT"></span>

**Audit** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**GuidInheritedObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (GuidInheritedObjectType), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Globally unique identifier (GUID) associated with the parent of the object to which these rights apply.

</dd> <dt>

**GuidObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (GuidObjectType), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

GUID associated with the type of object to which these rights apply.

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time, in the [CIM\_DATETIME](https://msdn.microsoft.com/library/aa387237) format, when the security descriptor was created.

This property is inherited from [**\_\_ACE**](https://msdn.microsoft.com/library/aa394621).

</dd> <dt>

**Trustee**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Trustee**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Trustee), [**WritePrivileges**](https://msdn.microsoft.com/library/aa393651) ("SeSecurityPrivilege", "SeRestorePrivilege")
</dt> </dl>

Object representing the user account, group account, or logon session to which an ACE applies.

</dd> </dl>

## Remarks

The **Win32\_ACE** class is derived from [**Win32\_MethodParameterClass**](https://msdn.microsoft.com/library/aa394200).

In the **AccessMask** property, the values of the individual rights are added together to form the value. For example, to grant the access permissions **FILE\_WRITE\_ATTRIBUTES**, **FILE\_READ\_EA** and **FILE\_WRITE\_EA** you add the associated values 256, 16, and 8. In this example, the value of **AccessMask** is 280.

Some values have different meanings depending on whether the **AccessMask** property is associated with a file or a directory. For example, when working with a file, the value 4 means **FILE\_APPEND\_DATA** or the right to add data to the file. The same value that is associated with a directory, means **FILE\_ADD\_SUBDIRECTORY** and grants the right to create a subdirectory.

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

[**\_\_ACE**](https://msdn.microsoft.com/library/aa394621)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> </dl>

 

 




