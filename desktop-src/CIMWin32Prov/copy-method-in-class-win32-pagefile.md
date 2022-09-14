---
description: Copies the logical paging file or directory specified in the object path to the location specified by the input parameter.
ms.assetid: e1ff3e91-dc30-4849-b80a-8838b527ad63
ms.tgt_platform: multiple
title: Copy method of the Win32_PageFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_PageFile.Copy
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Copy method of the Win32\_PageFile class

The **Copy** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method copies the logical paging file or directory specified in the object path to the location specified by the input parameter. A copy is not supported if overwriting an existing logical file is required.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Copy(
  [in] string FileName
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Fully qualified name of the copy of the file (or directory).

Example: c:\\temp\\newdirectory

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

[**Win32\_PageFile**](win32-pagefile.md)
</dt> </dl>

 

