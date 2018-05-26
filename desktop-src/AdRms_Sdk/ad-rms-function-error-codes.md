---
Description: Active Directory Rights Management Services (AD RMS) functions have the following status and error codes and corresponding hexadecimal values. These codes are defined in the MsdrmError.h header file that is included with this SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: af515274-9030-4b1a-8a9d-a42b0d0a7660
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: AD RMS Function Error Codes
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AD RMS Function Error Codes

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

Active Directory Rights Management Services (AD RMS) functions have the following status and error codes and corresponding hexadecimal values. These codes are defined in the MsdrmError.h header file that is included with this SDK.

<dl> <span id="E_DRM_INSUFFICIENT_BUFFER"></span><span id="e_drm_insufficient_buffer"></span>**E\_DRM\_INSUFFICIENT\_BUFFER** (ERROR\_INSUFFICIENT\_BUFFER)  
<span id="S_DRM_REQUEST_PREPARED"></span><span id="s_drm_request_prepared"></span>**S\_DRM\_REQUEST\_PREPARED** (0x0004CF00)  
<span id="S_DRM_ALREADY_ACTIVATED"></span><span id="s_drm_already_activated"></span>**S\_DRM\_ALREADY\_ACTIVATED** (0x0004CF01)  
<span id="S_DRM_CONNECTING"></span><span id="s_drm_connecting"></span>**S\_DRM\_CONNECTING** (0x0004CF02)  
<span id="S_DRM_CONNECTED"></span><span id="s_drm_connected"></span>**S\_DRM\_CONNECTED** (0x0004CF03)  
<span id="S_DRM_COMPLETED"></span><span id="s_drm_completed"></span>**S\_DRM\_COMPLETED** (0x0004CF04)  
<span id="S_DRM_INPROGRESS"></span><span id="s_drm_inprogress"></span>**S\_DRM\_INPROGRESS** (0x0004CF05)  
<span id="E_DRM_MANIFEST_POLICY_VIOLATION"></span><span id="e_drm_manifest_policy_violation"></span>**E\_DRM\_MANIFEST\_POLICY\_VIOLATION** (0x8004930C)  
<span id="E_DRM_INVALID_LICENSE"></span><span id="e_drm_invalid_license"></span>**E\_DRM\_INVALID\_LICENSE** (0x8004CF00)  
<span id="E_DRM_INFO_NOT_IN_LICENSE"></span><span id="e_drm_info_not_in_license"></span>**E\_DRM\_INFO\_NOT\_IN\_LICENSE** (0x8004CF01)  
<span id="E_DRM_INVALID_LICENSE_SIGNATURE"></span><span id="e_drm_invalid_license_signature"></span>**E\_DRM\_INVALID\_LICENSE\_SIGNATURE** (0x8004CF02)  
<span id="E_DRM_ENCRYPTION_NOT_PERMITTED"></span><span id="e_drm_encryption_not_permitted"></span>**E\_DRM\_ENCRYPTION\_NOT\_PERMITTED** (0x8004CF04)  
<span id="E_DRM_RIGHT_NOT_GRANTED"></span><span id="e_drm_right_not_granted"></span>**E\_DRM\_RIGHT\_NOT\_GRANTED** (0x8004CF05)  
<span id="E_DRM_INVALID_VERSION"></span><span id="e_drm_invalid_version"></span>**E\_DRM\_INVALID\_VERSION** (0x8004CF06)  
<span id="E_DRM_INVALID_ENCODING_TYPE"></span><span id="e_drm_invalid_encoding_type"></span>**E\_DRM\_INVALID\_ENCODING\_TYPE** (0x8004CF07)  
<span id="E_DRM_INVALID_NUMERICAL_VALUE"></span><span id="e_drm_invalid_numerical_value"></span>**E\_DRM\_INVALID\_NUMERICAL\_VALUE** (0x8004CF08)  
<span id="E_DRM_INVALID_ALGORITHM_TYPE"></span><span id="e_drm_invalid_algorithm_type"></span>**E\_DRM\_INVALID\_ALGORITHM\_TYPE** (0x8004CF09)  
<span id="E_DRM_ENV_NOT_LOADED"></span><span id="e_drm_env_not_loaded"></span>**E\_DRM\_ENV\_NOT\_LOADED** (0x8004CF0A)  
<span id="E_DRM_ENV_CANNOT_LOAD"></span><span id="e_drm_env_cannot_load"></span>**E\_DRM\_ENV\_CANNOT\_LOAD** (0x8004CF0B)  
<span id="E_DRM_TOO_MANY_LOADED_ENVIRONMENTS"></span><span id="e_drm_too_many_loaded_environments"></span>**E\_DRM\_TOO\_MANY\_LOADED\_ENVIRONMENTS** (0x8004CF0C)  
<span id="E_DRM_INCOMPATIBLE_OBJECTS"></span><span id="e_drm_incompatible_objects"></span>**E\_DRM\_INCOMPATIBLE\_OBJECTS** (0x8004CF0E)  
<span id="E_DRM_LIB_FAIL"></span><span id="e_drm_lib_fail"></span>**E\_DRM\_LIB\_FAIL** (0x8004CF0F)  
<span id="E_DRM_ENABLING_PRINCIPAL_FAILURE"></span><span id="e_drm_enabling_principal_failure"></span>**E\_DRM\_ENABLING\_PRINCIPAL\_FAILURE** (0x8004CF10)  
<span id="E_DRM_INFO_NOT_PRESENT"></span><span id="e_drm_info_not_present"></span>**E\_DRM\_INFO\_NOT\_PRESENT** (0x8004CF11)  
<span id="E_DRM_BAD_GET_INFO_QUERY"></span><span id="e_drm_bad_get_info_query"></span>**E\_DRM\_BAD\_GET\_INFO\_QUERY** (0x8004CF12)  
<span id="E_DRM_KEY_TYPE_UNSUPPORTED"></span><span id="e_drm_key_type_unsupported"></span>**E\_DRM\_KEY\_TYPE\_UNSUPPORTED** (0x8004CF13)  
<span id="E_DRM_CRYPTO_OPERATION_UNSUPPORTED"></span><span id="e_drm_crypto_operation_unsupported"></span>**E\_DRM\_CRYPTO\_OPERATION\_UNSUPPORTED** (0x8004CF14)  
<span id="E_DRM_CLOCK_ROLL_BACK_DETECTED"></span><span id="e_drm_clock_roll_back_detected"></span>**E\_DRM\_CLOCK\_ROLL\_BACK\_DETECTED** (0x8004CF15)  
<span id="E_DRM_QUERY_REPORTS_NO_RESULTS"></span><span id="e_drm_query_reports_no_results"></span>**E\_DRM\_QUERY\_REPORTS\_NO\_RESULTS** (0x8004CF16)  
<span id="E_DRM_UNEXPECTED_EXCEPTION"></span><span id="e_drm_unexpected_exception"></span>**E\_DRM\_UNEXPECTED\_EXCEPTION** (0x8004CF17)  
<span id="E_DRM_BIND_VALIDITY_TIME_VIOLATED"></span><span id="e_drm_bind_validity_time_violated"></span>**E\_DRM\_BIND\_VALIDITY\_TIME\_VIOLATED** (0x8004CF18)  
<span id="E_DRM_BROKEN_CERT_CHAIN"></span><span id="e_drm_broken_cert_chain"></span>**E\_DRM\_BROKEN\_CERT\_CHAIN** (0x8004CF19)  
<span id="E_DRM_BIND_POLICY_VIOLATION"></span><span id="e_drm_bind_policy_violation"></span>**E\_DRM\_BIND\_POLICY\_VIOLATION** (0x8004CF1B)  
<span id="E_DRM_BIND_REVOKED_LICENSE"></span><span id="e_drm_bind_revoked_license"></span>**E\_DRM\_BIND\_REVOKED\_LICENSE** (0x8004CF1C)  
<span id="E_DRM_BIND_REVOKED_ISSUER"></span><span id="e_drm_bind_revoked_issuer"></span>**E\_DRM\_BIND\_REVOKED\_ISSUER** (0x8004CF1D)  
<span id="E_DRM_BIND_REVOKED_PRINCIPAL"></span><span id="e_drm_bind_revoked_principal"></span>**E\_DRM\_BIND\_REVOKED\_PRINCIPAL** (0x8004CF1E)  
<span id="E_DRM_BIND_REVOKED_RESOURCE"></span><span id="e_drm_bind_revoked_resource"></span>**E\_DRM\_BIND\_REVOKED\_RESOURCE** (0x8004CF1F)  
<span id="E_DRM_BIND_REVOKED_MODULE"></span><span id="e_drm_bind_revoked_module"></span>**E\_DRM\_BIND\_REVOKED\_MODULE** (0x8004CF20)  
<span id="E_DRM_BIND_CONTENT_NOT_IN_EUL"></span><span id="e_drm_bind_content_not_in_eul"></span>**E\_DRM\_BIND\_CONTENT\_NOT\_IN\_EUL** (0x8004CF21)  
<span id="E_DRM_BIND_ACCESS_PRINCIPAL_NOT_ENABLING"></span><span id="e_drm_bind_access_principal_not_enabling"></span>**E\_DRM\_BIND\_ACCESS\_PRINCIPAL\_NOT\_ENABLING** (0x8004CF22)  
<span id="E_DRM_BIND_ACCESS_UNSATISFIED"></span><span id="e_drm_bind_access_unsatisfied"></span>**E\_DRM\_BIND\_ACCESS\_UNSATISFIED** (0x8004CF23)  
<span id="E_DRM_BIND_INDICATED_PRINCIPAL_MISSING"></span><span id="e_drm_bind_indicated_principal_missing"></span>**E\_DRM\_BIND\_INDICATED\_PRINCIPAL\_MISSING** (0x8004CF24)  
<span id="E_DRM_BIND_MACHINE_NOT_FOUND_IN_GROUP_IDENTITY"></span><span id="e_drm_bind_machine_not_found_in_group_identity"></span>**E\_DRM\_BIND\_MACHINE\_NOT\_FOUND\_IN\_GROUP\_IDENTITY** (0x8004CF25)  
<span id="E_DRM_LIB_UNSUPPORTED_PLUGIN"></span><span id="e_drm_lib_unsupported_plugin"></span>**E\_DRM\_LIB\_UNSUPPORTED\_PLUGIN** (0x8004CF26)  
<span id="E_DRM_BIND_REVOCATION_LIST_STALE"></span><span id="e_drm_bind_revocation_list_stale"></span>**E\_DRM\_BIND\_REVOCATION\_LIST\_STALE** (0x8004CF27)  
<span id="E_DRM_BIND_NO_APPLICABLE_REVOCATION_LIST"></span><span id="e_drm_bind_no_applicable_revocation_list"></span>**E\_DRM\_BIND\_NO\_APPLICABLE\_REVOCATION\_LIST** (0x8004CF28)  
<span id="E_DRM_INVALID_HANDLE"></span><span id="e_drm_invalid_handle"></span>**E\_DRM\_INVALID\_HANDLE** (0x8004CF2C)  
<span id="E_DRM_BIND_INTERVALTIME_VIOLATED"></span><span id="e_drm_bind_intervaltime_violated"></span>**E\_DRM\_BIND\_INTERVALTIME\_VIOLATED** (0x8004CF2F)  
<span id="E_DRM_BIND_NO_SATISFIED_RIGHTS_GROUP"></span><span id="e_drm_bind_no_satisfied_rights_group"></span>**E\_DRM\_BIND\_NO\_SATISFIED\_RIGHTS\_GROUP** (0x8004CF30)  
<span id="E_DRM_BIND_SPECIFIED_WORK_MISSING"></span><span id="e_drm_bind_specified_work_missing"></span>**E\_DRM\_BIND\_SPECIFIED\_WORK\_MISSING** (0x8004CF31)  
<span id="E_DRM_NO_MORE_DATA"></span><span id="e_drm_no_more_data"></span>**E\_DRM\_NO\_MORE\_DATA** (0x8004CF33)  
<span id="E_DRM_LICENSEACQUISITIONFAILED"></span><span id="e_drm_licenseacquisitionfailed"></span>**E\_DRM\_LICENSEACQUISITIONFAILED** (0x8004CF34)  
<span id="E_DRM_ID_MISMATCH"></span><span id="e_drm_id_mismatch"></span>**E\_DRM\_ID\_MISMATCH** (0x8004CF35)  
<span id="E_DRM_TOO_MANY_CERTS"></span><span id="e_drm_too_many_certs"></span>**E\_DRM\_TOO\_MANY\_CERTS** (0x8004CF36)  
<span id="E_DRM_NO_DPURL_FOUND"></span><span id="e_drm_no_dpurl_found"></span>**E\_DRM\_NO\_DPURL\_FOUND** (0x8004CF37)  
<span id="E_DRM_ALREADY_IN_PROGRESS"></span><span id="e_drm_already_in_progress"></span>**E\_DRM\_ALREADY\_IN\_PROGRESS** (0x8004CF38)  
<span id="E_DRM_GROUPID_NOT_SET"></span><span id="e_drm_groupid_not_set"></span>**E\_DRM\_GROUPID\_NOT\_SET** (0x8004CF39)  
<span id="E_DRM_RECORD_NOT_FOUND"></span><span id="e_drm_record_not_found"></span>**E\_DRM\_RECORD\_NOT\_FOUND** (0x8004CF3A)  
<span id="E_DRM_NO_CONNECT"></span><span id="e_drm_no_connect"></span>**E\_DRM\_NO\_CONNECT** (0x8004CF3B)  
<span id="E_DRM_NO_LICENSE"></span><span id="e_drm_no_license"></span>**E\_DRM\_NO\_LICENSE** (0x8004CF3C)  
<span id="E_DRM_NEEDS_MACHINE_ACTIVATION"></span><span id="e_drm_needs_machine_activation"></span>**E\_DRM\_NEEDS\_MACHINE\_ACTIVATION** (0x8004CF3D)  
<span id="E_DRM_NEEDS_GROUPIDENTITY_ACTIVATION"></span><span id="e_drm_needs_groupidentity_activation"></span>**E\_DRM\_NEEDS\_GROUPIDENTITY\_ACTIVATION** (0x8004CF3E)  
<span id="E_DRM_ACTIVATIONFAILED"></span><span id="e_drm_activationfailed"></span>**E\_DRM\_ACTIVATIONFAILED** (0x8004CF40)  
<span id="E_DRM_ABORTED"></span><span id="e_drm_aborted"></span>**E\_DRM\_ABORTED** (0x8004CF41)  
<span id="E_DRM_OUT_OF_QUOTA"></span><span id="e_drm_out_of_quota"></span>**E\_DRM\_OUT\_OF\_QUOTA** (0x8004CF42)  
<span id="E_DRM_AUTHENTICATION_FAILED"></span><span id="e_drm_authentication_failed"></span>**E\_DRM\_AUTHENTICATION\_FAILED** (0x8004CF43)  
<span id="E_DRM_SERVER_ERROR"></span><span id="e_drm_server_error"></span>**E\_DRM\_SERVER\_ERROR** (0x8004CF44)  
<span id="E_DRM_INSTALLATION_FAILED"></span><span id="e_drm_installation_failed"></span>**E\_DRM\_INSTALLATION\_FAILED** (0x8004CF45)  
<span id="E_DRM_HID_CORRUPTED"></span><span id="e_drm_hid_corrupted"></span>**E\_DRM\_HID\_CORRUPTED** (0x8004CF46)  
<span id="E_DRM_INVALID_SERVER_RESPONSE"></span><span id="e_drm_invalid_server_response"></span>**E\_DRM\_INVALID\_SERVER\_RESPONSE** (0x8004CF47)  
<span id="E_DRM_SERVICE_NOT_FOUND"></span><span id="e_drm_service_not_found"></span>**E\_DRM\_SERVICE\_NOT\_FOUND** (0x8004CF48)  
<span id="E_DRM_USE_DEFAULT"></span><span id="e_drm_use_default"></span>**E\_DRM\_USE\_DEFAULT** (0x8004CF49)  
<span id="E_DRM_SERVER_NOT_FOUND"></span><span id="e_drm_server_not_found"></span>**E\_DRM\_SERVER\_NOT\_FOUND** (0x8004CF4A)  
<span id="E_DRM_INVALID_EMAIL"></span><span id="e_drm_invalid_email"></span>**E\_DRM\_INVALID\_EMAIL** (0x8004CF4B)  
<span id="E_DRM_VALIDITYTIME_VIOLATION"></span><span id="e_drm_validitytime_violation"></span>**E\_DRM\_VALIDITYTIME\_VIOLATION** (0x8004CF4C)  
<span id="E_DRM_OUTDATED_MODULE"></span><span id="e_drm_outdated_module"></span>**E\_DRM\_OUTDATED\_MODULE** (0x8004CF4D)  
<span id="E_DRM_NOT_SET"></span><span id="e_drm_not_set"></span>**E\_DRM\_NOT\_SET** (0x8004CF4E)  
<span id="E_DRM_METADATA_NOT_SET"></span><span id="e_drm_metadata_not_set"></span>**E\_DRM\_METADATA\_NOT\_SET** (0x8004CF4F)  
<span id="E_DRM_INVALID_TIMEINFO"></span><span id="e_drm_invalid_timeinfo"></span>**E\_DRM\_INVALID\_TIMEINFO** (0x8004CF50)  
<span id="E_DRM_RIGHT_NOT_SET"></span><span id="e_drm_right_not_set"></span>**E\_DRM\_RIGHT\_NOT\_SET** (0x8004CF51)  
<span id="E_DRM_RIGHT_NOT_SET"></span><span id="e_drm_right_not_set"></span>**E\_DRM\_RIGHT\_NOT\_SET** (0x8004CF52)  
<span id="E_DRM_BIND_NTLM_FAIL"></span><span id="e_drm_bind_ntlm_fail"></span>**E\_DRM\_BIND\_NTLM\_FAIL** (0x8004CF53)  
<span id="E_DRM_INVALID_ISSUANCELICENSE_TEMPLATE"></span><span id="e_drm_invalid_issuancelicense_template"></span>**E\_DRM\_INVALID\_ISSUANCELICENSE\_TEMPLATE** (0x8004CF54)  
<span id="E_DRM_INVALID_KEY_LENGTH"></span><span id="e_drm_invalid_key_length"></span>**E\_DRM\_INVALID\_KEY\_LENGTH** (0x8004CF55)  
<span id="E_DRM_EXPIRED_OFFICIAL_ISSUANCELICENSE_TEMPLATE"></span><span id="e_drm_expired_official_issuancelicense_template"></span>**E\_DRM\_EXPIRED\_OFFICIAL\_ISSUANCELICENSE\_TEMPLATE** (0x8004CF57)  
<span id="E_DRM_INVALID_CLIENT_LICENSOR_CERTIFICATE"></span><span id="e_drm_invalid_client_licensor_certificate"></span>**E\_DRM\_INVALID\_CLIENT\_LICENSOR\_CERTIFICATE** (0x8004CF58)  
<span id="E_DRM_HID_INVALID"></span><span id="e_drm_hid_invalid"></span>**E\_DRM\_HID\_INVALID** (0x8004CF59)  
<span id="E_DRM_EMAIL_NOT_VERIFIED"></span><span id="e_drm_email_not_verified"></span>**E\_DRM\_EMAIL\_NOT\_VERIFIED** (0x8004CF5A)  
<span id="E_DRM_SERVICE_MOVED"></span><span id="e_drm_service_moved"></span>**E\_DRM\_SERVICE\_MOVED** (0x8004CF5B)  
<span id="E_DRM_SERVICE_GONE"></span><span id="e_drm_service_gone"></span>**E\_DRM\_SERVICE\_GONE** (0x8004CF5C)  
<span id="E_DRM_AD_ENTRY_NOT_FOUND"></span><span id="e_drm_ad_entry_not_found"></span>**E\_DRM\_AD\_ENTRY\_NOT\_FOUND** (0x8004CF5D)  
<span id="E_DRM_NOT_A_CHAIN"></span><span id="e_drm_not_a_chain"></span>**E\_DRM\_NOT\_A\_CHAIN** (0x8004CF5E)  
<span id="E_DRM_REQUEST_DENIED"></span><span id="e_drm_request_denied"></span>**E\_DRM\_REQUEST\_DENIED** (0x8004CF5F)  
<span id="E_DRM_DEBUGGER_DETECTED"></span><span id="e_drm_debugger_detected"></span>**E\_DRM\_DEBUGGER\_DETECTED** (0x8004CF60)  
<span id="E_DRM_INVALID_LOCKBOX_TYPE"></span><span id="e_drm_invalid_lockbox_type"></span>**E\_DRM\_INVALID\_LOCKBOX\_TYPE** (0x8004CF70)  
<span id="E_DRM_INVALID_LOCKBOX_PATH"></span><span id="e_drm_invalid_lockbox_path"></span>**E\_DRM\_INVALID\_LOCKBOX\_PATH** (0x8004CF71)  
<span id="E_DRM_INVALID_REGISTRY_PATH"></span><span id="e_drm_invalid_registry_path"></span>**E\_DRM\_INVALID\_REGISTRY\_PATH** (0x8004CF72)  
<span id="E_DRM_NO_AES_PROVIDER"></span><span id="e_drm_no_aes_provider"></span>**E\_DRM\_NO\_AES\_PROVIDER** (0x8004CF73)  
<span id="E_DRM_GLOBAL_OPTION_ALREADY_SET"></span><span id="e_drm_global_option_already_set"></span>**E\_DRM\_GLOBAL\_OPTION\_ALREADY\_SET** (0x8004CF74)  
<span id="E_DRM_OWNER_LICENSE_NOT_FOUND"></span><span id="e_drm_owner_license_not_found"></span>**E\_DRM\_OWNER\_LICENSE\_NOT\_FOUND** (0x8004CF75)  
<span id="E_DRM_INVALID_WINDOW"></span><span id="e_drm_invalid_window"></span>**E\_DRM\_INVALID\_WINDOW** (0x8004CF76)  
<span id="E_DRM_SAFEMODE_OS_DETECTED"></span><span id="e_drm_safemode_os_detected"></span>**E\_DRM\_SAFEMODE\_OS\_DETECTED** (0x8004CF778)  
<span id="E_DRM_PLATFORM_POLICY_VIOLATION"></span><span id="e_drm_platform_policy_violation"></span>**E\_DRM\_PLATFORM\_POLICY\_VIOLATION** (0x8004CF79)  
<span id="E_DRM_ISSUANCELICENSE_LENGTH_LIMIT_EXCEEDED"></span><span id="e_drm_issuancelicense_length_limit_exceeded"></span>**E\_DRM\_ISSUANCELICENSE\_LENGTH\_LIMIT\_EXCEEDED** (0x8004CF81)  
</dl>

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 or later<br/>                               |
| Header<br/>  | <dl> <dt>MsdrmError.h</dt> </dl> |



## See also

<dl> <dt>

[AD RMS Functions](ad-rms-functions.md)
</dt> </dl>

 

 




