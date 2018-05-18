---
title: UpdateClusterConfiguration method of the PS\_NetworkController class
description: Updates the Network Controller cluster configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '777d1de4-f7a3-4b20-937e-5de91446e8c2'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UpdateClusterConfiguration method", "UpdateClusterConfiguration method, PS_NetworkController class", "PS_NetworkController class, UpdateClusterConfiguration method"]
topic_type:
- apiref
api_name:
- PS_NetworkController.UpdateClusterConfiguration
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# UpdateClusterConfiguration method of the PS\_NetworkController class

Updates the Network Controller cluster configuration.

## Syntax


```mof
uint32 UpdateClusterConfiguration(
  [in] NetworkControllerClusterConfiguration ClusterConfiguration
);
```



## Parameters

<dl> <dt>

*ClusterConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) embedded instance containing the cluster configuration.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





