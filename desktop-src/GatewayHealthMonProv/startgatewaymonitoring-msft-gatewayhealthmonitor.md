---
title: StartGatewayMonitoring method of the MSFT\_GatewayHealthMonitor class
description: Starts the gateway health monitoring agent.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6a09be57-3ee9-4dea-b17c-b1ce1a5521cd
ms.prod: windows-server-dev
ms.technology:
- gateway-health-monitor
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- StartGatewayMonitoring method
- StartGatewayMonitoring method, MSFT_GatewayHealthMonitor class
- MSFT_GatewayHealthMonitor class, StartGatewayMonitoring method
topic_type:
- apiref
api_name:
- MSFT_GatewayHealthMonitor.StartGatewayMonitoring
api_location:
- GatewayHealthMonitorProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StartGatewayMonitoring method of the MSFT\_GatewayHealthMonitor class

Starts the gateway health monitoring agent.

## Syntax


```mof
uint32 StartGatewayMonitoring(
  [in] string InterfaceList[],
  [in] string ServiceList[]
);
```



## Parameters

<dl> <dt>

*InterfaceList* \[in\]
</dt> <dd>

Specifies the list of interfaces that are to be monitored.

</dd> <dt>

*ServiceList* \[in\]
</dt> <dd>

Specifies the list of services that are to be monitored.

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\GatewayHealthMonitor<br/>                                     |
| MOF<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_GatewayHealthMonitor**](msft-gatewayhealthmonitor.md)
</dt> </dl>

 

 





