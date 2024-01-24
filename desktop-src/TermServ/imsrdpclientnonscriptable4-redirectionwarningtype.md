---
title: IMsRdpClientNonScriptable4 RedirectionWarningType property
description: Controls the presence and appearance of the dialog box that notifies the user about redirection.
ms.assetid: 1aa79fc3-9620-466d-a93f-77a55ad76ede
ms.tgt_platform: multiple
keywords:
- RedirectionWarningType property Remote Desktop Services
- RedirectionWarningType property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , RedirectionWarningType property
- RedirectionWarningType property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , RedirectionWarningType property
- RedirectionWarningType property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , RedirectionWarningType property
- RedirectionWarningType property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , RedirectionWarningType property
- RedirectionWarningType property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , RedirectionWarningType property
- RedirectionWarningType property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , RedirectionWarningType property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable4.RedirectionWarningType
- IMsRdpClientNonScriptable4.get_RedirectionWarningType
- IMsRdpClientNonScriptable4.put_RedirectionWarningType
- IMsRdpClientNonScriptable5.RedirectionWarningType
- IMsRdpClientNonScriptable5.get_RedirectionWarningType
- IMsRdpClientNonScriptable5.put_RedirectionWarningType
- MsRdpClient6.RedirectionWarningType
- MsRdpClient7.RedirectionWarningType
- MsRdpClient8.RedirectionWarningType
- MsRdpClient9.RedirectionWarningType
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable4::RedirectionWarningType property

Controls the presence and appearance of the dialog box that notifies the user about redirection.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectionWarningType(
  [in]  RedirectionWarningType wrnType
);

HRESULT get_RedirectionWarningType(
  [out] RedirectionWarningType *pWrnType
);
```



## Property value

Sets the type of the dialog box that notifies the user of redirection.

<dt>

<span id="RedirectionWarningTypeDefault"></span><span id="redirectionwarningtypedefault"></span><span id="REDIRECTIONWARNINGTYPEDEFAULT"></span>

<span id="RedirectionWarningTypeDefault"></span><span id="redirectionwarningtypedefault"></span><span id="REDIRECTIONWARNINGTYPEDEFAULT"></span>**RedirectionWarningTypeDefault** (0x0000)


</dt> <dd>

The dialog box is not publisher specific.

</dd> <dt>

<span id="RedirectionWarningTypeUnsigned"></span><span id="redirectionwarningtypeunsigned"></span><span id="REDIRECTIONWARNINGTYPEUNSIGNED"></span>

<span id="RedirectionWarningTypeUnsigned"></span><span id="redirectionwarningtypeunsigned"></span><span id="REDIRECTIONWARNINGTYPEUNSIGNED"></span>**RedirectionWarningTypeUnsigned** (0x0001)


</dt> <dd>

The dialog box is for unsigned files.

</dd> <dt>

<span id="RedirectionWarningTypeUnknown"></span><span id="redirectionwarningtypeunknown"></span><span id="REDIRECTIONWARNINGTYPEUNKNOWN"></span>

<span id="RedirectionWarningTypeUnknown"></span><span id="redirectionwarningtypeunknown"></span><span id="REDIRECTIONWARNINGTYPEUNKNOWN"></span>**RedirectionWarningTypeUnknown** (0x0002)


</dt> <dd>

The dialog box is for an unknown publisher.

</dd> <dt>

<span id="RedirectionWarningTypeUser"></span><span id="redirectionwarningtypeuser"></span><span id="REDIRECTIONWARNINGTYPEUSER"></span>

<span id="RedirectionWarningTypeUser"></span><span id="redirectionwarningtypeuser"></span><span id="REDIRECTIONWARNINGTYPEUSER"></span>**RedirectionWarningTypeUser** (0x0003)


</dt> <dd>

The dialog box is for the user's files.

</dd> <dt>

<span id="RedirectionWarningTypeThirdPartySigned"></span><span id="redirectionwarningtypethirdpartysigned"></span><span id="REDIRECTIONWARNINGTYPETHIRDPARTYSIGNED"></span>

<span id="RedirectionWarningTypeThirdPartySigned"></span><span id="redirectionwarningtypethirdpartysigned"></span><span id="REDIRECTIONWARNINGTYPETHIRDPARTYSIGNED"></span>**RedirectionWarningTypeThirdPartySigned** (0x0004)


</dt> <dd>

The dialog box is displayed for third-party-certified, signed files.

</dd> <dt>

<span id="RedirectionWarningTypeTrusted"></span><span id="redirectionwarningtypetrusted"></span><span id="REDIRECTIONWARNINGTYPETRUSTED"></span>

<span id="RedirectionWarningTypeTrusted"></span><span id="redirectionwarningtypetrusted"></span><span id="REDIRECTIONWARNINGTYPETRUSTED"></span>**RedirectionWarningTypeTrusted** (0x0005)


</dt> <dd>

The dialog box is not displayed because the application is published by a trusted publisher.

</dd> <dt>

<span id="RedirectionWarningTypeMax"></span><span id="redirectionwarningtypemax"></span><span id="REDIRECTIONWARNINGTYPEMAX"></span>

<span id="RedirectionWarningTypeMax"></span><span id="redirectionwarningtypemax"></span><span id="REDIRECTIONWARNINGTYPEMAX"></span>**RedirectionWarningTypeMax** (0x0005)


</dt> <dd>

The dialog box is not displayed because the application is published by a trusted publisher.

</dd> </dl>

## Error codes

Returns **S\_OK** if successful.

## Remarks

The value **RedirectionWarningTypeDefault**, which is the default value of this property, exerts no control over the dialog box. The controlling property in this case is [**ShowRedirectionWarningDialog**](imsrdpclientnonscriptable3-showredirectionwarningdialog.md) in [**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md).

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

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> </dl>

 

 





