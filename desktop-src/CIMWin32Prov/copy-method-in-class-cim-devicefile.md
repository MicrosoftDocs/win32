---
description: Copy method of the CIM_DeviceFile class - The Copy method copies the logical file (or directory) specified in the object path to the location specified by the input parameter.
ms.assetid: 6c1c6172-80a2-4779-903a-935f8c7091a5
ms.tgt_platform: multiple
title: Copy method of the CIM_DeviceFile class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_DeviceFile.Copy
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Copy method of the CIM\_DeviceFile class

The **Copy** method copies the logical file (or directory) specified in the object path to the location specified by the input parameter. A copy is not supported if it requires overwriting an existing logical file. This method is inherited from [**CIM\_LogicalFile**](cim-logicalfile.md).

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

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

Fully qualified name of the destination file (or directory) copy.

Example: "c:\\temp\\newdirectory"

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error.

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

[CIM\_DeviceFile](copy-method-in-class-cim-devicefile.md)
</dt> <dt>

[**CIM\_DeviceFile**](cim-devicefile.md)
</dt> </dl>

 

