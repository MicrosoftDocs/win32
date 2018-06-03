---
Description: Configures BranchCache to operate in hosted cache client mode.
ms.assetid: ba648ae5-1d6e-42cb-a482-959fd955ec72
title: Enable\_BCHostedClientByServerNames method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enable\_BCHostedClientByServerNames method of the MSFT\_NetBranchCacheOrchestrator class

Configures BranchCache to operate in hosted cache client mode.

## Syntax


```mof
uint32 Enable_BCHostedClientByServerNames(
  [in] string  ServerNames[],
  [in] uint32  UseVersion,
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ServerNames* \[in\]
</dt> <dd>

Names of the hosted cache servers to use.

</dd> <dt>

*UseVersion* \[in\]
</dt> <dd>

Version of the offer protocol to use when contacting this hosted cache server.

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

 

 




