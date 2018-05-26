---
title: ISMTPCallback OnResponse method
description: Called by the Simple Mail Transport Protocol (SMTP) transport interface when a command response is received from the SMTP server.
ms.assetid: d8aaa2a9-6c8e-4aa0-aa12-8ca9ed48f9de
keywords:
- OnResponse method Windows Mail (formerly Outlook Express)
- OnResponse method Windows Mail (formerly Outlook Express) , ISMTPCallback interface
- ISMTPCallback interface Windows Mail (formerly Outlook Express) , OnResponse method
topic_type:
- apiref
api_name:
- ISMTPCallback.OnResponse
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

# ISMTPCallback::OnResponse method

\[**ISMTPCallback::OnResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by the Simple Mail Transport Protocol (SMTP) transport interface when a command response is received from the SMTP server.

## Syntax


```C++
HRESULT OnResponse(
  [in] LPSMTPRESPONSE pResponse
);
```



## Parameters

<dl> <dt>

*pResponse* \[in\]
</dt> <dd>

Type: **LPSMTPRESPONSE**

Specifies a pointer to the [**SMTPRESPONSE**](oe-smtpresponse.md) structure that contains the response information.

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



 

 





