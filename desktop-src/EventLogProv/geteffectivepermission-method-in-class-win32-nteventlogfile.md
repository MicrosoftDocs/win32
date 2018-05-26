---
Description: Determines whether or not the caller has all of the permissions on the Win32\_NTEventlogFile object and share where the file or directory is located, if the directory is on a share.
ms.assetid: e4e912d1-ea4b-481d-b86c-34d9d1eb664b
title: GetEffectivePermission method of the Win32\_NTEventlogFile class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GetEffectivePermission method of the Win32\_NTEventlogFile class

The **GetEffectivePermission** [WMI class](https://msdn.microsoft.com/library/aa393244) method determines whether or not the caller has all of the permissions on the Win32\_NTEventlogFile object and share where the file or directory is located, if the directory is on a share.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetEffectivePermission(
  [in] uint32 Permissions
);
```



## Parameters

<dl> <dt>

*Permissions* \[in\]
</dt> <dd>

Bitmap of permissions that the caller can inquire about.



| Value (Dec/Hex)                                                                                                                                                                                                                                                                                                                                                                                                                               | Meaning                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="FILE_READ_DATA__file__FILE_LIST_DIRECTORY__directory_"></span><span id="file_read_data__file__file_list_directory__directory_"></span><span id="FILE_READ_DATA__FILE__FILE_LIST_DIRECTORY__DIRECTORY_"></span><dl> <dt>**FILE\_READ\_DATA (file) FILE\_LIST\_DIRECTORY (directory)**</dt> <dt>1 (0x1)</dt> </dl>                 | Grants the right to read data from the file. For a directory, this value grants the right to list the contents of the directory.<br/> |
| <span id="FILE_WRITE_DATA__file__FILE_ADD_FILE__directory_"></span><span id="file_write_data__file__file_add_file__directory_"></span><span id="FILE_WRITE_DATA__FILE__FILE_ADD_FILE__DIRECTORY_"></span><dl> <dt>**FILE\_WRITE\_DATA (file) FILE\_ADD\_FILE (directory)**</dt> <dt>2 (0x2)</dt> </dl>                                     | Grants the right to write data to the file. For a directory, this value grants the right to create a file in the directory. <br/>     |
| <span id="FILE_APPEND_DATA__file__FILE_ADD_SUBDIRECTORY__directory_"></span><span id="file_append_data__file__file_add_subdirectory__directory_"></span><span id="FILE_APPEND_DATA__FILE__FILE_ADD_SUBDIRECTORY__DIRECTORY_"></span><dl> <dt>**FILE\_APPEND\_DATA (file) FILE\_ADD\_SUBDIRECTORY (directory)**</dt> <dt>4 (0x4)</dt> </dl> | Grants the right to append data to the file. For a directory, this value grants the right to create a subdirectory.<br/>              |
| <span id="FILE_READ_EA"></span><span id="file_read_ea"></span><dl> <dt>**FILE\_READ\_EA**</dt> <dt>8 (0x8)</dt> </dl>                                                                                                                                                                                                                      | Grants the right to read extended attributes.<br/>                                                                                    |
| <span id="FILE_WRITE_EA"></span><span id="file_write_ea"></span><dl> <dt>**FILE\_WRITE\_EA**</dt> <dt>16 (0x10)</dt> </dl>                                                                                                                                                                                                                 | Grants the right to write extended attributes.<br/>                                                                                   |
| <span id="FILE_EXECUTE__file__FILE_TRAVERSE_directory_"></span><span id="file_execute__file__file_traverse_directory_"></span><span id="FILE_EXECUTE__FILE__FILE_TRAVERSE_DIRECTORY_"></span><dl> <dt>**FILE\_EXECUTE (file) FILE\_TRAVERSE (directory)**</dt> <dt>32 (0x20)</dt> </dl>                                                    | Grants the right to execute a file. For a directory, the directory can be traversed. <br/>                                            |
| <span id="FILE_DELETE_CHILD__directory_"></span><span id="file_delete_child__directory_"></span><span id="FILE_DELETE_CHILD__DIRECTORY_"></span><dl> <dt>**FILE\_DELETE\_CHILD (directory)**</dt> <dt>64 (0x40)</dt> </dl>                                                                                                                 | Grants the right to delete a directory and all of the files it contains, even if the files are read-only.<br/>                        |
| <span id="FILE_READ_ATTRIBUTES"></span><span id="file_read_attributes"></span><dl> <dt>**FILE\_READ\_ATTRIBUTES**</dt> <dt>128 (0x80)</dt> </dl>                                                                                                                                                                                           | Grants the right to read file attributes.<br/>                                                                                        |
| <span id="FILE_WRITE_ATTRIBUTES"></span><span id="file_write_attributes"></span><dl> <dt>**FILE\_WRITE\_ATTRIBUTES**</dt> <dt>256 (0x100)</dt> </dl>                                                                                                                                                                                       | Grants the right to change file attributes. <br/>                                                                                     |
| <span id="DELETE"></span><span id="delete"></span><dl> <dt>**DELETE**</dt> <dt>65536 (0x10000)</dt> </dl>                                                                                                                                                                                                                                  | Grants delete access. <br/>                                                                                                           |
| <span id="READ_CONTROL"></span><span id="read_control"></span><dl> <dt>**READ\_CONTROL**</dt> <dt>131072 (0x20000)</dt> </dl>                                                                                                                                                                                                              | Grants read access to the security descriptor and owner.<br/>                                                                         |
| <span id="WRITE_DAC"></span><span id="write_dac"></span><dl> <dt>**WRITE\_DAC**</dt> <dt>262144 (0x40000)</dt> </dl>                                                                                                                                                                                                                       | Grants write access to the discretionary access control list (DACL).<br/>                                                             |
| <span id="WRITE_OWNER"></span><span id="write_owner"></span><dl> <dt>**WRITE\_OWNER**</dt> <dt>524288 (0x80000)</dt> </dl>                                                                                                                                                                                                                 | Assigns the write owner. <br/>                                                                                                        |
| <span id="SYNCHRONIZE"></span><span id="synchronize"></span><dl> <dt>**SYNCHRONIZE**</dt> <dt>1048576 (0x100000)</dt> </dl>                                                                                                                                                                                                                | Synchronizes access and allows a process to wait for an object to enter the signaled state.<br/>                                      |



 

</dd> </dl>

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                       |
| Namespace<br/>                | Root\\CIMV2<br/>                                                               |
| Header<br/>                   | <dl> <dt>Aclui.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>Ntevt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntevt.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_NTEventlogFile**](win32-nteventlogfile.md)
</dt> </dl>

 

 




