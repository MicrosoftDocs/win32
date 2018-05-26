---
title: GetClusterUpgradeProgress method of the PS\_NetworkController class
description: Retrieves the Network Controller upgrade status.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bffb284a-eccf-4fc8-8886-e70f749afd5b
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetClusterUpgradeProgress method
- GetClusterUpgradeProgress method, PS_NetworkController class
- PS_NetworkController class, GetClusterUpgradeProgress method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetClusterUpgradeProgress method of the PS\_NetworkController class

Retrieves the Network Controller upgrade status.

## Syntax


```mof
uint32 GetClusterUpgradeProgress(
  [out] NetworkControllerClusterUpgradeProgressInfo ClusterUpgradeProgress
);
```



## Parameters

<dl> <dt>

*ClusterUpgradeProgress* \[out\]
</dt> <dd>

Embedded instance of [**NetworkControllerClusterUpgradeProgressInfo**](networkcontrollerclusterupgradeprogressinfo.md) containing the cluster upgrade progress info.

</dd> </dl>

## Return value

TBD

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





