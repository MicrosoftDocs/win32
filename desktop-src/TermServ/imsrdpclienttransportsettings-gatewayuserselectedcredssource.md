---
title: IMsRdpClientTransportSettings GatewayUserSelectedCredsSource property
description: Sets or retrieves the user-specified Remote Desktop Gateway (RD Gateway) credential source.
ms.assetid: 0c12ddf6-52c2-40a2-af2b-effd4e8bbdb6
ms.tgt_platform: multiple
keywords:
- GatewayUserSelectedCredsSource property Remote Desktop Services
- GatewayUserSelectedCredsSource property Remote Desktop Services , IMsRdpClientTransportSettings interface
- IMsRdpClientTransportSettings interface Remote Desktop Services , GatewayUserSelectedCredsSource property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings.GatewayUserSelectedCredsSource
- IMsRdpClientTransportSettings.get_GatewayUserSelectedCredsSource
- IMsRdpClientTransportSettings.put_GatewayUserSelectedCredsSource
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings::GatewayUserSelectedCredsSource property

Sets or retrieves the user-specified Remote Desktop Gateway (RD Gateway) credential source.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayUserSelectedCredsSource(
  [in]  ULONG ulProxyCredsSource
);

HRESULT get_GatewayUserSelectedCredsSource(
  [out] ULONG *pulProxyCredsSource
);
```



## Property value

A **ULONG** variable that specifies the RD Gateway authentication method. This parameter can be one of the following values.

<dt>

<span id="TSC_PROXY_CREDS_MODE_USERPASS"></span><span id="tsc_proxy_creds_mode_userpass"></span>

<span id="TSC_PROXY_CREDS_MODE_USERPASS"></span><span id="tsc_proxy_creds_mode_userpass"></span>**TSC\_PROXY\_CREDS\_MODE\_USERPASS** (0 (0x0))


</dt> <dd>

Use a password (NTLM) as the authentication method for RD Gateway.

</dd> <dt>

<span id="TSC_PROXY_CREDS_MODE_SMARTCARD"></span><span id="tsc_proxy_creds_mode_smartcard"></span>

<span id="TSC_PROXY_CREDS_MODE_SMARTCARD"></span><span id="tsc_proxy_creds_mode_smartcard"></span>**TSC\_PROXY\_CREDS\_MODE\_SMARTCARD** (1 (0x1))


</dt> <dd>

Use a smart card as the authentication method for RD Gateway.

</dd> <dt>

<span id="TSC_PROXY_CREDS_MODE_ANY"></span><span id="tsc_proxy_creds_mode_any"></span>

<span id="TSC_PROXY_CREDS_MODE_ANY"></span><span id="tsc_proxy_creds_mode_any"></span>**TSC\_PROXY\_CREDS\_MODE\_ANY** (4 (0x4))


</dt> <dd>

Use any authentication method for RD Gateway.

</dd> </dl>

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

 

 





