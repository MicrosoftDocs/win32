---
title: IMsRdpClientNonScriptable5 AllowPromptingForCredentials property
description: Specifies whether the Remote Desktop ActiveX control can prompt the user for credentials.
ms.assetid: 9a780886-39ee-4d3b-9a54-fa209708d9f8
ms.tgt_platform: multiple
keywords:
- AllowPromptingForCredentials property Remote Desktop Services
- AllowPromptingForCredentials property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , AllowPromptingForCredentials property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable5.AllowPromptingForCredentials
- IMsRdpClientNonScriptable5.get_AllowPromptingForCredentials
- IMsRdpClientNonScriptable5.put_AllowPromptingForCredentials
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable5::AllowPromptingForCredentials property

Specifies whether the Remote Desktop ActiveX control can prompt the user for credentials. If this property contains **VARIANT\_TRUE**, the user can be prompted for credentials. If this property contains **VARIANT\_FALSE**, the user cannot be prompted for credentials.

This property is read/write.

## Syntax


```C++
HRESULT put_AllowPromptingForCredentials(
  [in]          VARIANT_BOOL fAllow
);

HRESULT get_AllowPromptingForCredentials(
  [out, retval] VARIANT_BOOL *pfAllow
);
```



## Property value

Specifies the new property value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable5 is defined as 4f6996d5-d7b1-412c-b0ff-063718566907<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> </dl>

 

 





