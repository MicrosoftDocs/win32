---
Description: 'Imports a cache package.'
ms.assetid: '1ba6e06d-4917-4673-b620-8c360051bfe9'
title: 'Import\_BCCachePackage method of the MSFT\_NetBranchCacheOrchestrator class'
---

# Import\_BCCachePackage method of the MSFT\_NetBranchCacheOrchestrator class

Imports a cache package.

## Syntax


```mof
uint32 Import_BCCachePackage(
  [in] string  Path,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Specifies the cache package to import

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetBranchCacheOrchestrator**](msft-netbranchcacheorchestrator.md)
</dt> </dl>

 

 




