---
title: IMsRdpClientNonScriptable3 PromptForCredentials property (Wuapi.h)
description: Specifies or retrieves whether the prompt for credentials dialog is enabled for the connection.
ms.assetid: 252ec5bd-bd52-40d4-ae48-b2c00c0720c0
ms.tgt_platform: multiple
keywords:
- PromptForCredentials property Remote Desktop Services
- PromptForCredentials property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , PromptForCredentials property
- PromptForCredentials property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , PromptForCredentials property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.PromptForCredentials
- IMsRdpClientNonScriptable3.get_PromptForCredentials
- IMsRdpClientNonScriptable3.put_PromptForCredentials
- IMsRdpClientNonScriptable4.PromptForCredentials
- IMsRdpClientNonScriptable4.get_PromptForCredentials
- IMsRdpClientNonScriptable4.put_PromptForCredentials
- IMsRdpClientNonScriptable5.PromptForCredentials
- IMsRdpClientNonScriptable5.get_PromptForCredentials
- IMsRdpClientNonScriptable5.put_PromptForCredentials
- MsRdpClient5.PromptForCredentials
- MsRdpClient6.PromptForCredentials
- MsRdpClient7.PromptForCredentials
- MsRdpClient8.PromptForCredentials
- MsRdpClient9.PromptForCredentials
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::PromptForCredentials property

Specifies or retrieves whether the prompt for credentials dialog is enabled for the connection.

This property is read/write.

## Syntax


```C++
HRESULT put_PromptForCredentials(
  [in]  VARIANT_BOOL fPrompt
);

HRESULT get_PromptForCredentials(
  [out] VARIANT_BOOL *pfPrompt
);
```



## Property value

Specifies whether the prompt for credentials dialog is enabled for the connection.

## Error codes

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Header<br/>                   | <dl> <dt>Wuapi.h</dt> </dl>            |
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

 

 





