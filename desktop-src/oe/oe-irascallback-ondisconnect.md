---
title: IRASCallback OnDisconnect method
description: Allows the client to decide if the current Remote Access Service (RAS) connection should be disconnected.
ms.assetid: c2464b20-528f-4166-a5f0-8e5b7e110e67
keywords:
- OnDisconnect method Windows Mail (formerly Outlook Express)
- OnDisconnect method Windows Mail (formerly Outlook Express) , IRASCallback interface
- IRASCallback interface Windows Mail (formerly Outlook Express) , OnDisconnect method
topic_type:
- apiref
api_name:
- IRASCallback.OnDisconnect
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

# IRASCallback::OnDisconnect method

\[**IRASCallback::OnDisconnect** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the client to decide if the current Remote Access Service (RAS) connection should be disconnected.

## Syntax


```C++
HRESULT OnDisconnect(
  [in] LPSTR         pszCurrentConnectoid,
  [in] BOOL          fConnectionOwner,
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

*fConnectionOwner* \[in\]
</dt> <dd>

Type: **BOOL**

Specifies a **BOOL** that indicates whether the client wants to terminate the current RAS connection. When this parameter is **TRUE**, the method returns S\_OK, which indicates that the client wants to disconnect the current session.

</dd> <dt>

*pTransport* \[in\]
</dt> <dd>

Type: **[**IRASTransport**](oe-irastransport.md)\***

Specifies a pointer to the [**IRASTransport**](oe-irastransport.md) object that established the connection.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                                  |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the client wants to terminate the RAS connection. <br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the client wants to keep the connection. <br/>          |



 

## Remarks

On application shutdown, the user may want to leave the RAS connection established even after the application using the connection has closed. The client application could show UI on this callback to prompt the user.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





