---
title: IHTTPMailTransport SendMessage method
description: Sends a message using an HTTP server that supports RFC 821 sending.
ms.assetid: 65b539b5-1352-433b-b205-5dbd3b61164b
keywords:
- SendMessage method Windows Mail (formerly Outlook Express)
- SendMessage method Windows Mail (formerly Outlook Express) , IHTTPMailTransport interface
- IHTTPMailTransport interface Windows Mail (formerly Outlook Express) , SendMessage method
topic_type:
- apiref
api_name:
- IHTTPMailTransport.SendMessage
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

# IHTTPMailTransport::SendMessage method

\[**IHTTPMailTransport::SendMessage** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends a message using an HTTP server that supports [RFC 821](http://www.ietf.org/rfc/rfc821.txt) sending.

## Syntax


```C++
HRESULT SendMessage(
  [in] LPCSTR           pszPath,
  [in] LPCSTR           pszFrom,
  [in] LPHTTPTARGETLIST pTargets,
  [in] BOOL             fSaveInSent,
  [in] IStream          *pMessageStream,
  [in] DWORD            dwContext
);
```



## Parameters

<dl> <dt>

*pszPath* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains a **null**-terminated string that is the complete URL to the resource.

</dd> <dt>

*pszFrom* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the "from" address associated with the outbound mail. The address must be of the form *mailbox@domain.extension*.

</dd> <dt>

*pTargets* \[in\]
</dt> <dd>

Type: **LPHTTPTARGETLIST**

Specifies a pointer to the [**HTTPTARGETLIST**](oe-httptargetlist.md) structure that contains the list of email addresses that receive copies of the message. This list should include all direct recipients as well as copied (cc) and blind-copied (bcc) recipients. Addresses must be of the form: *mailbox@domain.extension*.

</dd> <dt>

*fSaveInSent* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether the server should save a copy of the outbound message in the user's Sent Items folder. The server determines the specific behavior associated with saving an outbound message.

</dd> <dt>

*pMessageStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object that contains an [RFC 822](http://www.ietf.org/rfc/rfc822.txt) compliant message. This method does not validate the contents of the stream. The caller is responsible for ensuring that the message is [RFC 822](http://www.ietf.org/rfc/rfc822.txt) compliant.

</dd> <dt>

*dwContext* \[in\]
</dt> <dd>

Type: **DWORD**

Currently unused. Should be set to zero.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                                                   |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pszPath*, *pszFrom*, *pTargets*, or *pMessageStream* is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed. <br/>                              |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





