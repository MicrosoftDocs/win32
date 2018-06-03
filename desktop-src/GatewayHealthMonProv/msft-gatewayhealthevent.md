---
title: MSFT\_GatewayHealthEvent class
description: Gateway health event notifications.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ba492657-eb6e-459f-93bd-490c8071507e
ms.prod: windows-server-dev
ms.technology:
- gateway-health-monitor
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_GatewayHealthEvent class
- MSFT_GatewayHealthEvent class, described
topic_type:
- apiref
api_name:
- MSFT_GatewayHealthEvent
- MSFT_GatewayHealthEvent.Id
- MSFT_GatewayHealthEvent.HealthStatus
- MSFT_GatewayHealthEvent.Values
api_location:
- GatewayHealthMonitorProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_GatewayHealthEvent class

Gateway health event notifications.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), Indication, dynamic, provider("GatewayHealthMonitorProvider"), AMENDMENT]
class MSFT_GatewayHealthEvent
{
  string                    Id;
  boolean                   HealthStatus;
  MSFT_GatewayHealthContext Values[];
};
```

## Members

The **MSFT\_GatewayHealthEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_GatewayHealthEvent** class has these properties.

<dl> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The health status of the gateway on the host. 0 - Unhealthy, 1- Healthy

</dd> <dt>

**Id**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the identifier for the event. For now we pass null

</dd> <dt>

**Values**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_GatewayHealthContext** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**MSFT\_GatewayHealthContext**](msft-gatewayhealthcontext.md)")
</dt> </dl>

Contains an array of instances of the [**MSFT\_GatewayHealthContext**](msft-gatewayhealthcontext.md) class that represent the context of the event.

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\GatewayHealthMonitor<br/>                                     |
| MOF<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.dll</dt> </dl> |



 

 





