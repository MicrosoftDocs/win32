---
title: IMsRdpClientAdvancedSettings8 ClientProtocolSpec property
description: Specifies the remote desktop protocol used between the client and the server.
ms.assetid: DD607D54-CAEA-43EE-94EB-F983AEA0CC1E
ms.tgt_platform: multiple
keywords:
- ClientProtocolSpec property Remote Desktop Services
- ClientProtocolSpec property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , ClientProtocolSpec property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings8.ClientProtocolSpec
- IMsRdpClientAdvancedSettings8.get_ClientProtocolSpec
- IMsRdpClientAdvancedSettings8.put_ClientProtocolSpec
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings8::ClientProtocolSpec property

Specifies the remote desktop protocol used between the client and the server.

This property is read/write.

## Syntax


```C++
HRESULT put_ClientProtocolSpec(
  [in]  ClientSpec ClientMode
);

HRESULT get_ClientProtocolSpec(
  [out] ClientSpec *pClientMode
);
```



## Property value

A value of the [**ClientSpec**](clientspec.md) enumeration that specifies the remote desktop protocol used between the client and the server.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**ClientSpec**](clientspec.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> </dl>

 

 





