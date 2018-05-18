---
title: Dismount method of the Win32\_Volume class
description: The Dismount method dismounts a file system from a volume.This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see Calling a Method.
ms.assetid: 'f1a3cd65-97e5-406f-9df4-44752af6b868'
keywords: ["Dismount method", "Dismount method, Win32_Volume class", "Win32_Volume class, Dismount method"]
topic_type:
- apiref
api_name:
- Win32_Volume.Dismount
api_location:
- Vdswmi.dll
api_type:
- COM
---

# Dismount method of the Win32\_Volume class

The **Dismount** method dismounts a file system from a volume.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 Dismount(
  [in] boolean Force = FALSE,
  [in] boolean Permanent = FALSE
);
```



## Parameters

<dl> <dt>

*Force* \[in\]
</dt> <dd>

If **true**, the volume is dismounted even if there are open handles. The default is **false**.

</dd> <dt>

*Permanent* \[in\]
</dt> <dd>

If **true**, the volume is dismounted to a no-automount, offline state. The volume may be returned to the automount state by explicitly calling the [**Mount**](mount-method-in-class-win32-volume.md) method, or by creating a mount point for the volume. The default is **false**.

</dd> </dl>

## Return value



| Return code                                                                      | Description                                                 |
|----------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**0**</dt> </dl> | Success<br/>                                          |
| <dl> <dt>**1**</dt> </dl> | Access Denied<br/>                                    |
| <dl> <dt>**2**</dt> </dl> | Volume Has Mount Points<br/>                          |
| <dl> <dt>**3**</dt> </dl> | Volume Does Not Support The No-Autoremount State<br/> |
| <dl> <dt>**4**</dt> </dl> | Force Option Required<br/>                            |



 

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

 

 





