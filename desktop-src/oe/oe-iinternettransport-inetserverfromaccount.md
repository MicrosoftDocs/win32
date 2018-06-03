---
title: IInternetTransport InetServerFromAccount method
description: Populates an INETSERVER structure based on the specified IImnAccount object.
ms.assetid: f40382bc-c9cf-4332-a8d3-9cf926ce6118
keywords:
- InetServerFromAccount method Windows Mail (formerly Outlook Express)
- InetServerFromAccount method Windows Mail (formerly Outlook Express) , IInternetTransport interface
- IInternetTransport interface Windows Mail (formerly Outlook Express) , InetServerFromAccount method
topic_type:
- apiref
api_name:
- IInternetTransport.InetServerFromAccount
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

# IInternetTransport::InetServerFromAccount method

\[**IInternetTransport::InetServerFromAccount** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Populates an [**INETSERVER**](oe-inetserver.md) structure based on the specified [**IImnAccount**](oe-iimnaccount.md) object.

## Syntax


```C++
HRESULT InetServerFromAccount(
  [in]      IImnAccount  *pAccount,
  [in, out] LPINETSERVER pInetServer
);
```



## Parameters

<dl> <dt>

*pAccount* \[in\]
</dt> <dd>

Type: **[**IImnAccount**](oe-iimnaccount.md)\***

Specifies an [**IImnAccount**](oe-iimnaccount.md) object that represents an IMN account.

</dd> <dt>

*pInetServer* \[in, out\]
</dt> <dd>

Type: **LPINETSERVER**

Receives a pointer to an [**INETSERVER**](oe-inetserver.md) structure that contains the server information required to call [**IInternetTransport::Connect**](oe-iinternettransport-connect.md).

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                         |
|---------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success. <br/>                                      |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pAccount* or *pInetServer* is **NULL**. <br/> |
| <dl> <dt>**IXP\_E\_INVALID\_ACCOUNT**</dt> </dl> | Indicates that the account cannot be found. <br/>             |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





