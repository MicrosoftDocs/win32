---
title: IMimeMessage CreateWebPage method
description: Creates a moniker that can be used to bind to the HTML representation of the message object.
ms.assetid: 'e25cfe34-f538-47d8-b6a4-5353b80d013d'
keywords: ["CreateWebPage method Windows Mail (formerly Outlook Express)", "CreateWebPage method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , CreateWebPage method"]
topic_type:
- apiref
api_name:
- IMimeMessage.CreateWebPage
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::CreateWebPage method

Creates a moniker that can be used to bind to the HTML representation of the message object.

## Syntax


```C++
HRESULT CreateWebPage(
  [in]  IStream              *pRootStm,
  [in]  LPWEBPAGEOPTIONS     pOptions,
  [in]  IMimeMessageCallback *pCallback,
  [out] IMoniker             **ppMoniker
);
```



## Parameters

<dl> <dt>

*pRootStm* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to an [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) interface that is used as the primary HTML source for the webpage. If this parameter is **NULL**, choosesimeOLE chooses the correct body to use as the HTML source for the webpage.

</dd> <dt>

*pOptions* \[in\]
</dt> <dd>

Type: **LPWEBPAGEOPTIONS**

Specifies the [**WEBPAGEOPTIONS**](oe-webpageoptions.md) to use to build the webpage.

</dd> <dt>

*pCallback* \[in\]
</dt> <dd>

Type: **[**IMimeMessageCallback**](oe-imimemessagecallback.md)\***

Specifies a pointer to the [**IMimeMessageCallback**](oe-imimemessagecallback.md) interface to use to build the webpage.

</dd> <dt>

*ppMoniker* \[out\]
</dt> <dd>

Type: **[IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp)\*\***

Receives the address of a pointer to a [IMoniker](http://msdn.microsoft.com/library/com/htm/cmi_m_8otu.asp) interface. The client is responsible for releasing this object.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                                                                                                                                                                |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>                                                                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *ppMoniker* is **NULL** or that *pOptions* is not **NULL** and *pOptions*-&gt;**cbSize** does not equal the size of a valid [**WEBPAGEOPTIONS**](oe-webpageoptions.md) structure.<br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates an attempt to allocate memory failed.<br/>                                                                                                                                                   |



 

## Remarks

The moniker returned from this method can be loaded into another object that supports [**IPersistMoniker**](https://msdn.microsoft.com/library/ms775042).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





