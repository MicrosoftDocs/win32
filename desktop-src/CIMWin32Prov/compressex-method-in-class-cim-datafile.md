---
Description: 'Uses NTFS compression to compress the logical file (or directory) that is specified in the object path. This method is inherited from CIM\_LogicalFile.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '553b6a90-d16c-4abb-9015-66fe8e1606f6'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'CompressEx method of the CIM\_DataFile class'
---

# CompressEx method of the CIM\_DataFile class

The **CompressEx** method uses NTFS compression to compress the logical file (or directory) that is specified in the object path. This method is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md). This method is an extended version of the [**Compress**](compress-method-in-class-cim-datafile.md) method and is inherited from [CIM\_LogicalFile](https://msdn.microsoft.com/library/aa384832).

> \[!Important\]  
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](Http://Go.Microsoft.Com/FWLink/p/?LinkID=309367).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 CompressEx(
  [out] string  StopFileName,
  [in]  string  StartFileName,
  [in]  boolean Recursive
);
```



## Parameters

<dl> <dt>

*StopFileName* \[out\]
</dt> <dd>

String that represents the name of the file (or directory) where the method failed. This parameter is null if the method succeeds.

</dd> <dt>

*StartFileName* \[in\]
</dt> <dd>

String that represents the child file (or directory) to use as a starting point for this method. Typically, the *StartFileName* parameter is the *StopFileName* parameter that specifies the file or directory at which an error occurred from the previous method call. If this parameter is null, the operation is performed on the file or directory specified in the **ExecMethod** call.

If *StartFileName* is used, *Recursive* must be set to true as well.

</dd> <dt>

*Recursive* \[in\]
</dt> <dd>

If **TRUE**, the method is also applied recursively to files and directories within the directory specified by the [**CIM\_DataFile**](cim-datafile.md) instance. For file instances, this parameter is ignored.

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**0**
</dt> <dd>

Success.

</dd> <dt>

**2**
</dt> <dd>

Access denied.

</dd> <dt>

**8**
</dt> <dd>

Unspecified failure.

</dd> <dt>

**9**
</dt> <dd>

Invalid object.

</dd> <dt>

**10**
</dt> <dd>

Object already exists.

</dd> <dt>

**11**
</dt> <dd>

File system not NTFS.

</dd> <dt>

**12**
</dt> <dd>

Platform not Windows.

</dd> <dt>

**13**
</dt> <dd>

Drive not the same.

</dd> <dt>

**14**
</dt> <dd>

Directory not empty.

</dd> <dt>

**15**
</dt> <dd>

Sharing violation.

</dd> <dt>

**16**
</dt> <dd>

Invalid start file.

</dd> <dt>

**17**
</dt> <dd>

Privilege not held.

</dd> <dt>

**21**
</dt> <dd>

Invalid parameter.

</dd> </dl>

## Remarks

The **CompressEx** method in [**CIM\_DataFile**](cim-datafile.md) is implemented by WMI.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[CIM\_DataFile](compressex-method-in-class-cim-datafile.md)
</dt> <dt>

[**CIM\_DataFile**](cim-datafile.md)
</dt> <dt>

[WMI Tasks: Files and Folders](https://msdn.microsoft.com/library/aa394594)
</dt> <dt>

[**File and Directory Access Rights Constants**](https://msdn.microsoft.com/library/aa822867)
</dt> </dl>

 

 




