---
title: IPC\_TEMPLATE\_ISSUER\_LIST structure
description: Contains a list of template issuers.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: aa670dc0-f267-4a5e-ac53-ee46ebaba1d6
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_TEMPLATE_ISSUER_LIST structure Active Directory Rights Management Services SDK 2.0
- PIPC_TEMPLATE_ISSUER_LIST structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_TEMPLATE_ISSUER_LIST structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_TEMPLATE_ISSUER_LIST
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_TEMPLATE\_ISSUER\_LIST structure

Contains a list of template issuers in the form of [**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md) structures, returned by a call to [**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md).

## Syntax


```C++
typedef struct _IPC_TEMPLATE_ISSUER_LIST {
  DWORD               cTi;
  IPC_TEMPLATE_ISSUER aTi[ANYSIZE_ARRAY];
} IPC_TEMPLATE_ISSUER_LIST, *PIPC_TEMPLATE_ISSUER_LIST;typedef const IPC_TEMPLATE_ISSUER_LIST *PCIPC_TEMPLATE_ISSUER_LIST;
```



## Members

<dl> <dt>

**cTi**
</dt> <dd>

The number of issuers in the list.

</dd> <dt>

**aTi**
</dt> <dd>

An array of [**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md) structures that represent the issuers.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IpcGetTemplateIssuerList**](ipcgettemplateissuerlist.md)
</dt> <dt>

[**IPC\_TEMPLATE\_ISSUER**](ipc-template-issuer.md)
</dt> </dl>

 

 





