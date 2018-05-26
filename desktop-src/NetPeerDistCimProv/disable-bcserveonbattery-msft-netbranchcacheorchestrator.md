---
Description: A client may be configured to not listen for content discovery requests in distributed cache mode when operating on battery.
ms.assetid: eee04d3f-a5fe-4cc6-a9ef-c3d1777e8063
title: Disable\_BCServeOnBattery method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Disable\_BCServeOnBattery method of the MSFT\_NetBranchCacheOrchestrator class

A client may be configured to not listen for content discovery requests in distributed cache mode when operating on battery.

## Syntax


```mof
uint32 Disable_BCServeOnBattery(
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

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

 

 




