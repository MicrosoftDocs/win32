---
description: Compresses the logical directory entry file (or directory) specified in the object path.
ms.assetid: 4db13622-75c5-45db-8536-451059c0e477
ms.tgt_platform: multiple
title: Compress method of the Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory.Compress
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Compress method of the Win32\_Directory class

The **Compress** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method compresses the logical directory entry file (or directory) specified in the object path.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Compress();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) if the file was successfully compressed, and any other number to indicate an error.

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

The file system is not an NTFS.

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

Compression provides a way to free additional storage space on a disk drive without purchasing new hardware and without removing files or folders. Depending on the size of your hard disk and the type of files stored on that disk, you might be able to recover hundreds of megabytes of disk space and thus preclude the need to purchase a new hard drive and to take the computer offline until the new drive is installed.

The Compress method compresses all the files and subfolders within a specified folder. In addition, the class also includes an Uncompress method that removes compression from all the files and subfolders in a folder. Similar methods are also provided with the CIM\_Datafile class. This allows you to selectively compress or uncompress specific files within a folder.

Because compression imparts a slight performance penalty, it is not recommended for files or folders that are accessed on a routine basis; for example, you probably do not want to compress database files, log files, or user profile folders. Better candidates for compression are files and folders that are not accessed very often. For example, you might write a script to return a collection of folders on a drive that have not been accessed for a month or more and then compress each of those folders.

The amount of disk space freed by compressing folders varies depending on the type of files stored in that folder. For example, .jpg files are already compressed, and further compression has little effect on the size of the file. With other file types, however, the savings can be considerable. For example, a new folder was created on a Windows 2000-based test computer, and 33 Microsoft Word documents, taking up a total of 15 megabytes (MB) of disk space, were copied into that folder. When the documents were compressed, the folder took up only 7 MB of disk space.

## Examples

The following VBScript sample compresses the folder C:\\Scripts.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colFolders = objWMIService.ExecQuery _
 ("SELECT * FROM Win32_Directory WHERE Name = 'c:\\Scripts'")
For Each objFolder in colFolders
 errResults = objFolder.Compress
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
</dt> <dt>

[**Uncompress**](uncompress-method-in-class-win32-directory.md)
</dt> </dl>

 

