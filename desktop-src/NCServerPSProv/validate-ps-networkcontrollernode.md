---
title: Validate method of the PS\_NetworkControllerNode class
description: Performs validations on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4ce3f8fe-83ff-46f5-ba9a-7736b39c70d4
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Validate method
- Validate method, PS_NetworkControllerNode class
- PS_NetworkControllerNode class, Validate method
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.Validate
api_location:
- NCServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Validate method of the PS\_NetworkControllerNode class

Performs validations on the node.

## Syntax


```mof
uint32 Validate(
  [in] string                                    NodeName,
  [in] NetworkControllerClusterConfiguration     ClusterConfiguration,
  [in] NetworkControllerApplicationConfiguration ApplicationConfiguration
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node in the cluster.

</dd> <dt>

*ClusterConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) embedded instance containing cluster-specific information.

</dd> <dt>

*ApplicationConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) embedded instance containing application-specific information.

</dd> </dl>

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

[**PS\_NetworkControllerNode**](ps-networkcontrollernode.md)
</dt> </dl>

 

 





