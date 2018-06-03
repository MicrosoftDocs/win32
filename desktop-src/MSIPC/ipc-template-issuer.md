---
title: IPC\_TEMPLATE\_ISSUER structure
description: Contains information about the template issuer.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 529826bb-0bad-4233-a350-cf2db5d96527
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_TEMPLATE_ISSUER structure Active Directory Rights Management Services SDK 2.0
- PIPC_TEMPLATE_ISSUER structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_TEMPLATE_ISSUER structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_TEMPLATE_ISSUER
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_TEMPLATE\_ISSUER structure

Contains information about the template issuer, such as display name and whether the issuer allows a from-scratch policy.

## Syntax


```C++
typedef struct _IPC_TEMPLATE_ISSUER {
  IPC_CONNECTION_INFO connectionInfo;
  LPCWSTR             wszDisplayName;
  BOOL                fAllowFromScratch;
} IPC_TEMPLATE_ISSUER, *PIPC_TEMPLATE_ISSUER;typedef const IPC_TEMPLATE_ISSUER *PCIPC_TEMPLATE_ISSUER;
```



## Members

<dl> <dt>

**connectionInfo**
</dt> <dd>

The connection information of the issuer. For more information, see [**IPC\_CONNECTION\_INFO**](ipc-connection-info.md).

</dd> <dt>

**wszDisplayName**
</dt> <dd>

The display name of the issuer.

</dd> <dt>

**fAllowFromScratch**
</dt> <dd>

**TRUE** if the issuer allows creating a policy from scratch; otherwise, **FALSE**.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IPC\_CONNECTION\_INFO**](ipc-connection-info.md)
</dt> </dl>

 

 





