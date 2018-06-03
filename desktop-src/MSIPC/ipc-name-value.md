---
title: IPC\_NAME\_VALUE structure
description: Describes application specific data that is stored as part of the license.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: f9e98976-99ff-4df8-91f4-09efa88a4406
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_NAME_VALUE structure Active Directory Rights Management Services SDK 2.0
- PIPC_NAME_VALUE structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_NAME_VALUE structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_NAME_VALUE
api_location:
- Ipcbase.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_NAME\_VALUE structure

Describes application specific data that is stored as part of the license. The data is stored as name-value pairs.

## Syntax


```C++
typedef struct _IPC_NAME_VALUE {
  LPCWSTR wszName;
  DWORD   lcid;
  LPCWSTR wszValue;
} IPC_NAME_VALUE, *PIPC_NAME_VALUE;typedef const IPC_NAME_VALUE *PCIPC_NAME_VALUE;
```



## Members

<dl> <dt>

**wszName**
</dt> <dd>

The property name of the name-value pair.

</dd> <dt>

**lcid**
</dt> <dd>

The locale ID for the value.

This member, **lcid**, must be set to the locale ID that goes with the value, **wszValue**. For more information about platform behavior regarding locale ID, see the Frequently asked questions section of the [Release notes](release-notes--rtm-.md) topic.

</dd> <dt>

**wszValue**
</dt> <dd>

The property value to associate with the content or license.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[Release notes](release-notes--rtm-.md)
</dt> </dl>

 

 





