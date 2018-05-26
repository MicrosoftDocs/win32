---
Description: Modifies the cache file configuration.
ms.assetid: 09c1fe83-c216-4c4f-9bc7-cab4c36fa362
title: Set\_BCCacheByPath method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set\_BCCacheByPath method of the MSFT\_NetBranchCacheOrchestrator class

Modifies the cache file configuration.

## Syntax


```mof
uint32 Set_BCCacheByPath(
  [in]  string                   Path,
  [in]  string                   MoveTo,
  [in]  uint32                   Percentage,
  [in]  uint64                   SizeBytes,
  [in]  boolean                  Defragment,
  [in]  string                   PolicyStore,
  [in]  boolean                  PassThru,
  [in]  boolean                  Force,
  [out] MSFT_NetBranchCacheCache cmdletOutput
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Specifies the cache file to operate on.

</dd> <dt>

*MoveTo* \[in\]
</dt> <dd>

Specifies the new location on disk for this this cache file.

</dd> <dt>

*Percentage* \[in\]
</dt> <dd>

Specifies the new size (in terms of disk percentage) of this cache file.

</dd> <dt>

*SizeBytes* \[in\]
</dt> <dd>

Specifies the new size of this cache file.

</dd> <dt>

*Defragment* \[in\]
</dt> <dd>

Indicates the cache should be defragmented

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

Specifies the path to the group policy object that should be modified by this cmdlet.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates that the method should output an object that represents the modified cache in the *CmdletOutput* parameter.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives a [**MSFT\_NetBranchCacheCache**](msft-netbranchcachecache.md) object that represents the modified cache.

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
</dt> <dt>

[**MSFT\_NetBranchCacheCache**](msft-netbranchcachecache.md)
</dt> </dl>

 

 




