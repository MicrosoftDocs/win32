---
Description: The Win32\_LogicalFileAccess association WMI class relates the security settings of a file or directory and one member of its discretionary access control list (DACL).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 36bf5ebb-2b3e-4945-b461-72a9802a92ca
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32\_LogicalFileAccess class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_LogicalFileAccess class

The **Win32\_LogicalFileAccess** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the security settings of a file or directory and one member of its discretionary access control list (DACL). You cannot enumerate this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("SECRCW32"), UUID("{8502C590-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_LogicalFileAccess : Win32_SecuritySettingAccess
{
  uint32                               AccessMask;
  string                               GuidInheritedObjectType;
  string                               GuidObjectType;
  uint32                               Inheritance;
  uint32                               Type;
  Win32_LogicalFileSecuritySetting REF SecuritySetting;
  Win32_SID                        REF Trustee;
};
```

## Members

The **Win32\_LogicalFileAccess** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalFileAccess** class has these properties.

<dl> <dt>

**AccessMask**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags specifying what permissions are affected.

This property is inherited from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

<dt>

<span id="FILE_READ_DATA__file__FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__FILE_LIST_DIRECTORY__DIRECTORY_"></span>

<span id="FILE_READ_DATA__file__FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__FILE_LIST_DIRECTORY__DIRECTORY_"></span>**FILE\_READ\_DATA (file) FILE\_LIST\_DIRECTORY (directory)** (0 (0x0))


</dt> <dd>

Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.

</dd> <dt>

<span id="FILE_WRITE_DATA__file__FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__FILE_ADD_FILE__DIRECTORY_"></span>

<span id="FILE_WRITE_DATA__file__FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__FILE_ADD_FILE__DIRECTORY_"></span>**FILE\_WRITE\_DATA (file) FILE\_ADD\_FILE (directory)** (1 (0x1))


</dt> <dd>

Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.

</dd> <dt>

<span id="FILE_APPEND_DATA__file__FILE_ADD_SUBDIRECTORY"></span><span id="file_append_data__file__file_add_subdirectory"></span><span id="FILE_APPEND_DATA__FILE__FILE_ADD_SUBDIRECTORY"></span>

<span id="FILE_APPEND_DATA__file__FILE_ADD_SUBDIRECTORY"></span><span id="file_append_data__file__file_add_subdirectory"></span><span id="FILE_APPEND_DATA__FILE__FILE_ADD_SUBDIRECTORY"></span>**FILE\_APPEND\_DATA (file) FILE\_ADD\_SUBDIRECTORY** (4 (0x4))


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

<span id="FILE_EXECUTE__file__FILE_TRAVERSE_directory_"></span><span id="file_execute__file__file_traverse_directory_"></span><span id="FILE_EXECUTE__FILE__FILE_TRAVERSE_DIRECTORY_"></span>

<span id="FILE_EXECUTE__file__FILE_TRAVERSE_directory_"></span><span id="file_execute__file__file_traverse_directory_"></span><span id="FILE_EXECUTE__FILE__FILE_TRAVERSE_DIRECTORY_"></span>**FILE\_EXECUTE (file) FILE\_TRAVERSE (directory)** (32 (0x20))


</dt> <dd>

Grants the right to execute a file. For a directory, the directory can be traversed.

</dd> <dt>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>**FILE\_DELETE\_CHILD** (64 (0x40))


</dt> <dd>

Grants the right to delete a directory and all of the files it contains (its children), even if the files are read-only.

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

Grants write access to the discretionary access control list (DACL).

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

**GuidInheritedObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Globally unique identifier (GUID) of the type of object from which this object inherits.

This property is inherited from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

</dd> <dt>

**GuidObjectType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

GUID of the type of object to which the security settings are applied.

This property is inherited from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

</dd> <dt>

**Inheritance**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Bit flags specifying how the access rights are inherited.

This property is inherited from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

</dd> <dt>

**SecuritySetting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalFileSecuritySetting**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("SecuritySetting")
</dt> </dl>

Reference to the instance representing the security settings of the file or directory object. This property cannot be enumerated.

</dd> <dt>

**Trustee**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SID**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Trustee")
</dt> </dl>

Reference to the instance representing the entry on the object's DACL.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of access specified for the trustee.

This property is inherited from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

<dt>

<span id="Set"></span><span id="set"></span><span id="SET"></span>

**Set** (0)


</dt> <dd></dd> <dt>

<span id="Deny"></span><span id="deny"></span><span id="DENY"></span>

**Deny** (1)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_LogicalFileAccess** class is derived from [**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SecuritySettingAccess**](win32-securitysettingaccess.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> </dl>

 

 




