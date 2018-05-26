---
title: IHTTPMailTransport CommandGET method
description: Sends the GET command to the HTTPMail server.
ms.assetid: acf9a347-6da0-4cc2-9388-668bdccda1cb
keywords:
- CommandGET method Windows Mail (formerly Outlook Express)
- CommandGET method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , CommandGET method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.CommandGET
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IHTTPMailTransport::CommandGET method

\[**IHTTPMailTransport::CommandGET** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the GET command to the HTTPMail server.

## Syntax


```C++
HRESULT CommandGET(
  [in] LPCSTR pszPath,
  [in] LPCSTR *rgszAcceptTypes,
  [in] BOOL   fTranslate,
  [in] DWORD  dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the entity to retrieve.

</dd> <dt>

*rgszAcceptTypes* \[in\]
</dt> <dd>

Type: **LPCSTR\***

Specifies a pointer to an **LPCSTR** that contains a **null**-terminated list of MIME accept types accepted by the client.

</dd> <dt>

*fTranslate* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether to send the HTTP request header Translate.



| Value                                                                                                                                | Meaning                                                                |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Do not send the Translate request header. <br/>                  |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Send the Translate request header and set it to **FALSE**. <br/> |



 

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                      |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                   |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath* is **NULL**. <br/>                |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





