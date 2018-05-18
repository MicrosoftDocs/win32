---
title: IMimeMessage GetAttachments method
description: Gets an array of attachments for the message.
ms.assetid: 'd2f05ef0-2c13-4913-b753-331d533ecacd'
keywords: ["GetAttachments method Windows Mail (formerly Outlook Express)", "GetAttachments method Windows Mail (formerly Outlook Express) , IMimeMessage interface", "IMimeMessage interface Windows Mail (formerly Outlook Express) , GetAttachments method"]
topic_type:
- apiref
api_name:
- IMimeMessage.GetAttachments
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeMessage::GetAttachments method

Gets an array of attachments for the message.

## Syntax


```C++
HRESULT GetAttachments(
  [out] ULONG   *pcAttach,
  [out] LPHBODY *pprghAttach
);
```



## Parameters

<dl> <dt>

*pcAttach* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of attachments.

</dd> <dt>

*pprghAttach* \[out\]
</dt> <dd>

Type: **LPHBODY\***

Receives a pointer to an array of attachment body handles. *pcAttach* contains the size of the array. The client is responsible for freeing this pointer by calling [IMalloc::Free](http://msdn.microsoft.com/library/com/htm/cmi_m_1smd.asp).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_FAIL**</dt> </dl>        | Indicates that an unknown error has occurred. <br/>       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that *pcAttach* is **NULL**.<br/>               |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

A body in the message cannot be returned as an attachment if it meets any of the following criteria.

-   The body has a [multipart/\*](http://msdn.microsoft.com/library/cdosys/html/31d6dbf5-cbfb-45d7-82f1-66090942161d.asp) [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp).
-   The body is empty (for example, if [**IsType**](oe-imimebody-istype.md)([**IBT\_EMPTY**](oe-imsgbodytype.md)) returns S\_OK).
-   The client is hiding Transport Neutral Encapsulation Format (TNEF) attachments and the body's Content-Type is equal to application/ms-tnef.
-   The body has not been rendered, or it has been rendered and auto-inlined. The PID\_ATT\_RENDERED property is used to determine whether a body has been rendered and the PID\_ATT\_AUTOINLINED property is used to determine whether a body has been auto-inlined. Rendering a message using the [**IMimeMessage::CreateWebPage**](oe-imimemessage-createwebpage.md) method sets these properties. A client renders a message and then calls **IMimeMessage::GetAttachments** to get all the bodies that were not presented to the user. When a client renders a body (for example, using [**IMimeMessage::GetTextBody**](oe-imimemessage-gettextbody.md)), it should set the PID\_ATT\_RENDERED property to **TRUE** so that the body does not show up as an attachment.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





