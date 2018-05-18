---
Description: 'Describes a BranchCache cache.'
ms.assetid: 'a6dd60d2-5117-4ca9-becd-b3d5e78060a8'
title: 'MSFT\_NetBranchCacheCache class'
---

# MSFT\_NetBranchCacheCache class

Describes a BranchCache cache

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract]
class MSFT_NetBranchCacheCache : CIM_LogicalElement
{
  string InstanceID;
  uint32 MaxCacheSizeAsPercentageOfDiskVolume;
  uint64 MaxCacheSizeAsNumberOfBytes;
  uint64 CurrentSizeOnDiskAsNumberOfBytes;
  string CacheFileDirectoryPath;
};
```

## Members

The **MSFT\_NetBranchCacheCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheCache** class has these properties.

<dl> <dt>

**CacheFileDirectoryPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The directory path where the cache file is located

</dd> <dt>

**CurrentSizeOnDiskAsNumberOfBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the cache file on disk, in bytes

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

Identifies an instance of **MSFT\_NetBranchCacheCache**

</dd> <dt>

**MaxCacheSizeAsNumberOfBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum cache file size, in bytes

</dd> <dt>

**MaxCacheSizeAsPercentageOfDiskVolume**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum cache file size, represented as a percentage of the disk volume on which the cache is stored

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




