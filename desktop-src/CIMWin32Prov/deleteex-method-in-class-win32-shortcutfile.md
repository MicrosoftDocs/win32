---
description: Deletes the logical shortcut file (or directory) specified in the object path.
ms.assetid: 278cd856-bb8d-4494-b43c-f0858366e136
ms.tgt_platform: multiple
title: DeleteEx method of the Win32_ShortcutFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ShortcutFile.DeleteEx
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# DeleteEx method of the Win32\_ShortcutFile class

The **DeleteEx** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method deletes the logical shortcut file (or directory) specified in the object path. **DeleteEx** is an extended version of the [**Delete**](delete-method-in-class-win32-directory.md) method.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 DeleteEx(
  [out]          string StopFileName,
  [in, optional] string StartFileName
);
```



## Parameters

<dl> <dt>

*StopFileName* \[out\]
</dt> <dd>

Name of the file or directory where the **DeleteEx** method failed. This parameter is **null** if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

Names the child file or directory to use as a starting point for **DeleteEx**. The *StartFileName* parameter is typically the *StopFileName* parameter that specifies the file or directory at which an error occurred from the previous method call. If this parameter is **NULL**, the operation is performed on the file or directory specified in the ExecMethod call.

</dd> </dl>

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

[**Win32\_ShortcutFile**](win32-shortcutfile.md)
</dt> </dl>

 

