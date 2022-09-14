---
title: IMsRdpClientTransportSettings2 GatewayPreAuthRequirement property
description: Specifies or retrieves the setting for whether the Remote Desktop Gateway (RD Gateway) one-time password (OTP) feature is enabled.
ms.assetid: cc8f7ebb-16ba-45ed-ba66-de4a339946d0
ms.tgt_platform: multiple
keywords:
- GatewayPreAuthRequirement property Remote Desktop Services
- GatewayPreAuthRequirement property Remote Desktop Services , IMsRdpClientTransportSettings2 interface
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , GatewayPreAuthRequirement property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2.GatewayPreAuthRequirement
- IMsRdpClientTransportSettings2.get_GatewayPreAuthRequirement
- IMsRdpClientTransportSettings2.put_GatewayPreAuthRequirement
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2::GatewayPreAuthRequirement property

Specifies or retrieves the setting for whether the Remote Desktop Gateway (RD Gateway) one-time password (OTP) feature is enabled.

When OTP is enabled, **GatewayPreAuthRequirement** tries to query the OTP cookie from the Internet cookie store by using the [**GatewayPreAuthServerAddr**](imsrdpclienttransportsettings2-gatewaypreauthserveraddr.md) property. If successful, **GatewayPreAuthRequirement** sends the OTP cookie to the firewall server (such as Microsoft Internet Security and Acceleration \[ISA\] server) for pre-authentication.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayPreAuthRequirement(
  [in]  ULONG ulProxyPreAuthRequirement
);

HRESULT get_GatewayPreAuthRequirement(
  [out] ULONG *pulProxyPreAuthRequirement
);
```



## Property value

If set to 1, the OTP feature is enabled. If set to 0, the OTP feature is disabled.

## Error codes

Returns **S\_OK** if successful.

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

 

 





