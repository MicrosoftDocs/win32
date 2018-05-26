---
Description: Configures BranchCache to operate in hosted cache client mode.
ms.assetid: 3215335e-24ba-453a-93e6-0c0035ef06e3
title: Enable\_BCHostedClientByUseSCP method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enable\_BCHostedClientByUseSCP method of the MSFT\_NetBranchCacheOrchestrator class

Configures BranchCache to operate in hosted cache client mode.

## Syntax


```mof
uint32 Enable_BCHostedClientByUseSCP(
  [in] boolean UseSCP,
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*UseSCP* \[in\]
</dt> <dd>

Indicates the client should locate hosted cache servers using service connection points.

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

 

 




