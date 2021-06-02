---
title: IMsRdpClientNonScriptable3 WarnAboutClipboardRedirection property
description: Specifies or retrieves whether the security warning dialog box should be displayed to warn users about clipboard redirection.
ms.assetid: 2f3ca58b-3c89-4251-ae15-2c0aaf308893
ms.tgt_platform: multiple
keywords:
- WarnAboutClipboardRedirection property Remote Desktop Services
- WarnAboutClipboardRedirection property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , WarnAboutClipboardRedirection property
- WarnAboutClipboardRedirection property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , WarnAboutClipboardRedirection property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable3.get_WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable3.put_WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable4.WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable4.get_WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable4.put_WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable5.WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable5.get_WarnAboutClipboardRedirection
- IMsRdpClientNonScriptable5.put_WarnAboutClipboardRedirection
- MsRdpClient5.WarnAboutClipboardRedirection
- MsRdpClient6.WarnAboutClipboardRedirection
- MsRdpClient7.WarnAboutClipboardRedirection
- MsRdpClient8.WarnAboutClipboardRedirection
- MsRdpClient9.WarnAboutClipboardRedirection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::WarnAboutClipboardRedirection property

Specifies or retrieves whether the security warning dialog box should be displayed to warn users about clipboard redirection.

This property is read/write.

## Syntax


```C++
HRESULT put_WarnAboutClipboardRedirection(
  [in]  VARIANT_BOOL fWarn
);

HRESULT get_WarnAboutClipboardRedirection(
  [out] VARIANT_BOOL *pfWarn
);
```



## Property value

Specifies whether the security warning dialog box should be displayed to warn users about clipboard redirection.

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

 

 





