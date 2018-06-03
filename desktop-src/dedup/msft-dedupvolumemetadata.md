---
title: MSFT\_DedupVolumeMetadata class
description: Represents the data deduplication metadata for a volume.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 850FB2D0-B2C0-4351-93C7-F92B9AD90561
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_DedupVolumeMetadata class Data Deduplication API
- MSFT_DedupVolumeMetadata class Data Deduplication API , described
topic_type:
- apiref
api_name:
- MSFT_DedupVolumeMetadata
- MSFT_DedupVolumeMetadata.VolumeId
- MSFT_DedupVolumeMetadata.StoreId
- MSFT_DedupVolumeMetadata.Volume
- MSFT_DedupVolumeMetadata.DataChunkCount
- MSFT_DedupVolumeMetadata.DataContainerCount
- MSFT_DedupVolumeMetadata.DataChunkAverageSize
- MSFT_DedupVolumeMetadata.DataChunkMedianSize
- MSFT_DedupVolumeMetadata.DataMaxChunkCount
- MSFT_DedupVolumeMetadata.DataStoreUncompactedFreespace
- MSFT_DedupVolumeMetadata.StreamMapChunkCount
- MSFT_DedupVolumeMetadata.StreamMapContainerCount
- MSFT_DedupVolumeMetadata.StreamMapAverageChunkCount
- MSFT_DedupVolumeMetadata.StreamMapMedianChunkCount
- MSFT_DedupVolumeMetadata.StreamMapMaxChunkCount
- MSFT_DedupVolumeMetadata.HotspotChunkCount
- MSFT_DedupVolumeMetadata.HotspotContainerCount
- MSFT_DedupVolumeMetadata.HotspotMedianReferenceCount
- MSFT_DedupVolumeMetadata.CorruptionLogEntryCount
- MSFT_DedupVolumeMetadata.TotalChunkStoreSize
api_location:
- DdpWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_DedupVolumeMetadata class

Represents the data deduplication metadata for a volume.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[dynamic, provider("DeduplicationProvider"), ClassVersion("1.0"), AMENDMENT]
class MSFT_DedupVolumeMetadata
{
  String VolumeId;
  String StoreId;
  String Volume;
  uint64 DataChunkCount;
  uint32 DataContainerCount;
  uint32 DataChunkAverageSize;
  uint32 DataChunkMedianSize;
  uint32 DataMaxChunkCount;
  uint64 DataStoreUncompactedFreespace;
  uint64 StreamMapChunkCount;
  uint32 StreamMapContainerCount;
  uint32 StreamMapAverageChunkCount;
  uint32 StreamMapMedianChunkCount;
  uint32 StreamMapMaxChunkCount;
  uint64 HotspotChunkCount;
  uint32 HotspotContainerCount;
  uint32 HotspotMedianReferenceCount;
  uint32 CorruptionLogEntryCount;
  uint64 TotalChunkStoreSize;
};
```

## Members

The **MSFT\_DedupVolumeMetadata** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DedupVolumeMetadata** class has these properties.

<dl> <dt>

**CorruptionLogEntryCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of corruption log entries for the volume.

</dd> <dt>

**DataChunkAverageSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The data store size (not including chunk metadata) divided by the total number of data chunks in the data store.

</dd> <dt>

**DataChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of data chunks on the volume.

</dd> <dt>

**DataChunkMedianSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for system use.

</dd> <dt>

**DataContainerCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of containers in the data store.

</dd> <dt>

**DataMaxChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for system use.

</dd> <dt>

**DataStoreUncompactedFreespace**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**HotspotChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of hot spots on the volume.

</dd> <dt>

**HotspotContainerCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of containers in the hot spot store.

</dd> <dt>

**HotspotMedianReferenceCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**StoreId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The unique ID for the data deduplication chunk store.

</dd> <dt>

**StreamMapAverageChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**StreamMapChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of stream map chunks on the volume.

</dd> <dt>

**StreamMapContainerCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of containers in the stream map store.

</dd> <dt>

**StreamMapMaxChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**StreamMapMedianChunkCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is reserved for future use.

</dd> <dt>

**TotalChunkStoreSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total chunk store size.

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A drive letter (for example, D:) or volume GUID path for the volume.

</dd> <dt>

**VolumeId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A volume GUID path for the volume. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> </dl>

## Examples

For an example that uses the **MSFT\_DedupVolumeMetadata** class, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

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

 

 





