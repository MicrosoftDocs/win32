---
title: MSFT\_DedupVolume class
description: Represents a volume that has data deduplication metadata.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B8708702-062A-42A7-8AC3-DD9E27E0EC77
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupVolume class Data Deduplication API
- MSFT_DedupVolume class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupVolume
- MSFT_DedupVolume.VolumeId
- MSFT_DedupVolume.Volume
- MSFT_DedupVolume.Enabled
- MSFT_DedupVolume.DataAccessEnabled
- MSFT_DedupVolume.NoCompress
- MSFT_DedupVolume.Verify
- MSFT_DedupVolume.OptimizeInUseFiles
- MSFT_DedupVolume.OptimizePartialFiles
- MSFT_DedupVolume.UsageType
- MSFT_DedupVolume.MinimumFileAgeDays
- MSFT_DedupVolume.MinimumFileSize
- MSFT_DedupVolume.ChunkRedundancyThreshold
- MSFT_DedupVolume.InputOutputScale
- MSFT_DedupVolume.ExcludeFolder
- MSFT_DedupVolume.ExcludeFileType
- MSFT_DedupVolume.ExcludeFileTypeDefault
- MSFT_DedupVolume.NoCompressionFileType
- MSFT_DedupVolume.Capacity
- MSFT_DedupVolume.FreeSpace
- MSFT_DedupVolume.UsedSpace
- MSFT_DedupVolume.UnoptimizedSize
- MSFT_DedupVolume.SavedSpace
- MSFT_DedupVolume.SavingsRate
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_DedupVolume class

Represents a volume that has data deduplication metadata.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupVolume
{
  String  VolumeId;
  String  Volume;
  boolean Enabled;
  boolean DataAccessEnabled;
  boolean NoCompress;
  boolean Verify;
  boolean OptimizeInUseFiles;
  boolean OptimizePartialFiles;
  uint32  UsageType;
  uint32  MinimumFileAgeDays;
  uint32  MinimumFileSize;
  uint32  ChunkRedundancyThreshold;
  uint32  InputOutputScale;
  string  ExcludeFolder[];
  string  ExcludeFileType[];
  string  ExcludeFileTypeDefault[];
  string  NoCompressionFileType[];
  uint64  Capacity;
  uint64  FreeSpace;
  uint64  UsedSpace;
  uint64  UnoptimizedSize;
  uint64  SavedSpace;
  uint32  SavingsRate;
};
```

## Members

The **MSFT\_DedupVolume** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DedupVolume** class has these methods.



| Method                                            | Description                                                                                                                                                                 |
|:--------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Disable**](msft-dedupvolume-disable.md)       | Disables further data deduplication activity on one or more volumes.<br/>                                                                                             |
| [**Enable**](msft-dedupvolume-enable.md)         | Enables deduplication on the specified volumes by using default settings.<br/>                                                                                        |
| [**ExpandFile**](msft-dedupvolume-expandfile.md) | Reverts the deduplication process on a set of deduplicated files.<br/> **Windows Server 2012:** This method is not supported until Windows Server 2012 R2.<br/> |



 

### Properties

The **MSFT\_DedupVolume** class has these properties.

<dl> <dt>

**Capacity**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The capacity of the volume, in bytes.

</dd> <dt>

**ChunkRedundancyThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the number of identical chunks of data that are encountered during deduplication before the server creates a redundant copy of that chunk of data. Adding redundancy to the most referenced chunks of data increases the reliability of the system. Deduplication detects corruptions, and the deduplication scrubbing job restores the corrupted chunks from a redundant copy if available. The default value is 100 for identical chunks before a redundant copy is made. This property cannot be set to less than 20.

</dd> <dt>

**DataAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, data access is enabled.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, deduplication is enabled on this volume.

</dd> <dt>

**ExcludeFileType**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of file name extensions to exclude from data deduplication and optimization.

</dd> <dt>

**ExcludeFileTypeDefault**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Default list of file name extension types to exclude from data deduplication and optimization.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**ExcludeFolder**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of root folders under which all files are skipped during data deduplication and optimization. Full paths are accepted; however, mounted folders are ignored because the mounted folders can change after configuration.

</dd> <dt>

**FreeSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of free space on the volume, in bytes.

</dd> <dt>

**InputOutputScale**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum amount of I/O parallelism to use when optimizing the volume. This value can range from "1" to "36".

**Windows Server 2012 R2 and Windows Server 2012:** This property is not available before Windows Server 2016.

</dd> <dt>

**MinimumFileAgeDays**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Optimizes files that have not been accessed in the specified number of days. If the last access time is not available, then the last modified time is used.

</dd> <dt>

**MinimumFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the minimum size threshold, in bytes, for files to be optimized. Files that do not meet this minimum threshold are not optimized.

</dd> <dt>

**NoCompress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, the data are not to be compressed after deduplication.

</dd> <dt>

**NoCompressionFileType**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The list of file types to exclude from compression. These file types are deduplicated but not compressed, because typically the file format is already compressed.

</dd> <dt>

**OptimizeInUseFiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, files in use are optimized.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**OptimizePartialFiles**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, portions of files that have been modified recently are not optimized. This property is controlled by the **MinimumFileAgeDays** parameter.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

</dd> <dt>

**SavedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Saved space is the difference between the logical size of the optimized files and the logical size of the store, which is the deduplicated user data plus deduplication metadata. Note that this number remains unchanged as users delete files from or add new files to the volume until you run an optimization job or execute the [**Update**](msft-dedupvolumestatus-update.md) method of the [**MSFT\_DedupVolumeStatus**](msft-dedupvolumestatus.md) class. This number is most accurate after an optimization job runs or the **Update** method is executed.

</dd> <dt>

**SavingsRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ratio of saved space from deduplication to the logical size of all of the files on the volume and is expressed as a percentage. Note that this number remains unchanged as users delete files from or add new files to the volume until you run an optimization job or execute the [**Update**](msft-dedupvolumestatus-update.md) method of the [**MSFT\_DedupVolumeStatus**](msft-dedupvolumestatus.md) class. This number is most accurate after an optimization job runs or the **Update** method is executed.

</dd> <dt>

**UnoptimizedSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total logical size of all files on the volume, in bytes. This includes all files, optimized and non-optimized. Note that this number will remain steady as users delete optimized files from the volume-until you run an optimization job or execute the Update method of the [**MSFT\_DedupVolumeStatus**](msft-dedupvolumestatus.md) class. This number is most accurate after an optimization job runs or the Update method is executed.

</dd> <dt>

**UsageType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data to store on the volume.

**Windows Server 2012:** This property is not supported until Windows Server 2012 R2.

The possible values are:

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (1)


</dt> <dd>

General purpose files shares. This is the default value.

</dd> <dt>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)


</dt> <dd>

Hyper-V storage.

</dd> <dt>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)


</dt> <dd>

Backup storage.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not available before Windows Server 2016.

</dd> </dl>

</dd> <dt>

**UsedSpace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of used space on the volume, in bytes.

</dd> <dt>

**Verify**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If **True**, a byte-for-byte verification is performed for each duplicate chunk that is detected during optimization rather than relying on a cryptographically strong hash. We recommend to set this property to **false**.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A drive letter, for example, "D:", or volume **GUID** path for the volume.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A volume **GUID** path for the volume. A volume **GUID** path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a **GUID** that identifies the volume.

</dd> </dl>

## Examples

For an example that uses the **MSFT\_DedupVolume** class, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[Data Deduplication Management WMI API Reference](data-deduplication-management-wmi-api-reference.md)
</dt> </dl>

 

 





