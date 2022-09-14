---
title: IMsRdpClientNonScriptable3 NegotiateSecurityLayer property
description: Specifies or retrieves whether the negotiation security layer is enabled for the connection.
ms.assetid: 7fc9e3c7-0723-48c4-8d29-5f68a24a522c
ms.tgt_platform: multiple
keywords:
- NegotiateSecurityLayer property Remote Desktop Services
- NegotiateSecurityLayer property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , NegotiateSecurityLayer property
- NegotiateSecurityLayer property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , NegotiateSecurityLayer property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.NegotiateSecurityLayer
- IMsRdpClientNonScriptable3.get_NegotiateSecurityLayer
- IMsRdpClientNonScriptable3.put_NegotiateSecurityLayer
- IMsRdpClientNonScriptable4.NegotiateSecurityLayer
- IMsRdpClientNonScriptable4.get_NegotiateSecurityLayer
- IMsRdpClientNonScriptable4.put_NegotiateSecurityLayer
- IMsRdpClientNonScriptable5.NegotiateSecurityLayer
- IMsRdpClientNonScriptable5.get_NegotiateSecurityLayer
- IMsRdpClientNonScriptable5.put_NegotiateSecurityLayer
- MsRdpClient5.NegotiateSecurityLayer
- MsRdpClient6.NegotiateSecurityLayer
- MsRdpClient7.NegotiateSecurityLayer
- MsRdpClient8.NegotiateSecurityLayer
- MsRdpClient9.NegotiateSecurityLayer
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::NegotiateSecurityLayer property

Specifies or retrieves whether the negotiation security layer is enabled for the connection.

This property is read/write.

## Syntax


```C++
HRESULT put_NegotiateSecurityLayer(
  [in]  VARIANT_BOOL fNegotiate
);

HRESULT get_NegotiateSecurityLayer(
  [out] VARIANT_BOOL *pfNegotiate
);
```



## Property value

Specifies whether to enable negotiation of the security layer.

## Remarks

If this property is set to **VARIANT\_FALSE** and Network Level Authentication (NLA) is enabled on the client operating system, the client will not negotiate the security layer and instead, it will use NLA to secure the RDP connection. If this property is set to **VARIANT\_TRUE**, then the client will negotiate between NLA and basic RDP security.

> [!Note]  
> Disabling security layer negotiation is only possible when connecting to a Remote Desktop Session Host (RD Session Host) server running Windows Vista or later operating systems. If this property is enabled and the client attempts to connect to an RD Session Host server running an earlier operating system, the connection will fail.

 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable3 is defined as b3378d90-0728-45c7-8ed7-b6159fb92219<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> </dl>

 

 





