---
title: Win32\_VolumeUserQuota class
description: The Win32\_VolumeUserQuota association class relates per user quotas to quota enabled volumes.
ms.assetid: 7533ebf3-d552-4140-933d-3c81d722f680
keywords:
- Win32_VolumeUserQuota class
- Win32_VolumeUserQuota class, described
topic_type:
- apiref
api_name:
- Win32_VolumeUserQuota
- Win32_VolumeUserQuota.Account
- Win32_VolumeUserQuota.DiskSpaceUsed
- Win32_VolumeUserQuota.Status
- Win32_VolumeUserQuota.Limit
- Win32_VolumeUserQuota.Volume
- Win32_VolumeUserQuota.WarningLimit
api_location:
- Vdswmi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_VolumeUserQuota class

The **Win32\_VolumeUserQuota** association class relates per user quotas to quota-enabled volumes. A system administrator can configure Windows to prevent disk space use that is more than a user's quota, and then log an event when a user exceeds the specified disk space limit. A system administrator can also log an event when a user exceeds a specified disk space warning level. A disk quota cannot be set for an administrator account.

**Windows XP and earlier:** This class is not available.

The following syntax is simplified from Managed Object format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_VolumeUserQuota
{
  Win32_Account REF Account;
  uint64            DiskSpaceUsed;
  uint32            Status;
  uint64            Limit;
  Win32_Volume  REF Volume;
  uint64            WarningLimit;
};
```

## Members

The **Win32\_VolumeUserQuota** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_VolumeUserQuota** class has these properties.

<dl> <dt>

**Account**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Account**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to the volume.

</dd> <dt>

**DiskSpaceUsed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Number of bytes that a user or group is using.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Limit set for this user or group in bytes.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Status of a disk quota.

The following table lists the possible values.



| Value                                                                        | Meaning             |
|------------------------------------------------------------------------------|---------------------|
| <dl> <dt>0</dt> </dl> | OK<br/>       |
| <dl> <dt>1</dt> </dl> | Warning<br/>  |
| <dl> <dt>2</dt> </dl> | Exceeded<br/> |



 

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

Reference to a volume.

</dd> <dt>

**WarningLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (Bytes)
</dt> </dl>

Number of bytes a user or group can use before receiving a warning.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

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

[Storage Volume Provider](storage-volume-provider.md)
</dt> <dt>

[**Win32\_Volume**](win32-volume.md)
</dt> <dt>

[**Win32\_VolumeQuota**](win32-volumequota.md)
</dt> <dt>

[**Win32\_DefragAnalysis**](win32-defraganalysis.md)
</dt> <dt>

[**Win32\_MountPoint**](win32-mountpoint.md)
</dt> </dl>

 

 





