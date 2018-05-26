---
title: ISMTPTransport CommandMAIL method
description: Sends the MAIL FROM command to the server.
ms.assetid: 562c353b-c098-4edf-ac93-15bcbcebd605
keywords:
- CommandMAIL method Windows Mail (formerly Outlook Express)
- CommandMAIL method Windows Mail (formerly Outlook Express) , ISMTPTransport interface
- ISMTPTransport interface Windows Mail (formerly Outlook Express) , CommandMAIL method
topic_type:
- apiref
api_name:
- ISMTPTransport.CommandMAIL
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

# ISMTPTransport::CommandMAIL method

\[**ISMTPTransport::CommandMAIL** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the MAIL FROM: command to the server.

## Syntax


```C++
HRESULT CommandMAIL(
  [in] LPSTR pszEmailFrom
);
```



## Parameters

<dl> <dt>

*pszEmailFrom* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the sender's mailbox (for example, &lt;someone@example.com&gt;).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                 | Description                                                        |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Indicates success. <br/>                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                | Indicates that *pszEmailFrom* is **NULL**. <br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>               | Indicates that an attempt to allocate memory failed. <br/>   |
| <dl> <dt>**IXP\_E\_BUSY**</dt> </dl>                 | Indicates that the server connection is busy. <br/>          |
| <dl> <dt>**IXP\_E\_NOT\_INIT**</dt> </dl>            | Indicates that the transport has not been initialized. <br/> |
| <dl> <dt>**IXP\_E\_SOCKET\_WRITE\_ERROR**</dt> </dl> | Indicates that a transmission error occurred. <br/>          |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





