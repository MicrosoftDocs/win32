---
title: IMsRdpClientNonScriptable4 MarkRdpSettingsSecure property
description: Specifies whether Remote Desktop Protocol (RDP) settings are marked as secure.
ms.assetid: 04b419ed-821e-43e0-ac76-b8d6f6dfcc30
ms.tgt_platform: multiple
keywords:
- MarkRdpSettingsSecure property Remote Desktop Services
- MarkRdpSettingsSecure property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , MarkRdpSettingsSecure property
- MarkRdpSettingsSecure property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , MarkRdpSettingsSecure property
- MarkRdpSettingsSecure property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , MarkRdpSettingsSecure property
- MarkRdpSettingsSecure property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , MarkRdpSettingsSecure property
- MarkRdpSettingsSecure property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , MarkRdpSettingsSecure property
- MarkRdpSettingsSecure property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , MarkRdpSettingsSecure property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.MarkRdpSettingsSecure
- IMsRdpClientNonScriptable4.get_MarkRdpSettingsSecure
- IMsRdpClientNonScriptable4.put_MarkRdpSettingsSecure
- IMsRdpClientNonScriptable5.MarkRdpSettingsSecure
- IMsRdpClientNonScriptable5.get_MarkRdpSettingsSecure
- IMsRdpClientNonScriptable5.put_MarkRdpSettingsSecure
- MsRdpClient6.MarkRdpSettingsSecure
- MsRdpClient7.MarkRdpSettingsSecure
- MsRdpClient8.MarkRdpSettingsSecure
- MsRdpClient9.MarkRdpSettingsSecure
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::MarkRdpSettingsSecure property

Specifies whether [Remote Desktop Protocol](remote-desktop-protocol.md) (RDP) settings are marked as secure. This indicates that the settings applied to the control have been signed by a third-party or trusted publisher.

This property is read/write.

## Syntax


```C++
HRESULT put_MarkRdpSettingsSecure(
  [in]  VARIANT_BOOL fRdpSecure
);

HRESULT get_MarkRdpSettingsSecure(
  [out] VARIANT_BOOL *pfRdpSecure
);
```



## Property value

Sets whether RDP settings are marked as secure.

## Error codes

Returns **S\_OK** if successful.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IMsRdpClientNonScriptable4 is defined as f50fa8aa-1c7d-4f59-b15c-a90cacae1fcb<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> </dl>

 

 





