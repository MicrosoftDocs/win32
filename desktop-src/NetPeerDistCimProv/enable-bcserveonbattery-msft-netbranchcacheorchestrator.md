---
Description: Configures a client to listen for content discovery requests in distributed cache mode when operating on battery.
ms.assetid: eaa8fc6e-06b4-4228-937a-1c1c9efe5747
title: Enable\_BCServeOnBattery method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable\_BCServeOnBattery method of the MSFT\_NetBranchCacheOrchestrator class

Configures a client to listen for content discovery requests in distributed cache mode when operating on battery.

## Syntax


```mof
uint32 Enable_BCServeOnBattery(
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

 

 




