---
Description: Adds a new republication cache file to increase the amount of storage available on a hosted cache server.
ms.assetid: 3dd9cd2b-332e-4277-98f9-ca69e3981e28
title: Add\_BCDataCacheExtensionBySizeBytes method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Add\_BCDataCacheExtensionBySizeBytes method of the MSFT\_NetBranchCacheOrchestrator class

Adds a new republication cache file to increase the amount of storage available on a hosted cache server.

## Syntax


```mof
uint32 Add_BCDataCacheExtensionBySizeBytes(
  [in]  uint64                                SizeBytes,
  [in]  string                                Path,
  [in]  boolean                               PassThru,
  [in]  boolean                               Force,
  [out] MSFT_NetBranchCacheDataCacheExtension cmdletOutput
);
```



## Parameters

<dl> <dt>

*SizeBytes* \[in\]
</dt> <dd>

Specifies the new size of this cache file.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Specifies the cache file to operate on.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Indicates that the method should output an object that represents the newly created cache extension in the *CmdletOutput* parameter.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives a [**MSFT\_NetBranchCacheDataCacheExtension**](msft-netbranchcachedatacacheextension.md) object that represents the newly created cache extension.

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

 

 




