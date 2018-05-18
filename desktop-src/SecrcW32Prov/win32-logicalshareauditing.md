---
Description: 'The Win32\_LogicalShareAuditing association WMI class relates the security settings of a share and one member of its system access control list (SACL).'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '415b0160-02d5-4195-8d3d-afbf32f8c38d'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_LogicalShareAuditing class'
---

# Win32\_LogicalShareAuditing class

The **Win32\_LogicalShareAuditing** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security settings of a share and one member of its system access control list (SACL).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C594-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_LogicalShareAuditing : Win32_SecuritySettingAuditing
{
  uint32                                AuditedAccessMask;
  string                                GuidInheritedObjectType;
  string                                GuidObjectType;
  uint32                                Inheritance;
  uint32                                Type;
  Win32_LogicalShareSecuritySetting REF SecuritySetting;
  Win32_SID                         REF Trustee;
};
```

## Members

The **Win32\_LogicalShareAuditing** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalShareAuditing** class has these properties.

<dl> <dt>

**AuditedAccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags specifying what activities are audited.

This property is inherited from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

<dt>

<span id="FILE_LIST_DIRECTORY"></span><span id="file_list_directory"></span>

<span id="FILE_LIST_DIRECTORY"></span><span id="file_list_directory"></span>**FILE\_LIST\_DIRECTORY** (0)


</dt> <dd>

Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.

</dd> <dt>

<span id="FILE_ADD_FILE"></span><span id="file_add_file"></span>

<span id="FILE_ADD_FILE"></span><span id="file_add_file"></span>**FILE\_ADD\_FILE** (1)


</dt> <dd>

Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.

</dd> <dt>

<span id="FILE_ADD_SUBDIRECTORY"></span><span id="file_add_subdirectory"></span>

<span id="FILE_ADD_SUBDIRECTORY"></span><span id="file_add_subdirectory"></span>**FILE\_ADD\_SUBDIRECTORY** (2)


</dt> <dd>

Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.

</dd> <dt>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>**FILE\_READ\_EA** (3)


</dt> <dd>

Grants the right to read extended attributes.

</dd> <dt>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>**FILE\_WRITE\_EA** (4)


</dt> <dd>

Grants the right to write extended attributes.

</dd> <dt>

<span id="FILE_TRAVERSE"></span><span id="file_traverse"></span>

<span id="FILE_TRAVERSE"></span><span id="file_traverse"></span>**FILE\_TRAVERSE** (5)


</dt> <dd>

Grants the right to execute a file. For a directory, the directory can be traversed.

</dd> <dt>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>**FILE\_DELETE\_CHILD** (6)


</dt> <dd>

Grants the right to delete a directory and all of the files it contains (its children), even if the files are read-only.

</dd> <dt>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>**FILE\_READ\_ATTRIBUTES** (7)


</dt> <dd>

Grants the right to read file attributes.

</dd> <dt>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>**FILE\_WRITE\_ATTRIBUTES** (8)


</dt> <dd>

Grants the right to change file attributes.

</dd> <dt>

<span id="DELETE"></span><span id="delete"></span>

<span id="DELETE"></span><span id="delete"></span>**DELETE** (16)


</dt> <dd>

Grants delete access.

</dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL** (17)


</dt> <dd>

Grants read access to the security descriptor and owner.

</dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC** (18)


</dt> <dd>

Grants write access to the discretionary access control list (DACL).

</dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>**WRITE\_OWNER** (19)


</dt> <dd>

Assigns the write owner.

</dd> <dt>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>**SYNCHRONIZE** (20)


</dt> <dd>

Synchronizes access and allows a process to wait for an object to enter the signaled state.

</dd> </dl>

</dd> <dt>

**GuidInheritedObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the type of object from which this object inherits.

This property is inherited from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

</dd> <dt>

**GuidObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the type of object to which the security settings are applied.

This property is inherited from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

</dd> <dt>

**Inheritance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags specifying how the audit policies are inherited.

This property is inherited from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

</dd> <dt>

**SecuritySetting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalShareSecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SecuritySetting")
</dt> </dl>

Reference to the instance representing the security settings of the share object.

</dd> <dt>

**Trustee**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Trustee")
</dt> </dl>

Reference to the instance representing the entry on the object's SACL.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of access specified for the trustee.

This property is inherited from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

<dt>

<span id="Audit_success"></span><span id="audit_success"></span><span id="AUDIT_SUCCESS"></span>

**Audit success** (0)


</dt> <dd></dd> <dt>

<span id="Audit_failure"></span><span id="audit_failure"></span><span id="AUDIT_FAILURE"></span>

**Audit failure** (1)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_LogicalShareAuditing** class is derived from [**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md).

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

[**Win32\_SecuritySettingAuditing**](win32-securitysettingauditing.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




