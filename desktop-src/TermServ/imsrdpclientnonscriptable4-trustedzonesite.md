---
title: IMsRdpClientNonScriptable4 TrustedZoneSite property
description: Specifies whether the website from which the user launched the connection is in the trusted sites list of the user's client computer.
ms.assetid: cb7efacc-b13b-494c-ab02-35c4f914744c
ms.tgt_platform: multiple
keywords:
- TrustedZoneSite property Remote Desktop Services
- TrustedZoneSite property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , TrustedZoneSite property
- TrustedZoneSite property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , TrustedZoneSite property
- TrustedZoneSite property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , TrustedZoneSite property
- TrustedZoneSite property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , TrustedZoneSite property
- TrustedZoneSite property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , TrustedZoneSite property
- TrustedZoneSite property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , TrustedZoneSite property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.TrustedZoneSite
- IMsRdpClientNonScriptable4.get_TrustedZoneSite
- IMsRdpClientNonScriptable4.put_TrustedZoneSite
- IMsRdpClientNonScriptable5.TrustedZoneSite
- IMsRdpClientNonScriptable5.get_TrustedZoneSite
- IMsRdpClientNonScriptable5.put_TrustedZoneSite
- MsRdpClient6.TrustedZoneSite
- MsRdpClient7.TrustedZoneSite
- MsRdpClient8.TrustedZoneSite
- MsRdpClient9.TrustedZoneSite
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::TrustedZoneSite property

Specifies whether the website from which the user launched the connection is in the trusted sites list of the user's client computer.

This property is read/write.

## Syntax


```C++
HRESULT put_TrustedZoneSite(
  [in]  VARIANT_BOOL fIsTrustedZone
);

HRESULT get_TrustedZoneSite(
  [out] VARIANT_BOOL *pfIsTrustedZone
);
```



## Property value

Sets the TrustedZoneSite property. This method has no effect on whether the website from which the user launched the connection is in the trusted sites list of the client computer.

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

 

 





