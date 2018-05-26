---
title: Notification type
description: Specifies the way notifications about tracked document content usage is sent to the content owner.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: B4EA9DCB-9294-439E-B0DA-E79FE016902C
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCD_CT_NOTIFICATION_TYPE_DISABLED
- IPCD_CT_NOTIFICATION_TYPE_ENABLED
- IPCD_CT_NOTIFICATION_TYPE_DENY_ONLY
api_location:
- Ipcprot.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Notification type

Specifies the way notifications about tracked document content usage is sent to the content owner.

<dl> <dt>

<span id="IPCD_CT_NOTIFICATION_TYPE_DISABLED"></span><span id="ipcd_ct_notification_type_disabled"></span>**IPCD\_CT\_NOTIFICATION\_TYPE\_DISABLED**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Specifies that a notifications are disabled.


</dt> </dl> </dd> <dt>

<span id="IPCD_CT_NOTIFICATION_TYPE_ENABLED"></span><span id="ipcd_ct_notification_type_enabled"></span>**IPCD\_CT\_NOTIFICATION\_TYPE\_ENABLED**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Specifies that a notification will be sent when a user accesses the content. This includes the notification for unsuccessful attempts.


</dt> </dl> </dd> <dt>

<span id="IPCD_CT_NOTIFICATION_TYPE_DENY_ONLY"></span><span id="ipcd_ct_notification_type_deny_only"></span>**IPCD\_CT\_NOTIFICATION\_TYPE\_DENY\_ONLY**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



Specifies that a notification will be sent every time a user unsuccessfully tries to access the content.


</dt> </dl> </dd> <dt>


</dt> <dd> <dl> <dt>


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[Tracking Content](tracking-content.md)
</dt> <dt>

[**Notification preference**](notification-preference.md)
</dt> <dt>

[**IpcCreateLicenseMetadataHandle**](ipccreatelicensemetadatahandle.md)
</dt> <dt>

[**IpcSetLicenseMetadataProperty**](ipcsetlicensemetadataproperty.md)
</dt> <dt>

[**IpcSerializeLicenseWithMetadata**](ipcserializelicensemetadata.md)
</dt> <dt>

[**IpcfEncryptFileWithMetadata**](ipcfencryptfilewithmetadata.md)
</dt> <dt>

[**IpcfEncryptFileStreamWithMetadata**](ipcfencryptfilestreamwithmetadata.md)
</dt> <dt>

[**IpcRegisterLicense**](ipcregisterlicense.md)
</dt> </dl>

 

 





