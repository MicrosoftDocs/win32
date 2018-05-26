---
title: INNTPCallback OnResponse method
description: In one or more calls, sets up a NNTPRESPONSE structure that is the general holder for all of the data returned from the INNTPTransport commands.
ms.assetid: e8891124-f35a-4bcb-97b2-5c2fa0ac0601
keywords:
- OnResponse method Windows Mail (formerly Outlook Express)
- OnResponse method Windows Mail (formerly Outlook Express) , INNTPCallback interface
- INNTPCallback interface Windows Mail (formerly Outlook Express) , OnResponse method
topic_type:
- apiref
api_name:
- INNTPCallback.OnResponse
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

# INNTPCallback::OnResponse method

\[**OnResponse** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

In one or more calls, sets up a [**NNTPRESPONSE**](oe-nntpresponse.md) structure that is the general holder for all of the data returned from the [**INNTPTransport**](oe-inntptransport.md) commands.

## Syntax


```C++
HRESULT OnResponse(
  [in] LPNNTPRESPONSE pResponse
);
```



## Parameters

<dl> <dt>

*pResponse* \[in\]
</dt> <dd>

Type: **LPNNTPRESPONSE**

Specifies a [**NNTPRESPONSE**](oe-nntpresponse.md) structure.

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



 

 





