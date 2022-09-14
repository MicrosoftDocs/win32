---
description: The DeleteEx method deletes the logical file (or directory) specified in the object path. This method is an extended version of the Delete method.
ms.assetid: 53785f2e-8796-446c-8228-9abc2d9a0d68
ms.tgt_platform: multiple
title: DeleteEx method of the CIM_LogicalFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_LogicalFile.DeleteEx
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# DeleteEx method of the CIM\_LogicalFile class

The **DeleteEx** method deletes the logical file (or directory) specified in the object path. This method is an extended version of the [**Delete**](delete-method-in-class-cim-logicalfile.md) method.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

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

String that represents the name of the file (or directory) where the method failed. This parameter is null if the method succeeds.

</dd> <dt>

*StartFileName* \[in, optional\]
</dt> <dd>

String that names the child file (or directory) to use as a starting point for the method. Typically, this parameter is the *StopFileName* parameter specifying the file or directory at which an error occurred from the previous method call. If this parameter is null, the operation is performed on the file or directory specified in the [**ExecMethod**](/windows/desktop/WmiSdk/swbemservices-execmethod) call.

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

[CIM\_LogicalFile](deleteex-method-in-class-cim-logicalfile.md)
</dt> <dt>

[**CIM\_LogicalFile**](cim-logicalfile.md)
</dt> </dl>

 

