---
title: ITsSbClientConnection UserName property
description: Retrieves a value that indicates the name of the user who initiated the connection.
ms.assetid: 74f4b8fb-efd4-46d7-9d2f-dd9ef583eb54
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
ms.topic: reference
ms.date: 05/31/2018
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

A pointer to a user name. When you have finished using the string, free it by calling the [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                       |
| IDL<br/>                      | <dl> <dt>Sbtsv.idl</dt> </dl> |



## See also

<dl> <dt>

[**ITsSbClientConnection**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbclientconnection)
</dt> </dl>

 

