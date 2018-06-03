---
title: IMimeMessage GetTextBody method
description: Gets the text body for the message.
ms.assetid: 99be1733-2952-42b2-9d34-695222b27947
keywords:
- GetTextBody method Windows Mail (formerly Outlook Express)
- GetTextBody method Windows Mail (formerly Outlook Express) , IMimeMessage interface
- IMimeMessage interface Windows Mail (formerly Outlook Express) , GetTextBody method
topic_type:
- apiref
api_name:
- IMimeMessage.GetTextBody
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

# IMimeMessage::GetTextBody method

Gets the text body for the message.

## Syntax


```C++
HRESULT GetTextBody(
  [in]  DWORD        dwTxtType,
  [in]  ENCODINGTYPE ietEncoding,
  [out] IStream      **ppStream,
  [out] LPHBODY      phBody
);
```



## Parameters

<dl> <dt>

*dwTxtType* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the type of text body to retrieve.



| Value                                                                                                                                                                                                             | Meaning                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| <span id="TXT_PLAIN"></span><span id="txt_plain"></span><dl> <dt>**TXT\_PLAIN**</dt> <dt>0x00000001</dt> </dl> | [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) is text/plain. <br/> |
| <span id="TXT_HTML"></span><span id="txt_html"></span><dl> <dt>**TXT\_HTML**</dt> <dt>0x00000002</dt> </dl>    | [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp) is text/html. <br/>  |



 

</dd> <dt>

*ietEncoding* \[in\]
</dt> <dd>

Type: **[**ENCODINGTYPE**](oe-encodingtype.md)**

Specifies an [**ENCODINGTYPE**](oe-encodingtype.md) value that indicates how the data in *ppStream* should be encoded. Either **IET\_DECODED**, **IET\_BINARY**, or **IET\_UNICODE** is a typical value for this parameter.

</dd> <dt>

*ppStream* \[out\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\*\***

Receives an address to a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains the text body. The client is responsible for releasing this object.

</dd> <dt>

*phBody* \[out\]
</dt> <dd>

Type: **LPHBODY**

Receives the handle of the text body that was found.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                                        |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success.<br/>                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Indicates that an unknown error has occurred.<br/>                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed.<br/>                    |
| <dl> <dt>**MIME\_E\_INVALID\_TEXT\_TYPE**</dt> </dl> | Indicates that the value specified by *dwTxtType* is not valid. <br/>        |
| <dl> <dt>**MIME\_E\_NOT\_FOUND**</dt> </dl>          | Indicates that the message does not have a text body. <br/>                  |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>            | Indicates that the text body that was found does not contain any data. <br/> |



 

## Remarks

Typically, if a client supports HTML, the client would request TXT\_HTML first. If that fails, then it would request TXT\_PLAIN.

This method excludes bodies that are marked as attachments. The text body is usually what a client requests to display the body of a message to the user. MimeOLE treats a text/enriched type body as text/html and converts it to valid HTML.

For a MIME Encapsulation of Aggregate HTML Documents (MHTML) message, MimeOLE uses the start parameter that is associated with multipart/related bodies to locate the correct text body.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





