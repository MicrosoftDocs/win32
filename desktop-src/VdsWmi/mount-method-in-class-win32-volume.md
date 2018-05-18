---
title: Mount method of the Win32\_Volume class
description: The Mount method mounts a file system on the volume.This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see Calling a Method.
ms.assetid: 'f1a3cd65-97e5-406f-9df4-44752af6b868'
keywords: ["Mount method", "Mount method, Win32_Volume class", "Win32_Volume class, Mount method"]
topic_type:
- apiref
api_name:
- Win32_Volume.Mount
api_location:
- Vdswmi.dll
api_type:
- COM
---

# Mount method of the Win32\_Volume class

The **Mount** method mounts a file system on the volume.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Mount();
```



## Parameters

This method has no parameters.

## Return value



| Return code                                                                      | Description              |
|----------------------------------------------------------------------------------|--------------------------|
| <dl> <dt>**0**</dt> </dl> | Success<br/>       |
| <dl> <dt>**1**</dt> </dl> | Access Denied<br/> |
| <dl> <dt>**2**</dt> </dl> | Unknown Error<br/> |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| Header<br/>                   | <dl> <dt>Vds.h</dt> </dl>      |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





