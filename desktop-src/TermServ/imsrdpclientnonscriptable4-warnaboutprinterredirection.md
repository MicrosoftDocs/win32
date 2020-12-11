---
title: IMsRdpClientNonScriptable4 WarnAboutPrinterRedirection property
description: Controls whether the redirection dialog box displays a message about printer redirection before starting a session.
ms.assetid: 12c5bc8d-7bc1-4a94-a9b8-6b852772c936
ms.tgt_platform: multiple
keywords:
- WarnAboutPrinterRedirection property Remote Desktop Services
- WarnAboutPrinterRedirection property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , WarnAboutPrinterRedirection property
- WarnAboutPrinterRedirection property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , WarnAboutPrinterRedirection property
- WarnAboutPrinterRedirection property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , WarnAboutPrinterRedirection property
- WarnAboutPrinterRedirection property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , WarnAboutPrinterRedirection property
- WarnAboutPrinterRedirection property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , WarnAboutPrinterRedirection property
- WarnAboutPrinterRedirection property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , WarnAboutPrinterRedirection property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.WarnAboutPrinterRedirection
- IMsRdpClientNonScriptable4.get_WarnAboutPrinterRedirection
- IMsRdpClientNonScriptable4.put_WarnAboutPrinterRedirection
- IMsRdpClientNonScriptable5.WarnAboutPrinterRedirection
- IMsRdpClientNonScriptable5.get_WarnAboutPrinterRedirection
- IMsRdpClientNonScriptable5.put_WarnAboutPrinterRedirection
- MsRdpClient6.WarnAboutPrinterRedirection
- MsRdpClient7.WarnAboutPrinterRedirection
- MsRdpClient8.WarnAboutPrinterRedirection
- MsRdpClient9.WarnAboutPrinterRedirection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::WarnAboutPrinterRedirection property

Controls whether the redirection dialog box displays a message about printer redirection before starting a session.

This property is read/write.

## Syntax


```C++
HRESULT put_WarnAboutPrinterRedirection(
  [in]  VARIANT_BOOL fWarn
);

HRESULT get_WarnAboutPrinterRedirection(
  [out] VARIANT_BOOL *pfWarn
);
```



## Property value

Sets whether the redirection dialog box displays a message about printer redirection.

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

 

 





