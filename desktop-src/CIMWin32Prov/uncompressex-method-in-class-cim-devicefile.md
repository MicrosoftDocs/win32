---
description: Uncompresses the logical device file (or directory) specified in the object path. This method is an extended version of the Uncompress method. This method is inherited from CIM\_LogicalFile.
ms.assetid: dfa53b75-56ef-4119-83b9-08b4371762c6
ms.tgt_platform: multiple
title: UncompressEx method of the CIM_DeviceFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DeviceFile.UncompressEx
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# UncompressEx method of the CIM\_DeviceFile class

The **UncompressEx** method uncompresses the logical device file (or directory) specified in the object path. This method is an extended version of the [**Uncompress**](uncompress-method-in-class-cim-devicefile.md) method. This method is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 UncompressEx(
  [out] string REF StopFileName,
  [in]  string     StartFileName,
  [in]  boolean    Recursive
);
```



## Parameters

<dl> <dt>

*StopFileName* \[out\]
</dt> <dd>

String that represent the name of the file (or directory) where the method failed. This parameter is **null** if the method succeeds.

</dd> <dt>

*StartFileName* \[in\]
</dt> <dd>

String that represents the child file (or directory) to use as a starting point for the method. Typically, the *StartFileName* parameter is the *StopFileName* parameter specifying the file or directory at which an error occurred from the previous method call. If this parameter is **NULL**, the operation is performed on the file or directory specified in the [**ExecMethod**](/windows/desktop/WmiSdk/swbemservices-execmethod) call.

</dd> <dt>

*Recursive* \[in\]
</dt> <dd>

If **TRUE**, this method is also applied recursively to files and directories within the directory specified by the [**CIM\_DeviceFile**](cim-devicefile.md) instance. For file instances, this parameter is ignored.

</dd> </dl>

## Return value

Returns a value of 0 on success, and any other number to indicate an error.

<dl> <dt>


</dt> <dd>

0

Success.

</dd> <dt>


</dt> <dd>

2

Access denied.

</dd> <dt>


</dt> <dd>

8

Unspecified failure.

</dd> <dt>


</dt> <dd>

9

Invalid object.

</dd> <dt>


</dt> <dd>

10

Object already exists.

</dd> <dt>


</dt> <dd>

11

File system not NTFS.

</dd> <dt>


</dt> <dd>

12

Platform not Windows.

</dd> <dt>


</dt> <dd>

13

Drive not the same.

</dd> <dt>


</dt> <dd>

14

Directory not empty.

</dd> <dt>


</dt> <dd>

15

Sharing violation.

</dd> <dt>


</dt> <dd>

16

Invalid start file.

</dd> <dt>


</dt> <dd>

17

Privilege not held.

</dd> <dt>


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

[CIM\_DeviceFile](uncompressex-method-in-class-cim-devicefile.md)
</dt> <dt>

[**CIM\_DeviceFile**](cim-devicefile.md)
</dt> </dl>

 

