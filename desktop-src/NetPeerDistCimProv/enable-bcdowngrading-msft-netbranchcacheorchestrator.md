---
Description: Client may be instructed to operate in a downgraded mode, in which it will issue specified version requests to content servers.
ms.assetid: 86b223f1-ceef-4423-b612-02866ddab911
title: Enable\_BCDowngrading method of the MSFT\_NetBranchCacheOrchestrator class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enable\_BCDowngrading method of the MSFT\_NetBranchCacheOrchestrator class

Client may be instructed to operate in a downgraded mode, in which it will issue specified version requests to content servers.

## Syntax


```mof
uint32 Enable_BCDowngrading(
  [in] uint32  Version,
  [in] string  PolicyStore,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Version* \[in\]
</dt> <dd>

Specifies whether or not the client should operate in a downgraded mode and which version should be used.

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

 

 




