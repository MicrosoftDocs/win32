---
title: Win32\_MountPoint class
description: The Win32\_MountPoint class associates a volume to the directory where it is mounted.
ms.assetid: 7961d062-d3d1-47a0-8d85-68da4080ed7a
keywords:
- Win32_MountPoint class
- Win32_MountPoint class, described
topic_type:
- apiref
api_name:
- Win32_MountPoint
- Win32_MountPoint.Directory
- Win32_MountPoint.Volume
api_location:
- Vdswmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_MountPoint class

The **Win32\_MountPoint** class associates a volume to the directory where it is mounted.

**Windows XP and earlier:** This class is not available.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_MountPoint
{
  Win32_Directory REF Directory;
  Win32_Volume    REF Volume;
};
```

## Members

The **Win32\_MountPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_MountPoint** class has these properties.

<dl> <dt>

**Directory**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Directory**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the directory where the volume is mounted.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Volume**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the mounted volume.

</dd> </dl>

## Remarks

There may not be any way to search from Win32\_MountPoint to get to the associated Win32\_DiskDrive; such a combination is only possible with a drive letter mount. Instead, you can use the IOCTL\_STORAGE\_GET\_DEVICE\_NUMBER ioctl, to query the list of disks/partitions for a certain volume (and viceversa). For more information, see [here](http://blogs.msdn.com/b/adioltean/archive/2005/05/04/414806.aspx).

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

[**Win32\_VolumeUserQuota**](win32-volumeuserquota.md)
</dt> <dt>

[**Win32\_DefragAnalysis**](win32-defraganalysis.md)
</dt> </dl>

 

 





