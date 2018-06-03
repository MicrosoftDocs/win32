---
title: IPC\_LICENSE\_METADATA structure
description: Represents the metadata for content tracking.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B9F0D158-BFE3-49A0-B6AB-8FC023F4CFC5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IPC_LICENSE_METADATA structure Active Directory Rights Management Services SDK 2.0
- PIPC_LICENSE_METADATA structure pointer Active Directory Rights Management Services SDK 2.0
- PCIPC_LICENSE_METADATA structure pointer Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IPC_LICENSE_METADATA
api_location:
- Ipcfile.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IPC\_LICENSE\_METADATA structure

Represents the metadata for content tracking.

## Syntax


```C++
typedef struct _IPC_LICENSE_METADATA {
  DWORD    cbSize;
  DWORD    dwNotificationType;
  DWORD    dwNotificationPreference;
  FILETIME ftDateModified;
  FILETIME ftDateCreated;
  LPCWSTR  wszContentName;
} IPC_LICENSE_METADATA, *PIPC_LICENSE_METADATA;typedef const IPC_LICENSE_METADATA *PCIPC_LICENSE_METADATA;
```



## Members

<dl> <dt>

**cbSize**
</dt> <dd>

This is the size of this structure and needs to be initialized to `sizeof(IPC_LICENSE_METADATA)`.

</dd> <dt>

**dwNotificationType**
</dt> <dd>

Type of notification from one of the following. For more information, see [**Notification type**](notification-type.md).

</dd> <dt>

**dwNotificationPreference**
</dt> <dd>

Type of notification preference from [**Notification preference**](notification-preference.md).

</dd> <dt>

**ftDateModified**
</dt> <dd>

Modification date of the unprotected content..

</dd> <dt>

**ftDateCreated**
</dt> <dd>

Creation date of the unprotected content.

</dd> <dt>

**wszContentName**
</dt> <dd>

Name by which the content should be identified.

</dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcfile.h (include Msipc.h)</dt> </dl> |



 

 





