---
title: ISMTPTransport SendMessage method
description: Sends a Simple Mail Transport Protocol (SMTP) message.
ms.assetid: d41de1ab-1d1b-4ed1-86ed-ee605e34a26c
keywords:
- SendMessage method Windows Mail (formerly Outlook Express)
- SendMessage method Windows Mail (formerly Outlook Express) , ISMTPTransport interface
- ISMTPTransport interface Windows Mail (formerly Outlook Express) , SendMessage method
topic_type:
- apiref
api_name:
- ISMTPTransport.SendMessage
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

# ISMTPTransport::SendMessage method

\[**ISMTPTransport::SendMessage** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends a Simple Mail Transport Protocol (SMTP) message.

## Syntax


```C++
HRESULT SendMessage(
  [in] LPSMTPMESSAGE pMessage
);
```



## Parameters

<dl> <dt>

*pMessage* \[in\]
</dt> <dd>

Type: **LPSMTPMESSAGE**

Specifies a pointer to the [**SMTPMESSAGE**](oe-smtpmessage.md) structure that contains the message to send.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                   | Description                                                                                                                                                                                   |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                          | Indicates success. <br/>                                                                                                                                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                  | Indicates that *pMessage* is **NULL** or that the message stream is **NULL**. <br/>                                                                                                     |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>                 | Indicates that an attempt to allocate memory failed. <br/>                                                                                                                              |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                   | Indicates that the transport is busy. <br/>                                                                                                                                             |
| <dl> <dt>**IXP\_E\_INVALID\_ADDRESS\_LIST**</dt> </dl> | Indicates that **rInetAddrList** contains invalid entries. <br/>                                                                                                                        |
| <dl> <dt>**IXP\_E\_NOT\_CONNECTED**</dt> </dl>         | Indicates that [**Connect**](oe-iinternettransport-connect.md) has not been called or that the current connection has been lost. The transport does not automatically reconnect. <br/> |
| <dl> <dt>**IXP\_S\_SMTP\_NO\_DSN\_SUPPORT**</dt> </dl> | Indicates that the server doesn't support DSN.<br/>                                                                                                                                     |



 

## Remarks

[**Connect**](oe-iinternettransport-connect.md) must be called before this method and the transport must be in the ready state. When the message is finished or if an error ocurrs, [**OnResponse**](oe-ismtpcallback-onresponse.md) is called.

This method duplicates the contents of *pMessage* and adds a reference for *pMessage*-&gt;**pstmMsg** so that the client can free *pMessage* immediately after calling this method.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





