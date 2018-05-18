---
title: IPC\_OAUTH2\_CALLBACK\_INFO structure
description: Describes data that pertains to the authentication callback.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'CD7D862D-49BF-4CD1-8487-A4CBB33C3743'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_OAUTH2_CALLBACK_INFO structure Active Directory Rights Management Services SDK 2.0", "IPC_OATH2_CALLBACK_INFO structure Active Directory Rights Management Services SDK 2.0", "PIPC_OATH2_CALLBACK_INFO structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_OATH2_CALLBACK_INFO
api_location:
- Ipcbase.h
api_type:
- HeaderDef
---

# IPC\_OAUTH2\_CALLBACK\_INFO structure

Describes data that pertains to the authentication callback.

## Syntax


```C++
typedef struct _IPC_OATH2_CALLBACK_INFO {
  DWORD               cbSize;
  IPC_OAUTH2_CALLBACK pfnCallback;
  LPVOID              pvContext;
} IPC_OATH2_CALLBACK_INFO, *PIPC_OATH2_CALLBACK_INFO;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

This is the size of the structure and needs to be initialized to

`sizeof(IPC_OAUTH2_CALLBACK_INFO)`.

</dd> <dt>

**pfnCallback**
</dt> <dd>

An application-defined function for the RMS client to call when requesting an OAuth authentication token.

</dd> <dt>

**pvContext**
</dt> <dd>

Pointer to an application-defined structure which is passed to the function pointed to by *pfnCallback* when the RMS client requests an OAuth authentication token.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



 

 





