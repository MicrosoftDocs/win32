---
title: IMsRdpClientTransportSettings GatewayHostname property
description: Specifies the host name of the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 34c4b3b7-3768-4d98-b1e8-7fcb8f9c758d
ms.tgt_platform: multiple
keywords:
- GatewayHostname property Remote Desktop Services
- GatewayHostname property Remote Desktop Services , IMsRdpClientTransportSettings interface
- IMsRdpClientTransportSettings interface Remote Desktop Services , GatewayHostname property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings.GatewayHostname
- IMsRdpClientTransportSettings.get_GatewayHostname
- IMsRdpClientTransportSettings.put_GatewayHostname
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings::GatewayHostname property

Specifies the host name of the Remote Desktop Gateway (RD Gateway) server.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayHostname(
  [in]  BSTR newVal
);

HRESULT get_GatewayHostname(
  [out] BSTR *pProxyHostname
);
```



## Property value

A string that contains the RD Gateway server host name.

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

 

 





