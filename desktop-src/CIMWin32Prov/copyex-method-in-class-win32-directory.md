---
description: Copies the logical directory entry file or directory specified in the object path to the location specified by the FileName parameter. This method is an extended version of the Copy method.
ms.assetid: c15bd1ae-a60d-4875-a76e-99486820c42c
ms.tgt_platform: multiple
title: CopyEx method of the Win32_Directory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Directory.CopyEx
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# CopyEx method of the Win32\_Directory class

The **CopyEx** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method copies the logical directory entry file or directory specified in the object path to the location specified by the *FileName* parameter. This method is an extended version of the [**Copy**](copy-method-in-class-win32-directory.md) method. A copy is not supported if overwriting an existing logical file is required.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 CopyEx(
  [in]           string  FileName,
  [out]          string  StopFileName,
  [in, optional] string  StartFileName,
  [in, optional] boolean Recursive
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Fully qualified name of the copy of the file (or directory). Example: c:\\temp\\newdirectory.

</dd> <dt>

*StopFileName* \[out\]
</dt> <dd>

Name of the file or directory where the **CopyEx** method failed. This parameter will be **null** if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

Names the child file or directory to use as a starting point for **CopyEx**. The *StartFileName* parameter is typically the *StopFileName* parameter specifying the file or directory at which an error occurred from the previous method call. If this parameter is **NULL**, the operation is performed on the file or directory specified in the **ExecMethod** call.

If *StartFileName* is used, *Recursive* must be set to true as well.

</dd> <dt>

*Recursive* \[in, optional\]
</dt> <dd>

If **true**, files and directories will be copied recursively within the directory specified by the [**CIM\_LogicalFile**](cim-logicalfile.md) instance.

> [!Note]  
> For file instances, the *Recursive* input parameter is ignored.

 

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

 

