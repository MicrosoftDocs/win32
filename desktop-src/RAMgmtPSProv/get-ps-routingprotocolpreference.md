---
title: Get method of the PS\_RoutingProtocolPreference class
description: Retrieves the preference level of the specified routing protocol.
audience: developer
ms.assetid: '4ea2ea36-ef27-4c51-846b-16c728f738e9'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_RoutingProtocolPreference class", "PS_RoutingProtocolPreference class, Get method"]
topic_type:
- apiref
api_name:
- PS_RoutingProtocolPreference.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_RoutingProtocolPreference class

Retrieves the preference level of the specified routing protocol.

## Syntax


```mof
uint32 Get(
  [out] ProtocolPreference cmdletOutput
);
```



## Parameters

<dl> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

The [**ProtocolPreference**](protocolpreference.md) object that receives the retrieved routing protocol preference.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RoutingProtocolPreference**](ps-routingprotocolpreference.md)
</dt> </dl>

 

 





