---
title: IPC\_USER structure
description: Represents a user or a group ID of a particular type.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 34162096-c365-4bfc-9b11-665559681b31
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_USER structure Active Directory Rights Management Services SDK 2.0
- PIPC_USER structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_USER structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_USER
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
---

# IPC\_USER structure

Represents a user or a group ID of a particular type.

## Syntax


```C++
typedef struct _IPC_USER {
  DWORD   dwType;
  LPCWSTR wszID;
} IPC_USER, *PIPC_USER;typedef const IPC_USER *PCIPC_USER;
```



## Members

<dl> <dt>

**dwType**
</dt> <dd>

The type of principal that has been granted rights in the license. The value of **wszID** must match the specified type.

<dt>

<span id="IPC_USER_TYPE_EMAIL"></span><span id="ipc_user_type_email"></span>

<span id="IPC_USER_TYPE_EMAIL"></span><span id="ipc_user_type_email"></span>**IPC\_USER\_TYPE\_EMAIL** (1)


</dt> <dd>

Email address.

</dd> <dt>

<span id="IPC_USER_TYPE_IPC"></span><span id="ipc_user_type_ipc"></span>

<span id="IPC_USER_TYPE_IPC"></span><span id="ipc_user_type_ipc"></span>**IPC\_USER\_TYPE\_IPC** (2)


</dt> <dd>

IPC-internal user or group ID.

</dd> </dl> </dd> <dt>

**wszID**
</dt> <dd>

The user or group ID. Depending on the value of **dwType** this is either an email address or one of the following user or group ID values.

If **wszID** is set to one of the values in the possible values set that follows, **dwType** should be set to **IPC\_USER\_TYPE\_IPC**.

<dt>

<span id="IPC_USER_ID_EVERYONE"></span><span id="ipc_user_id_everyone"></span>

<span id="IPC_USER_ID_EVERYONE"></span><span id="ipc_user_id_everyone"></span>**IPC\_USER\_ID\_EVERYONE** (\_TEXT("ANYONE"))


</dt> <dd>

IPC group ID for the group that contains all users.

</dd> <dt>

<span id="IPC_USER_ID_NULL"></span><span id="ipc_user_id_null"></span>

<span id="IPC_USER_ID_NULL"></span><span id="ipc_user_id_null"></span>**IPC\_USER\_ID\_NULL** (\_TEXT("NULL"))


</dt> <dd>

IPC user ID used to represent the absence of a user.

</dd> <dt>

<span id="IPC_USER_ID_OWNER"></span><span id="ipc_user_id_owner"></span>

<span id="IPC_USER_ID_OWNER"></span><span id="ipc_user_id_owner"></span>**IPC\_USER\_ID\_OWNER** (\_TEXT("OWNER"))


</dt> <dd>

IPC user ID used to represent the owner principal.

</dd> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





