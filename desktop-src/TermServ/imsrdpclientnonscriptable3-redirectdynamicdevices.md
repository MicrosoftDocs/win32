---
title: IMsRdpClientNonScriptable3 RedirectDynamicDevices property
description: Specifies or retrieves whether dynamically attached Plug and Play (PnP) devices that are enumerated while in a session are available for redirection.
ms.assetid: 8cc5d6a4-108b-4505-8937-f6e790a5c2ba
ms.tgt_platform: multiple
keywords:
- RedirectDynamicDevices property Remote Desktop Services
- RedirectDynamicDevices property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , RedirectDynamicDevices property
- RedirectDynamicDevices property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , RedirectDynamicDevices property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.RedirectDynamicDevices
- IMsRdpClientNonScriptable3.get_RedirectDynamicDevices
- IMsRdpClientNonScriptable3.put_RedirectDynamicDevices
- IMsRdpClientNonScriptable4.RedirectDynamicDevices
- IMsRdpClientNonScriptable4.get_RedirectDynamicDevices
- IMsRdpClientNonScriptable4.put_RedirectDynamicDevices
- IMsRdpClientNonScriptable5.RedirectDynamicDevices
- IMsRdpClientNonScriptable5.get_RedirectDynamicDevices
- IMsRdpClientNonScriptable5.put_RedirectDynamicDevices
- MsRdpClient5.RedirectDynamicDevices
- MsRdpClient6.RedirectDynamicDevices
- MsRdpClient7.RedirectDynamicDevices
- MsRdpClient8.RedirectDynamicDevices
- MsRdpClient9.RedirectDynamicDevices
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::RedirectDynamicDevices property

Specifies or retrieves whether dynamically attached Plug and Play (PnP) devices that are enumerated while in a session are available for redirection.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectDynamicDevices(
  [in]  VARIANT_BOOL fRedirectDynamicDevices
);

HRESULT get_RedirectDynamicDevices(
  [out] VARIANT_BOOL *pfRedirectDynamicDevices
);
```



## Property value

Specifies whether dynamically attached PnP devices that are enumerated while in a session are available for redirection.

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

 

 





