---
title: IMsRdpClientNonScriptable3 EnableCredSspSupport property
description: Specifies or retrieves whether the Credential Security Service Provider (CredSSP) is enabled for this connection.
ms.assetid: 770da50b-2a93-4274-9b6f-c24c13f08549
ms.tgt_platform: multiple
keywords:
- EnableCredSspSupport property Remote Desktop Services
- EnableCredSspSupport property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , EnableCredSspSupport property
- EnableCredSspSupport property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , EnableCredSspSupport property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.EnableCredSspSupport
- IMsRdpClientNonScriptable3.get_EnableCredSspSupport
- IMsRdpClientNonScriptable3.put_EnableCredSspSupport
- IMsRdpClientNonScriptable4.EnableCredSspSupport
- IMsRdpClientNonScriptable4.get_EnableCredSspSupport
- IMsRdpClientNonScriptable4.put_EnableCredSspSupport
- IMsRdpClientNonScriptable5.EnableCredSspSupport
- IMsRdpClientNonScriptable5.get_EnableCredSspSupport
- IMsRdpClientNonScriptable5.put_EnableCredSspSupport
- MsRdpClient5.EnableCredSspSupport
- MsRdpClient6.EnableCredSspSupport
- MsRdpClient7.EnableCredSspSupport
- MsRdpClient8.EnableCredSspSupport
- MsRdpClient9.EnableCredSspSupport
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::EnableCredSspSupport property

Specifies or retrieves whether the Credential Security Service Provider (CredSSP) is enabled for this connection.

This property is read/write.

## Syntax


```C++
HRESULT put_EnableCredSspSupport(
  [in]  VARIANT_BOOL fEnableSupport
);

HRESULT get_EnableCredSspSupport(
  [out] VARIANT_BOOL *pfEnableSupport
);
```



## Property value

Specifies whether CredSSP is enabled for this connection.

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

 

 





