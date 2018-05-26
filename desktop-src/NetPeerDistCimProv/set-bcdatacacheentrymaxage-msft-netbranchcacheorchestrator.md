---
Description: Sets the maximum age of an entry in the data cache.
ms.assetid: 54a5ff3e-5f5c-4258-b1d3-19986d3cb047
title: Set\_BCDataCacheEntryMaxAge method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set\_BCDataCacheEntryMaxAge method of the MSFT\_NetBranchCacheOrchestrator class

Sets the maximum age of an entry in the data cache.

## Syntax


```mof
uint32 Set_BCDataCacheEntryMaxAge(
  [in] uint32  TimeDays,
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*TimeDays* \[in\]
</dt> <dd>

The maximum number of days a cache entry is valid in the data cache.

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

Path to the group policy object that should be modified by this cmdlet.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Indicates the operation should not prompt for confirmation.

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

 

 




