---
Description: Describes a BranchCache primary cache.
ms.assetid: a087f98d-f1bf-448b-b0b8-752e6c7f4331
title: MSFT\_NetBranchCachePrimaryCache class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_NetBranchCachePrimaryCache class

Describes a BranchCache primary cache

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract]
class MSFT_NetBranchCachePrimaryCache : MSFT_NetBranchCacheCache
{
  uint64 CurrentActiveCacheSize;
};
```

## Members

The **MSFT\_NetBranchCachePrimaryCache** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetBranchCachePrimaryCache** class has these properties.

<dl> <dt>

**CurrentActiveCacheSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The current size of the cached data, in bytes

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



 

 




