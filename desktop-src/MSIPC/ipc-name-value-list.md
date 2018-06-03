---
title: IPC\_NAME\_VALUE\_LIST structure
description: Provides a name-value list structure.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: a6fb4e33-973f-4841-8c88-60796bbb9364
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_NAME_VALUE_LIST structure Active Directory Rights Management Services SDK 2.0
- PIPC_NAME_VALUE_LIST structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_NAME_VALUE_LIST structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_NAME_VALUE_LIST
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_NAME\_VALUE\_LIST structure

Provides a name-value list structure that contains a collection of name-value pairs.

## Syntax


```C++
typedef struct _IPC_NAME_VALUE_LIST {
  DWORD          cNameValuePairs;
  IPC_NAME_VALUE aNameValuePairs[ANYSIZE_ARRAY];
} IPC_NAME_VALUE_LIST, *PIPC_NAME_VALUE_LIST;typedef const IPC_NAME_VALUE_LIST *PCIPC_NAME_VALUE_LIST;
```



## Members

<dl> <dt>

**cNameValuePairs**
</dt> <dd>

The number of name-value pairs in the list.

</dd> <dt>

**aNameValuePairs**
</dt> <dd>

The array of name-value pairs. For more information, see [**IPC\_NAME\_VALUE**](ipc-name-value.md).

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPC\_NAME\_VALUE**](ipc-name-value.md)
</dt> </dl>

 

 





