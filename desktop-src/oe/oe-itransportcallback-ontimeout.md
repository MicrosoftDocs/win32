---
title: ITransportCallback OnTimeout method
description: Called by a transport when a timeout period has expired.
ms.assetid: 4174fa42-24d2-46e3-822d-92c46c069d8f
keywords:
- OnTimeout method Windows Mail (formerly Outlook Express)
- OnTimeout method Windows Mail (formerly Outlook Express) , ITransportCallback interface
- ITransportCallback interface Windows Mail (formerly Outlook Express) , OnTimeout method
topic_type:
- apiref
api_name:
- ITransportCallback.OnTimeout
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

# ITransportCallback::OnTimeout method

\[**ITransportCallback::OnTimeout** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Called by a transport when a timeout period has expired.

## Syntax


```C++
HRESULT OnTimeout(
  [in, out] DWORD              *pdwTimeout,
  [in]      IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*pdwTimeout* \[in, out\]
</dt> <dd>

Type: **DWORD\***

Specifies a pointer to a **DWORD** that contains the current timeout value in seconds. A client can reset this value to a new timeout value and return S\_OK, in which case the client will continue waiting during the new timeout period.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnTimeout**.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values: 



| Return code                                                                             | Description                                                                                                                 |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the transport should wait an additional timeout period as specified by the value of *pdwTimeout*.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the transport should terminate its connection and return to the disconnected state. <br/>              |



 

## Remarks

A timeout is defined as a period of time in which no activity has occurred. A client can specify a timeout in the [**INETSERVER**](oe-inetserver.md) structure that is passed to the [**Connect**](oe-iinternettransport-connect.md) method. When this method is called, the client must return a value that indicates whether the transport should continue to wait or should terminate the connection to the server.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





