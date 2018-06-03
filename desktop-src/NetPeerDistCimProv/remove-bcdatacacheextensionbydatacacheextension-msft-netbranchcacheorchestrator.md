---
Description: Deletes a cache file.
ms.assetid: a4571f58-0c19-4633-8c7f-ca9a41302290
title: Remove\_BCDataCacheExtensionByDataCacheExtension method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Remove\_BCDataCacheExtensionByDataCacheExtension method of the MSFT\_NetBranchCacheOrchestrator class

Deletes a cache file.

## Syntax


```mof
uint32 Remove_BCDataCacheExtensionByDataCacheExtension(
  [in] string  DataCacheExtension[],
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*DataCacheExtension* \[in\]
</dt> <dd>

The cache extension which should be removed

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>NetPeerDistCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetPeerDistCim.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetBranchCacheOrchestrator**](msft-netbranchcacheorchestrator.md)
</dt> </dl>

 

 




