---
title: IIMAPCallback OnResponse method
description: Called by the Internet Message Access Protocol (IMAP) transport interface when a command response or an unsolicited response is received from the IMAP server.
ms.assetid: c47e2d7f-ac0e-484e-82cb-63a5684a8e2c
keywords:
- OnResponse method Windows Mail (formerly Outlook Express)
- OnResponse method Windows Mail (formerly Outlook Express) , IIMAPCallback interface
- IIMAPCallback interface Windows Mail (formerly Outlook Express) , OnResponse method
topic_type:
- apiref
api_name:
- IIMAPCallback.OnResponse
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

# IIMAPCallback::OnResponse method

\[**IIMAPCallback::OnResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the Internet Message Access Protocol (IMAP) transport interface when a command response or an unsolicited response is received from the IMAP server.

## Syntax


```C++
HRESULT OnResponse(
  [in] const IMAP_RESPONSE *pirIMAPResponse
);
```



## Parameters

<dl> <dt>

*pirIMAPResponse* \[in\]
</dt> <dd>

Type: **const [**IMAP\_RESPONSE**](oe-imap-response.md)\***

Specifies a pointer to the [**IMAP\_RESPONSE**](oe-imap-response.md) structure returned to the client by this callback.

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



 

 





