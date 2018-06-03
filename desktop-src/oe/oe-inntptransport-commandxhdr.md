---
title: INNTPTransport CommandXHDR method
description: Issues an XHDR command to the server.
ms.assetid: caabba30-99c0-4bbd-9310-cd925b17445f
keywords:
- CommandXHDR method Windows Mail (formerly Outlook Express)
- CommandXHDR method Windows Mail (formerly Outlook Express) , INNTPTransport interface
- INNTPTransport interface Windows Mail (formerly Outlook Express) , CommandXHDR method
topic_type:
- apiref
api_name:
- INNTPTransport.CommandXHDR
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

# INNTPTransport::CommandXHDR method

\[**INNTPTransport::CommandXHDR** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Issues an `XHDR` command to the server. This command can specify a range of messages or a single message to retrieve the header from. If *pRange* is **NULL** and *pszMessageId* is **NULL** the header is retrieved from the message pointed to by the server's current message pointer (see STAT, NEXT, LAST).

## Syntax


```C++
HRESULT CommandXHDR(
  [in]           LPSTR   pszHeader,
  [in, optional] LPRANGE pRange,
  [in, optional] LPSTR   pszMessageId
);
```



## Parameters

<dl> <dt>

*pszHeader* \[in\]
</dt> <dd>

Type: **LPSTR**

Which header to retrieve. IE "subject" or "xref"

</dd> <dt>

*pRange* \[in, optional\]
</dt> <dd>

Type: **LPRANGE**

Range of messages to retrieve the header from

</dd> <dt>

*pszMessageId* \[in, optional\]
</dt> <dd>

Type: **LPSTR**

Message ID of the message to retrieve the header from

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





