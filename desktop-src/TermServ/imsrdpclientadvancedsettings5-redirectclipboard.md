---
title: IMsRdpClientAdvancedSettings5 RedirectClipboard property
description: Sets or retrieves the configuration for clipboard redirection.
ms.assetid: c653f593-9912-4ade-a0a3-70d9afac2ab1
ms.tgt_platform: multiple
keywords:
- RedirectClipboard property Remote Desktop Services
- RedirectClipboard property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , RedirectClipboard property
- RedirectClipboard property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , RedirectClipboard property
- RedirectClipboard property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , RedirectClipboard property
- RedirectClipboard property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , RedirectClipboard property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings5.RedirectClipboard
- IMsRdpClientAdvancedSettings5.get_RedirectClipboard
- IMsRdpClientAdvancedSettings5.put_RedirectClipboard
- IMsRdpClientAdvancedSettings6.RedirectClipboard
- IMsRdpClientAdvancedSettings6.get_RedirectClipboard
- IMsRdpClientAdvancedSettings6.put_RedirectClipboard
- IMsRdpClientAdvancedSettings7.RedirectClipboard
- IMsRdpClientAdvancedSettings7.get_RedirectClipboard
- IMsRdpClientAdvancedSettings7.put_RedirectClipboard
- IMsRdpClientAdvancedSettings8.RedirectClipboard
- IMsRdpClientAdvancedSettings8.get_RedirectClipboard
- IMsRdpClientAdvancedSettings8.put_RedirectClipboard
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings5::RedirectClipboard property

Sets or retrieves the configuration for clipboard redirection.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectClipboard(
  [in]  VARIANT_BOOL fRedirectClipboard
);

HRESULT get_RedirectClipboard(
  [out] VARIANT_BOOL *pfRedirectClipboard
);
```



## Property value

Sets the clipboard redirection mode to **TRUE** or **FALSE**. If set to **TRUE**, clipboard redirection mode is enabled.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings5 is defined as FBA7F64E-6783-4405-DA45-FA4A763DABD0<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
</dt> </dl>

 

 





