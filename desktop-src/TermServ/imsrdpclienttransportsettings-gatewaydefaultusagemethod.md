---
title: IMsRdpClientTransportSettings GatewayDefaultUsageMethod property
description: The default usage method for Remote Desktop Gateway (RD Gateway).
ms.assetid: 7014538d-550a-4246-ad32-406ef67fb112
ms.tgt_platform: multiple
keywords:
- GatewayDefaultUsageMethod property Remote Desktop Services
- GatewayDefaultUsageMethod property Remote Desktop Services , IMsRdpClientTransportSettings interface
- IMsRdpClientTransportSettings interface Remote Desktop Services , GatewayDefaultUsageMethod property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings.GatewayDefaultUsageMethod
- IMsRdpClientTransportSettings.get_GatewayDefaultUsageMethod
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings::GatewayDefaultUsageMethod property

The default usage method for Remote Desktop Gateway (RD Gateway).

This property is read-only.

## Syntax


```C++
HRESULT get_GatewayDefaultUsageMethod(
  [out] ULONG *pulProxyDefaultUsageMethod
);
```



## Property value

A pointer to the default usage method for RD Gateway. Returns a union of the user settings that are set by [**put\_GatewayUsageMethod()**](imsrdpclienttransportsettings-gatewayusagemethod.md), and group policy settings. If no user settings were set by **put\_GatewayUsageMethod()**, **get\_GatewayDefaultUsageMethod()** will return the default value of **TSC\_PROXY\_MODE\_DETECT**.

## Error codes

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientTransportSettings is defined as 720298C0-A099-46f5-9F82-96921BAE4701<br/> |



## See also

<dl> <dt>

[**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md)
</dt> </dl>

 

 





