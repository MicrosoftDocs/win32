---
title: IInternetTransport GetStatus method
description: Gets the current status of the transport.
ms.assetid: fc22f913-768e-4426-a431-ecda4560da22
keywords:
- GetStatus method Windows Mail (formerly Outlook Express)
- GetStatus method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , GetStatus method
topic_type:
- apiref
api_name:
- IInternetTransport.GetStatus
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

# IInternetTransport::GetStatus method

\[**IInternetTransport::GetStatus** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Gets the current status of the transport.

## Syntax


```C++
HRESULT GetStatus(
  [out] IXPSTATUS *pCurrentStatus
);
```



## Parameters

<dl> <dt>

*pCurrentStatus* \[out\]
</dt> <dd>

Type: **[**IXPSTATUS**](oe-ixpstatus.md)\***

Receives a pointer to the [**IXPSTATUS**](oe-ixpstatus.md) value that indicates the transport status.

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



 

 





