---
title: LogEvent method of the PS\_NetworkControllerNode class
description: Logs an event on the node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2c2d4417-7fa7-4662-ad64-6e1892063911'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["LogEvent method", "LogEvent method, PS_NetworkControllerNode class", "PS_NetworkControllerNode class, LogEvent method"]
topic_type:
- apiref
api_name:
- PS_NetworkControllerNode.LogEvent
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# LogEvent method of the PS\_NetworkControllerNode class

Logs an event on the node.

## Syntax


```mof
uint32 LogEvent(
  [in] uint32                                    EventId,
  [in] NetworkControllerClusterConfiguration     OldClusterConfiguration,
  [in] NetworkControllerClusterConfiguration     NewClusterConfiguration,
  [in] NetworkControllerApplicationConfiguration OldApplicationConfiguration,
  [in] NetworkControllerApplicationConfiguration NewApplicationConfiguration
);
```



## Parameters

<dl> <dt>

*EventId* \[in\]
</dt> <dd>

The event ID.

</dd> <dt>

*OldClusterConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) embedded instance containing old cluster-specific information.

</dd> <dt>

*NewClusterConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerClusterConfiguration**](networkcontrollerclusterconfiguration.md) embedded instance containing new cluster-specific information.

</dd> <dt>

*OldApplicationConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) embedded instance containing old application-specific information.

</dd> <dt>

*NewApplicationConfiguration* \[in\]
</dt> <dd>

A [**NetworkControllerApplicationConfiguration**](networkcontrollerapplicationconfiguration.md) embedded instance containing new application-specific information.

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

 

 





