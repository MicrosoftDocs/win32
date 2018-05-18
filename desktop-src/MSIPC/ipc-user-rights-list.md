---
title: IPC\_USER\_RIGHTS\_LIST structure
description: Contains a list of user rights structures that defines the use restrictions associated with a license object.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'd2c9461f-d9d7-484d-a257-3eb958db4aa8'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IPC_USER_RIGHTS_LIST structure Active Directory Rights Management Services SDK 2.0", "PIPC_USER_RIGHTS_LIST structure pointer Active Directory Rights Management Services SDK 2.0", "PCIPC_USER_RIGHTS_LIST structure pointer Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IPC_USER_RIGHTS_LIST
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# IPC\_USER\_RIGHTS\_LIST structure

Contains a list of user rights structures that defines the use restrictions associated with a license object.

## Syntax


```C++
typedef struct _IPC_USER_RIGHTS_LIST {
  DWORD           cbSize;
  DWORD           cUserRights;
  IPC_USER_RIGHTS rgUserRights[ANYSIZE_ARRAY];
} IPC_USER_RIGHTS_LIST, *PIPC_USER_RIGHTS_LIST;typedef const IPC_USER_RIGHTS_LIST *PCIPC_USER_RIGHTS_LIST;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

When used with [**IpcSetLicenseProperty**](ipcsetlicenseproperty.md), **cbSize** is an input and must be set to `sizeof(IPC_USER_RIGHTS_LIST)`.

When used with [**IpcGetLicenseProperty**](ipcgetlicenseproperty.md) or [**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md), **cbSize** has no meaning and should be ignored.

</dd> <dt>

**cUserRights**
</dt> <dd>

The number of elements in **rgUserRights**.

</dd> <dt>

**rgUserRights**
</dt> <dd>

An array of [**IPC\_USER\_RIGHTS**](ipc-user-rights.md) structures.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**IpcGetLicenseProperty**](ipcgetlicenseproperty.md)
</dt> <dt>

[**IpcGetSerializedLicenseProperty**](ipcgetserializedlicenseproperty.md)
</dt> <dt>

[**IpcSetLicenseProperty**](ipcsetlicenseproperty.md)
</dt> <dt>

[**IPC\_USER\_RIGHTS**](ipc-user-rights.md)
</dt> </dl>

 

 





