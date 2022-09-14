---
description: Renames the directory entry file specified in the object path.
ms.assetid: 8bfe1b69-5f93-4408-a742-f03a9cb16bfe
ms.tgt_platform: multiple
title: Rename method of the Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory.Rename
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Rename method of the Win32\_Directory class

The **Rename** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method renames the directory entry file specified in the object path. A rename is not supported if the destination is on another drive or if overwriting an existing logical file is required.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Rename(
   string FileName
);
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Fully qualified new name of the file (or directory). Example: c:\\temp\\newfile.txt.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the file was successfully renamed, and any other number to indicate an error.

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

To rename a folder, first bind to the folder in question and then call the Rename method. As the sole parameter to the method, pass the new name for the folder as a complete path name. For example, if the folder in the C:\\Scripts\\Logs\\Backup is to be renamed C:\\Scripts\\Archive, you must pass C:\\Scripts\\Archive as the complete folder name. Passing only the folder name - Archive - results in an Invalid path error.

The Win32\_Directory class does not provide a one-step method for moving folders. Instead, moving a folder generally involves two steps:

<dl> 1. Copying the folder to its new location  
2. Deleting the original folder  
</dl>

The one exception to this two-step process involves moving a folder to a new location on the same drive. For example, suppose you want to move C:\\Temp to C:\\Scripts\\Temporary Files\\Archive. As long as the current location and the new location are on the same drive, you can move the folder by simply calling the Rename method and passing the new location as the method parameter. This approach effectively allows you to move the folder in a single step. However, the script fails if the current drive and the new drive are different. An attempt to rename C:\\Temp to D:\\Temp fails with a "Drive not the same" error.

## Examples

The following code, from the [Move a Folder Using WMI](https://Gallery.TechNet.Microsoft.Com/f4f9643c-d7ed-4f54-b155-c6515396431f) VBScript sample on TechNet Gallery, uses the Rename method to move the folder C:\\Scripts to C:\\Admins\\Documents\\Archive\\VBScript.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colFolders = objWMIService.ExecQuery _ 
    ("Select * from Win32_Directory where name = 'c:\\Scripts'") 
 
For Each objFolder in colFolders 
    errResults = objFolder.Rename("C:\Admins\Documents\Archive\VBScript") 
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

 

