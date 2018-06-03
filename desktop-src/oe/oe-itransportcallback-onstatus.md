---
title: ITransportCallback OnStatus method
description: Allows the client to provide a user with a high-level progress indicator.
ms.assetid: d13c272a-30f6-4629-a783-0da643d7470b
keywords:
- OnStatus method Windows Mail (formerly Outlook Express)
- OnStatus method Windows Mail (formerly Outlook Express) , ITransportCallback interface
- ITransportCallback interface Windows Mail (formerly Outlook Express) , OnStatus method
topic_type:
- apiref
api_name:
- ITransportCallback.OnStatus
api_location:
- Msoe.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITransportCallback::OnStatus method

\[**ITransportCallback::OnStatus** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the client to provide a user with a high-level progress indicator.

## Syntax


```C++
HRESULT OnStatus(
  [in] IXPSTATUS          ixpstatus,
  [in] IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*ixpstatus* \[in\]
</dt> <dd>

Type: **[**IXPSTATUS**](oe-ixpstatus.md)**

Specifies an [**IXPSTATUS**](oe-ixpstatus.md) value that indicates the current status of the transport.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnStatus**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





