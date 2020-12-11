---
title: IMsRdpClientNonScriptable4 PromptForCredsOnClient property
description: Specifies whether the client control displays a dialog box that prompts for credentials.
ms.assetid: 426676be-0150-4a33-acd0-26423966f32a
ms.tgt_platform: multiple
keywords:
- PromptForCredsOnClient property Remote Desktop Services
- PromptForCredsOnClient property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , PromptForCredsOnClient property
- PromptForCredsOnClient property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , PromptForCredsOnClient property
- PromptForCredsOnClient property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , PromptForCredsOnClient property
- PromptForCredsOnClient property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , PromptForCredsOnClient property
- PromptForCredsOnClient property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , PromptForCredsOnClient property
- PromptForCredsOnClient property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , PromptForCredsOnClient property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.PromptForCredsOnClient
- IMsRdpClientNonScriptable4.get_PromptForCredsOnClient
- IMsRdpClientNonScriptable4.put_PromptForCredsOnClient
- IMsRdpClientNonScriptable5.PromptForCredsOnClient
- IMsRdpClientNonScriptable5.get_PromptForCredsOnClient
- IMsRdpClientNonScriptable5.put_PromptForCredsOnClient
- MsRdpClient6.PromptForCredsOnClient
- MsRdpClient7.PromptForCredsOnClient
- MsRdpClient8.PromptForCredsOnClient
- MsRdpClient9.PromptForCredsOnClient
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::PromptForCredsOnClient property

Specifies whether the client control displays a dialog box that prompts for credentials.

This property is read/write.

## Syntax


```C++
HRESULT put_PromptForCredsOnClient(
  [in]  VARIANT_BOOL fPromptForCredsOnClient
);

HRESULT get_PromptForCredsOnClient(
  [out] VARIANT_BOOL *pfPromptForCredsOnClient
);
```



## Property value

Sets whether the client control displays a dialog box that prompts for credentials.

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

 

 





