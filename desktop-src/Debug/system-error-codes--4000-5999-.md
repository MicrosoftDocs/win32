---
description: Describes error codes 4000-5999 defined in the WinError.h header file and is intended for developers.
ms.assetid: 1d2f7160-6322-4c75-abbc-4a882bbdf7ce
title: System Error Codes (4000-5999) (WinError.h)
ms.topic: reference
ms.date: 07/18/2019
---

# System Error Codes (4000-5999)

> [!NOTE]
> This information is intended for developers debugging system errors. For other errors, such as issues with Windows Update, there is a list of resources on the [Error codes](system-error-codes.md) page.

The following list describes [system error codes](system-error-codes.md) for errors 4000 to 5999. They are returned by the [**GetLastError**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) function when many functions fail. To retrieve the description text for the error in your application, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag.

<dl> <dt>

<span id="ERROR_WINS_INTERNAL"></span><span id="error_wins_internal"></span>**ERROR\_WINS\_INTERNAL**
</dt> <dd> <dl> <dt>

4000 (0xFA0)
</dt> <dt>



WINS encountered an error while processing the command.


</dt> </dl> </dd> <dt>

<span id="ERROR_CAN_NOT_DEL_LOCAL_WINS"></span><span id="error_can_not_del_local_wins"></span>**ERROR\_CAN\_NOT\_DEL\_LOCAL\_WINS**
</dt> <dd> <dl> <dt>

4001 (0xFA1)
</dt> <dt>



The local WINS cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_STATIC_INIT"></span><span id="error_static_init"></span>**ERROR\_STATIC\_INIT**
</dt> <dd> <dl> <dt>

4002 (0xFA2)
</dt> <dt>



The importation from the file failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_INC_BACKUP"></span><span id="error_inc_backup"></span>**ERROR\_INC\_BACKUP**
</dt> <dd> <dl> <dt>

4003 (0xFA3)
</dt> <dt>



The backup failed. Was a full backup done before?


</dt> </dl> </dd> <dt>

<span id="ERROR_FULL_BACKUP"></span><span id="error_full_backup"></span>**ERROR\_FULL\_BACKUP**
</dt> <dd> <dl> <dt>

4004 (0xFA4)
</dt> <dt>



The backup failed. Check the directory to which you are backing the database.


</dt> </dl> </dd> <dt>

<span id="ERROR_REC_NON_EXISTENT"></span><span id="error_rec_non_existent"></span>**ERROR\_REC\_NON\_EXISTENT**
</dt> <dd> <dl> <dt>

4005 (0xFA5)
</dt> <dt>



The name does not exist in the WINS database.


</dt> </dl> </dd> <dt>

<span id="ERROR_RPL_NOT_ALLOWED"></span><span id="error_rpl_not_allowed"></span>**ERROR\_RPL\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

4006 (0xFA6)
</dt> <dt>



Replication with a nonconfigured partner is not allowed.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_CONTENTINFO_VERSION_UNSUPPORTED"></span><span id="peerdist_error_contentinfo_version_unsupported"></span>**PEERDIST\_ERROR\_CONTENTINFO\_VERSION\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

4050 (0xFD2)
</dt> <dt>



The version of the supplied content information is not supported.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_CANNOT_PARSE_CONTENTINFO"></span><span id="peerdist_error_cannot_parse_contentinfo"></span>**PEERDIST\_ERROR\_CANNOT\_PARSE\_CONTENTINFO**
</dt> <dd> <dl> <dt>

4051 (0xFD3)
</dt> <dt>



The supplied content information is malformed.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_MISSING_DATA"></span><span id="peerdist_error_missing_data"></span>**PEERDIST\_ERROR\_MISSING\_DATA**
</dt> <dd> <dl> <dt>

4052 (0xFD4)
</dt> <dt>



The requested data cannot be found in local or peer caches.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_NO_MORE"></span><span id="peerdist_error_no_more"></span>**PEERDIST\_ERROR\_NO\_MORE**
</dt> <dd> <dl> <dt>

4053 (0xFD5)
</dt> <dt>



No more data is available or required.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_NOT_INITIALIZED"></span><span id="peerdist_error_not_initialized"></span>**PEERDIST\_ERROR\_NOT\_INITIALIZED**
</dt> <dd> <dl> <dt>

4054 (0xFD6)
</dt> <dt>



The supplied object has not been initialized.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_ALREADY_INITIALIZED"></span><span id="peerdist_error_already_initialized"></span>**PEERDIST\_ERROR\_ALREADY\_INITIALIZED**
</dt> <dd> <dl> <dt>

4055 (0xFD7)
</dt> <dt>



The supplied object has already been initialized.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_SHUTDOWN_IN_PROGRESS"></span><span id="peerdist_error_shutdown_in_progress"></span>**PEERDIST\_ERROR\_SHUTDOWN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

4056 (0xFD8)
</dt> <dt>



A shutdown operation is already in progress.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_INVALIDATED"></span><span id="peerdist_error_invalidated"></span>**PEERDIST\_ERROR\_INVALIDATED**
</dt> <dd> <dl> <dt>

4057 (0xFD9)
</dt> <dt>



The supplied object has already been invalidated.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_ALREADY_EXISTS"></span><span id="peerdist_error_already_exists"></span>**PEERDIST\_ERROR\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

4058 (0xFDA)
</dt> <dt>



An element already exists and was not replaced.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_OPERATION_NOTFOUND"></span><span id="peerdist_error_operation_notfound"></span>**PEERDIST\_ERROR\_OPERATION\_NOTFOUND**
</dt> <dd> <dl> <dt>

4059 (0xFDB)
</dt> <dt>



Can not cancel the requested operation as it has already been completed.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_ALREADY_COMPLETED"></span><span id="peerdist_error_already_completed"></span>**PEERDIST\_ERROR\_ALREADY\_COMPLETED**
</dt> <dd> <dl> <dt>

4060 (0xFDC)
</dt> <dt>



Can not perform the reqested operation because it has already been carried out.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_OUT_OF_BOUNDS"></span><span id="peerdist_error_out_of_bounds"></span>**PEERDIST\_ERROR\_OUT\_OF\_BOUNDS**
</dt> <dd> <dl> <dt>

4061 (0xFDD)
</dt> <dt>



An operation accessed data beyond the bounds of valid data.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_VERSION_UNSUPPORTED"></span><span id="peerdist_error_version_unsupported"></span>**PEERDIST\_ERROR\_VERSION\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

4062 (0xFDE)
</dt> <dt>



The requested version is not supported.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_INVALID_CONFIGURATION"></span><span id="peerdist_error_invalid_configuration"></span>**PEERDIST\_ERROR\_INVALID\_CONFIGURATION**
</dt> <dd> <dl> <dt>

4063 (0xFDF)
</dt> <dt>



A configuration value is invalid.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_NOT_LICENSED"></span><span id="peerdist_error_not_licensed"></span>**PEERDIST\_ERROR\_NOT\_LICENSED**
</dt> <dd> <dl> <dt>

4064 (0xFE0)
</dt> <dt>



The SKU is not licensed.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_SERVICE_UNAVAILABLE"></span><span id="peerdist_error_service_unavailable"></span>**PEERDIST\_ERROR\_SERVICE\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

4065 (0xFE1)
</dt> <dt>



PeerDist Service is still initializing and will be available shortly.


</dt> </dl> </dd> <dt>

<span id="PEERDIST_ERROR_TRUST_FAILURE"></span><span id="peerdist_error_trust_failure"></span>**PEERDIST\_ERROR\_TRUST\_FAILURE**
</dt> <dd> <dl> <dt>

4066 (0xFE2)
</dt> <dt>



Communication with one or more computers will be temporarily blocked due to recent errors.


</dt> </dl> </dd> <dt>

<span id="ERROR_DHCP_ADDRESS_CONFLICT"></span><span id="error_dhcp_address_conflict"></span>**ERROR\_DHCP\_ADDRESS\_CONFLICT**
</dt> <dd> <dl> <dt>

4100 (0x1004)
</dt> <dt>



The DHCP client has obtained an IP address that is already in use on the network. The local interface will be disabled until the DHCP client can obtain a new address.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_GUID_NOT_FOUND"></span><span id="error_wmi_guid_not_found"></span>**ERROR\_WMI\_GUID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4200 (0x1068)
</dt> <dt>



The GUID passed was not recognized as valid by a WMI data provider.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_INSTANCE_NOT_FOUND"></span><span id="error_wmi_instance_not_found"></span>**ERROR\_WMI\_INSTANCE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4201 (0x1069)
</dt> <dt>



The instance name passed was not recognized as valid by a WMI data provider.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_ITEMID_NOT_FOUND"></span><span id="error_wmi_itemid_not_found"></span>**ERROR\_WMI\_ITEMID\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4202 (0x106A)
</dt> <dt>



The data item ID passed was not recognized as valid by a WMI data provider.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_TRY_AGAIN"></span><span id="error_wmi_try_again"></span>**ERROR\_WMI\_TRY\_AGAIN**
</dt> <dd> <dl> <dt>

4203 (0x106B)
</dt> <dt>



The WMI request could not be completed and should be retried.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_DP_NOT_FOUND"></span><span id="error_wmi_dp_not_found"></span>**ERROR\_WMI\_DP\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4204 (0x106C)
</dt> <dt>



The WMI data provider could not be located.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_UNRESOLVED_INSTANCE_REF"></span><span id="error_wmi_unresolved_instance_ref"></span>**ERROR\_WMI\_UNRESOLVED\_INSTANCE\_REF**
</dt> <dd> <dl> <dt>

4205 (0x106D)
</dt> <dt>



The WMI data provider references an instance set that has not been registered.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_ALREADY_ENABLED"></span><span id="error_wmi_already_enabled"></span>**ERROR\_WMI\_ALREADY\_ENABLED**
</dt> <dd> <dl> <dt>

4206 (0x106E)
</dt> <dt>



The WMI data block or event notification has already been enabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_GUID_DISCONNECTED"></span><span id="error_wmi_guid_disconnected"></span>**ERROR\_WMI\_GUID\_DISCONNECTED**
</dt> <dd> <dl> <dt>

4207 (0x106F)
</dt> <dt>



The WMI data block is no longer available.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_SERVER_UNAVAILABLE"></span><span id="error_wmi_server_unavailable"></span>**ERROR\_WMI\_SERVER\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

4208 (0x1070)
</dt> <dt>



The WMI data service is not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_DP_FAILED"></span><span id="error_wmi_dp_failed"></span>**ERROR\_WMI\_DP\_FAILED**
</dt> <dd> <dl> <dt>

4209 (0x1071)
</dt> <dt>



The WMI data provider failed to carry out the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_INVALID_MOF"></span><span id="error_wmi_invalid_mof"></span>**ERROR\_WMI\_INVALID\_MOF**
</dt> <dd> <dl> <dt>

4210 (0x1072)
</dt> <dt>



The WMI MOF information is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_INVALID_REGINFO"></span><span id="error_wmi_invalid_reginfo"></span>**ERROR\_WMI\_INVALID\_REGINFO**
</dt> <dd> <dl> <dt>

4211 (0x1073)
</dt> <dt>



The WMI registration information is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_ALREADY_DISABLED"></span><span id="error_wmi_already_disabled"></span>**ERROR\_WMI\_ALREADY\_DISABLED**
</dt> <dd> <dl> <dt>

4212 (0x1074)
</dt> <dt>



The WMI data block or event notification has already been disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_READ_ONLY"></span><span id="error_wmi_read_only"></span>**ERROR\_WMI\_READ\_ONLY**
</dt> <dd> <dl> <dt>

4213 (0x1075)
</dt> <dt>



The WMI data item or data block is read only.


</dt> </dl> </dd> <dt>

<span id="ERROR_WMI_SET_FAILURE"></span><span id="error_wmi_set_failure"></span>**ERROR\_WMI\_SET\_FAILURE**
</dt> <dd> <dl> <dt>

4214 (0x1076)
</dt> <dt>



The WMI data item or data block could not be changed.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_APPCONTAINER"></span><span id="error_not_appcontainer"></span>**ERROR\_NOT\_APPCONTAINER**
</dt> <dd> <dl> <dt>

4250 (0x109A)
</dt> <dt>



This operation is only valid in the context of an app container.


</dt> </dl> </dd> <dt>

<span id="ERROR_APPCONTAINER_REQUIRED"></span><span id="error_appcontainer_required"></span>**ERROR\_APPCONTAINER\_REQUIRED**
</dt> <dd> <dl> <dt>

4251 (0x109B)
</dt> <dt>



This application can only run in the context of an app container.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_SUPPORTED_IN_APPCONTAINER"></span><span id="error_not_supported_in_appcontainer"></span>**ERROR\_NOT\_SUPPORTED\_IN\_APPCONTAINER**
</dt> <dd> <dl> <dt>

4252 (0x109C)
</dt> <dt>



This functionality is not supported in the context of an app container.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_PACKAGE_SID_LENGTH"></span><span id="error_invalid_package_sid_length"></span>**ERROR\_INVALID\_PACKAGE\_SID\_LENGTH**
</dt> <dd> <dl> <dt>

4253 (0x109D)
</dt> <dt>



The length of the SID supplied is not a valid length for app container SIDs.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MEDIA"></span><span id="error_invalid_media"></span>**ERROR\_INVALID\_MEDIA**
</dt> <dd> <dl> <dt>

4300 (0x10CC)
</dt> <dt>



The media identifier does not represent a valid medium.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_LIBRARY"></span><span id="error_invalid_library"></span>**ERROR\_INVALID\_LIBRARY**
</dt> <dd> <dl> <dt>

4301 (0x10CD)
</dt> <dt>



The library identifier does not represent a valid library.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_MEDIA_POOL"></span><span id="error_invalid_media_pool"></span>**ERROR\_INVALID\_MEDIA\_POOL**
</dt> <dd> <dl> <dt>

4302 (0x10CE)
</dt> <dt>



The media pool identifier does not represent a valid media pool.


</dt> </dl> </dd> <dt>

<span id="ERROR_DRIVE_MEDIA_MISMATCH"></span><span id="error_drive_media_mismatch"></span>**ERROR\_DRIVE\_MEDIA\_MISMATCH**
</dt> <dd> <dl> <dt>

4303 (0x10CF)
</dt> <dt>



The drive and medium are not compatible or exist in different libraries.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_OFFLINE"></span><span id="error_media_offline"></span>**ERROR\_MEDIA\_OFFLINE**
</dt> <dd> <dl> <dt>

4304 (0x10D0)
</dt> <dt>



The medium currently exists in an offline library and must be online to perform this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_LIBRARY_OFFLINE"></span><span id="error_library_offline"></span>**ERROR\_LIBRARY\_OFFLINE**
</dt> <dd> <dl> <dt>

4305 (0x10D1)
</dt> <dt>



The operation cannot be performed on an offline library.


</dt> </dl> </dd> <dt>

<span id="ERROR_EMPTY"></span><span id="error_empty"></span>**ERROR\_EMPTY**
</dt> <dd> <dl> <dt>

4306 (0x10D2)
</dt> <dt>



The library, drive, or media pool is empty.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_EMPTY"></span><span id="error_not_empty"></span>**ERROR\_NOT\_EMPTY**
</dt> <dd> <dl> <dt>

4307 (0x10D3)
</dt> <dt>



The library, drive, or media pool must be empty to perform this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_UNAVAILABLE"></span><span id="error_media_unavailable"></span>**ERROR\_MEDIA\_UNAVAILABLE**
</dt> <dd> <dl> <dt>

4308 (0x10D4)
</dt> <dt>



No media is currently available in this media pool or library.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_DISABLED"></span><span id="error_resource_disabled"></span>**ERROR\_RESOURCE\_DISABLED**
</dt> <dd> <dl> <dt>

4309 (0x10D5)
</dt> <dt>



A resource required for this operation is disabled.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CLEANER"></span><span id="error_invalid_cleaner"></span>**ERROR\_INVALID\_CLEANER**
</dt> <dd> <dl> <dt>

4310 (0x10D6)
</dt> <dt>



The media identifier does not represent a valid cleaner.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_CLEAN"></span><span id="error_unable_to_clean"></span>**ERROR\_UNABLE\_TO\_CLEAN**
</dt> <dd> <dl> <dt>

4311 (0x10D7)
</dt> <dt>



The drive cannot be cleaned or does not support cleaning.


</dt> </dl> </dd> <dt>

<span id="ERROR_OBJECT_NOT_FOUND"></span><span id="error_object_not_found"></span>**ERROR\_OBJECT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4312 (0x10D8)
</dt> <dt>



The object identifier does not represent a valid object.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATABASE_FAILURE"></span><span id="error_database_failure"></span>**ERROR\_DATABASE\_FAILURE**
</dt> <dd> <dl> <dt>

4313 (0x10D9)
</dt> <dt>



Unable to read from or write to the database.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATABASE_FULL"></span><span id="error_database_full"></span>**ERROR\_DATABASE\_FULL**
</dt> <dd> <dl> <dt>

4314 (0x10DA)
</dt> <dt>



The database is full.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_INCOMPATIBLE"></span><span id="error_media_incompatible"></span>**ERROR\_MEDIA\_INCOMPATIBLE**
</dt> <dd> <dl> <dt>

4315 (0x10DB)
</dt> <dt>



The medium is not compatible with the device or media pool.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NOT_PRESENT"></span><span id="error_resource_not_present"></span>**ERROR\_RESOURCE\_NOT\_PRESENT**
</dt> <dd> <dl> <dt>

4316 (0x10DC)
</dt> <dt>



The resource required for this operation does not exist.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_OPERATION"></span><span id="error_invalid_operation"></span>**ERROR\_INVALID\_OPERATION**
</dt> <dd> <dl> <dt>

4317 (0x10DD)
</dt> <dt>



The operation identifier is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIA_NOT_AVAILABLE"></span><span id="error_media_not_available"></span>**ERROR\_MEDIA\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

4318 (0x10DE)
</dt> <dt>



The media is not mounted or ready for use.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEVICE_NOT_AVAILABLE"></span><span id="error_device_not_available"></span>**ERROR\_DEVICE\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

4319 (0x10DF)
</dt> <dt>



The device is not ready for use.


</dt> </dl> </dd> <dt>

<span id="ERROR_REQUEST_REFUSED"></span><span id="error_request_refused"></span>**ERROR\_REQUEST\_REFUSED**
</dt> <dd> <dl> <dt>

4320 (0x10E0)
</dt> <dt>



The operator or administrator has refused the request.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_DRIVE_OBJECT"></span><span id="error_invalid_drive_object"></span>**ERROR\_INVALID\_DRIVE\_OBJECT**
</dt> <dd> <dl> <dt>

4321 (0x10E1)
</dt> <dt>



The drive identifier does not represent a valid drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_LIBRARY_FULL"></span><span id="error_library_full"></span>**ERROR\_LIBRARY\_FULL**
</dt> <dd> <dl> <dt>

4322 (0x10E2)
</dt> <dt>



Library is full. No slot is available for use.


</dt> </dl> </dd> <dt>

<span id="ERROR_MEDIUM_NOT_ACCESSIBLE"></span><span id="error_medium_not_accessible"></span>**ERROR\_MEDIUM\_NOT\_ACCESSIBLE**
</dt> <dd> <dl> <dt>

4323 (0x10E3)
</dt> <dt>



The transport cannot access the medium.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_LOAD_MEDIUM"></span><span id="error_unable_to_load_medium"></span>**ERROR\_UNABLE\_TO\_LOAD\_MEDIUM**
</dt> <dd> <dl> <dt>

4324 (0x10E4)
</dt> <dt>



Unable to load the medium into the drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_INVENTORY_DRIVE"></span><span id="error_unable_to_inventory_drive"></span>**ERROR\_UNABLE\_TO\_INVENTORY\_DRIVE**
</dt> <dd> <dl> <dt>

4325 (0x10E5)
</dt> <dt>



Unable to retrieve the drive status.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_INVENTORY_SLOT"></span><span id="error_unable_to_inventory_slot"></span>**ERROR\_UNABLE\_TO\_INVENTORY\_SLOT**
</dt> <dd> <dl> <dt>

4326 (0x10E6)
</dt> <dt>



Unable to retrieve the slot status.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_INVENTORY_TRANSPORT"></span><span id="error_unable_to_inventory_transport"></span>**ERROR\_UNABLE\_TO\_INVENTORY\_TRANSPORT**
</dt> <dd> <dl> <dt>

4327 (0x10E7)
</dt> <dt>



Unable to retrieve status about the transport.


</dt> </dl> </dd> <dt>

<span id="ERROR_TRANSPORT_FULL"></span><span id="error_transport_full"></span>**ERROR\_TRANSPORT\_FULL**
</dt> <dd> <dl> <dt>

4328 (0x10E8)
</dt> <dt>



Cannot use the transport because it is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_CONTROLLING_IEPORT"></span><span id="error_controlling_ieport"></span>**ERROR\_CONTROLLING\_IEPORT**
</dt> <dd> <dl> <dt>

4329 (0x10E9)
</dt> <dt>



Unable to open or close the inject/eject port.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNABLE_TO_EJECT_MOUNTED_MEDIA"></span><span id="error_unable_to_eject_mounted_media"></span>**ERROR\_UNABLE\_TO\_EJECT\_MOUNTED\_MEDIA**
</dt> <dd> <dl> <dt>

4330 (0x10EA)
</dt> <dt>



Unable to eject the medium because it is in a drive.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLEANER_SLOT_SET"></span><span id="error_cleaner_slot_set"></span>**ERROR\_CLEANER\_SLOT\_SET**
</dt> <dd> <dl> <dt>

4331 (0x10EB)
</dt> <dt>



A cleaner slot is already reserved.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLEANER_SLOT_NOT_SET"></span><span id="error_cleaner_slot_not_set"></span>**ERROR\_CLEANER\_SLOT\_NOT\_SET**
</dt> <dd> <dl> <dt>

4332 (0x10EC)
</dt> <dt>



A cleaner slot is not reserved.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLEANER_CARTRIDGE_SPENT"></span><span id="error_cleaner_cartridge_spent"></span>**ERROR\_CLEANER\_CARTRIDGE\_SPENT**
</dt> <dd> <dl> <dt>

4333 (0x10ED)
</dt> <dt>



The cleaner cartridge has performed the maximum number of drive cleanings.


</dt> </dl> </dd> <dt>

<span id="ERROR_UNEXPECTED_OMID"></span><span id="error_unexpected_omid"></span>**ERROR\_UNEXPECTED\_OMID**
</dt> <dd> <dl> <dt>

4334 (0x10EE)
</dt> <dt>



Unexpected on-medium identifier.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_DELETE_LAST_ITEM"></span><span id="error_cant_delete_last_item"></span>**ERROR\_CANT\_DELETE\_LAST\_ITEM**
</dt> <dd> <dl> <dt>

4335 (0x10EF)
</dt> <dt>



The last remaining item in this group or resource cannot be deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_MESSAGE_EXCEEDS_MAX_SIZE"></span><span id="error_message_exceeds_max_size"></span>**ERROR\_MESSAGE\_EXCEEDS\_MAX\_SIZE**
</dt> <dd> <dl> <dt>

4336 (0x10F0)
</dt> <dt>



The message provided exceeds the maximum size allowed for this parameter.


</dt> </dl> </dd> <dt>

<span id="ERROR_VOLUME_CONTAINS_SYS_FILES"></span><span id="error_volume_contains_sys_files"></span>**ERROR\_VOLUME\_CONTAINS\_SYS\_FILES**
</dt> <dd> <dl> <dt>

4337 (0x10F1)
</dt> <dt>



The volume contains system or paging files.


</dt> </dl> </dd> <dt>

<span id="ERROR_INDIGENOUS_TYPE"></span><span id="error_indigenous_type"></span>**ERROR\_INDIGENOUS\_TYPE**
</dt> <dd> <dl> <dt>

4338 (0x10F2)
</dt> <dt>



The media type cannot be removed from this library since at least one drive in the library reports it can support this media type.


</dt> </dl> </dd> <dt>

<span id="ERROR_NO_SUPPORTING_DRIVES"></span><span id="error_no_supporting_drives"></span>**ERROR\_NO\_SUPPORTING\_DRIVES**
</dt> <dd> <dl> <dt>

4339 (0x10F3)
</dt> <dt>



This offline media cannot be mounted on this system since no enabled drives are present which can be used.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLEANER_CARTRIDGE_INSTALLED"></span><span id="error_cleaner_cartridge_installed"></span>**ERROR\_CLEANER\_CARTRIDGE\_INSTALLED**
</dt> <dd> <dl> <dt>

4340 (0x10F4)
</dt> <dt>



A cleaner cartridge is present in the tape library.


</dt> </dl> </dd> <dt>

<span id="ERROR_IEPORT_FULL"></span><span id="error_ieport_full"></span>**ERROR\_IEPORT\_FULL**
</dt> <dd> <dl> <dt>

4341 (0x10F5)
</dt> <dt>



Cannot use the inject/eject port because it is not empty.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_OFFLINE"></span><span id="error_file_offline"></span>**ERROR\_FILE\_OFFLINE**
</dt> <dd> <dl> <dt>

4350 (0x10FE)
</dt> <dt>



This file is currently not available for use on this computer.


</dt> </dl> </dd> <dt>

<span id="ERROR_REMOTE_STORAGE_NOT_ACTIVE"></span><span id="error_remote_storage_not_active"></span>**ERROR\_REMOTE\_STORAGE\_NOT\_ACTIVE**
</dt> <dd> <dl> <dt>

4351 (0x10FF)
</dt> <dt>



The remote storage service is not operational at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_REMOTE_STORAGE_MEDIA_ERROR"></span><span id="error_remote_storage_media_error"></span>**ERROR\_REMOTE\_STORAGE\_MEDIA\_ERROR**
</dt> <dd> <dl> <dt>

4352 (0x1100)
</dt> <dt>



The remote storage service encountered a media error.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_A_REPARSE_POINT"></span><span id="error_not_a_reparse_point"></span>**ERROR\_NOT\_A\_REPARSE\_POINT**
</dt> <dd> <dl> <dt>

4390 (0x1126)
</dt> <dt>



The file or directory is not a reparse point.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPARSE_ATTRIBUTE_CONFLICT"></span><span id="error_reparse_attribute_conflict"></span>**ERROR\_REPARSE\_ATTRIBUTE\_CONFLICT**
</dt> <dd> <dl> <dt>

4391 (0x1127)
</dt> <dt>



The reparse point attribute cannot be set because it conflicts with an existing attribute.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_REPARSE_DATA"></span><span id="error_invalid_reparse_data"></span>**ERROR\_INVALID\_REPARSE\_DATA**
</dt> <dd> <dl> <dt>

4392 (0x1128)
</dt> <dt>



The data present in the reparse point buffer is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPARSE_TAG_INVALID"></span><span id="error_reparse_tag_invalid"></span>**ERROR\_REPARSE\_TAG\_INVALID**
</dt> <dd> <dl> <dt>

4393 (0x1129)
</dt> <dt>



The tag present in the reparse point buffer is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_REPARSE_TAG_MISMATCH"></span><span id="error_reparse_tag_mismatch"></span>**ERROR\_REPARSE\_TAG\_MISMATCH**
</dt> <dd> <dl> <dt>

4394 (0x112A)
</dt> <dt>



There is a mismatch between the tag specified in the request and the tag present in the reparse point.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_DATA_NOT_FOUND"></span><span id="error_app_data_not_found"></span>**ERROR\_APP\_DATA\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4400 (0x1130)
</dt> <dt>



Fast Cache data not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_DATA_EXPIRED"></span><span id="error_app_data_expired"></span>**ERROR\_APP\_DATA\_EXPIRED**
</dt> <dd> <dl> <dt>

4401 (0x1131)
</dt> <dt>



Fast Cache data expired.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_DATA_CORRUPT"></span><span id="error_app_data_corrupt"></span>**ERROR\_APP\_DATA\_CORRUPT**
</dt> <dd> <dl> <dt>

4402 (0x1132)
</dt> <dt>



Fast Cache data corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_DATA_LIMIT_EXCEEDED"></span><span id="error_app_data_limit_exceeded"></span>**ERROR\_APP\_DATA\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

4403 (0x1133)
</dt> <dt>



Fast Cache data has exceeded its max size and cannot be updated.


</dt> </dl> </dd> <dt>

<span id="ERROR_APP_DATA_REBOOT_REQUIRED"></span><span id="error_app_data_reboot_required"></span>**ERROR\_APP\_DATA\_REBOOT\_REQUIRED**
</dt> <dd> <dl> <dt>

4404 (0x1134)
</dt> <dt>



Fast Cache has been ReArmed and requires a reboot until it can be updated.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_ROLLBACK_DETECTED"></span><span id="error_secureboot_rollback_detected"></span>**ERROR\_SECUREBOOT\_ROLLBACK\_DETECTED**
</dt> <dd> <dl> <dt>

4420 (0x1144)
</dt> <dt>



Secure Boot detected that rollback of protected data has been attempted.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_POLICY_VIOLATION"></span><span id="error_secureboot_policy_violation"></span>**ERROR\_SECUREBOOT\_POLICY\_VIOLATION**
</dt> <dd> <dl> <dt>

4421 (0x1145)
</dt> <dt>



The value is protected by Secure Boot policy and cannot be modified or deleted.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_INVALID_POLICY"></span><span id="error_secureboot_invalid_policy"></span>**ERROR\_SECUREBOOT\_INVALID\_POLICY**
</dt> <dd> <dl> <dt>

4422 (0x1146)
</dt> <dt>



The Secure Boot policy is invalid.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_POLICY_PUBLISHER_NOT_FOUND"></span><span id="error_secureboot_policy_publisher_not_found"></span>**ERROR\_SECUREBOOT\_POLICY\_PUBLISHER\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

4423 (0x1147)
</dt> <dt>



A new Secure Boot policy did not contain the current publisher on its update list.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_POLICY_NOT_SIGNED"></span><span id="error_secureboot_policy_not_signed"></span>**ERROR\_SECUREBOOT\_POLICY\_NOT\_SIGNED**
</dt> <dd> <dl> <dt>

4424 (0x1148)
</dt> <dt>



The Secure Boot policy is either not signed or is signed by a non-trusted signer.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_NOT_ENABLED"></span><span id="error_secureboot_not_enabled"></span>**ERROR\_SECUREBOOT\_NOT\_ENABLED**
</dt> <dd> <dl> <dt>

4425 (0x1149)
</dt> <dt>



Secure Boot is not enabled on this machine.


</dt> </dl> </dd> <dt>

<span id="ERROR_SECUREBOOT_FILE_REPLACED"></span><span id="error_secureboot_file_replaced"></span>**ERROR\_SECUREBOOT\_FILE\_REPLACED**
</dt> <dd> <dl> <dt>

4426 (0x114A)
</dt> <dt>



Secure Boot requires that certain files and drivers are not replaced by other files or drivers.


</dt> </dl> </dd> <dt>

<span id="ERROR_OFFLOAD_READ_FLT_NOT_SUPPORTED"></span><span id="error_offload_read_flt_not_supported"></span>**ERROR\_OFFLOAD\_READ\_FLT\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

4440 (0x1158)
</dt> <dt>



The copy offload read operation is not supported by a filter.


</dt> </dl> </dd> <dt>

<span id="ERROR_OFFLOAD_WRITE_FLT_NOT_SUPPORTED"></span><span id="error_offload_write_flt_not_supported"></span>**ERROR\_OFFLOAD\_WRITE\_FLT\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

4441 (0x1159)
</dt> <dt>



The copy offload write operation is not supported by a filter.


</dt> </dl> </dd> <dt>

<span id="ERROR_OFFLOAD_READ_FILE_NOT_SUPPORTED"></span><span id="error_offload_read_file_not_supported"></span>**ERROR\_OFFLOAD\_READ\_FILE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

4442 (0x115A)
</dt> <dt>



The copy offload read operation is not supported for the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_OFFLOAD_WRITE_FILE_NOT_SUPPORTED"></span><span id="error_offload_write_file_not_supported"></span>**ERROR\_OFFLOAD\_WRITE\_FILE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

4443 (0x115B)
</dt> <dt>



The copy offload write operation is not supported for the file.


</dt> </dl> </dd> <dt>

<span id="ERROR_VOLUME_NOT_SIS_ENABLED"></span><span id="error_volume_not_sis_enabled"></span>**ERROR\_VOLUME\_NOT\_SIS\_ENABLED**
</dt> <dd> <dl> <dt>

4500 (0x1194)
</dt> <dt>



Single Instance Storage is not available on this volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENT_RESOURCE_EXISTS"></span><span id="error_dependent_resource_exists"></span>**ERROR\_DEPENDENT\_RESOURCE\_EXISTS**
</dt> <dd> <dl> <dt>

5001 (0x1389)
</dt> <dt>



The operation cannot be completed because other resources are dependent on this resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENCY_NOT_FOUND"></span><span id="error_dependency_not_found"></span>**ERROR\_DEPENDENCY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5002 (0x138A)
</dt> <dt>



The cluster resource dependency cannot be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENCY_ALREADY_EXISTS"></span><span id="error_dependency_already_exists"></span>**ERROR\_DEPENDENCY\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

5003 (0x138B)
</dt> <dt>



The cluster resource cannot be made dependent on the specified resource because it is already dependent.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NOT_ONLINE"></span><span id="error_resource_not_online"></span>**ERROR\_RESOURCE\_NOT\_ONLINE**
</dt> <dd> <dl> <dt>

5004 (0x138C)
</dt> <dt>



The cluster resource is not online.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOST_NODE_NOT_AVAILABLE"></span><span id="error_host_node_not_available"></span>**ERROR\_HOST\_NODE\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5005 (0x138D)
</dt> <dt>



A cluster node is not available for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NOT_AVAILABLE"></span><span id="error_resource_not_available"></span>**ERROR\_RESOURCE\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5006 (0x138E)
</dt> <dt>



The cluster resource is not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NOT_FOUND"></span><span id="error_resource_not_found"></span>**ERROR\_RESOURCE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5007 (0x138F)
</dt> <dt>



The cluster resource could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_SHUTDOWN_CLUSTER"></span><span id="error_shutdown_cluster"></span>**ERROR\_SHUTDOWN\_CLUSTER**
</dt> <dd> <dl> <dt>

5008 (0x1390)
</dt> <dt>



The cluster is being shut down.


</dt> </dl> </dd> <dt>

<span id="ERROR_CANT_EVICT_ACTIVE_NODE"></span><span id="error_cant_evict_active_node"></span>**ERROR\_CANT\_EVICT\_ACTIVE\_NODE**
</dt> <dd> <dl> <dt>

5009 (0x1391)
</dt> <dt>



A cluster node cannot be evicted from the cluster unless the node is down or it is the last node.


</dt> </dl> </dd> <dt>

<span id="ERROR_OBJECT_ALREADY_EXISTS"></span><span id="error_object_already_exists"></span>**ERROR\_OBJECT\_ALREADY\_EXISTS**
</dt> <dd> <dl> <dt>

5010 (0x1392)
</dt> <dt>



The object already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_OBJECT_IN_LIST"></span><span id="error_object_in_list"></span>**ERROR\_OBJECT\_IN\_LIST**
</dt> <dd> <dl> <dt>

5011 (0x1393)
</dt> <dt>



The object is already in the list.


</dt> </dl> </dd> <dt>

<span id="ERROR_GROUP_NOT_AVAILABLE"></span><span id="error_group_not_available"></span>**ERROR\_GROUP\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5012 (0x1394)
</dt> <dt>



The cluster group is not available for any new requests.


</dt> </dl> </dd> <dt>

<span id="ERROR_GROUP_NOT_FOUND"></span><span id="error_group_not_found"></span>**ERROR\_GROUP\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5013 (0x1395)
</dt> <dt>



The cluster group could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_GROUP_NOT_ONLINE"></span><span id="error_group_not_online"></span>**ERROR\_GROUP\_NOT\_ONLINE**
</dt> <dd> <dl> <dt>

5014 (0x1396)
</dt> <dt>



The operation could not be completed because the cluster group is not online.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOST_NODE_NOT_RESOURCE_OWNER"></span><span id="error_host_node_not_resource_owner"></span>**ERROR\_HOST\_NODE\_NOT\_RESOURCE\_OWNER**
</dt> <dd> <dl> <dt>

5015 (0x1397)
</dt> <dt>



The operation failed because either the specified cluster node is not the owner of the resource, or the node is not a possible owner of the resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_HOST_NODE_NOT_GROUP_OWNER"></span><span id="error_host_node_not_group_owner"></span>**ERROR\_HOST\_NODE\_NOT\_GROUP\_OWNER**
</dt> <dd> <dl> <dt>

5016 (0x1398)
</dt> <dt>



The operation failed because either the specified cluster node is not the owner of the group, or the node is not a possible owner of the group.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESMON_CREATE_FAILED"></span><span id="error_resmon_create_failed"></span>**ERROR\_RESMON\_CREATE\_FAILED**
</dt> <dd> <dl> <dt>

5017 (0x1399)
</dt> <dt>



The cluster resource could not be created in the specified resource monitor.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESMON_ONLINE_FAILED"></span><span id="error_resmon_online_failed"></span>**ERROR\_RESMON\_ONLINE\_FAILED**
</dt> <dd> <dl> <dt>

5018 (0x139A)
</dt> <dt>



The cluster resource could not be brought online by the resource monitor.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_ONLINE"></span><span id="error_resource_online"></span>**ERROR\_RESOURCE\_ONLINE**
</dt> <dd> <dl> <dt>

5019 (0x139B)
</dt> <dt>



The operation could not be completed because the cluster resource is online.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUM_RESOURCE"></span><span id="error_quorum_resource"></span>**ERROR\_QUORUM\_RESOURCE**
</dt> <dd> <dl> <dt>

5020 (0x139C)
</dt> <dt>



The cluster resource could not be deleted or brought offline because it is the quorum resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_QUORUM_CAPABLE"></span><span id="error_not_quorum_capable"></span>**ERROR\_NOT\_QUORUM\_CAPABLE**
</dt> <dd> <dl> <dt>

5021 (0x139D)
</dt> <dt>



The cluster could not make the specified resource a quorum resource because it is not capable of being a quorum resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SHUTTING_DOWN"></span><span id="error_cluster_shutting_down"></span>**ERROR\_CLUSTER\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

5022 (0x139E)
</dt> <dt>



The cluster software is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_STATE"></span><span id="error_invalid_state"></span>**ERROR\_INVALID\_STATE**
</dt> <dd> <dl> <dt>

5023 (0x139F)
</dt> <dt>



The group or resource is not in the correct state to perform the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_PROPERTIES_STORED"></span><span id="error_resource_properties_stored"></span>**ERROR\_RESOURCE\_PROPERTIES\_STORED**
</dt> <dd> <dl> <dt>

5024 (0x13A0)
</dt> <dt>



The properties were stored but not all changes will take effect until the next time the resource is brought online.


</dt> </dl> </dd> <dt>

<span id="ERROR_NOT_QUORUM_CLASS"></span><span id="error_not_quorum_class"></span>**ERROR\_NOT\_QUORUM\_CLASS**
</dt> <dd> <dl> <dt>

5025 (0x13A1)
</dt> <dt>



The cluster could not make the specified resource a quorum resource because it does not belong to a shared storage class.


</dt> </dl> </dd> <dt>

<span id="ERROR_CORE_RESOURCE"></span><span id="error_core_resource"></span>**ERROR\_CORE\_RESOURCE**
</dt> <dd> <dl> <dt>

5026 (0x13A2)
</dt> <dt>



The cluster resource could not be deleted since it is a core resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUM_RESOURCE_ONLINE_FAILED"></span><span id="error_quorum_resource_online_failed"></span>**ERROR\_QUORUM\_RESOURCE\_ONLINE\_FAILED**
</dt> <dd> <dl> <dt>

5027 (0x13A3)
</dt> <dt>



The quorum resource failed to come online.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUMLOG_OPEN_FAILED"></span><span id="error_quorumlog_open_failed"></span>**ERROR\_QUORUMLOG\_OPEN\_FAILED**
</dt> <dd> <dl> <dt>

5028 (0x13A4)
</dt> <dt>



The quorum log could not be created or mounted successfully.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTERLOG_CORRUPT"></span><span id="error_clusterlog_corrupt"></span>**ERROR\_CLUSTERLOG\_CORRUPT**
</dt> <dd> <dl> <dt>

5029 (0x13A5)
</dt> <dt>



The cluster log is corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTERLOG_RECORD_EXCEEDS_MAXSIZE"></span><span id="error_clusterlog_record_exceeds_maxsize"></span>**ERROR\_CLUSTERLOG\_RECORD\_EXCEEDS\_MAXSIZE**
</dt> <dd> <dl> <dt>

5030 (0x13A6)
</dt> <dt>



The record could not be written to the cluster log since it exceeds the maximum size.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTERLOG_EXCEEDS_MAXSIZE"></span><span id="error_clusterlog_exceeds_maxsize"></span>**ERROR\_CLUSTERLOG\_EXCEEDS\_MAXSIZE**
</dt> <dd> <dl> <dt>

5031 (0x13A7)
</dt> <dt>



The cluster log exceeds its maximum size.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTERLOG_CHKPOINT_NOT_FOUND"></span><span id="error_clusterlog_chkpoint_not_found"></span>**ERROR\_CLUSTERLOG\_CHKPOINT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5032 (0x13A8)
</dt> <dt>



No checkpoint record was found in the cluster log.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTERLOG_NOT_ENOUGH_SPACE"></span><span id="error_clusterlog_not_enough_space"></span>**ERROR\_CLUSTERLOG\_NOT\_ENOUGH\_SPACE**
</dt> <dd> <dl> <dt>

5033 (0x13A9)
</dt> <dt>



The minimum required disk space needed for logging is not available.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUM_OWNER_ALIVE"></span><span id="error_quorum_owner_alive"></span>**ERROR\_QUORUM\_OWNER\_ALIVE**
</dt> <dd> <dl> <dt>

5034 (0x13AA)
</dt> <dt>



The cluster node failed to take control of the quorum resource because the resource is owned by another active node.


</dt> </dl> </dd> <dt>

<span id="ERROR_NETWORK_NOT_AVAILABLE"></span><span id="error_network_not_available"></span>**ERROR\_NETWORK\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5035 (0x13AB)
</dt> <dt>



A cluster network is not available for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_NODE_NOT_AVAILABLE"></span><span id="error_node_not_available"></span>**ERROR\_NODE\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5036 (0x13AC)
</dt> <dt>



A cluster node is not available for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_ALL_NODES_NOT_AVAILABLE"></span><span id="error_all_nodes_not_available"></span>**ERROR\_ALL\_NODES\_NOT\_AVAILABLE**
</dt> <dd> <dl> <dt>

5037 (0x13AD)
</dt> <dt>



All cluster nodes must be running to perform this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_FAILED"></span><span id="error_resource_failed"></span>**ERROR\_RESOURCE\_FAILED**
</dt> <dd> <dl> <dt>

5038 (0x13AE)
</dt> <dt>



A cluster resource failed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_NODE"></span><span id="error_cluster_invalid_node"></span>**ERROR\_CLUSTER\_INVALID\_NODE**
</dt> <dd> <dl> <dt>

5039 (0x13AF)
</dt> <dt>



The cluster node is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_EXISTS"></span><span id="error_cluster_node_exists"></span>**ERROR\_CLUSTER\_NODE\_EXISTS**
</dt> <dd> <dl> <dt>

5040 (0x13B0)
</dt> <dt>



The cluster node already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_JOIN_IN_PROGRESS"></span><span id="error_cluster_join_in_progress"></span>**ERROR\_CLUSTER\_JOIN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5041 (0x13B1)
</dt> <dt>



A node is in the process of joining the cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_NOT_FOUND"></span><span id="error_cluster_node_not_found"></span>**ERROR\_CLUSTER\_NODE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5042 (0x13B2)
</dt> <dt>



The cluster node was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_LOCAL_NODE_NOT_FOUND"></span><span id="error_cluster_local_node_not_found"></span>**ERROR\_CLUSTER\_LOCAL\_NODE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5043 (0x13B3)
</dt> <dt>



The cluster local node information was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_EXISTS"></span><span id="error_cluster_network_exists"></span>**ERROR\_CLUSTER\_NETWORK\_EXISTS**
</dt> <dd> <dl> <dt>

5044 (0x13B4)
</dt> <dt>



The cluster network already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_NOT_FOUND"></span><span id="error_cluster_network_not_found"></span>**ERROR\_CLUSTER\_NETWORK\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5045 (0x13B5)
</dt> <dt>



The cluster network was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETINTERFACE_EXISTS"></span><span id="error_cluster_netinterface_exists"></span>**ERROR\_CLUSTER\_NETINTERFACE\_EXISTS**
</dt> <dd> <dl> <dt>

5046 (0x13B6)
</dt> <dt>



The cluster network interface already exists.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETINTERFACE_NOT_FOUND"></span><span id="error_cluster_netinterface_not_found"></span>**ERROR\_CLUSTER\_NETINTERFACE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5047 (0x13B7)
</dt> <dt>



The cluster network interface was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_REQUEST"></span><span id="error_cluster_invalid_request"></span>**ERROR\_CLUSTER\_INVALID\_REQUEST**
</dt> <dd> <dl> <dt>

5048 (0x13B8)
</dt> <dt>



The cluster request is not valid for this object.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_NETWORK_PROVIDER"></span><span id="error_cluster_invalid_network_provider"></span>**ERROR\_CLUSTER\_INVALID\_NETWORK\_PROVIDER**
</dt> <dd> <dl> <dt>

5049 (0x13B9)
</dt> <dt>



The cluster network provider is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_DOWN"></span><span id="error_cluster_node_down"></span>**ERROR\_CLUSTER\_NODE\_DOWN**
</dt> <dd> <dl> <dt>

5050 (0x13BA)
</dt> <dt>



The cluster node is down.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_UNREACHABLE"></span><span id="error_cluster_node_unreachable"></span>**ERROR\_CLUSTER\_NODE\_UNREACHABLE**
</dt> <dd> <dl> <dt>

5051 (0x13BB)
</dt> <dt>



The cluster node is not reachable.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_NOT_MEMBER"></span><span id="error_cluster_node_not_member"></span>**ERROR\_CLUSTER\_NODE\_NOT\_MEMBER**
</dt> <dd> <dl> <dt>

5052 (0x13BC)
</dt> <dt>



The cluster node is not a member of the cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_JOIN_NOT_IN_PROGRESS"></span><span id="error_cluster_join_not_in_progress"></span>**ERROR\_CLUSTER\_JOIN\_NOT\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5053 (0x13BD)
</dt> <dt>



A cluster join operation is not in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_NETWORK"></span><span id="error_cluster_invalid_network"></span>**ERROR\_CLUSTER\_INVALID\_NETWORK**
</dt> <dd> <dl> <dt>

5054 (0x13BE)
</dt> <dt>



The cluster network is not valid.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_UP"></span><span id="error_cluster_node_up"></span>**ERROR\_CLUSTER\_NODE\_UP**
</dt> <dd> <dl> <dt>

5056 (0x13C0)
</dt> <dt>



The cluster node is up.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_IPADDR_IN_USE"></span><span id="error_cluster_ipaddr_in_use"></span>**ERROR\_CLUSTER\_IPADDR\_IN\_USE**
</dt> <dd> <dl> <dt>

5057 (0x13C1)
</dt> <dt>



The cluster IP address is already in use.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_NOT_PAUSED"></span><span id="error_cluster_node_not_paused"></span>**ERROR\_CLUSTER\_NODE\_NOT\_PAUSED**
</dt> <dd> <dl> <dt>

5058 (0x13C2)
</dt> <dt>



The cluster node is not paused.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NO_SECURITY_CONTEXT"></span><span id="error_cluster_no_security_context"></span>**ERROR\_CLUSTER\_NO\_SECURITY\_CONTEXT**
</dt> <dd> <dl> <dt>

5059 (0x13C3)
</dt> <dt>



No cluster security context is available.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_NOT_INTERNAL"></span><span id="error_cluster_network_not_internal"></span>**ERROR\_CLUSTER\_NETWORK\_NOT\_INTERNAL**
</dt> <dd> <dl> <dt>

5060 (0x13C4)
</dt> <dt>



The cluster network is not configured for internal cluster communication.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_ALREADY_UP"></span><span id="error_cluster_node_already_up"></span>**ERROR\_CLUSTER\_NODE\_ALREADY\_UP**
</dt> <dd> <dl> <dt>

5061 (0x13C5)
</dt> <dt>



The cluster node is already up.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_ALREADY_DOWN"></span><span id="error_cluster_node_already_down"></span>**ERROR\_CLUSTER\_NODE\_ALREADY\_DOWN**
</dt> <dd> <dl> <dt>

5062 (0x13C6)
</dt> <dt>



The cluster node is already down.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_ALREADY_ONLINE"></span><span id="error_cluster_network_already_online"></span>**ERROR\_CLUSTER\_NETWORK\_ALREADY\_ONLINE**
</dt> <dd> <dl> <dt>

5063 (0x13C7)
</dt> <dt>



The cluster network is already online.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_ALREADY_OFFLINE"></span><span id="error_cluster_network_already_offline"></span>**ERROR\_CLUSTER\_NETWORK\_ALREADY\_OFFLINE**
</dt> <dd> <dl> <dt>

5064 (0x13C8)
</dt> <dt>



The cluster network is already offline.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_ALREADY_MEMBER"></span><span id="error_cluster_node_already_member"></span>**ERROR\_CLUSTER\_NODE\_ALREADY\_MEMBER**
</dt> <dd> <dl> <dt>

5065 (0x13C9)
</dt> <dt>



The cluster node is already a member of the cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_LAST_INTERNAL_NETWORK"></span><span id="error_cluster_last_internal_network"></span>**ERROR\_CLUSTER\_LAST\_INTERNAL\_NETWORK**
</dt> <dd> <dl> <dt>

5066 (0x13CA)
</dt> <dt>



The cluster network is the only one configured for internal cluster communication between two or more active cluster nodes. The internal communication capability cannot be removed from the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_HAS_DEPENDENTS"></span><span id="error_cluster_network_has_dependents"></span>**ERROR\_CLUSTER\_NETWORK\_HAS\_DEPENDENTS**
</dt> <dd> <dl> <dt>

5067 (0x13CB)
</dt> <dt>



One or more cluster resources depend on the network to provide service to clients. The client access capability cannot be removed from the network.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_OPERATION_ON_QUORUM"></span><span id="error_invalid_operation_on_quorum"></span>**ERROR\_INVALID\_OPERATION\_ON\_QUORUM**
</dt> <dd> <dl> <dt>

5068 (0x13CC)
</dt> <dt>



This operation cannot be performed on the cluster resource as it the quorum resource. You may not bring the quorum resource offline or modify its possible owners list.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENCY_NOT_ALLOWED"></span><span id="error_dependency_not_allowed"></span>**ERROR\_DEPENDENCY\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

5069 (0x13CD)
</dt> <dt>



The cluster quorum resource is not allowed to have any dependencies.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_PAUSED"></span><span id="error_cluster_node_paused"></span>**ERROR\_CLUSTER\_NODE\_PAUSED**
</dt> <dd> <dl> <dt>

5070 (0x13CE)
</dt> <dt>



The cluster node is paused.


</dt> </dl> </dd> <dt>

<span id="ERROR_NODE_CANT_HOST_RESOURCE"></span><span id="error_node_cant_host_resource"></span>**ERROR\_NODE\_CANT\_HOST\_RESOURCE**
</dt> <dd> <dl> <dt>

5071 (0x13CF)
</dt> <dt>



The cluster resource cannot be brought online. The owner node cannot run this resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_NOT_READY"></span><span id="error_cluster_node_not_ready"></span>**ERROR\_CLUSTER\_NODE\_NOT\_READY**
</dt> <dd> <dl> <dt>

5072 (0x13D0)
</dt> <dt>



The cluster node is not ready to perform the requested operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_SHUTTING_DOWN"></span><span id="error_cluster_node_shutting_down"></span>**ERROR\_CLUSTER\_NODE\_SHUTTING\_DOWN**
</dt> <dd> <dl> <dt>

5073 (0x13D1)
</dt> <dt>



The cluster node is shutting down.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_JOIN_ABORTED"></span><span id="error_cluster_join_aborted"></span>**ERROR\_CLUSTER\_JOIN\_ABORTED**
</dt> <dd> <dl> <dt>

5074 (0x13D2)
</dt> <dt>



The cluster join operation was aborted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INCOMPATIBLE_VERSIONS"></span><span id="error_cluster_incompatible_versions"></span>**ERROR\_CLUSTER\_INCOMPATIBLE\_VERSIONS**
</dt> <dd> <dl> <dt>

5075 (0x13D3)
</dt> <dt>



The cluster join operation failed due to incompatible software versions between the joining node and its sponsor.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_MAXNUM_OF_RESOURCES_EXCEEDED"></span><span id="error_cluster_maxnum_of_resources_exceeded"></span>**ERROR\_CLUSTER\_MAXNUM\_OF\_RESOURCES\_EXCEEDED**
</dt> <dd> <dl> <dt>

5076 (0x13D4)
</dt> <dt>



This resource cannot be created because the cluster has reached the limit on the number of resources it can monitor.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SYSTEM_CONFIG_CHANGED"></span><span id="error_cluster_system_config_changed"></span>**ERROR\_CLUSTER\_SYSTEM\_CONFIG\_CHANGED**
</dt> <dd> <dl> <dt>

5077 (0x13D5)
</dt> <dt>



The system configuration changed during the cluster join or form operation. The join or form operation was aborted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_TYPE_NOT_FOUND"></span><span id="error_cluster_resource_type_not_found"></span>**ERROR\_CLUSTER\_RESOURCE\_TYPE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5078 (0x13D6)
</dt> <dt>



The specified resource type was not found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESTYPE_NOT_SUPPORTED"></span><span id="error_cluster_restype_not_supported"></span>**ERROR\_CLUSTER\_RESTYPE\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

5079 (0x13D7)
</dt> <dt>



The specified node does not support a resource of this type. This may be due to version inconsistencies or due to the absence of the resource DLL on this node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESNAME_NOT_FOUND"></span><span id="error_cluster_resname_not_found"></span>**ERROR\_CLUSTER\_RESNAME\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5080 (0x13D8)
</dt> <dt>



The specified resource name is not supported by this resource DLL. This may be due to a bad (or changed) name supplied to the resource DLL.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NO_RPC_PACKAGES_REGISTERED"></span><span id="error_cluster_no_rpc_packages_registered"></span>**ERROR\_CLUSTER\_NO\_RPC\_PACKAGES\_REGISTERED**
</dt> <dd> <dl> <dt>

5081 (0x13D9)
</dt> <dt>



No authentication package could be registered with the RPC server.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_OWNER_NOT_IN_PREFLIST"></span><span id="error_cluster_owner_not_in_preflist"></span>**ERROR\_CLUSTER\_OWNER\_NOT\_IN\_PREFLIST**
</dt> <dd> <dl> <dt>

5082 (0x13DA)
</dt> <dt>



You cannot bring the group online because the owner of the group is not in the preferred list for the group. To change the owner node for the group, move the group.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_DATABASE_SEQMISMATCH"></span><span id="error_cluster_database_seqmismatch"></span>**ERROR\_CLUSTER\_DATABASE\_SEQMISMATCH**
</dt> <dd> <dl> <dt>

5083 (0x13DB)
</dt> <dt>



The join operation failed because the cluster database sequence number has changed or is incompatible with the locker node. This may happen during a join operation if the cluster database was changing during the join.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESMON_INVALID_STATE"></span><span id="error_resmon_invalid_state"></span>**ERROR\_RESMON\_INVALID\_STATE**
</dt> <dd> <dl> <dt>

5084 (0x13DC)
</dt> <dt>



The resource monitor will not allow the fail operation to be performed while the resource is in its current state. This may happen if the resource is in a pending state.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_GUM_NOT_LOCKER"></span><span id="error_cluster_gum_not_locker"></span>**ERROR\_CLUSTER\_GUM\_NOT\_LOCKER**
</dt> <dd> <dl> <dt>

5085 (0x13DD)
</dt> <dt>



A non locker code got a request to reserve the lock for making global updates.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUM_DISK_NOT_FOUND"></span><span id="error_quorum_disk_not_found"></span>**ERROR\_QUORUM\_DISK\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5086 (0x13DE)
</dt> <dt>



The quorum disk could not be located by the cluster service.


</dt> </dl> </dd> <dt>

<span id="ERROR_DATABASE_BACKUP_CORRUPT"></span><span id="error_database_backup_corrupt"></span>**ERROR\_DATABASE\_BACKUP\_CORRUPT**
</dt> <dd> <dl> <dt>

5087 (0x13DF)
</dt> <dt>



The backed up cluster database is possibly corrupt.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_ALREADY_HAS_DFS_ROOT"></span><span id="error_cluster_node_already_has_dfs_root"></span>**ERROR\_CLUSTER\_NODE\_ALREADY\_HAS\_DFS\_ROOT**
</dt> <dd> <dl> <dt>

5088 (0x13E0)
</dt> <dt>



A DFS root already exists in this cluster node.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_PROPERTY_UNCHANGEABLE"></span><span id="error_resource_property_unchangeable"></span>**ERROR\_RESOURCE\_PROPERTY\_UNCHANGEABLE**
</dt> <dd> <dl> <dt>

5089 (0x13E1)
</dt> <dt>



An attempt to modify a resource property failed because it conflicts with another existing property.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_MEMBERSHIP_INVALID_STATE"></span><span id="error_cluster_membership_invalid_state"></span>**ERROR\_CLUSTER\_MEMBERSHIP\_INVALID\_STATE**
</dt> <dd> <dl> <dt>

5890 (0x1702)
</dt> <dt>



An operation was attempted that is incompatible with the current membership state of the node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_QUORUMLOG_NOT_FOUND"></span><span id="error_cluster_quorumlog_not_found"></span>**ERROR\_CLUSTER\_QUORUMLOG\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

5891 (0x1703)
</dt> <dt>



The quorum resource does not contain the quorum log.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_MEMBERSHIP_HALT"></span><span id="error_cluster_membership_halt"></span>**ERROR\_CLUSTER\_MEMBERSHIP\_HALT**
</dt> <dd> <dl> <dt>

5892 (0x1704)
</dt> <dt>



The membership engine requested shutdown of the cluster service on this node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INSTANCE_ID_MISMATCH"></span><span id="error_cluster_instance_id_mismatch"></span>**ERROR\_CLUSTER\_INSTANCE\_ID\_MISMATCH**
</dt> <dd> <dl> <dt>

5893 (0x1705)
</dt> <dt>



The join operation failed because the cluster instance ID of the joining node does not match the cluster instance ID of the sponsor node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NETWORK_NOT_FOUND_FOR_IP"></span><span id="error_cluster_network_not_found_for_ip"></span>**ERROR\_CLUSTER\_NETWORK\_NOT\_FOUND\_FOR\_IP**
</dt> <dd> <dl> <dt>

5894 (0x1706)
</dt> <dt>



A matching cluster network for the specified IP address could not be found.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PROPERTY_DATA_TYPE_MISMATCH"></span><span id="error_cluster_property_data_type_mismatch"></span>**ERROR\_CLUSTER\_PROPERTY\_DATA\_TYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

5895 (0x1707)
</dt> <dt>



The actual data type of the property did not match the expected data type of the property.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_EVICT_WITHOUT_CLEANUP"></span><span id="error_cluster_evict_without_cleanup"></span>**ERROR\_CLUSTER\_EVICT\_WITHOUT\_CLEANUP**
</dt> <dd> <dl> <dt>

5896 (0x1708)
</dt> <dt>



The cluster node was evicted from the cluster successfully, but the node was not cleaned up. To determine what cleanup steps failed and how to recover, see the Failover Clustering application event log using Event Viewer.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PARAMETER_MISMATCH"></span><span id="error_cluster_parameter_mismatch"></span>**ERROR\_CLUSTER\_PARAMETER\_MISMATCH**
</dt> <dd> <dl> <dt>

5897 (0x1709)
</dt> <dt>



Two or more parameter values specified for a resource's properties are in conflict.


</dt> </dl> </dd> <dt>

<span id="ERROR_NODE_CANNOT_BE_CLUSTERED"></span><span id="error_node_cannot_be_clustered"></span>**ERROR\_NODE\_CANNOT\_BE\_CLUSTERED**
</dt> <dd> <dl> <dt>

5898 (0x170A)
</dt> <dt>



This computer cannot be made a member of a cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_WRONG_OS_VERSION"></span><span id="error_cluster_wrong_os_version"></span>**ERROR\_CLUSTER\_WRONG\_OS\_VERSION**
</dt> <dd> <dl> <dt>

5899 (0x170B)
</dt> <dt>



This computer cannot be made a member of a cluster because it does not have the correct version of Windows installed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_CANT_CREATE_DUP_CLUSTER_NAME"></span><span id="error_cluster_cant_create_dup_cluster_name"></span>**ERROR\_CLUSTER\_CANT\_CREATE\_DUP\_CLUSTER\_NAME**
</dt> <dd> <dl> <dt>

5900 (0x170C)
</dt> <dt>



A cluster cannot be created with the specified cluster name because that cluster name is already in use. Specify a different name for the cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSCFG_ALREADY_COMMITTED"></span><span id="error_cluscfg_already_committed"></span>**ERROR\_CLUSCFG\_ALREADY\_COMMITTED**
</dt> <dd> <dl> <dt>

5901 (0x170D)
</dt> <dt>



The cluster configuration action has already been committed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSCFG_ROLLBACK_FAILED"></span><span id="error_cluscfg_rollback_failed"></span>**ERROR\_CLUSCFG\_ROLLBACK\_FAILED**
</dt> <dd> <dl> <dt>

5902 (0x170E)
</dt> <dt>



The cluster configuration action could not be rolled back.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSCFG_SYSTEM_DISK_DRIVE_LETTER_CONFLICT"></span><span id="error_cluscfg_system_disk_drive_letter_conflict"></span>**ERROR\_CLUSCFG\_SYSTEM\_DISK\_DRIVE\_LETTER\_CONFLICT**
</dt> <dd> <dl> <dt>

5903 (0x170F)
</dt> <dt>



The drive letter assigned to a system disk on one node conflicted with the drive letter assigned to a disk on another node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_OLD_VERSION"></span><span id="error_cluster_old_version"></span>**ERROR\_CLUSTER\_OLD\_VERSION**
</dt> <dd> <dl> <dt>

5904 (0x1710)
</dt> <dt>



One or more nodes in the cluster are running a version of Windows that does not support this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_MISMATCHED_COMPUTER_ACCT_NAME"></span><span id="error_cluster_mismatched_computer_acct_name"></span>**ERROR\_CLUSTER\_MISMATCHED\_COMPUTER\_ACCT\_NAME**
</dt> <dd> <dl> <dt>

5905 (0x1711)
</dt> <dt>



The name of the corresponding computer account doesn't match the Network Name for this resource.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NO_NET_ADAPTERS"></span><span id="error_cluster_no_net_adapters"></span>**ERROR\_CLUSTER\_NO\_NET\_ADAPTERS**
</dt> <dd> <dl> <dt>

5906 (0x1712)
</dt> <dt>



No network adapters are available.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_POISONED"></span><span id="error_cluster_poisoned"></span>**ERROR\_CLUSTER\_POISONED**
</dt> <dd> <dl> <dt>

5907 (0x1713)
</dt> <dt>



The cluster node has been poisoned.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_GROUP_MOVING"></span><span id="error_cluster_group_moving"></span>**ERROR\_CLUSTER\_GROUP\_MOVING**
</dt> <dd> <dl> <dt>

5908 (0x1714)
</dt> <dt>



The group is unable to accept the request since it is moving to another node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_TYPE_BUSY"></span><span id="error_cluster_resource_type_busy"></span>**ERROR\_CLUSTER\_RESOURCE\_TYPE\_BUSY**
</dt> <dd> <dl> <dt>

5909 (0x1715)
</dt> <dt>



The resource type cannot accept the request since is too busy performing another operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_CALL_TIMED_OUT"></span><span id="error_resource_call_timed_out"></span>**ERROR\_RESOURCE\_CALL\_TIMED\_OUT**
</dt> <dd> <dl> <dt>

5910 (0x1716)
</dt> <dt>



The call to the cluster resource DLL timed out.


</dt> </dl> </dd> <dt>

<span id="ERROR_INVALID_CLUSTER_IPV6_ADDRESS"></span><span id="error_invalid_cluster_ipv6_address"></span>**ERROR\_INVALID\_CLUSTER\_IPV6\_ADDRESS**
</dt> <dd> <dl> <dt>

5911 (0x1717)
</dt> <dt>



The address is not valid for an IPv6 Address resource. A global IPv6 address is required, and it must match a cluster network. Compatibility addresses are not permitted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INTERNAL_INVALID_FUNCTION"></span><span id="error_cluster_internal_invalid_function"></span>**ERROR\_CLUSTER\_INTERNAL\_INVALID\_FUNCTION**
</dt> <dd> <dl> <dt>

5912 (0x1718)
</dt> <dt>



An internal cluster error occurred. A call to an invalid function was attempted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PARAMETER_OUT_OF_BOUNDS"></span><span id="error_cluster_parameter_out_of_bounds"></span>**ERROR\_CLUSTER\_PARAMETER\_OUT\_OF\_BOUNDS**
</dt> <dd> <dl> <dt>

5913 (0x1719)
</dt> <dt>



A parameter value is out of acceptable range.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PARTIAL_SEND"></span><span id="error_cluster_partial_send"></span>**ERROR\_CLUSTER\_PARTIAL\_SEND**
</dt> <dd> <dl> <dt>

5914 (0x171A)
</dt> <dt>



A network error occurred while sending data to another node in the cluster. The number of bytes transmitted was less than required.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_REGISTRY_INVALID_FUNCTION"></span><span id="error_cluster_registry_invalid_function"></span>**ERROR\_CLUSTER\_REGISTRY\_INVALID\_FUNCTION**
</dt> <dd> <dl> <dt>

5915 (0x171B)
</dt> <dt>



An invalid cluster registry operation was attempted.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_STRING_TERMINATION"></span><span id="error_cluster_invalid_string_termination"></span>**ERROR\_CLUSTER\_INVALID\_STRING\_TERMINATION**
</dt> <dd> <dl> <dt>

5916 (0x171C)
</dt> <dt>



An input string of characters is not properly terminated.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_STRING_FORMAT"></span><span id="error_cluster_invalid_string_format"></span>**ERROR\_CLUSTER\_INVALID\_STRING\_FORMAT**
</dt> <dd> <dl> <dt>

5917 (0x171D)
</dt> <dt>



An input string of characters is not in a valid format for the data it represents.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_DATABASE_TRANSACTION_IN_PROGRESS"></span><span id="error_cluster_database_transaction_in_progress"></span>**ERROR\_CLUSTER\_DATABASE\_TRANSACTION\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5918 (0x171E)
</dt> <dt>



An internal cluster error occurred. A cluster database transaction was attempted while a transaction was already in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_DATABASE_TRANSACTION_NOT_IN_PROGRESS"></span><span id="error_cluster_database_transaction_not_in_progress"></span>**ERROR\_CLUSTER\_DATABASE\_TRANSACTION\_NOT\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5919 (0x171F)
</dt> <dt>



An internal cluster error occurred. There was an attempt to commit a cluster database transaction while no transaction was in progress.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NULL_DATA"></span><span id="error_cluster_null_data"></span>**ERROR\_CLUSTER\_NULL\_DATA**
</dt> <dd> <dl> <dt>

5920 (0x1720)
</dt> <dt>



An internal cluster error occurred. Data was not properly initialized.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PARTIAL_READ"></span><span id="error_cluster_partial_read"></span>**ERROR\_CLUSTER\_PARTIAL\_READ**
</dt> <dd> <dl> <dt>

5921 (0x1721)
</dt> <dt>



An error occurred while reading from a stream of data. An unexpected number of bytes was returned.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_PARTIAL_WRITE"></span><span id="error_cluster_partial_write"></span>**ERROR\_CLUSTER\_PARTIAL\_WRITE**
</dt> <dd> <dl> <dt>

5922 (0x1722)
</dt> <dt>



An error occurred while writing to a stream of data. The required number of bytes could not be written.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_CANT_DESERIALIZE_DATA"></span><span id="error_cluster_cant_deserialize_data"></span>**ERROR\_CLUSTER\_CANT\_DESERIALIZE\_DATA**
</dt> <dd> <dl> <dt>

5923 (0x1723)
</dt> <dt>



An error occurred while deserializing a stream of cluster data.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENT_RESOURCE_PROPERTY_CONFLICT"></span><span id="error_dependent_resource_property_conflict"></span>**ERROR\_DEPENDENT\_RESOURCE\_PROPERTY\_CONFLICT**
</dt> <dd> <dl> <dt>

5924 (0x1724)
</dt> <dt>



One or more property values for this resource are in conflict with one or more property values associated with its dependent resource(s).


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NO_QUORUM"></span><span id="error_cluster_no_quorum"></span>**ERROR\_CLUSTER\_NO\_QUORUM**
</dt> <dd> <dl> <dt>

5925 (0x1725)
</dt> <dt>



A quorum of cluster nodes was not present to form a cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_IPV6_NETWORK"></span><span id="error_cluster_invalid_ipv6_network"></span>**ERROR\_CLUSTER\_INVALID\_IPV6\_NETWORK**
</dt> <dd> <dl> <dt>

5926 (0x1726)
</dt> <dt>



The cluster network is not valid for an IPv6 Address resource, or it does not match the configured address.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_IPV6_TUNNEL_NETWORK"></span><span id="error_cluster_invalid_ipv6_tunnel_network"></span>**ERROR\_CLUSTER\_INVALID\_IPV6\_TUNNEL\_NETWORK**
</dt> <dd> <dl> <dt>

5927 (0x1727)
</dt> <dt>



The cluster network is not valid for an IPv6 Tunnel resource. Check the configuration of the IP Address resource on which the IPv6 Tunnel resource depends.


</dt> </dl> </dd> <dt>

<span id="ERROR_QUORUM_NOT_ALLOWED_IN_THIS_GROUP"></span><span id="error_quorum_not_allowed_in_this_group"></span>**ERROR\_QUORUM\_NOT\_ALLOWED\_IN\_THIS\_GROUP**
</dt> <dd> <dl> <dt>

5928 (0x1728)
</dt> <dt>



Quorum resource cannot reside in the Available Storage group.


</dt> </dl> </dd> <dt>

<span id="ERROR_DEPENDENCY_TREE_TOO_COMPLEX"></span><span id="error_dependency_tree_too_complex"></span>**ERROR\_DEPENDENCY\_TREE\_TOO\_COMPLEX**
</dt> <dd> <dl> <dt>

5929 (0x1729)
</dt> <dt>



The dependencies for this resource are nested too deeply.


</dt> </dl> </dd> <dt>

<span id="ERROR_EXCEPTION_IN_RESOURCE_CALL"></span><span id="error_exception_in_resource_call"></span>**ERROR\_EXCEPTION\_IN\_RESOURCE\_CALL**
</dt> <dd> <dl> <dt>

5930 (0x172A)
</dt> <dt>



The call into the resource DLL raised an unhandled exception.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RHS_FAILED_INITIALIZATION"></span><span id="error_cluster_rhs_failed_initialization"></span>**ERROR\_CLUSTER\_RHS\_FAILED\_INITIALIZATION**
</dt> <dd> <dl> <dt>

5931 (0x172B)
</dt> <dt>



The RHS process failed to initialize.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NOT_INSTALLED"></span><span id="error_cluster_not_installed"></span>**ERROR\_CLUSTER\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

5932 (0x172C)
</dt> <dt>



The Failover Clustering feature is not installed on this node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCES_MUST_BE_ONLINE_ON_THE_SAME_NODE"></span><span id="error_cluster_resources_must_be_online_on_the_same_node"></span>**ERROR\_CLUSTER\_RESOURCES\_MUST\_BE\_ONLINE\_ON\_THE\_SAME\_NODE**
</dt> <dd> <dl> <dt>

5933 (0x172D)
</dt> <dt>



The resources must be online on the same node for this operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_MAX_NODES_IN_CLUSTER"></span><span id="error_cluster_max_nodes_in_cluster"></span>**ERROR\_CLUSTER\_MAX\_NODES\_IN\_CLUSTER**
</dt> <dd> <dl> <dt>

5934 (0x172E)
</dt> <dt>



A new node can not be added since this cluster is already at its maximum number of nodes.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_TOO_MANY_NODES"></span><span id="error_cluster_too_many_nodes"></span>**ERROR\_CLUSTER\_TOO\_MANY\_NODES**
</dt> <dd> <dl> <dt>

5935 (0x172F)
</dt> <dt>



This cluster can not be created since the specified number of nodes exceeds the maximum allowed limit.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_OBJECT_ALREADY_USED"></span><span id="error_cluster_object_already_used"></span>**ERROR\_CLUSTER\_OBJECT\_ALREADY\_USED**
</dt> <dd> <dl> <dt>

5936 (0x1730)
</dt> <dt>



An attempt to use the specified cluster name failed because an enabled computer object with the given name already exists in the domain.


</dt> </dl> </dd> <dt>

<span id="ERROR_NONCORE_GROUPS_FOUND"></span><span id="error_noncore_groups_found"></span>**ERROR\_NONCORE\_GROUPS\_FOUND**
</dt> <dd> <dl> <dt>

5937 (0x1731)
</dt> <dt>



This cluster cannot be destroyed. It has non-core application groups which must be deleted before the cluster can be destroyed.


</dt> </dl> </dd> <dt>

<span id="ERROR_FILE_SHARE_RESOURCE_CONFLICT"></span><span id="error_file_share_resource_conflict"></span>**ERROR\_FILE\_SHARE\_RESOURCE\_CONFLICT**
</dt> <dd> <dl> <dt>

5938 (0x1732)
</dt> <dt>



File share associated with file share witness resource cannot be hosted by this cluster or any of its nodes.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_EVICT_INVALID_REQUEST"></span><span id="error_cluster_evict_invalid_request"></span>**ERROR\_CLUSTER\_EVICT\_INVALID\_REQUEST**
</dt> <dd> <dl> <dt>

5939 (0x1733)
</dt> <dt>



Eviction of this node is invalid at this time. Due to quorum requirements node eviction will result in cluster shutdown. If it is the last node in the cluster, destroy cluster command should be used.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SINGLETON_RESOURCE"></span><span id="error_cluster_singleton_resource"></span>**ERROR\_CLUSTER\_SINGLETON\_RESOURCE**
</dt> <dd> <dl> <dt>

5940 (0x1734)
</dt> <dt>



Only one instance of this resource type is allowed in the cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_GROUP_SINGLETON_RESOURCE"></span><span id="error_cluster_group_singleton_resource"></span>**ERROR\_CLUSTER\_GROUP\_SINGLETON\_RESOURCE**
</dt> <dd> <dl> <dt>

5941 (0x1735)
</dt> <dt>



Only one instance of this resource type is allowed per resource group.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_PROVIDER_FAILED"></span><span id="error_cluster_resource_provider_failed"></span>**ERROR\_CLUSTER\_RESOURCE\_PROVIDER\_FAILED**
</dt> <dd> <dl> <dt>

5942 (0x1736)
</dt> <dt>



The resource failed to come online due to the failure of one or more provider resources.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_CONFIGURATION_ERROR"></span><span id="error_cluster_resource_configuration_error"></span>**ERROR\_CLUSTER\_RESOURCE\_CONFIGURATION\_ERROR**
</dt> <dd> <dl> <dt>

5943 (0x1737)
</dt> <dt>



The resource has indicated that it cannot come online on any node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_GROUP_BUSY"></span><span id="error_cluster_group_busy"></span>**ERROR\_CLUSTER\_GROUP\_BUSY**
</dt> <dd> <dl> <dt>

5944 (0x1738)
</dt> <dt>



The current operation cannot be performed on this group at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NOT_SHARED_VOLUME"></span><span id="error_cluster_not_shared_volume"></span>**ERROR\_CLUSTER\_NOT\_SHARED\_VOLUME**
</dt> <dd> <dl> <dt>

5945 (0x1739)
</dt> <dt>



The directory or file is not located on a cluster shared volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_SECURITY_DESCRIPTOR"></span><span id="error_cluster_invalid_security_descriptor"></span>**ERROR\_CLUSTER\_INVALID\_SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

5946 (0x173A)
</dt> <dt>



The Security Descriptor does not meet the requirements for a cluster.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SHARED_VOLUMES_IN_USE"></span><span id="error_cluster_shared_volumes_in_use"></span>**ERROR\_CLUSTER\_SHARED\_VOLUMES\_IN\_USE**
</dt> <dd> <dl> <dt>

5947 (0x173B)
</dt> <dt>



There is one or more shared volumes resources configured in the cluster. Those resources must be moved to available storage in order for operation to succeed.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_USE_SHARED_VOLUMES_API"></span><span id="error_cluster_use_shared_volumes_api"></span>**ERROR\_CLUSTER\_USE\_SHARED\_VOLUMES\_API**
</dt> <dd> <dl> <dt>

5948 (0x173C)
</dt> <dt>



This group or resource cannot be directly manipulated. Use shared volume APIs to perform desired operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_BACKUP_IN_PROGRESS"></span><span id="error_cluster_backup_in_progress"></span>**ERROR\_CLUSTER\_BACKUP\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5949 (0x173D)
</dt> <dt>



Back up is in progress. Please wait for backup completion before trying this operation again.


</dt> </dl> </dd> <dt>

<span id="ERROR_NON_CSV_PATH"></span><span id="error_non_csv_path"></span>**ERROR\_NON\_CSV\_PATH**
</dt> <dd> <dl> <dt>

5950 (0x173E)
</dt> <dt>



The path does not belong to a cluster shared volume.


</dt> </dl> </dd> <dt>

<span id="ERROR_CSV_VOLUME_NOT_LOCAL"></span><span id="error_csv_volume_not_local"></span>**ERROR\_CSV\_VOLUME\_NOT\_LOCAL**
</dt> <dd> <dl> <dt>

5951 (0x173F)
</dt> <dt>



The cluster shared volume is not locally mounted on this node.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_WATCHDOG_TERMINATING"></span><span id="error_cluster_watchdog_terminating"></span>**ERROR\_CLUSTER\_WATCHDOG\_TERMINATING**
</dt> <dd> <dl> <dt>

5952 (0x1740)
</dt> <dt>



The cluster watchdog is terminating.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_VETOED_MOVE_INCOMPATIBLE_NODES"></span><span id="error_cluster_resource_vetoed_move_incompatible_nodes"></span>**ERROR\_CLUSTER\_RESOURCE\_VETOED\_MOVE\_INCOMPATIBLE\_NODES**
</dt> <dd> <dl> <dt>

5953 (0x1741)
</dt> <dt>



A resource vetoed a move between two nodes because they are incompatible.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_INVALID_NODE_WEIGHT"></span><span id="error_cluster_invalid_node_weight"></span>**ERROR\_CLUSTER\_INVALID\_NODE\_WEIGHT**
</dt> <dd> <dl> <dt>

5954 (0x1742)
</dt> <dt>



The request is invalid either because node weight cannot be changed while the cluster is in disk-only quorum mode, or because changing the node weight would violate the minimum cluster quorum requirements.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_VETOED_CALL"></span><span id="error_cluster_resource_vetoed_call"></span>**ERROR\_CLUSTER\_RESOURCE\_VETOED\_CALL**
</dt> <dd> <dl> <dt>

5955 (0x1743)
</dt> <dt>



The resource vetoed the call.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESMON_SYSTEM_RESOURCES_LACKING"></span><span id="error_resmon_system_resources_lacking"></span>**ERROR\_RESMON\_SYSTEM\_RESOURCES\_LACKING**
</dt> <dd> <dl> <dt>

5956 (0x1744)
</dt> <dt>



Resource could not start or run because it could not reserve sufficient system resources.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_DESTINATION"></span><span id="error_cluster_resource_vetoed_move_not_enough_resources_on_destination"></span>**ERROR\_CLUSTER\_RESOURCE\_VETOED\_MOVE\_NOT\_ENOUGH\_RESOURCES\_ON\_DESTINATION**
</dt> <dd> <dl> <dt>

5957 (0x1745)
</dt> <dt>



A resource vetoed a move between two nodes because the destination currently does not have enough resources to complete the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_VETOED_MOVE_NOT_ENOUGH_RESOURCES_ON_SOURCE"></span><span id="error_cluster_resource_vetoed_move_not_enough_resources_on_source"></span>**ERROR\_CLUSTER\_RESOURCE\_VETOED\_MOVE\_NOT\_ENOUGH\_RESOURCES\_ON\_SOURCE**
</dt> <dd> <dl> <dt>

5958 (0x1746)
</dt> <dt>



A resource vetoed a move between two nodes because the source currently does not have enough resources to complete the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_GROUP_QUEUED"></span><span id="error_cluster_group_queued"></span>**ERROR\_CLUSTER\_GROUP\_QUEUED**
</dt> <dd> <dl> <dt>

5959 (0x1747)
</dt> <dt>



The requested operation can not be completed because the group is queued for an operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_LOCKED_STATUS"></span><span id="error_cluster_resource_locked_status"></span>**ERROR\_CLUSTER\_RESOURCE\_LOCKED\_STATUS**
</dt> <dd> <dl> <dt>

5960 (0x1748)
</dt> <dt>



The requested operation can not be completed because a resource has locked status.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SHARED_VOLUME_FAILOVER_NOT_ALLOWED"></span><span id="error_cluster_shared_volume_failover_not_allowed"></span>**ERROR\_CLUSTER\_SHARED\_VOLUME\_FAILOVER\_NOT\_ALLOWED**
</dt> <dd> <dl> <dt>

5961 (0x1749)
</dt> <dt>



The resource cannot move to another node because a cluster shared volume vetoed the operation.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_NODE_DRAIN_IN_PROGRESS"></span><span id="error_cluster_node_drain_in_progress"></span>**ERROR\_CLUSTER\_NODE\_DRAIN\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

5962 (0x174A)
</dt> <dt>



A node drain is already in progress.

This value was also named **ERROR\_CLUSTER\_NODE\_EVACUATION\_IN\_PROGRESS**


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_DISK_NOT_CONNECTED"></span><span id="error_cluster_disk_not_connected"></span>**ERROR\_CLUSTER\_DISK\_NOT\_CONNECTED**
</dt> <dd> <dl> <dt>

5963 (0x174B)
</dt> <dt>



Clustered storage is not connected to the node.


</dt> </dl> </dd> <dt>

<span id="ERROR_DISK_NOT_CSV_CAPABLE"></span><span id="error_disk_not_csv_capable"></span>**ERROR\_DISK\_NOT\_CSV\_CAPABLE**
</dt> <dd> <dl> <dt>

5964 (0x174C)
</dt> <dt>



The disk is not configured in a way to be used with CSV. CSV disks must have at least one partition that is formatted with NTFS.


</dt> </dl> </dd> <dt>

<span id="ERROR_RESOURCE_NOT_IN_AVAILABLE_STORAGE"></span><span id="error_resource_not_in_available_storage"></span>**ERROR\_RESOURCE\_NOT\_IN\_AVAILABLE\_STORAGE**
</dt> <dd> <dl> <dt>

5965 (0x174D)
</dt> <dt>



The resource must be part of the Available Storage group to complete this action.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SHARED_VOLUME_REDIRECTED"></span><span id="error_cluster_shared_volume_redirected"></span>**ERROR\_CLUSTER\_SHARED\_VOLUME\_REDIRECTED**
</dt> <dd> <dl> <dt>

5966 (0x174E)
</dt> <dt>



CSVFS failed operation as volume is in redirected mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_SHARED_VOLUME_NOT_REDIRECTED"></span><span id="error_cluster_shared_volume_not_redirected"></span>**ERROR\_CLUSTER\_SHARED\_VOLUME\_NOT\_REDIRECTED**
</dt> <dd> <dl> <dt>

5967 (0x174F)
</dt> <dt>



CSVFS failed operation as volume is not in redirected mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_CANNOT_RETURN_PROPERTIES"></span><span id="error_cluster_cannot_return_properties"></span>**ERROR\_CLUSTER\_CANNOT\_RETURN\_PROPERTIES**
</dt> <dd> <dl> <dt>

5968 (0x1750)
</dt> <dt>



Cluster properties cannot be returned at this time.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_CONTAINS_UNSUPPORTED_DIFF_AREA_FOR_SHARED_VOLUMES"></span><span id="error_cluster_resource_contains_unsupported_diff_area_for_shared_volumes"></span>**ERROR\_CLUSTER\_RESOURCE\_CONTAINS\_UNSUPPORTED\_DIFF\_AREA\_FOR\_SHARED\_VOLUMES**
</dt> <dd> <dl> <dt>

5969 (0x1751)
</dt> <dt>



The clustered disk resource contains software snapshot diff area that are not supported for Cluster Shared Volumes.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_IS_IN_MAINTENANCE_MODE"></span><span id="error_cluster_resource_is_in_maintenance_mode"></span>**ERROR\_CLUSTER\_RESOURCE\_IS\_IN\_MAINTENANCE\_MODE**
</dt> <dd> <dl> <dt>

5970 (0x1752)
</dt> <dt>



The operation cannot be completed because the resource is in maintenance mode.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_AFFINITY_CONFLICT"></span><span id="error_cluster_affinity_conflict"></span>**ERROR\_CLUSTER\_AFFINITY\_CONFLICT**
</dt> <dd> <dl> <dt>

5971 (0x1753)
</dt> <dt>



The operation cannot be completed because of cluster affinity conflicts.


</dt> </dl> </dd> <dt>

<span id="ERROR_CLUSTER_RESOURCE_IS_REPLICA_VIRTUAL_MACHINE"></span><span id="error_cluster_resource_is_replica_virtual_machine"></span>**ERROR\_CLUSTER\_RESOURCE\_IS\_REPLICA\_VIRTUAL\_MACHINE**
</dt> <dd> <dl> <dt>

5972 (0x1754)
</dt> <dt>



The operation cannot be completed because the resource is a replica virtual machine.


</dt> </dl> </dd> </dl>


## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>WinError.h</dt> </dl> |



## See also

<dl> <dt>

[System Error Codes](system-error-codes.md)
</dt> </dl>

 

 




