---
Description: Uncompresses the logical codec file (or directory) specified in the object path.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: abe74267-1274-4b20-82ac-51ca94d7af33
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Uncompress method of the Win32\_CodecFile class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Uncompress method of the Win32\_CodecFile class

The **Uncompress** [WMI class](https://msdn.microsoft.com/library/aa393244) method uncompresses the logical codec file (or directory) specified in the object path.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Uncompress();
```



## Parameters

This method has no parameters.

## Return value

Returns an integer value of 0 (zero) if the file was successfully decompressed, and any other number to indicate an error.

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



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_CodecFile**](win32-codecfile.md)
</dt> </dl>

 

 




