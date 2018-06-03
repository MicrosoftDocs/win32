---
title: ISMTPTransport CommandRCPT method
description: Sends the RCPT TO command to the server.
ms.assetid: 24850796-b4fd-4d39-8150-00b1323c805d
keywords:
- CommandRCPT method Windows Mail (formerly Outlook Express)
- CommandRCPT method Windows Mail (formerly Outlook Express) , ISMTPTransport interface
- ISMTPTransport interface Windows Mail (formerly Outlook Express) , CommandRCPT method
topic_type:
- apiref
api_name:
- ISMTPTransport.CommandRCPT
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

# ISMTPTransport::CommandRCPT method

\[**ISMTPTransport::CommandRCPT** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sends the RCPT TO: command to the server.

## Syntax


```C++
HRESULT CommandRCPT(
  [in] LPSTR pszEmailTo
);
```



## Parameters

<dl> <dt>

*pszEmailTo* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the recipient's mailbox (for example, &lt;someone@example.com&gt;).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                       |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *pszEmailTo* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





