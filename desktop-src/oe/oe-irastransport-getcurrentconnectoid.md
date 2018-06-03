---
title: IRASTransport GetCurrentConnectoid method
description: Returns entry name of the current Remote Access Service (RAS) connection.
ms.assetid: 1a0e337e-927f-48cf-bf81-8a6b3e760413
keywords:
- GetCurrentConnectoid method Windows Mail (formerly Outlook Express)
- GetCurrentConnectoid method Windows Mail (formerly Outlook Express) , IRASTransport interface
- IRASTransport interface Windows Mail (formerly Outlook Express) , GetCurrentConnectoid method
topic_type:
- apiref
api_name:
- IRASTransport.GetCurrentConnectoid
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

# IRASTransport::GetCurrentConnectoid method

\[**IRASTransport::GetCurrentConnectoid** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns entry name of the current Remote Access Service (RAS) connection.

## Syntax


```C++
HRESULT GetCurrentConnectoid(
  [in] LPSTR pszConnectoid,
  [in] ULONG cchMax
);
```



## Parameters

<dl> <dt>

*pszConnectoid* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the phone book entry used to establish the remote access connection.

</dd> <dt>

*cchMax* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the size in bytes of *pszConnectoid*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                           | Description                                                                               |
|-------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Indicates success. <br/>                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>          | Indicates that *pszConnectoid* is **NULL** or that *cchMax* is out of bounds. <br/> |
| <dl> <dt>**IXP\_E\_NOT\_CONNECTED**</dt> </dl> | Indicates that there is no connection. <br/>                                        |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





