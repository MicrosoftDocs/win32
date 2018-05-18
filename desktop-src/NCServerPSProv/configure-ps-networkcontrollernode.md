---
title: Configure method of the PS\_NetworkControllerNode class
description: Configures the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '69f05dfa-cec0-4637-9d03-cbe76beb0853'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Configure method", "Configure method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, Configure method"]
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.Configure
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# Configure method of the PS\_NetworkControllerNode class

Configures the node.

## Syntax


```mof
uint32 Configure(
  [in] NetworkControllerClusterConfiguration     ClusterConfiguration,
  [in] NetworkControllerApplicationConfiguration ApplicationConfiguration,
  [in] uint32                                    InitialReplicaSize
);
```



## Parameters

<dl> <dt>

*ClusterConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) embedded instance containing cluster-specific information.

</dd> <dt>

*ApplicationConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) embedded instance containing application-specific information.

</dd> <dt>

*InitialReplicaSize* \[in\]
</dt> <dd>

Initial cluster replica size

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

 

 





