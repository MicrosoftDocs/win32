---
Description: 'Represents a BranchCache data cache.'
ms.assetid: '4afafaf7-abf9-4290-9801-6bc47bf67521'
title: 'MSFT\_NetBranchCacheDataCache class'
---

# MSFT\_NetBranchCacheDataCache class

Represents a BranchCache data cache

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetPeerDist")]
class MSFT_NetBranchCacheDataCache : MSFT_NetBranchCachePrimaryCache
{
  string DataCacheExtensions[];
};
```

## Members

The **MSFT\_NetBranchCacheDataCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCacheDataCache** class has these properties.

<dl> <dt>

**DataCacheExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

DataCacheExtensions

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




