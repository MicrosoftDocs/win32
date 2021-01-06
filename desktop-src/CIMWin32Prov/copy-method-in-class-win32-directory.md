---
description: Copies the logical directory entry file or directory specified in the object path to the location specified by the input parameter.
ms.assetid: 038e23d7-71db-4db6-8fb1-e84e972510c9
ms.tgt_platform: multiple
title: Copy method of the Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory.Copy
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Copy method of the Win32\_Directory class

The **Copy** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method copies the logical directory entry file or directory specified in the object path to the location specified by the input parameter. A copy is not supported if overwriting an existing logical file is required.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Copy(
   string FileName
);
```



## Parameters

<dl> <dt>

*FileName* 
</dt> <dd>

Fully qualified name of the copy of the file (or directory). Example: c:\\temp\\newdirectory

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the file was successfully copied, and any other number to indicate an error.

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

Folders often need to be copied from one location to another. For example, you might copy a folder from one server to another to create a backup copy of that folder. Or you might have a templates folder that needs to be copied to user workstations, or a scripts folder that should be copied to all of your DNS servers.

The Win32\_Directory Copy method enables you to copy a folder from one location to another, either on the same computer (for example, copying a folder from drive C to drive D) or on a remote computer. To copy a folder, you return an instance of the folder to be copied and then call the Copy method, passing as a parameter the target location for the new copy of the folder. For example, this line of code copies a folder to the Scripts folder on drive F:

`objFolder.Copy("F:\Scripts")`

WMI will not overwrite an existing folder when executing the Copy method. This means that the copy operation fails if the destination folder exists. For example, suppose you have a folder named Scripts and you attempt to copy that folder to a remote share named \\\\atl-fs-01\\archive. If a folder named Scripts already exists on that share, the copy operation fails.

## Examples

The followng code sample, taken from the [Copy a Folder Using WMI](https://Gallery.TechNet.Microsoft.Com/71b8f517-0240-42a2-be5c-e5a3921604d2), uses the Copy method to copy the folder C:\\Scripts to D:\\Archive.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:" _ 
    & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2") 
 
Set colFolders = objWMIService.ExecQuery( _ 
    "Select * from Win32_Directory where Name = 'c:\\Scripts'") 
 
For Each objFolder in colFolders 
    errResults  = objFolder.Copy("D:\Archive") 
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

 

