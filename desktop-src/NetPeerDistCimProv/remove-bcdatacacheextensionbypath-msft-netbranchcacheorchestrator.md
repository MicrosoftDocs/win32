---
Description: 'Deletes a cache file.'
ms.assetid: '3a56af16-95ed-4aa1-a067-c58a62a889e3'
title: 'Remove\_BCDataCacheExtensionByPath method of the MSFT\_NetBranchCacheOrchestrator class'
---

# Remove\_BCDataCacheExtensionByPath method of the MSFT\_NetBranchCacheOrchestrator class

Deletes a cache file.

## Syntax


```mof
uint32 Remove_BCDataCacheExtensionByPath(
  [in] string  Path,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Specifies the cache file to operate on.

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

 

 




