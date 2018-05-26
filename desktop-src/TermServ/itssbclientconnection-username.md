---
title: ITsSbClientConnection UserName property
description: Retrieves a value that indicates the name of the user who initiated the connection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 74f4b8fb-efd4-46d7-9d2f-dd9ef583eb54
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- UserName property Remote Desktop Services
- UserName property Remote Desktop Services , ITsSbClientConnection interface
- ITsSbClientConnection interface Remote Desktop Services , UserName property
topic_type:
- apiref
api_name:
- ITsSbClientConnection.UserName
- ITsSbClientConnection.get_UserName
api_location:
- Sbtsv.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ITsSbClientConnection::UserName property

Retrieves a value that indicates the name of the user who initiated the connection.

This property is read-only.

## Syntax


```C++
HRESULT get_UserName(
  [out, retval] BSTR *pVal
);
```



## Property value

A pointer to a user name. When you have finished using the string, free it by calling the [**SysFreeString**](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbClientConnection**](/windows/win32/sbtsv/nn-sbtsv-itssbclientconnection?branch=master)
</dt> </dl>

 

 





