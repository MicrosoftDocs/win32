---
title: ISMTPTransport2 CommandRCPT2 method
description: Sends the RCPT TO command to the server with Delivery Status Notification (DSN) support.
ms.assetid: b7aac7c1-2f8f-4ac0-82ef-b2da07edb347
keywords:
- CommandRCPT2 method Windows Mail (formerly Outlook Express)
- CommandRCPT2 method Windows Mail (formerly Outlook Express) , ISMTPTransport2 interface
- ISMTPTransport2 interface Windows Mail (formerly Outlook Express) , CommandRCPT2 method
topic_type:
- apiref
api_name:
- ISMTPTransport2.CommandRCPT2
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

# ISMTPTransport2::CommandRCPT2 method

\[**ISMTPTransport2::CommandRCPT2** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the RCPT TO: command to the server with Delivery Status Notification (DSN) support.

## Syntax


```C++
HRESULT CommandRCPT2(
  [in] LPSTR        pszEmailTo,
  [in] INETADDRTYPE atDSN
);
```



## Parameters

<dl> <dt>

*pszEmailTo* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the recipient's mailbox (for example, &lt;someone@example.com&gt;).

</dd> <dt>

*atDSN* \[in\]
</dt> <dd>

Type: **[**INETADDRTYPE**](oe-inetaddrtype.md)**

Specifies a [**INETADDRTYPE**](oe-inetaddrtype.md) value that indicates how to handle DSN.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszEmailTo* is **NULL**. <br/> |



 

## Remarks

The transport must send the EHLO command to the server before making a request for a DSN.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





