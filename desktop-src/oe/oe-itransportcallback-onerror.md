---
title: ITransportCallback OnError method
description: Handles high-level errors such as TCP/IP and connection failures.
ms.assetid: '156a21d8-eb6f-4874-873c-3f12672f93ee'
keywords: ["OnError method Windows Mail (formerly Outlook Express)", "OnError method Windows Mail (formerly Outlook Express) , ITransportCallback interface", "ITransportCallback interface Windows Mail (formerly Outlook Express) , OnError method"]
topic_type:
- apiref
api_name:
- ITransportCallback.OnError
api_location:
- Msoe.dll
api_type:
- COM
---

# ITransportCallback::OnError method

\[**ITransportCallback::OnError** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Handles high-level errors such as TCP/IP and connection failures.

## Syntax


```C++
HRESULT OnError(
  [in] IXPSTATUS          ixpstatus,
  [in] LPIXPRESULT        pResult,
  [in] IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*ixpstatus* \[in\]
</dt> <dd>

Type: **[**IXPSTATUS**](oe-ixpstatus.md)**

Specifies an [**IXPSTATUS**](oe-ixpstatus.md) value that indicates the current status of the transport.

</dd> <dt>

*pResult* \[in\]
</dt> <dd>

Type: **LPIXPRESULT**

Specifies a pointer to an [**IXPRESULT**](oe-ixpresult.md) structure that contains the error information.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnError**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

A transport calls this method when it encounters a fatal error like disconnection from the server. Normal protocol errors are returned through each transport's **OnResponse** method.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





