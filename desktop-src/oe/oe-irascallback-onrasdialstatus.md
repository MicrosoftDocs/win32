---
title: IRASCallback OnRasDialStatus method
description: Provides Remote Access Service (RAS) connection state information to the client application.
ms.assetid: 7e6908be-8f14-45c6-8e77-5d351d106548
keywords:
- OnRasDialStatus method Windows Mail (formerly Outlook Express)
- OnRasDialStatus method Windows Mail (formerly Outlook Express) , IRASCallback interface
- IRASCallback interface Windows Mail (formerly Outlook Express) , OnRasDialStatus method
topic_type:
- apiref
api_name:
- IRASCallback.OnRasDialStatus
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

# IRASCallback::OnRasDialStatus method

\[**IRASCallback::OnRasDialStatus** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides Remote Access Service (RAS) connection state information to the client application.

## Syntax


```C++
HRESULT OnRasDialStatus(
  [in] RASCONNSTATE  rasconnstate,
  [in] DWORD         dwError,
  [in] IRASTransport *pTransport
);
```



## Parameters

<dl> <dt>

*rasconnstate* \[in\]
</dt> <dd>

Type: **[RASCONNSTATE](http://msdn.microsoft.com/library/rras/rras/rasconnstate.asp)**

Specifies a value from the [RASCONNSTATE](http://msdn.microsoft.com/library/rras/rras/rasconnstate.asp) enumeration that indicates the current state of the RAS connection.

</dd> <dt>

*dwError* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the error. This parameter is zero when there is no error.

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



 

 





