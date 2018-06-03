---
Description: Configures BranchCache to operate in hosted cache server mode.
ms.assetid: 45caae22-d058-4091-825c-2fd6fd6cba23
title: Enable\_BCHostedServer method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable\_BCHostedServer method of the MSFT\_NetBranchCacheOrchestrator class

Configures BranchCache to operate in hosted cache server mode.

## Syntax


```mof
uint32 Enable_BCHostedServer(
  [in] boolean RegisterSCP,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*RegisterSCP* \[in\]
</dt> <dd>

Indicates the hosted cache server should register a service connection point.

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

 

 




