---
Description: Sets the minimum latency that must exist between client and server before transparent caching functions are used.
ms.assetid: d43aa560-5267-4ba5-9fc5-d313670fd9e0
title: Set\_BCMinSMBLatency method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Set\_BCMinSMBLatency method of the MSFT\_NetBranchCacheOrchestrator class

Sets the minimum latency that must exist between client and server before transparent caching functions are used.

## Syntax


```mof
uint32 Set_BCMinSMBLatency(
  [in] uint32  LatencyMilliseconds,
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*LatencyMilliseconds* \[in\]
</dt> <dd>

Minimum latency that must exist between client and server before BranchCache should be used.

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

Path to the group policy object that should be modified by this cmdlet.

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

 

 




