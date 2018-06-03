---
title: IPOP3Callback OnResponse method
description: Called by the Post Office Protocol version 3 (POP3) transport interface when a command response is received from the POP3 server.
ms.assetid: 5554e849-cd3e-4324-a512-1ca57543a4e2
keywords:
- OnResponse method Windows Mail (formerly Outlook Express)
- OnResponse method Windows Mail (formerly Outlook Express) , IPOP3Callback interface
- IPOP3Callback interface Windows Mail (formerly Outlook Express) , OnResponse method
topic_type:
- apiref
api_name:
- IPOP3Callback.OnResponse
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

# IPOP3Callback::OnResponse method

\[**IPOP3Callback::OnResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the Post Office Protocol version 3 (POP3) transport interface when a command response is received from the POP3 server.

## Syntax


```C++
HRESULT OnResponse(
  [in] LPPOP3RESPONSE pResponse
);
```



## Parameters

<dl> <dt>

*pResponse* \[in\]
</dt> <dd>

Type: **LPPOP3RESPONSE**

Specifies a pointer to the [**POP3RESPONSE**](oe-pop3response.md) structure that contains the response information.

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



 

 





