---
description: The Delete WMI class method will delete the logical file (or directory) specified in the object path.
ms.assetid: 5663b8a8-3089-475b-8a36-454a7315bfca
ms.tgt_platform: multiple
title: Delete method of the Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory.Delete
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Delete method of the Win32\_Directory class

The **Delete** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method will delete the logical file (or directory) specified in the object path.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Delete();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) if the file was successfully deleted, and any other number to indicate an error.

<dl> <dt>

**0**
</dt> <dd>

The request was successful.

</dd> <dt>

**2**
</dt> <dd>

Access was denied.

</dd> <dt>

**8**
</dt> <dd>

An unspecified failure occurred.

</dd> <dt>

**9**
</dt> <dd>

The name specified was not valid.

</dd> <dt>

**10**
</dt> <dd>

The object specified already exists.

</dd> <dt>

**11**
</dt> <dd>

The file system is not NTFS.

</dd> <dt>

**12**
</dt> <dd>

The platform is not Windows.

</dd> <dt>

**13**
</dt> <dd>

The drive is not the same.

</dd> <dt>

**14**
</dt> <dd>

The directory is not empty.

</dd> <dt>

**15**
</dt> <dd>

There has been a sharing violation.

</dd> <dt>

**16**
</dt> <dd>

The start file specified was not valid.

</dd> <dt>

**17**
</dt> <dd>

A privilege required for the operation is not held.

</dd> <dt>

**21**
</dt> <dd>

A parameter specified is not valid.

</dd> </dl>

## Remarks

Folders are not necessarily permanent additions to a file system. At some point, folders might need to be deleted, perhaps because they are no longer required, because the role of the computer has changed, or because the folders were created by mistake.

Delete allows you to delete folders: you simply bind to the folder in question and then call the Delete method. After the Delete method is called, the folder is permanently removed from the file system; it is not sent to the Recycle Bin. In addition, no confirmation notice ("Are you sure you want to delete this folder?") is issued. Instead, the folder is immediately removed.

You cannot delete read-only folders using the FileSystemObject; however, this can be done using WMI. If your script uses WMI and you do not want to remove a read-only folder, you must use the Readable property to check the folder status before deleting it.

## Examples

The following VBScript code sample deletes the folder C:\\Scripts.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colFolders = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_Directory WHERE Name = 'c:\\Scripts'")
For Each objFolder in colFolders
 errResults = objFolder.Delete
 Wscript.Echo errResults
Next
```



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

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_Directory**](win32-directory.md)
</dt> </dl>

 

