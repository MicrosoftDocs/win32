---
description: WMI classes that represent files or directories, such as Win32\_CodecFile or CIM\_DataFile, contain an AccessMask property.
ms.assetid: 9020b337-d44f-4247-b623-68a1bcf35abb
ms.tgt_platform: multiple
title: File and Directory Access Rights Constants (Winnt.h)
ms.topic: reference
ms.date: 05/31/2018
---

# File and Directory Access Rights Constants

WMI classes that represent files or directories, such as [**Win32\_CodecFile**](/windows/desktop/CIMWin32Prov/win32-codecfile) or [**CIM\_DataFile**](/windows/desktop/CIMWin32Prov/cim-datafile), contain an **AccessMask** property. This property contains bit settings that specify the access rights a user or group must have for specific access or operations on the file. For more information, see [File Security and Access Rights](/windows/desktop/FileIO/file-security-and-access-rights) and [Changing Access Security on Securable Objects](changing-access-security-on-securable-objects.md).

The file or directory classes which contain an **AccessMask** property include:

-   [**CIM\_DataFile**](/windows/desktop/CIMWin32Prov/cim-datafile)
-   [**CIM\_Directory**](/windows/desktop/CIMWin32Prov/cim-directory)
-   [**CIM\_LogicalFile**](/windows/desktop/CIMWin32Prov/cim-logicalfile)
-   [**Win32\_CodecFile**](/windows/desktop/CIMWin32Prov/win32-codecfile)
-   [**Win32\_Directory**](/windows/desktop/CIMWin32Prov/win32-directory)
-   [**Win32\_NTEventLogFile**](/previous-versions/windows/desktop/legacy/aa394225(v=vs.85))
-   [**Win32\_Share**](/windows/desktop/CIMWin32Prov/win32-share)
-   [**Win32\_ShortcutFile**](/windows/desktop/CIMWin32Prov/win32-shortcutfile)

The following list lists the values for file and directory access rights in the **AccessMask** property. This property is a bitmap.

<dl> <dt>

<span id="FILE_READ_DATA"></span><span id="file_read_data"></span>**FILE\_READ\_DATA**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Grants the right to read data from the file.


</dt> </dl> </dd> <dt>

<span id="FILE_LIST_DIRECTORY"></span><span id="file_list_directory"></span>**FILE\_LIST\_DIRECTORY**
</dt> <dd> <dl> <dt>

1 (0x1)
</dt> <dt>



Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.


</dt> </dl> </dd> <dt>

<span id="FILE_WRITE_DATA"></span><span id="file_write_data"></span>**FILE\_WRITE\_DATA**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



Grants the right to write data to the file.


</dt> </dl> </dd> <dt>

<span id="FILE_ADD_FILE"></span><span id="file_add_file"></span>**FILE\_ADD\_FILE**
</dt> <dd> <dl> <dt>

2 (0x2)
</dt> <dt>



Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory.


</dt> </dl> </dd> <dt>

<span id="FILE_APPEND_DATA"></span><span id="file_append_data"></span>**FILE\_APPEND\_DATA**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.


</dt> </dl> </dd> <dt>

<span id="FILE_ADD_SUBDIRECTORY"></span><span id="file_add_subdirectory"></span>**FILE\_ADD\_SUBDIRECTORY**
</dt> <dd> <dl> <dt>

4 (0x4)
</dt> <dt>



Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.


</dt> </dl> </dd> <dt>

<span id="FILE_READ_EA"></span><span id="file_read_ea"></span>**FILE\_READ\_EA**
</dt> <dd> <dl> <dt>

8 (0x8)
</dt> <dt>



Grants the right to read extended attributes.


</dt> </dl> </dd> <dt>

<span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span>**FILE\_WRITE\_EA**
</dt> <dd> <dl> <dt>

16 (0x10)
</dt> <dt>



Grants the right to write extended attributes.


</dt> </dl> </dd> <dt>

<span id="FILE_EXECUTE"></span><span id="file_execute"></span>**FILE\_EXECUTE**
</dt> <dd> <dl> <dt>

32 (0x20)
</dt> <dt>



Grants the right to execute a file.


</dt> </dl> </dd> <dt>

<span id="FILE_TRAVERSE"></span><span id="file_traverse"></span>**FILE\_TRAVERSE**
</dt> <dd> <dl> <dt>

32 (0x20)
</dt> <dt>



Grants the right to execute a file. For a directory, the directory can be traversed.


</dt> </dl> </dd> <dt>

<span id="FILE_DELETE_CHILD"></span><span id="file_delete_child"></span>**FILE\_DELETE\_CHILD**
</dt> <dd> <dl> <dt>

64 (0x40)
</dt> <dt>



Grants the right to delete a directory and all the files it contains (its children), even if the files are read-only.


</dt> </dl> </dd> <dt>

<span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span>**FILE\_READ\_ATTRIBUTES**
</dt> <dd> <dl> <dt>

128 (0x80)
</dt> <dt>



Grants the right to read file attributes.


</dt> </dl> </dd> <dt>

<span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span>**FILE\_WRITE\_ATTRIBUTES**
</dt> <dd> <dl> <dt>

256 (0x100)
</dt> <dt>



Grants the right to change file attributes.


</dt> </dl> </dd> <dt>

<span id="DELETE"></span><span id="delete"></span>**DELETE**
</dt> <dd> <dl> <dt>

65536 (0x10000)
</dt> <dt>



Grants the right to delete the object.


</dt> </dl> </dd> <dt>

<span id="READ_CONTROL"></span><span id="read_control"></span>**READ\_CONTROL**
</dt> <dd> <dl> <dt>

131072 (0x20000)
</dt> <dt>



Grants the right to read the information in the security descriptor for the object, not including the information in the SACL.


</dt> </dl> </dd> <dt>

<span id="WRITE_DAC"></span><span id="write_dac"></span>**WRITE\_DAC**
</dt> <dd> <dl> <dt>

262144 (0x40000)
</dt> <dt>



Grants the right to modify the DACL in the object security descriptor for the object.


</dt> </dl> </dd> <dt>

<span id="WRITE_OWNER"></span><span id="write_owner"></span>**WRITE\_OWNER**
</dt> <dd> <dl> <dt>

524288 (0x80000)
</dt> <dt>



Grants the right to change the owner in the security descriptor for the object.


</dt> </dl> </dd> <dt>

<span id="SYNCHRONIZE"></span><span id="synchronize"></span>**SYNCHRONIZE**
</dt> <dd> <dl> <dt>

1048576 (0x100000)
</dt> <dt>



Grants the right to use the object for synchronization. This enables a process to wait until the object is in signaled state. Some object types do not support this access right.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winnt.h</dt> </dl> |



## See also

<dl> <dt>

[WMI Security Constants](wmi-security-constants.md)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 

