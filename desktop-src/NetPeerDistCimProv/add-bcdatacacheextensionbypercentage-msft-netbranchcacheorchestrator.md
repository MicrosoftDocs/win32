---
Description: Adds a new republication cache file to increase the amount of storage available on a hosted cache server.
ms.assetid: 300a80a9-cac1-48c3-8948-ea593d93d8e0
title: Add\_BCDataCacheExtensionByPercentage method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add\_BCDataCacheExtensionByPercentage method of the MSFT\_NetBranchCacheOrchestrator class

Adds a new republication cache file to increase the amount of storage available on a hosted cache server.

## Syntax


```mof
uint32 Add_BCDataCacheExtensionByPercentage(
  [in]  uint32  Percentage,
  [in]  string  Path,
  [in]  boolean PassThru,
  [in]  boolean Force,
  [out] string  cmdletOutput
);
```



## Parameters

<dl> <dt>

*Percentage* \[in\]
</dt> <dd>

Specifies the new size (in terms of disk percentage) of this cache file.

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

 

 




