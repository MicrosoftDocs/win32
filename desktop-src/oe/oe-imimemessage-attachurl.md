---
title: IMimeMessage AttachURL method
description: Attaches the contents of a URL to the message and creates an MSHTML message. Usually, the attached URL is referenced by another body in the message.
ms.assetid: 3b95187b-9463-4707-9188-accc5726ef1f
keywords:
- AttachURL method Windows Mail (formerly Outlook Express)
- AttachURL method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , AttachURL method
topic_type:
- apiref
api_name:
- IMimeMessage.AttachURL
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

# IMimeMessage::AttachURL method

Attaches the contents of a URL to the message and creates an MSHTML message. Usually, the attached URL is referenced by another body in the message.

## Syntax


```C++
HRESULT AttachURL(
  [in]  LPCSTR  pszBase,
  [in]  LPCSTR  pszURL,
  [in]  DWORD   dwFlags,
  [in]  IStream *pstmURL,
  [out] LPSTR   *ppszCIDURL,
  [out] LPHBODY phBody
);
```



## Parameters

<dl> <dt>

*pszBase* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies together with *pszURL* a valid URL. *pszBase* specifies the base URL and *pszURL* specifies the relative URL.

</dd> <dt>

*pszURL* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies together with *pszBase* a valid URL. *pszBase* specifies the base URL and *pszURL* specifies the relative URL. When *pstmURL* is **NULL**, *pszURL* must specify a valid resource that MimeOLE has read access to.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask that affects the behavior of this method.



| Value                                                                                                                                                                                                                                                         | Meaning                                                                                                                                                                                              |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="URL_ATTACH_INTO_MIXED"></span><span id="url_attach_into_mixed"></span><dl> <dt>**URL\_ATTACH\_INTO\_MIXED**</dt> <dt>0x00000001</dt> </dl>       | Indicates that the body must be created in the [multipart/mixed](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) section of the message. <br/>   |
| <span id="URL_ATTACH_GENERATE_CID"></span><span id="url_attach_generate_cid"></span><dl> <dt>**URL\_ATTACH\_GENERATE\_CID**</dt> <dt>0x00000002</dt> </dl> | Indicates that the [Content-ID](http://msdn.microsoft.com/library/ms526943.aspx) must be generated and stored on the new body. <br/>                                         |
| <span id="URL_ATTACH_SET_CNTTYPE"></span><span id="url_attach_set_cnttype"></span><dl> <dt>**URL\_ATTACH\_SET\_CNTTYPE**</dt> <dt>0x00000004</dt> </dl>    | Indicates that the [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) must be derived from the URL and stored on the new body. <br/> |



 

</dd> <dt>

*pstmURL* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the data for the URL. MimeOLE increments the reference count for this object and does not release it until the whole message object is freed or until [**HandsOffStorage**](oe-imimemessagetree-handsoffstorage.md) is called.

</dd> <dt>

*ppszCIDURL* \[out\]
</dt> <dd>

Type: **LPSTR\***

Receives a pointer to the generated [Content-ID](http://msdn.microsoft.com/library/ms526943.aspx) string when *dwFlags* is specified as **URL\_ATTACH\_GENERATE\_CID**. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the new body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

The contents of a URL can be retrieved in two ways.

-   A client passes the contents of the URL into this method in the *pstmURL* parameter.
-   A client specifies a valid URL in the *pszBase* and *pszURL* parameters. Then, when the message is saved or when a client requests the data for the body, MimeOLE downloads the content.

Data in the object that *pstmURL* points to or the resource specified by *pszBase* and *pszURL* must be stored in either [**IET\_BINARY**](oe-encodingtype.md) or **IET\_DECODED** type. For more information, see **ENCODINGTYPE**.

When **URL\_ATTACH\_INTO\_MIXED** is specified in the *dwFlags* parameter, this method creates the new body in the [multipart/mixed](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) section of the message. If a multipart/mixed section does not exist, one is created. Otherwise, this method creates the new body in the multipart/related section of the message. If a multipart/related section does not exist, one is created.

When a client sets *pszBase* and *pszURL* to **NULL** and specifies the **URL\_ATTACH\_GENERATE\_CID** flag in the *dwFlags* parameter, MimeOLE generates and sets the PID\_HDR\_CNTID property of the new body. The client can receive a pointer to the generated [Content-ID](http://msdn.microsoft.com/library/ms526943.aspx) from the *ppszCIDURL* parameter.

When a client specifies a valid URL in *pszURL* but does not specify **URL\_ATTACH\_GENERATE\_CID** in the *dwFlags*, MimeOLE sets the PID\_HDR\_CNTLOC property for the new body.

When a client specifies a valid URL in *pszURL* and specifies **URL\_ATTACH\_SET\_CNTTYPE** in the *dwFlags*, MimeOLE sets the PID\_HDR\_CNTTYPE property for the new body. And when a client specifies a valid base URL in *pszBase*, MimeOLE sets the PIDR\_HDR\_CNTBASE property for the new body to *pszBase*.

To display an image inline with the body text of a message, a client can pass in the URL of the image and then reference the [Content-ID](http://msdn.microsoft.com/library/ms526943.aspx) string returned in *ppszCIDURL* in HTML.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





