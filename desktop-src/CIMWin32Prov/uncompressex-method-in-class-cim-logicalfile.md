---
description: Uncompresses the logical file (or directory) specified in the object path. This method is an extended version of the Uncompress method.
ms.assetid: 383475ba-77d4-4bfb-a241-9c37aa594a1e
ms.tgt_platform: multiple
title: UncompressEx method of the CIM_LogicalFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_LogicalFile.UncompressEx
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# UncompressEx method of the CIM\_LogicalFile class

The **UncompressEx** method uncompresses the logical file (or directory) specified in the object path. This method is an extended version of the [**Uncompress**](uncompress-method-in-class-cim-logicalfile.md) method.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 UncompressEx(
  [out]          string  StopFileName,
  [in, optional] string  StartFileName,
  [in, optional] boolean Recursive
);
```



## Parameters

<dl> <dt>

*StopFileName* \[out\]
</dt> <dd>

Name of the file (or directory) where the method failed. This parameter is **null** if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

Name of the child file (or directory) to use as a starting point for the method. Typically, this parameter is the *StopFileName* parameter specifying the file or directory at which an error occurred from the previous method call. If this parameter is **null**, the operation is performed on the file or directory specified in the [**ExecMethod**](/windows/desktop/WmiSdk/swbemservices-execmethod) call.

</dd> <dt>

*Recursive* \[in, optional\]
</dt> <dd>

If **TRUE**, the method is also applied recursively to files and directories within the directory specified by the [**CIM\_LogicalFile**](cim-logicalfile.md) instance. For file instances, this parameter is ignored.

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error.

<dl> <dt>

**Success**
</dt> <dd>

0

Success.

</dd> <dt>

**Access Denied**
</dt> <dd>

2

Access denied.

</dd> <dt>

**Unspecified failure**
</dt> <dd>

8

Unspecified failure.

</dd> <dt>

**Invalid object**
</dt> <dd>

9

Invalid object.

</dd> <dt>

**Object already exists**
</dt> <dd>

10

Object already exists.

</dd> <dt>

**File system not NTFS**
</dt> <dd>

11

File system not NTFS.

</dd> <dt>

**Platform not NT/Windows 2000**
</dt> <dd>

12

Platform not Windows.

</dd> <dt>

**Drive not the same**
</dt> <dd>

13

Drive not the same.

</dd> <dt>

**Directory not empty**
</dt> <dd>

14

Directory not empty.

</dd> <dt>

**Sharing violation**
</dt> <dd>

15

Sharing violation.

</dd> <dt>

**Invalid start file**
</dt> <dd>

16

Invalid start file.

</dd> <dt>

**Privilege not held**
</dt> <dd>

17

Privilege not held.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

Invalid parameter.

</dd> </dl>

## Remarks

This method is currently not implemented by WMI. To use this method, you must implement it in your own provider.

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

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

[CIM\_LogicalFile](uncompressex-method-in-class-cim-logicalfile.md)
</dt> <dt>

[**CIM\_LogicalFile**](cim-logicalfile.md)
</dt> </dl>

 

