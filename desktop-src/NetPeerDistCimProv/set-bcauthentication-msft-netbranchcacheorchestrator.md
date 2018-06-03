---
Description: Specifies the authentication scheme for clients.
ms.assetid: aee9f924-9964-45f0-a91f-6bd9fd508c6d
title: Set\_BCAuthentication method of the MSFT\_NetBranchCacheOrchestrator class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set\_BCAuthentication method of the MSFT\_NetBranchCacheOrchestrator class

Specifies the authentication scheme for clients.

## Syntax


```mof
uint32 Set_BCAuthentication(
  [in] uint32  Mode,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*Mode* \[in\]
</dt> <dd>

Specifies the authentication mode.

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

 

 




