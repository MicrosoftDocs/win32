---
title: IPC\_CONNECTION\_INFO structure
description: Provides information on the rights management services (RMS) server to which to connect.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'e5d7fd8c-5f20-415f-914f-0e681413f099'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_CONNECTION_INFO structure Active Directory Rights Management Services SDK 2.0", "PIPC_CONNECTION_INFO structure pointer Active Directory Rights Management Services SDK 2.0", "PCIPC_CONNECTION_INFO structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_CONNECTION_INFO
api_location:
- Ipcbase.h
api_type:
- HeaderDef
---

# IPC\_CONNECTION\_INFO structure

Provides information on the rights management services (RMS) server to which to connect.

## Syntax


```C++
typedef struct _IPC_CONNECTION_INFO {
  LPCWSTR wszExtranetUrl;
  LPCWSTR wszIntranetUrl;
} IPC_CONNECTION_INFO, *PIPC_CONNECTION_INFO;typedef const IPC_CONNECTION_INFO *PCIPC_CONNECTION_INFO;
```



## Members

<dl> <dt>

**wszExtranetUrl**
</dt> <dd>

The extranet URL.

</dd> <dt>

**wszIntranetUrl**
</dt> <dd>

The intranet URL.

Intranet URL, **wszIntranetUrl**, is required if extranet URL, **wszExtranetUrl**, is **NULL**.

</dd> </dl>

## Remarks

The structure always contains the intranet URL and may optionally contain an extranet URL. In typical client scenarios, the connection info is not required. It is useful only in advanced server scenarios in which the application manages the server URLs.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



 

 





