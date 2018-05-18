---
title: Win32\_DiskQuota class
description: The Win32\_DiskQuota association WMI class tracks disk space usage for NTFS file system volumes.
ms.assetid: '713f0641-00e7-41a4-a2d4-ecf7ef00e8cf'
keywords: ["Win32_DiskQuota class", "Win32_DiskQuota class, described"]
topic_type:
- apiref
api_name:
- Win32_DiskQuota
- Win32_DiskQuota.DiskSpaceUsed
- Win32_DiskQuota.Limit
- Win32_DiskQuota.QuotaVolume
- Win32_DiskQuota.Status
- Win32_DiskQuota.User
- Win32_DiskQuota.WarningLimit
api_location:
- Wmipdskq.dll
api_type:
- DllExport
---

# Win32\_DiskQuota class

The **Win32\_DiskQuota** association [WMI class](https://msdn.microsoft.com/library/aa393244) tracks disk space usage for NTFS file system volumes. A system administrator (SA) can configure Windows to prevent further disk space use, and log an event when a user exceeds a specified disk space limit. An SA can also log an event when a user exceeds a specified disk space warning level. This class is new in Windows XP.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_DiskQuota
{
  uint64                DiskSpaceUsed;
  uint64                Limit;
  Win32_LogicalDisk REF QuotaVolume;
  uint32                Status;
  Win32_Account     REF User;
  uint64                WarningLimit;
};
```

## Members

The **Win32\_DiskQuota** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DiskQuota** class has these properties.

<dl> <dt>

**DiskSpaceUsed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (bytes)
</dt> </dl>

Number of bytes currently in use by this particular user or group.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**Limit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (bytes)
</dt> </dl>

Limit set for this particular user or group.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**QuotaVolume**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalDisk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing disk quotas.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the disk quota.

The values are:



| Value                                                                        | Meaning               |
|------------------------------------------------------------------------------|-----------------------|
| <dl> <dt>0</dt> </dl> | "OK"<br/>       |
| <dl> <dt>1</dt> </dl> | "Warning"<br/>  |
| <dl> <dt>2</dt> </dl> | "Exceeded"<br/> |



 

</dd> <dt>

**User**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Account**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reference to the instance representing the user account associated with a disk quota.

</dd> <dt>

**WarningLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) (bytes)
</dt> </dl>

Warning limit set for this particular user or group.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Wmipdskq.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wmipdskq.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 





