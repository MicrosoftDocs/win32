---
title: UpdateNodeConfiguration method of the PS\_NetworkControllerNode class
description: Updates the node configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd152e77d-99b2-4f19-94c5-c948e0da29a8'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["UpdateNodeConfiguration method", "UpdateNodeConfiguration method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, UpdateNodeConfiguration method"]
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.UpdateNodeConfiguration
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# UpdateNodeConfiguration method of the PS\_NetworkControllerNode class

Updates the node configuration.

## Syntax


```mof
uint32 UpdateNodeConfiguration(
  [in] NetworkControllerClusterConfiguration ClusterConfiguration
);
```



## Parameters

<dl> <dt>

*ClusterConfiguration* \[in\]
</dt> <dd>

An embedded [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) instance containing the cluster configuration.

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

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





