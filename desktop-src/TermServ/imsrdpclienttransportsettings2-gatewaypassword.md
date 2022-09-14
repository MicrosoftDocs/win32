---
title: IMsRdpClientTransportSettings2 GatewayPassword property
description: Specifies the password that a user provides to connect to the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: f29078e5-49ab-45a0-8d79-4b57d7c35e3a
ms.tgt_platform: multiple
keywords:
- GatewayPassword property Remote Desktop Services
- GatewayPassword property Remote Desktop Services , IMsRdpClientTransportSettings2 interface
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , GatewayPassword property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2.GatewayPassword
- IMsRdpClientTransportSettings2.put_GatewayPassword
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2::GatewayPassword property

Specifies the password that a user provides to connect to the Remote Desktop Gateway (RD Gateway) server.

This property is write-only.

## Syntax


```C++
HRESULT put_GatewayPassword(
  [in] BSTR proxyPassword
);
```



## Property value

The password that a user provides to connect to the RD Gateway server.

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

 

 





