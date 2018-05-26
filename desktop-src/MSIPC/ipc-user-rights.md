---
title: IPC\_USER\_RIGHTS structure
description: A structure that is used to specify rights per user.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 4da8b5f9-68e9-44b6-a341-b10c350fbebb
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_USER_RIGHTS structure Active Directory Rights Management Services SDK 2.0
- PIPC_USER_RIGHTS structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_USER_RIGHTS structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_USER_RIGHTS
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
---

# IPC\_USER\_RIGHTS structure

A structure that is used to specify rights per user.

## Syntax


```C++
typedef struct _IPC_USER_RIGHTS {
  IPC_USER User;
  DWORD    cRights;
  LPCWSTR  *rgwszRights;
} IPC_USER_RIGHTS, *PIPC_USER_RIGHTS;typedef const IPC_USER_RIGHTS *PCIPC_USER_RIGHTS;
```



## Members

<dl> <dt>

**User**
</dt> <dd>

The user or group to be granted the specified rights.

</dd> <dt>

**cRights**
</dt> <dd>

The number of elements in **rgwszRights**.

</dd> <dt>

**rgwszRights**
</dt> <dd>

A string array of rights. Rights depend on the developer to map them to meaningful behavior for each application. For a list of reserved rights and detailed information on rights, see [**Rights**](rights.md).

Valid characters for a rights string are as follows:

<dl> <dd>\[A-Z\] (Uppercase characters)</dd> <dd>\[a-z\] (Lowercase characters)</dd> <dd>\[0-9\] (Numeric characters)</dd> <dd>\[- \_ .\] (Special characters)</dd> </dl>

> [!Note]  
> The name cannot contain special characters used for XML markup and cannot exceed 256 characters in length.

 

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**Rights**](rights.md)
</dt> </dl>

 

 





