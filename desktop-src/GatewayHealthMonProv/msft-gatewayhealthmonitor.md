---
title: MSFT\_GatewayHealthMonitor class
description: Manages a gateway health monitoring agent.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c4b334e7-0478-41a0-9605-2dace0d1d888'
ms.prod: 'windows-server-dev'
ms.technology:
- 'gateway-health-monitor'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_GatewayHealthMonitor class", "MSFT_GatewayHealthMonitor class, described"]
topic_type:
- apiref
api_name:
- MSFT_GatewayHealthMonitor
api_location:
- GatewayHealthMonitorProvider.dll
api_type:
- DllExport
---

# MSFT\_GatewayHealthMonitor class

Manages a gateway health monitoring agent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("GatewayHealthMonitorProvider"), AMENDMENT]
class MSFT_GatewayHealthMonitor
{
};
```

## Members

The **MSFT\_GatewayHealthMonitor** class has these types of members:

-   [Methods](#methods)

### Methods

The **MSFT\_GatewayHealthMonitor** class has these methods.



| Method                                                                             | Description                                            |
|:-----------------------------------------------------------------------------------|:-------------------------------------------------------|
| [**StartGatewayMonitoring**](startgatewaymonitoring-msft-gatewayhealthmonitor.md) | Starts the gateway health monitoring agent.<br/> |
| [**StopGatewayMonitoring**](stopgatewaymonitoring-msft-gatewayhealthmonitor.md)   | Stops the gateway health monitoring agent.<br/>  |



 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\GatewayHealthMonitor<br/>                                     |
| MOF<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.dll</dt> </dl> |



 

 





