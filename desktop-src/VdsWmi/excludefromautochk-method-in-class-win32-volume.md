---
title: ExcludeFromAutoChk method of the Win32\_Volume class
description: The ExcludeFromAutoChk method excludes volumes from the Chkdsk operation to be run at the next reboot.If not excluded, Chkdsk is performed on the volume if the dirty bit is set for the disk.
ms.assetid: 264e2c98-1689-4dd1-b0df-85381936c9b3
keywords:
- ExcludeFromAutoChk method
- ExcludeFromAutoChk method, Win32_Volume class
- Win32_Volume class, ExcludeFromAutoChk method
topic_type:
- apiref
api_name:
- Win32_Volume.ExcludeFromAutoChk
api_location:
- Vdswmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ExcludeFromAutoChk method of the Win32\_Volume class

The **ExcludeFromAutoChk** method excludes volumes from the Chkdsk operation to be run at the next reboot.

If not excluded, [**Chkdsk**](chkdsk-method-in-class-win32-volume.md) is performed on the volume if the dirty bit is set for the disk.

> [!Note]  
> Calls to exclude volumes are not cumulative. That is, if a call is made to exclude some volumes, then a new list is not added to the list of volumes that were already marked for exclusion. The new list overwrites the previous list.

 

This method is applicable to only the volume instances that represent a physical disk, and is not applicable to mapped logical drives.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ExcludeFromAutoChk(
  [in] string Volume[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

List of volumes that are excluded from AutoChk at the next reboot. The string consists of the drive letter followed by a colon for the logical disk.

Example: "C:"

</dd> </dl>

## Return value



| Return code                                                                      | Description                         |
|----------------------------------------------------------------------------------|-------------------------------------|
| <dl> <dt>**0**</dt> </dl> | Success<br/>                  |
| <dl> <dt>**1**</dt> </dl> | Remote Drive<br/>             |
| <dl> <dt>**2**</dt> </dl> | Removable Drive<br/>          |
| <dl> <dt>**3**</dt> </dl> | Drive Not Root Directory<br/> |
| <dl> <dt>**4**</dt> </dl> | Unknown Drive<br/>            |



 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





