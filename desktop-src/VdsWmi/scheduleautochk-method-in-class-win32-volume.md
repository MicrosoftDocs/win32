---
title: ScheduleAutoChk method of the Win32\_Volume class
description: Schedules AutoChk to be run at the next reboot if the volume's dirty bit has been set.
ms.assetid: '15acca0b-c009-4355-8132-cdcd335675d6'
keywords: ["ScheduleAutoChk method", "ScheduleAutoChk method, Win32_Volume class", "Win32_Volume class, ScheduleAutoChk method"]
topic_type:
- apiref
api_name:
- Win32_Volume.ScheduleAutoChk
api_location:
- Vdswmi.dll
api_type:
- COM
---

# ScheduleAutoChk method of the Win32\_Volume class

The **ScheduleAutoChk** method schedules AutoChk to be run at the next reboot if the volume's dirty bit has been set. The method is only applicable to those volume instances that represent a physical disk. It is not applicable to mapped logical drives.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ScheduleAutoChk(
  [in] string Volume[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

List of volumes scheduled for AutoChk at the next reboot. The string consists of the drive letter, mount point name, or volume globally unique identifier (GUID) name.

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
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Vds.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>Vdswmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> </dl>

 

 





