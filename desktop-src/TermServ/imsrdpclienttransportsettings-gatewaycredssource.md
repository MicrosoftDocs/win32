---
title: IMsRdpClientTransportSettings GatewayCredsSource property
description: Specifies or retrieves the Remote Desktop Gateway (RD Gateway) authentication method.
ms.assetid: 3b05edcb-f678-4d80-99fd-b76d27c80c68
ms.tgt_platform: multiple
keywords:
- GatewayCredsSource property Remote Desktop Services
- GatewayCredsSource property Remote Desktop Services , IMsRdpClientTransportSettings interface
- IMsRdpClientTransportSettings interface Remote Desktop Services , GatewayCredsSource property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings.GatewayCredsSource
- IMsRdpClientTransportSettings.get_GatewayCredsSource
- IMsRdpClientTransportSettings.put_GatewayCredsSource
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings::GatewayCredsSource property

Specifies or retrieves the Remote Desktop Gateway (RD Gateway) authentication method.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayCredsSource(
  [in]  ULONG ulProxyCredsSource
);

HRESULT get_GatewayCredsSource(
  [out] ULONG *pulProxyCredsSource
);
```



## Property value

A **ULONG** variable that specifies the RD Gateway authentication method. This parameter can be one of the following values.

<dt>

TSC\_PROXY\_CREDS\_MODE\_USERPASS (0)
</dt> <dd>

Use a password (NTLM) as the authentication method for RD Gateway.

</dd> <dt>

TSC\_PROXY\_CREDS\_MODE\_SMARTCARD (1)
</dt> <dd>

Use a smart card as the authentication method for RD Gateway.

</dd> <dt>

TSC\_PROXY\_CREDS\_MODE\_ANY (4)
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

 

 





