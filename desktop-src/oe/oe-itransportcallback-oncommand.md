---
title: ITransportCallback OnCommand method
description: Used for logging and debugging commands sent to and responses received from the server.
ms.assetid: 81f64dfe-f1bf-4ccb-ac2a-56b054e4423b
keywords:
- OnCommand method Windows Mail (formerly Outlook Express)
- OnCommand method Windows Mail (formerly Outlook Express) , ITransportCallback interface
- ITransportCallback interface Windows Mail (formerly Outlook Express) , OnCommand method
topic_type:
- apiref
api_name:
- ITransportCallback.OnCommand
api_location:
- Msoe.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ITransportCallback::OnCommand method

\[**ITransportCallback::OnCommand** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Used for logging and debugging commands sent to and responses received from the server.

## Syntax


```C++
HRESULT OnCommand(
  [in] CMDTYPE            cmdtype,
  [in] LPSTR              pszLine,
  [in] HRESULT            hrResponse,
  [in] IInternetTransport *pTransport
);
```



## Parameters

<dl> <dt>

*cmdtype* \[in\]
</dt> <dd>

Type: **[**CMDTYPE**](oe-cmdtype.md)**

Specifies a [**CMDTYPE**](oe-cmdtype.md) that indicates a transport command or server response.

</dd> <dt>

*pszLine* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the data sent to or received from the server.

</dd> <dt>

*hrResponse* \[in\]
</dt> <dd>

Type: **HRESULT**

Specifies a response code. A failure code indicates that the transport has received an error from the server and that the current operation is probably going to fail.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IInternetTransport**](oe-iinternettransport.md)\***

Specifies a pointer to the [**IInternetTransport**](oe-iinternettransport.md) object that called **OnCommand**.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is not called when the call to [**Connect**](oe-iinternettransport-connect.md) passes **iitDISABLE\_ONCOMMAND** to the *fCommandLogging* parameter.

Calling this method costs a small amount of overhead.

## Requirements



|                                     |                                                                                                            |
|-------------------------------------|------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                       |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                             |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                      |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                    |
| DLL<br/>                      | <dl> <dt>Msoe.dll (version 6.0 or later)</dt> </dl> |



 

 





