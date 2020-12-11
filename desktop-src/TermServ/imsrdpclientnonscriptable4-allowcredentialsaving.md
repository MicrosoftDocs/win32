---
title: IMsRdpClientNonScriptable4 AllowCredentialSaving property
description: Specifies whether the credentials dialog box displays a check box that enables the saving of credentials.
ms.assetid: c5148ff0-0d7f-413d-b2a8-ff942668bee6
ms.tgt_platform: multiple
keywords:
- AllowCredentialSaving property Remote Desktop Services
- AllowCredentialSaving property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , AllowCredentialSaving property
- AllowCredentialSaving property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , AllowCredentialSaving property
- AllowCredentialSaving property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , AllowCredentialSaving property
- AllowCredentialSaving property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , AllowCredentialSaving property
- AllowCredentialSaving property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , AllowCredentialSaving property
- AllowCredentialSaving property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , AllowCredentialSaving property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.AllowCredentialSaving
- IMsRdpClientNonScriptable4.get_AllowCredentialSaving
- IMsRdpClientNonScriptable4.put_AllowCredentialSaving
- IMsRdpClientNonScriptable5.AllowCredentialSaving
- IMsRdpClientNonScriptable5.get_AllowCredentialSaving
- IMsRdpClientNonScriptable5.put_AllowCredentialSaving
- MsRdpClient6.AllowCredentialSaving
- MsRdpClient7.AllowCredentialSaving
- MsRdpClient8.AllowCredentialSaving
- MsRdpClient9.AllowCredentialSaving
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::AllowCredentialSaving property

Specifies whether the credentials dialog box displays a check box that enables the saving of credentials.

This property is read/write.

## Syntax


```C++
HRESULT put_AllowCredentialSaving(
  [in]  VARIANT_BOOL fAllowSave
);

HRESULT get_AllowCredentialSaving(
  [out] VARIANT_BOOL *pfAllowSave
);
```



## Property value

Sets whether the credentials dialog box displays a check box that enables the saving of credentials.

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

 

 





