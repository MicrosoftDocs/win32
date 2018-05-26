---
title: IPC\_CREDENTIAL\_SYMMETRIC\_KEY structure
description: Symmetric key credential structure used to authenticate to an RMS Server.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: D0B283EA-3087-4DC9-B701-80995C1A4DCD
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_CREDENTIAL_SYMMETRIC_KEY structure Active Directory Rights Management Services SDK 2.0
- PIPC_CREDENTIAL_SYMMETRIC_KEY structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_CREDENTIAL_SYMMETRIC_KEY structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_CREDENTIAL_SYMMETRIC_KEY
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
---

# IPC\_CREDENTIAL\_SYMMETRIC\_KEY structure

Symmetric key credential structure used to authenticate to an RMS Server.

## Syntax


```C++
typedef struct _IPC_CREDENTIAL_SYMMETRIC_KEY {
  LPCWSTR wszBase64Key;
  LPCWSTR wszAppPrincipalId;
  LPCWSTR wszBposTenantId;
} IPC_CREDENTIAL_SYMMETRIC_KEY, *PIPC_CREDENTIAL_SYMMETRIC_KEY;typedef const IPC_CREDENTIAL_SYMMETRIC_KEY *PCIPC_CREDENTIAL_SYMMETRIC_KEY;
```



## Members

<dl> <dt>

**wszBase64Key**
</dt> <dd>

Symmetric key in the form of Base64 encoded string.

</dd> <dt>

**wszAppPrincipalId**
</dt> <dd>

Application principal Id.

</dd> <dt>

**wszBposTenantId**
</dt> <dd>

BPOS Tenant Id.

</dd> </dl>

## Remarks

The Symmetric key, Service Principal Name and BPOS Id can be acquired by registering the Service Principal via ACS. For guidance on setting up the service for your application see [Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md).

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[Enable your service application to work with cloud based RMS](how-to-use-file-api-with-aadrm--cloud-.md)
</dt> </dl>

 

 





