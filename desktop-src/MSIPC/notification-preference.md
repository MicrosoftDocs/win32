---
title: Notification preference
description: Specifies the users's notification preference for a tracked document.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'F500738B-D749-4903-81CB-1DF2B5C7AA22'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCD_CT_NOTIFICATION_PREF_DEFAULT
- IPCD_CT_NOTIFICATION_PREF_DIGEST
api_location:
- Ipcprot.h
api_type:
- HeaderDef
---

# Notification preference

Specifies the users's notification preference for a tracked document.

<dl> <dt>

<span id="IPCD_CT_NOTIFICATION_PREF_DEFAULT"></span><span id="ipcd_ct_notification_pref_default"></span>**IPCD\_CT\_NOTIFICATION\_PREF\_DEFAULT**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Specifies that a notifications are sent every time the content is accessed.


</dt> </dl> </dd> <dt>

<span id="IPCD_CT_NOTIFICATION_PREF_DIGEST"></span><span id="ipcd_ct_notification_pref_digest"></span>**IPCD\_CT\_NOTIFICATION\_PREF\_DIGEST**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Specifies that notifications are sent as a digest notification, for example once every day.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |



## See also

<dl> <dt>

[**License metadata property types**](license-metadata-property-types.md)
</dt> <dt>

[**Notification preference**](notification-preference.md)
</dt> <dt>

[**Notification type**](notification-type.md)
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

 

 





