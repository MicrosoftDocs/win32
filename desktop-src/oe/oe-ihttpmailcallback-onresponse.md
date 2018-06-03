---
title: IHTTPMailCallback OnResponse method
description: Called by the HTTPMail transport interface when a command response is received from the HTTP server.
ms.assetid: a2da38fc-8820-43a1-b4c9-434f3c1f1610
keywords:
- OnResponse method Windows Mail (formerly Outlook Express)
- OnResponse method Windows Mail (formerly Outlook Express) , IHTTPMailCallback interface
- IHTTPMailCallback interface Windows Mail (formerly Outlook Express) , OnResponse method
topic_type:
- apiref
api_name:
- IHTTPMailCallback.OnResponse
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

# IHTTPMailCallback::OnResponse method

\[**IHTTPMailCallback::OnResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the HTTPMail transport interface when a command response is received from the HTTP server.

## Syntax


```C++
HRESULT OnResponse(
  [in] LPHTTPMAILRESPONSE pResponse
);
```



## Parameters

<dl> <dt>

*pResponse* \[in\]
</dt> <dd>

Type: **LPHTTPMAILRESPONSE**

Specifies a pointer to the [**HTTPMAILRESPONSE**](oe-httpmailresponse.md) structure that contains the response information.

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



 

 





