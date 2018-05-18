---
title: IPC\_TIL structure
description: Contains a list of template information in the form of IPC\_TEMPLATE\_INFO structures, returned by a call to IpcGetTemplateList.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '1edace67-2624-4119-9b82-8ca85365ee8d'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_TIL structure Active Directory Rights Management Services SDK 2.0", "PIPC_TIL structure pointer Active Directory Rights Management Services SDK 2.0", "PCIPC_TIL structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_TIL
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# IPC\_TIL structure

Contains a list of template information in the form of [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structures, returned by a call to [**IpcGetTemplateList**](ipcgettemplatelist.md).

## Syntax


```C++
typedef struct _IPC_TIL {
  DWORD             cTi;
  IPC_TEMPLATE_INFO aTi[ANYSIZE_ARRAY];
} IPC_TIL, *PIPC_TIL;typedef const IPC_TIL *PCIPC_TIL;
```



## Members

<dl> <dt>

**cTi**
</dt> <dd>

The number of [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structures in the list.

</dd> <dt>

**aTi**
</dt> <dd>

An array of [**IPC\_TEMPLATE\_INFO**](ipc-template-info.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IpcGetTemplateList**](ipcgettemplatelist.md)
</dt> <dt>

[**IPC\_TEMPLATE\_INFO**](ipc-template-info.md)
</dt> </dl>

 

 





