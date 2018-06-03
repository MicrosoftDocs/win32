---
title: IMimeMessageTree ResolveURL method
description: Maps a MIME Encapsulation of Aggregate HTML Documents (MHTML) URL to a body in the message. This method should only be used on MHTML messages that have a multipart/related section.
ms.assetid: d47dc5b5-353b-4b34-b7fa-5e0d9eac809a
keywords:
- ResolveURL method Windows Mail (formerly Outlook Express)
- ResolveURL method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , ResolveURL method
topic_type:
- apiref
api_name:
- IMimeMessageTree.ResolveURL
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

# IMimeMessageTree::ResolveURL method

Maps a MIME Encapsulation of Aggregate HTML Documents (MHTML) URL to a body in the message. This method should only be used on MHTML messages that have a [multipart/related](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) section.

## Syntax


```C++
HRESULT ResolveURL(
  [in]  HBODY   hRelated,
  [in]  LPCSTR  pszBase,
  [in]  LPCSTR  pszURL,
  [in]  DWORD   dwFlags,
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*hRelated* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the [multipart/related](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) section to search in. When this parameter is **NULL**, the method uses the first multipart/related section in the message.

</dd> <dt>

*pszBase* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the URL. When this parameter is **NULL**, the method uses the [Content-Base](http://msdn.microsoft.com/library/cdosys/html/4aca7ccf-7eeb-44e6-b74c-ee2ae337cc70.asp) header in the [multipart/related](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) section, unless **URL\_RESULVE\_NO\_BASE** is specified in *dwFlags*.

</dd> <dt>

*pszURL* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies the URL to resolve.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the resolution behavior.



| Value                                                                                                                                                                               | Meaning                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="URL_RESOLVE_RENDERED"></span><span id="url_resolve_rendered"></span><dl> <dt>**URL\_RESOLVE\_RENDERED**</dt> </dl> | Indicates that if a body is found that matches the specified URL, that the PID\_ATT\_RENDERED property for that body should be set to **TRUE**.<br/> |
| <span id="URL_RESULVE_NO_BASE"></span><span id="url_resulve_no_base"></span><dl> <dt>**URL\_RESULVE\_NO\_BASE**</dt> </dl>   | Indicates that the **IMimeMessageTree::ResolveURL** method should not attempt to use a base URL when trying to resolve the URL.<br/>                 |



 

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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>       | Indicates that *pszURL* is **NULL**. <br/>          |
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

[**IMimeMessageTree**](oe-imimemessagetree.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[MIME Encapsulation of Aggregate HTML Documents (MHTML)](http://msdn.microsoft.com/library/cdosys/html/e0df4075-c8a3-4844-8b81-74abdf5d5565.asp)
</dt> <dt>

[Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp)
</dt> </dl>

 

 





