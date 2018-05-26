---
title: ITsSbClientConnection Domain property
description: Retrieves a value that indicates the domain name of the Remote Desktop Connection (RDC) client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 628f450d-10f4-4405-8d7c-ae58c72c2755
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- Domain property Remote Desktop Services
- Domain property Remote Desktop Services , ITsSbClientConnection interface
- ITsSbClientConnection interface Remote Desktop Services , Domain property
topic_type:
- apiref
api_name:
- ITsSbClientConnection.Domain
- ITsSbClientConnection.get_Domain
api_location:
- Sbtsv.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ITsSbClientConnection::Domain property

Retrieves a value that indicates the domain name of the Remote Desktop Connection (RDC) client.

This property is read-only.

## Syntax


```C++
HRESULT get_Domain(
  [out, retval] BSTR *pVal
);
```



## Property value

A pointer to a **BSTR** variable that contains the domain name of the RDC client. When you have finished using the string, free it by calling the [**SysFreeString**](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function.

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

 

 





