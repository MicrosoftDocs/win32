---
title: IRASCallback OnLogonPrompt method
description: Prompts for connection information to pass to the transport to establish a Remote Access Service (RAS) connection.
ms.assetid: 71d2b1e2-10a9-4812-a942-27eb77c30819
keywords:
- OnLogonPrompt method Windows Mail (formerly Outlook Express)
- OnLogonPrompt method Windows Mail (formerly Outlook Express) , IRASCallback interface
- IRASCallback interface Windows Mail (formerly Outlook Express) , OnLogonPrompt method
topic_type:
- apiref
api_name:
- IRASCallback.OnLogonPrompt
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

# IRASCallback::OnLogonPrompt method

\[**IRASCallback::OnLogonPrompt** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Prompts for connection information to pass to the transport to establish a Remote Access Service (RAS) connection.

## Syntax


```C++
HRESULT OnLogonPrompt(
  [in, out] LPIXPRASLOGON pRasLogon,
  [in]      IRASTransport *pTransport
);
```



## Parameters

<dl> <dt>

*pRasLogon* \[in, out\]
</dt> <dd>

Type: **LPIXPRASLOGON**

Receives a pointer to the [**IXPRASLOGON**](oe-ixpraslogon.md) structure that contains the connection information.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IRASTransport**](oe-irastransport.md)\***

Specifies a pointer to the [**IRASTransport**](oe-irastransport.md) object that established the connection.

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



 

 





