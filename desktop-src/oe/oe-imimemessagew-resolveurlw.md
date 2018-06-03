---
title: IMimeMessageW ResolveURLW method
description: Maps a MIME Encapsulation of Aggregate HTML Documents (MHTML) URL to a body in the message.
ms.assetid: 91251f66-318a-449f-938e-448b878dbac1
keywords:
- ResolveURLW method Windows Mail (formerly Outlook Express)
- ResolveURLW method Windows Mail (formerly Outlook Express) , IMimeMessageW interface
- IMimeMessageW interface Windows Mail (formerly Outlook Express) , ResolveURLW method
topic_type:
- apiref
api_name:
- IMimeMessageW.ResolveURLW
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimeMessageW::ResolveURLW method

\[**ResolveURLW** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Maps a MIME Encapsulation of Aggregate HTML Documents (MHTML) URL to a body in the message. This method should be used only on MHTML messages that have a multipart/related section.

## Syntax


```C++
HRESULT ResolveURLW(
  [in]  HBODY   hRelated,
  [in]  LPCWSTR pwszBase,
  [in]  LPCWSTR pwszURL,
  [in]  DWORD   dwFlags,
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*hRelated* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the multipart/related section to search in. When this parameter is **NULL**, the method uses the first multipart/related section in the message.

</dd> <dt>

*pwszBase* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the URL. When this parameter is **NULL**, the method uses the Content-Base header in the multipart/related section, unless **URL\_RESULVE\_NO\_BASE** is specified in *dwFlags*.

</dd> <dt>

*pwszURL* \[in\]
</dt> <dd>

Type: **LPCWSTR**

Specifies the URL to resolve.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the resolution behavior.



| Value                                                                                                                                                                               | Meaning                                                                                                                                               |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="URL_RESOLVE_RENDERED"></span><span id="url_resolve_rendered"></span><dl> <dt>**URL\_RESOLVE\_RENDERED**</dt> </dl> | Indicates that if a body is found that matches the specified URL, the PID\_ATT\_RENDERED property for that body should be set to **TRUE**.<br/> |
| <span id="URL_RESULVE_NO_BASE"></span><span id="url_resulve_no_base"></span><dl> <dt>**URL\_RESULVE\_NO\_BASE**</dt> </dl>   | Indicates that the **IMimeMessageW::ResolveURLW** method should not attempt to use a base URL when trying to resolve the URL.<br/>              |



 

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the body that the URL resolved to.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                        | Description                                               |
|----------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>               | Indicates success.<br/>                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>             | Indicates that an unknown error has occurred. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pwszURL* is **NULL**. <br/>         |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl> | Indicates that the URL could not be resolved.<br/>  |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IMimeMessageW**](oe-imimemessagew.md)
</dt> <dt>

[MIME Encapsulation of Aggregate HTML Documents (MHTML)](http://msdn.microsoft.com/library/cdosys/html/e0df4075-c8a3-4844-8b81-74abdf5d5565.asp)
</dt> </dl>

 

 





