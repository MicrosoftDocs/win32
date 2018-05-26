---
title: IIMAPTransport Append method
description: Sends the APPEND command to the Internet Message Access Protocol (IMAP) server.
ms.assetid: 103b7b9b-78a7-421f-a12b-41eb484f3e22
keywords:
- Append method Windows Mail (formerly Outlook Express)
- Append method Windows Mail (formerly Outlook Express) , IIMAPTransport interface
- IIMAPTransport interface Windows Mail (formerly Outlook Express) , Append method
topic_type:
- apiref
api_name:
- IIMAPTransport.Append
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

# IIMAPTransport::Append method

\[**IIMAPTransport::Append** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the APPEND command to the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
HRESULT Append(
  [in] WPARAM        wParam,
  [in] LPARAM        lParam,
  [in] IIMAPCallback *pCBHandler,
  [in] LPCSTR        lpszMailboxName,
  [in] LPCSTR        lpszMessageFlags,
  [in] FILETIME      ftMessageDateTime,
  [in] LPSTREAM      lpstmMessageToSave
);
```



## Parameters

<dl> <dt>

*wParam* \[in\]
</dt> <dd>

Type: **WPARAM**

Specifies a **WPARAM** that together with *lParam* forms a unique transaction ID assigned by the caller to this IMAP command and its responses. The value can be anything except zero, which is reserved for unsolicited responses.

</dd> <dt>

*lParam* \[in\]
</dt> <dd>

Type: **LPARAM**

Specifies an **LPARAM** that together with *wParam* forms a unique transaction ID assigned by the caller to this IMAP command and its responses. The value can be anything except zero, which is reserved for unsolicited responses.

</dd> <dt>

*pCBHandler* \[in\]
</dt> <dd>

Type: **[**IIMAPCallback**](oe-iimapcallback.md)\***

Specifies a pointer to the [**IIMAPCallback**](oe-iimapcallback.md) interface to use to process the responses for this command. If this parameter is **NULL**, then the default callback interface is used. The default callback interface is specified in the [**IIMAPTransport::InitNew**](oe-iimaptransport-initnew.md) method, which initialized this [**IIMAPTransport**](oe-iimaptransport.md) object.

</dd> <dt>

*lpszMailboxName* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains the IMAP-compliant mailbox name as a multibyte string.

</dd> <dt>

*lpszMessageFlags* \[in\]
</dt> <dd>

Type: **LPCSTR**

Specifies an **LPCSTR** that contains an IMAP-compliant list of message flags to set for message. Set this parameter to **NULL** to indicate no message flags. See [**IMAP\_MSGFLAGS**](oe-imap-msgflags-constants.md) for a list of flags; use the message flag names described, not the constants.

</dd> <dt>

*ftMessageDateTime* \[in\]
</dt> <dd>

Type: **[FILETIME](http://msdn.microsoft.com/library/com/htm/cms_a2z_3vdx.asp)**

Specifies the date and time (Greenwich Mean Time (GMT)/UTC) to associate with the message.

</dd> <dt>

*lpstmMessageToSave* \[in\]
</dt> <dd>

Type: **LPSTREAM**

Specifies a stream that contains the message to save in [RFC 822](http://www.ietf.org/rfc/rfc822.txt) format.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                     | Description                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                            | Indicates success. <br/>                                                                         |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | Indicates that an unknown error has occurred. <br/>                                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                   | Indicates that an attempt to allocate memory failed. <br/>                                       |
| <dl> <dt>**IXP\_E\_IMAP\_IMPROPER\_SVRSTATE**</dt> </dl> | Indicates that the server is not in an authenticated state and cannot accept this command. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





