---
title: IMsRdpClientTransportSettings2 GatewayEncryptedOtpCookieSize property
description: Specifies or retrieves the size of the encrypted one-time password (OTP) cookie.
ms.assetid: a4fdcd06-59ae-407f-9ac6-dfe4b52fb5d7
ms.tgt_platform: multiple
keywords:
- GatewayEncryptedOtpCookieSize property Remote Desktop Services
- GatewayEncryptedOtpCookieSize property Remote Desktop Services , IMsRdpClientTransportSettings2 interface
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , GatewayEncryptedOtpCookieSize property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2.GatewayEncryptedOtpCookieSize
- IMsRdpClientTransportSettings2.get_GatewayEncryptedOtpCookieSize
- IMsRdpClientTransportSettings2.put_GatewayEncryptedOtpCookieSize
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2::GatewayEncryptedOtpCookieSize property

Specifies or retrieves the size of the encrypted one-time password (OTP) cookie.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayEncryptedOtpCookieSize(
  [in]  ULONG ulEncryptedOtpCookieSize
);

HRESULT get_GatewayEncryptedOtpCookieSize(
  [out] ULONG *pulEncryptedOtpCookieSize
);
```



## Property value

Specifies or retrieves the size of the encrypted one-time password (OTP) cookie.

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

 

 





