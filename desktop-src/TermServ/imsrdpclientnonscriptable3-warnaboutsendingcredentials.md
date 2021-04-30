---
title: IMsRdpClientNonScriptable3 WarnAboutSendingCredentials property
description: Specifies or retrieves whether the security warning dialog box should include a warning about sending credentials to the remote server before starting a session.
ms.assetid: b97baef5-4a51-4e5c-bd53-10cff175533c
ms.tgt_platform: multiple
keywords:
- WarnAboutSendingCredentials property Remote Desktop Services
- WarnAboutSendingCredentials property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , WarnAboutSendingCredentials property
- WarnAboutSendingCredentials property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , WarnAboutSendingCredentials property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.WarnAboutSendingCredentials
- IMsRdpClientNonScriptable3.get_WarnAboutSendingCredentials
- IMsRdpClientNonScriptable3.put_WarnAboutSendingCredentials
- IMsRdpClientNonScriptable4.WarnAboutSendingCredentials
- IMsRdpClientNonScriptable4.get_WarnAboutSendingCredentials
- IMsRdpClientNonScriptable4.put_WarnAboutSendingCredentials
- IMsRdpClientNonScriptable5.WarnAboutSendingCredentials
- IMsRdpClientNonScriptable5.get_WarnAboutSendingCredentials
- IMsRdpClientNonScriptable5.put_WarnAboutSendingCredentials
- MsRdpClient5.WarnAboutSendingCredentials
- MsRdpClient6.WarnAboutSendingCredentials
- MsRdpClient7.WarnAboutSendingCredentials
- MsRdpClient8.WarnAboutSendingCredentials
- MsRdpClient9.WarnAboutSendingCredentials
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::WarnAboutSendingCredentials property

Specifies or retrieves whether the security warning dialog box should include a warning about sending credentials to the remote server before starting a session.

This property is read/write.

## Syntax


```C++
HRESULT put_WarnAboutSendingCredentials(
  [in]  VARIANT_BOOL fWarn
);

HRESULT get_WarnAboutSendingCredentials(
  [out] VARIANT_BOOL *pfWarn
);
```



## Property value

Specifies whether the security warning dialog box should include a warning about sending credentials to the remote server before starting a session.

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

 

 





