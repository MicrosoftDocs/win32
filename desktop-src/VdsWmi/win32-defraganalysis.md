---
title: Win32\_DefragAnalysis class
description: The Win32\_DefragAnalysis class represents fragmentation values on a volume.
ms.assetid: 90f26c7d-e54f-4abc-a5e8-3dba859a92be
keywords:
- Win32_DefragAnalysis class
- Win32_DefragAnalysis class, described
topic_type:
- apiref
api_name:
- Win32_DefragAnalysis
- Win32_DefragAnalysis.AverageFileSize
- Win32_DefragAnalysis.AverageFragmentsPerFile
- Win32_DefragAnalysis.AverageFreeSpacePerExtent
- Win32_DefragAnalysis.ClusterSize
- Win32_DefragAnalysis.ExcessFolderFragments
- Win32_DefragAnalysis.FilePercentFragmentation
- Win32_DefragAnalysis.FragmentedFolders
- Win32_DefragAnalysis.FreeSpace
- Win32_DefragAnalysis.FreeSpacePercent
- Win32_DefragAnalysis.FreeSpacePercentFragmentation
- Win32_DefragAnalysis.LargestFreeSpaceExtent
- Win32_DefragAnalysis.MFTPercentInUse
- Win32_DefragAnalysis.MFTRecordCount
- Win32_DefragAnalysis.PageFileSize
- Win32_DefragAnalysis.TotalExcessFragments
- Win32_DefragAnalysis.TotalFiles
- Win32_DefragAnalysis.TotalFolders
- Win32_DefragAnalysis.TotalFragmentedFiles
- Win32_DefragAnalysis.TotalFreeSpaceExtents
- Win32_DefragAnalysis.TotalMFTFragments
- Win32_DefragAnalysis.TotalPageFileFragments
- Win32_DefragAnalysis.TotalPercentFragmentation
- Win32_DefragAnalysis.TotalUnmoveableFiles
- Win32_DefragAnalysis.UsedSpace
- Win32_DefragAnalysis.VolumeName
- Win32_DefragAnalysis.VolumeSize
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

# Win32\_DefragAnalysis class

The **Win32\_DefragAnalysis** class represents fragmentation values on a volume. An instance of the **Win32\_DefragAnalysis** class is passed as an out parameter from the [**Win32\_Volume**](win32-volume.md) methods [**DefragAnalysis**](defraganalysis-method-in-class-win32-volume.md) and [**Defrag**](defrag-method-in-class-win32-volume.md).

**Windows XP:** This class is not available.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class Win32_DefragAnalysis
{
  uint64 AverageFileSize;
  real64 AverageFragmentsPerFile;
  real64 AverageFreeSpacePerExtent;
  uint64 ClusterSize;
  uint64 ExcessFolderFragments;
  uint32 FilePercentFragmentation;
  uint64 FragmentedFolders;
  uint64 FreeSpace;
  uint32 FreeSpacePercent;
  uint32 FreeSpacePercentFragmentation;
  uint64 LargestFreeSpaceExtent;
  uint32 MFTPercentInUse;
  uint64 MFTRecordCount;
  uint64 PageFileSize;
  uint64 TotalExcessFragments;
  uint64 TotalFiles;
  uint64 TotalFolders;
  uint64 TotalFragmentedFiles;
  uint64 TotalFreeSpaceExtents;
  uint64 TotalMFTFragments;
  uint64 TotalPageFileFragments;
  uint32 TotalPercentFragmentation;
  uint64 TotalUnmoveableFiles;
  uint64 UsedSpace;
  string VolumeName;
  uint64 VolumeSize;
};
```

## Members

The **Win32\_DefragAnalysis** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_DefragAnalysis** class has these properties.

<dl> <dt>

**AverageFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Average size of the files on a volume in bytes.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**AverageFragmentsPerFile**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Average number of fragments per file on a volume.

</dd> <dt>

**AverageFreeSpacePerExtent**
</dt> <dd> <dl> <dt>

Data type: **real64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Average size of free space extents on the volume.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**ClusterSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size, in bytes, of the file system allocation unit.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**ExcessFolderFragments**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of excess folder fragments on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**FilePercentFragmentation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of files on a volume that are fragmented.

</dd> <dt>

**FragmentedFolders**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of fragmented folders (subdirectories) on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes currently available for use on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**FreeSpacePercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percent of volume that is free space.

</dd> <dt>

**FreeSpacePercentFragmentation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is no longer available for use as of Windows Vista. Instead, use **AverageFreeSpacePerExtent**, **LargestFreeSpaceExtent**, and **TotalFreeSpaceExtents** to determine the free space fragmentation state of a volume.

**Windows Server 2003:** Percentage of free space on a volume that is fragmented. Be aware that this value may not be computed reliably and that the value may be very close to zero.

</dd> <dt>

**LargestFreeSpaceExtent**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Size of the largest free space extent on the volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

**Windows Server 2003:** This property is not available.

</dd> <dt>

**MFTPercentInUse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Percentage of the Master File Table that is in use.

</dd> <dt>

**MFTRecordCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of records in the Master File Table on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**PageFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is no longer available for use as of Windows Vista. The value is always zero and there is no substitute property to use in this class.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

**Windows Server 2003:** Size of a page file on a volume, in bytes. If there is no page file on a volume, this property is **NULL**.

</dd> <dt>

**TotalExcessFragments**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of excess file fragments on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalFiles**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of files on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalFolders**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of folders (subdirectories) on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalFragmentedFiles**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of fragmented files on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalFreeSpaceExtents**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of free space extents on the volume.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**TotalMFTFragments**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of Master File Table fragments on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalPageFileFragments**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is no longer available for use as of Windows Vista. The value is always zero and there is no substitute property to use in this class.

**Windows Server 2003:** Number of fragments for a page file. If there is no page file on a volume, this property is **NULL**.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**TotalPercentFragmentation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is no longer available for use as of Windows Vista. Instead, use **FilePercentFragmentation** to determine whether the volume should be defragmented. The **AverageFreeSpacePerExtent**, **LargestFreeSpaceExtent**, and **TotalFreeSpaceExtents** properties report the free space fragmentation state of the volume.

**Windows Server 2003:** Percent of the volume that is fragmented. Be aware that this field is computed as the average of **FreeSpacePercentFragmentation** and **FilePercentFragmentation** and may be inaccurate because **FreeSpacePercentFragmentation** is inaccurate.

</dd> <dt>

**TotalUnmoveableFiles**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total number of immovable files on the volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

**Windows Server 2003:** This property is not available.

</dd> <dt>

**UsedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of bytes currently used on a volume.

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/windows/desktop/aa393262).

</dd> <dt>

**VolumeName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the volume for which this report is generated. This property can be the drive letter, mount point, or the volume GUID name.

</dd> <dt>

**VolumeSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Total size of a volume in bytes.

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

[**Win32\_VolumeUserQuota**](win32-volumeuserquota.md)
</dt> <dt>

[**Win32\_MountPoint**](win32-mountpoint.md)
</dt> </dl>

 

 





