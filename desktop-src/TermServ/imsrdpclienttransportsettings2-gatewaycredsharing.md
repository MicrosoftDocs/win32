---
title: IMsRdpClientTransportSettings2 GatewayCredSharing property
description: Specifies or retrieves the setting for whether the Remote Desktop Gateway (RD Gateway) credential sharing feature is enabled.
ms.assetid: 296dc578-376d-41f6-988a-286fe744959f
ms.tgt_platform: multiple
keywords:
- GatewayCredSharing property Remote Desktop Services
- GatewayCredSharing property Remote Desktop Services , IMsRdpClientTransportSettings2 interface
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , GatewayCredSharing property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2.GatewayCredSharing
- IMsRdpClientTransportSettings2.get_GatewayCredSharing
- IMsRdpClientTransportSettings2.put_GatewayCredSharing
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2::GatewayCredSharing property

Specifies or retrieves the setting for whether the Remote Desktop Gateway (RD Gateway) credential sharing feature is enabled. When the feature is enabled, the Remote Desktop ActiveX control tries to use the same credentials to authenticate to the Remote Desktop Session Host (RD Session Host) server and to the RD Gateway server.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayCredSharing(
  [in]  ULONG ulProxyCredSharing
);

HRESULT get_GatewayCredSharing(
  [out] ULONG *pulProxyCredSharing
);
```



## Property value

If set to one, credential sharing is enabled. If set to zero, credential sharing is disabled.

## Error codes

Returns **S\_OK** if successful.

## Remarks

This property is used by the ActiveX control to implement a single prompt for credential sharing between the RD Session Host server and the RD Gateway server. Credential sharing does not support web-based password sharing with [**GatewayPassword**](imsrdpclienttransportsettings2-gatewaypassword.md) or [**ClearTextPassword**](imstscnonscriptable-cleartextpassword.md).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                    |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>            |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>            |
| IID<br/>                      | IID\_IMsRdpClientTransportSettings2 is defined as 67341688-D606-4c73-A5D2-2E0489009319<br/> |



## See also

<dl> <dt>

[**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md)
</dt> <dt>

[**IMsRdpClientTransportSettings2**](imsrdpclienttransportsettings2.md)
</dt> </dl>

 

 





