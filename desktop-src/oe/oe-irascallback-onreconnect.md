---
title: IRASCallback OnReconnect method
description: Prompts the user to pick which connection to use.
ms.assetid: 0d47210b-4ab3-4641-9625-c9ae2ce2f62c
keywords:
- OnReconnect method Windows Mail (formerly Outlook Express)
- OnReconnect method Windows Mail (formerly Outlook Express) , IRASCallback interface
- IRASCallback interface Windows Mail (formerly Outlook Express) , OnReconnect method
topic_type:
- apiref
api_name:
- IRASCallback.OnReconnect
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

# IRASCallback::OnReconnect method

\[**IRASCallback::OnReconnect** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Prompts the user to pick which connection to use.

## Syntax


```C++
HRESULT OnReconnect(
  [in] LPSTR         pszCurrentConnectoid,
  [in] LPSTR         pszNewConnectoid,
  [in] IRASTransport *pTransport
);
```



## Parameters

<dl> <dt>

*pszCurrentConnectoid* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the phone book entry used to establish the remote access connection.

</dd> <dt>

*pszNewConnectoid* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies an **LPSTR** that contains the phone book entry used to establish the new remote access connection.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IRASTransport**](oe-irastransport.md)\***

Specifies a pointer to the [**IRASTransport**](oe-irastransport.md) object that established the connection.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                         | Description                                                                                                   |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                | Indicates that the user wants to use the new connection specified by *pszNewConnectoid*. <br/>          |
| <dl> <dt>**S\_FALSE**</dt> </dl>             | Indicates that the user wants to keep the current connection specified by *pszCurrentConnectoid*. <br/> |
| <dl> <dt>**IXP\_E\_USER\_CANCEL**</dt> </dl> | Indicates that the user cancelled the prompt. <br/>                                                     |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





