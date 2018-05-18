---
title: MSCluster\_StorageSpacesDirect class
description: Class for Storage Spaces direct management.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '95921b98-3bcb-4e69-b952-6ad287c0020f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_StorageSpacesDirect class", "MSCluster_StorageSpacesDirect class, described"]
topic_type:
- apiref
api_name:
- MSCluster_StorageSpacesDirect
- MSCluster_StorageSpacesDirect.Name
- MSCluster_StorageSpacesDirect.State
- MSCluster_StorageSpacesDirect.CacheState
- MSCluster_StorageSpacesDirect.CachePageSizeKBytes
- MSCluster_StorageSpacesDirect.CacheMetadataReserveBytes
- MSCluster_StorageSpacesDirect.CacheDeviceModel
- MSCluster_StorageSpacesDirect.CacheModeSSD
- MSCluster_StorageSpacesDirect.CacheModeHDD
- MSCluster_StorageSpacesDirect.Node
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_StorageSpacesDirect class

Class for Storage Spaces direct management.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("MSCLUSTEREXT"), AMENDMENT]
class MSCluster_StorageSpacesDirect
{
  string Name;
  uint32 State;
  uint32 CacheState;
  uint32 CachePageSizeKBytes;
  uint64 CacheMetadataReserveBytes;
  string CacheDeviceModel[];
  uint32 CacheModeSSD;
  uint32 CacheModeHDD;
  string Node;
};
```

## Members

The **MSCluster\_StorageSpacesDirect** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_StorageSpacesDirect** class has these methods.



| Method                                                                                         | Description                                                     |
|:-----------------------------------------------------------------------------------------------|:----------------------------------------------------------------|
| [**DisableStorageSpacesDirect**](mscluster-storagespacesdirect-disablestoragespacesdirect.md) | Disables Storage Spaces Direct.<br/>                      |
| [**EnableStorageSpacesDirect**](mscluster-storagespacesdirect-enablestoragespacesdirect.md)   | Enables Storage Spaces Direct.<br/>                       |
| [**GetStorageSpacesDirect**](mscluster-storagespacesdirect-getstoragespacesdirect.md)         | Gets Storage Spaces Direct.<br/>                          |
| [**GetStorageSpacesDirectDisk**](mscluster-storagespacesdirect-getstoragespacesdirectdisk.md) | Sets Storage Spaces Direct Disk.<br/>                     |
| [**PostCreatePool**](mscluster-storagespacesdirect-postcreatepool.md)                         | Creates storage tiers used by Storage Spaces Direct.<br/> |
| [**RepairStorageSpacesDirect**](mscluster-storagespacesdirect-repairstoragespacesdirect.md)   | Repairs Storage Spaces Direct<br/>                        |
| [**SetStorageSpacesDirect**](mscluster-storagespacesdirect-setstoragespacesdirect.md)         | Sets Storage Spaces Direct.<br/>                          |
| [**SetStorageSpacesDirectDisk**](mscluster-storagespacesdirect-setstoragespacesdirectdisk.md) | Sets Storage Spaces Direct Disk.<br/>                     |



 

### Properties

The **MSCluster\_StorageSpacesDirect** class has these properties.

<dl> <dt>

**CacheDeviceModel**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The model prefixes of the disks to be used for cache.

</dd> <dt>

**CacheMetadataReserveBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

How many bytes that the cache should leave unused.

</dd> <dt>

**CacheModeHDD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The desired state for cache HDD.

</dd> <dt>

**CacheModeSSD**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The desired state for cache SSD.

</dd> <dt>

**CachePageSizeKBytes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Cache page size in KB.

</dd> <dt>

**CacheState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cache state.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The friendly name of the collection.

</dd> <dt>

**Node**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The node name.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of Storage Spaces Direct.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\MSCluster<br/>                                                                |
| MOF<br/>                      | <dl> <dt>ClusWmiExt.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl>    |



 

 





