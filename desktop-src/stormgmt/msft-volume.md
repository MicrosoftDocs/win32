---
title: MSFT\_Volume class
description: Represents a volume on a computer.
ms.assetid: '007dd46a-4812-4273-beaa-74fbe9520c7d'
keywords: ["MSFT_Volume class Windows Storage Management API", "MSFT_Volume class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_Volume
- MSFT_Volume.DriveLetter
- MSFT_Volume.Path
- MSFT_Volume.HealthStatus
- MSFT_Volume.FileSystem
- MSFT_Volume.FileSystemLabel
- MSFT_Volume.FileSystemType
- MSFT_Volume.Size
- MSFT_Volume.SizeRemaining
- MSFT_Volume.DriveType
- MSFT_Volume.DedupMode
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_Volume class

Represents a volume on a computer.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_Volume : MSFT_StorageObject
{
  Char16 DriveLetter;
  String Path;
  UInt16 HealthStatus;
  String FileSystem;
  String FileSystemLabel;
  UInt16 FileSystemType;
  UInt64 Size;
  UInt64 SizeRemaining;
  UInt32 DriveType;
  UInt32 DedupMode;
};
```

## Members

The **MSFT\_Volume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_Volume** class has these methods.



| Method                                                                   | Description                                                                       |
|:-------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**DeleteObject**](msft-volume-deleteobject.md)                         | Deletes the volume.<br/>                                                    |
| [**Diagnose**](msft-volume-diagnose.md)                                 | Performs a diagnostic on the volume, returning any actionable results.<br/> |
| [**Flush**](msft-volume-flush.md)                                       | Flushes the cached data in the volume's file system to disk.<br/>           |
| [**Format**](format-msft-volume.md)                                     | Formats the volume.<br/>                                                    |
| [**GetAttributes**](msft-volume-getattributes.md)                       | Retrieves the volume attributes.<br/>                                       |
| [**GetCorruptionCount**](msft-volume-getcorruptioncount.md)             | Retrieves the corruption count for the volume.<br/>                         |
| [**GetDedupProperties**](msft-volume-getdeduplicationstatistics.md)     | Gets deduplication properties of the volume.<br/>                           |
| [**GetSupportedClusterSizes**](msft-volume-getsupportedclustersizes.md) | Retrieves the supported cluster sizes for the volume.<br/>                  |
| [**GetSupportedFileSystems**](msft-volume-getsupportedfilesystems.md)   | Retrieves the names of file systems that are supported on the volume.<br/>  |
| [**Optimize**](optimize-msft-volume.md)                                 | Optimizes the volume.<br/>                                                  |
| [**Repair**](repair-msft-volume.md)                                     | Repairs the volume.<br/>                                                    |
| [**Resize**](msft-volume-resize.md)                                     | Resizes the volume.<br/>                                                    |
| [**SetAttributes**](msft-volume-setattributes.md)                       | Sets or changes the volume attributes.<br/>                                 |
| [**SetDedupMode**](msft-volume-setdeduplication.md)                     | Enables or disables deduplication on the volume.<br/>                       |
| [**SetFileSystemLabel**](msft-volume-setfilesystemlabel.md)             | Sets the file system label for the volume.<br/>                             |



 

### Properties

The **MSFT\_Volume** class has these properties.

<dl> <dt>

**DedupMode**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** Indicates whether deduplication is available, disabled, or the deduplication mode of the volume.

<dl> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)
</dt> <dt>

<span id="GeneralPurpose"></span><span id="generalpurpose"></span><span id="GENERALPURPOSE"></span>**GeneralPurpose** (1)
</dt> <dt>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)
</dt> <dt>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)
</dt> <dt>

<span id="NotAvailable"></span><span id="notavailable"></span><span id="NOTAVAILABLE"></span>**NotAvailable** (4)
</dt> </dl>

</dd> <dt>

**DriveLetter**
</dt> <dd> <dl> <dt>

Data type: **Char16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume drive letter.

</dd> <dt>

**DriveType**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the volume.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Invalid_Root_Path"></span><span id="invalid_root_path"></span><span id="INVALID_ROOT_PATH"></span>**Invalid Root Path** (1)
</dt> <dt>

<span id="Removable"></span><span id="removable"></span><span id="REMOVABLE"></span>**Removable** (2)
</dt> <dt>

<span id="Fixed"></span><span id="fixed"></span><span id="FIXED"></span>**Fixed** (3)
</dt> <dt>

<span id="Remote"></span><span id="remote"></span><span id="REMOTE"></span>**Remote** (4)
</dt> <dt>

<span id="CD-ROM"></span><span id="cd-rom"></span>**CD-ROM** (5)
</dt> <dt>

<span id="RAM_Disk"></span><span id="ram_disk"></span><span id="RAM_DISK"></span>**RAM Disk** (6)
</dt> </dl>

</dd> <dt>

**FileSystem**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume's file system. One of the following:

-   "NTFS"
-   "ReFS"
-   "FAT32"
-   "CSVFS"

</dd> <dt>

**FileSystemLabel**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The volume's file system label.

</dd> <dt>

**FileSystemType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**Starting in Windows 10:** The underlying file system on the volume. It can have one of the following values:

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

 (Threshold)
</dt> <dt>

<span id="UFS"></span><span id="ufs"></span>**UFS** (2)
</dt> <dt>

<span id="HFS"></span><span id="hfs"></span>**HFS** (3)
</dt> <dt>

<span id="FAT"></span><span id="fat"></span>**FAT** (4)
</dt> <dt>

<span id="FAT16"></span><span id="fat16"></span>**FAT16** (5)
</dt> <dt>

<span id="FAT32"></span><span id="fat32"></span>**FAT32** (6)
</dt> <dt>

<span id="NTFS4"></span><span id="ntfs4"></span>**NTFS4** (7)
</dt> <dt>

<span id="NTFS5"></span><span id="ntfs5"></span>**NTFS5** (8)
</dt> <dt>

<span id="XFS"></span><span id="xfs"></span>**XFS** (9)
</dt> <dt>

<span id="AFS"></span><span id="afs"></span>**AFS** (10)
</dt> <dt>

<span id="EXT2"></span><span id="ext2"></span>**EXT2** (11)
</dt> <dt>

<span id="EXT3"></span><span id="ext3"></span>**EXT3** (12)
</dt> <dt>

<span id="ReiserFS"></span><span id="reiserfs"></span><span id="REISERFS"></span>**ReiserFS** (13)
</dt> <dt>

<span id="NTFS"></span><span id="ntfs"></span>**NTFS** (14)
</dt> <dt>

<span id="ReFS"></span><span id="refs"></span><span id="REFS"></span>**ReFS** (15)
</dt> <dt>

<span id="CSVFS_NTFS"></span><span id="csvfs_ntfs"></span>**CSVFS\_NTFS** (0x8000)
</dt> <dt>

<span id="CSVFS_ReFS"></span><span id="csvfs_refs"></span><span id="CSVFS_REFS"></span>**CSVFS\_ReFS** (0x8001)
</dt> </dl>

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the volume.

<dl> <dt>

<span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span>**Healthy** (0)
</dt> <dt>

<span id="Scan_Needed"></span><span id="scan_needed"></span><span id="SCAN_NEEDED"></span>**Scan Needed** (1)
</dt> <dt>

<span id="Spot_Fix_Needed"></span><span id="spot_fix_needed"></span><span id="SPOT_FIX_NEEDED"></span>**Spot Fix Needed** (2)
</dt> <dt>

<span id="Full_Repair_Needed"></span><span id="full_repair_needed"></span><span id="FULL_REPAIR_NEEDED"></span>**Full Repair Needed** (3 )
</dt> </dl>

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The volume path.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

Total size, in bytes, of the volume.

</dd> <dt>

**SizeRemaining**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bytes")
</dt> </dl>

The total space, in bytes, that is currently free on the volume.

</dd> </dl>

## Remarks

**Starting in Windows 10:** **MSFT\_Volume** derives from [**MSFT\_StorageObject**](msft-storageobject.md). It now inherits the property *ObjectId*, which was formerly a property of **MSFT\_Volume**.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





