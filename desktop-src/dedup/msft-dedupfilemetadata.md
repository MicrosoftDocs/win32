---
title: MSFT\_DedupFileMetadata class
description: Represents a file that has data deduplication metadata.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5de043eb-74eb-427f-8a45-7764b6b7f20e
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupFileMetadata class Data Deduplication API
- MSFT_DedupFileMetadata class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupFileMetadata
- MSFT_DedupFileMetadata.Path
- MSFT_DedupFileMetadata.Volume
- MSFT_DedupFileMetadata.VolumeId
- MSFT_DedupFileMetadata.FilesCount
- MSFT_DedupFileMetadata.OptimizedFilesCount
- MSFT_DedupFileMetadata.Size
- MSFT_DedupFileMetadata.SizeOnDisk
- MSFT_DedupFileMetadata.DedupSize
- MSFT_DedupFileMetadata.DedupChunkCount
- MSFT_DedupFileMetadata.DedupDistinctSize
- MSFT_DedupFileMetadata.DedupDistinctChunkCount
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DedupFileMetadata class

Represents a file that has data deduplication metadata.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupFileMetadata
{
  string Path[];
  string Volume;
  string VolumeId;
  uint64 FilesCount;
  uint64 OptimizedFilesCount;
  uint64 Size;
  uint64 SizeOnDisk;
  uint64 DedupSize;
  uint64 DedupChunkCount;
  uint64 DedupDistinctSize;
  uint64 DedupDistinctChunkCount;
};
```

## Members

The **MSFT\_DedupFileMetadata** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_DedupFileMetadata** class has these methods.



| Method                                            | Description                                                                              |
|:--------------------------------------------------|:-----------------------------------------------------------------------------------------|
| [**Measure**](msft-dedupfilemetadata-measure.md) | Returns a class representing the deduplication metadata for a specified file.<br/> |



 

### Properties

The **MSFT\_DedupFileMetadata** class has these properties.

<dl> <dt>

**DedupChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of variable-sized chunks that are used in the optimized file.

</dd> <dt>

**DedupDistinctChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of variable-sized chunks that are used in the optimized file, but are not used by other optimized files.

</dd> <dt>

**DedupDistinctSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the unique portion of the file, in bytes, after it has been optimized.

</dd> <dt>

**DedupSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the file, in bytes, after it has been optimized.

</dd> <dt>

**FilesCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of files on the volume.

</dd> <dt>

**OptimizedFilesCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of optimized files on the volume. This number remains unchanged as users delete files from or add files to the volume until you run a garbage collection job. This number is most accurate after a garbage collection job runs.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The path of the file.

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the file, in bytes, before it was optimized.

</dd> <dt>

**SizeOnDisk**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The amount of space that was allocated to the file before it was optimized, in bytes, based on the cluster size of the partition.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A drive letter, for example, "D:", or a volume **GUID** path for the volume.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A volume **GUID** path for the volume. A volume **GUID** path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a **GUID** that identifies the volume.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[Data Deduplication Management WMI API Reference](data-deduplication-management-wmi-api-reference.md)
</dt> </dl>

 

 





