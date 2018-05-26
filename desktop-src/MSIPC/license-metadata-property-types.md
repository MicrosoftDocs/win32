---
title: License metadata property types
description: Property types for license metadata.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B8111A3E-6227-49DF-A313-E775BC0F9B18
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPC_MD_CONTENT_PATH
- IPC_MD_CONTENT_NAME
- IPC_MD_NOTIFICATION_TYPE
- IPC_MD_NOTIFICATION_PREFERENCE
- IPC_MD_DATE_MODIFIED
- IPC_MD_DATE_CREATED
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# License metadata property types

Property types for license metadata.

<dl> <dt>

<span id="IPC_MD_CONTENT_PATH"></span><span id="ipc_md_content_path"></span>**IPC\_MD\_CONTENT\_PATH**
</dt> <dd> <dl> <dt>

0x00000000
</dt> <dt>



Full path of the content which is being protected using the given license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvMetadata* is of type **LPCWSTR**.


</dt> </dl> </dd> <dt>

<span id="IPC_MD_CONTENT_NAME"></span><span id="ipc_md_content_name"></span>**IPC\_MD\_CONTENT\_NAME**
</dt> <dd> <dl> <dt>

0x00000001
</dt> <dt>



Name of the content being protected using the given license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvProperty* is of type **LPCWSTR**.


</dt> </dl> </dd> <dt>

<span id="IPC_MD_NOTIFICATION_TYPE"></span><span id="ipc_md_notification_type"></span>**IPC\_MD\_NOTIFICATION\_TYPE**
</dt> <dd> <dl> <dt>

0x00000002
</dt> <dt>



Desired [**Notification type**](notification-type.md) for the content protected using this license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvMetadata* is of type **LPDWORD**.


</dt> </dl> </dd> <dt>

<span id="IPC_MD_NOTIFICATION_PREFERENCE"></span><span id="ipc_md_notification_preference"></span>**IPC\_MD\_NOTIFICATION\_PREFERENCE**
</dt> <dd> <dl> <dt>

0x00000003
</dt> <dt>



Desired [**Notification preference**](notification-preference.md) for the content protected using this license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvProperty* is of type **LPDWORD**.


</dt> </dl> </dd> <dt>

<span id="IPC_MD_DATE_MODIFIED"></span><span id="ipc_md_date_modified"></span>**IPC\_MD\_DATE\_MODIFIED**
</dt> <dd> <dl> <dt>

0x00000004
</dt> <dt>



Modification date of the content protected with the the given license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvMetadata* is of type pointer to **FILETIME\***.


</dt> </dl> </dd> <dt>

<span id="IPC_MD_DATE_CREATED"></span><span id="ipc_md_date_created"></span>**IPC\_MD\_DATE\_CREATED**
</dt> <dd> <dl> <dt>

0x00000005
</dt> <dt>



Date created of the content which is being protected using the given license.

For [**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md), the *pvMetadata* is of type pointer to **FILETIME\*** .


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



 

 





