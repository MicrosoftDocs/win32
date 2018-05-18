---
title: MSFT\_GatewayHealthContext class
description: Describes the health context for a gateway.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'daa0a974-0241-476b-9491-ceaa7190eb35'
ms.prod: 'windows-server-dev'
ms.technology:
- 'gateway-health-monitor'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_GatewayHealthContext class", "MSFT_GatewayHealthContext class, described"]
topic_type:
- apiref
api_name:
- MSFT_GatewayHealthContext
- MSFT_GatewayHealthContext.Name
- MSFT_GatewayHealthContext.Type
- MSFT_GatewayHealthContext.State
api_location:
- GatewayHealthMonitorProvider.dll
api_type:
- DllExport
---

# MSFT\_GatewayHealthContext class

Describes the health context for a gateway.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("GatewayHealthMonitorProvider"), AMENDMENT]
class MSFT_GatewayHealthContext
{
  string Name;
  uint32 Type;
  uint32 State;
};
```

## Members

The **MSFT\_GatewayHealthContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_GatewayHealthContext** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the health context.

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current state of the health context.

</dd> <dt>

**Type**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of health context.

</dd> </dl>

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                              |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\GatewayHealthMonitor<br/>                                     |
| MOF<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>GatewayHealthMonitorProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_GatewayHealthEvent**](msft-gatewayhealthevent.md)
</dt> </dl>

 

 





