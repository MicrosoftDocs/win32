---
title: MDM registration error values (MDMRegistration.h)
description: The following error values are with MDM registration.
ms.assetid: 1f42ed5e-e221-47ec-a019-ed06c05d55d0
topic_type:
- apiref
api_name:
- E_DATATYPE_MISMATCH
- MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR
- MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR
- MREGISTER_E_DEVICE_AUTHENTICATION_ERROR
- MENROLL_E_DEVICE_AUTHENTICATION_ERROR
- MREGISTER_E_DEVICE_AUTHORIZATION_ERROR
- MENROLL_E_DEVICE_AUTHORIZATION_ERROR
- MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR
- MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR
- MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR
- MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR
- MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR
- MENROLL_E_DEVICE_INTERNALSERVICE_ERROR
- MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR
- MENROLL_E_DEVICE_INVALIDSECURITY_ERROR
- MREGISTER_E_DEVICE_UNKNOWN_ERROR
- MENROLL_E_DEVICE_UNKNOWN_ERROR
- MREGISTER_E_REGISTRATION_IN_PROGRESS
- MENROLL_E_ENROLLMENT_IN_PROGRESS
- MREGISTER_E_DEVICE_ALREADY_REGISTERED
- MENROLL_E_DEVICE_ALREADY_ENROLLED
- MREGISTER_E_DEVICE_NOT_REGISTERED
- MENROLL_E_DEVICE_NOT_ENROLLED
- MREGISTER_E_DISCOVERY_REDIRECTED
- MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR
- MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID
- MREGISTER_E_DISCOVERY_FAILED
- MENROLL_E_PASSWORD_NEEDED
- MENROLL_E_WAB_ERROR
- MENROLL_E_CONNECTIVITY
- MENROLL_S_ENROLLMENT_SUSPENDED
- MENROLL_E_INVALIDSSLCERT
- MENROLL_E_DEVICECAPREACHED
- MENROLL_E_DEVICENOTSUPPORTED
- MENROLL_E_NOTSUPPORTED
- MREGISTER_E_NOTELIGIBLETORENEW
- MENROLL_E_INMAINTENANCE
- MENROLL_E_USERLICENSE
- MENROLL_E_ENROLLMENTDATAINVALID
- MENROLL_E_INSECUREREDIRECT
- MENROLL_E_PLATFORM_WRONG_STATE
- MENROLL_E_PLATFORM_LICENSE_ERROR
- MENROLL_E_PLATFORM_UNKNOWN_ERROR
- MENROLL_E_PROV_CSP_CERTSTORE
- MENROLL_E_PROV_CSP_W7
- MENROLL_E_PROV_CSP_DMCLIENT
- MENROLL_E_PROV_CSP_PFW
- MENROLL_E_PROV_CSP_MISC
- MENROLL_E_PROV_UNKNOWN
- MENROLL_E_PROV_SSLCERTNOTFOUND
- MENROLL_E_PROV_CSP_APPMGMT
- MENROLL_E_DEVICE_MANAGEMENT_BLOCKED
- MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED
- MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT
- MENROLL_E_EMPTY_MESSAGE
- MENROLL_E_USER_CANCELED
- MENROLL_E_MDM_NOT_CONFIGURED
api_location:
- MDMRegistration.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MDM registration error values

The following error values are with MDM registration.

<dl> <dt>

<span id="E_DATATYPE_MISMATCH"></span><span id="e_datatype_mismatch"></span>**E\_DATATYPE\_MISMATCH**
</dt> <dd> <dl> <dt>

0x8007065d
</dt> <dt>



The datatype does not match the expected datatype.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_MESSAGE_FORMAT_ERROR"></span><span id="mregister_e_device_message_format_error"></span>**MREGISTER\_E\_DEVICE\_MESSAGE\_FORMAT\_ERROR**
</dt> <dd> <dl> <dt>

0x80190001
</dt> <dt>



Invalid Schema, Message Format Error from server.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_MESSAGE_FORMAT_ERROR"></span><span id="menroll_e_device_message_format_error"></span>**MENROLL\_E\_DEVICE\_MESSAGE\_FORMAT\_ERROR**
</dt> <dd> <dl> <dt>

0x80180001
</dt> <dt>



Invalid Schema , Message Format Error from server.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_AUTHENTICATION_ERROR"></span><span id="mregister_e_device_authentication_error"></span>**MREGISTER\_E\_DEVICE\_AUTHENTICATION\_ERROR**
</dt> <dd> <dl> <dt>

0x80190002
</dt> <dt>



Server failed to authenticate the user.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_AUTHENTICATION_ERROR"></span><span id="menroll_e_device_authentication_error"></span>**MENROLL\_E\_DEVICE\_AUTHENTICATION\_ERROR**
</dt> <dd> <dl> <dt>

0x80180002
</dt> <dt>



Server failed to authenticate the user.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_AUTHORIZATION_ERROR"></span><span id="mregister_e_device_authorization_error"></span>**MREGISTER\_E\_DEVICE\_AUTHORIZATION\_ERROR**
</dt> <dd> <dl> <dt>

0x80190003
</dt> <dt>



The user is not authorized to enroll.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_AUTHORIZATION_ERROR"></span><span id="menroll_e_device_authorization_error"></span>**MENROLL\_E\_DEVICE\_AUTHORIZATION\_ERROR**
</dt> <dd> <dl> <dt>

0x80180003
</dt> <dt>



The user is not authorized to enroll.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_CERTIFCATEREQUEST_ERROR"></span><span id="mregister_e_device_certifcaterequest_error"></span>**MREGISTER\_E\_DEVICE\_CERTIFCATEREQUEST\_ERROR**
</dt> <dd> <dl> <dt>

0x80190004
</dt> <dt>



The user has no permission for the certificate template or the certificate authority is unreachable.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_CERTIFCATEREQUEST_ERROR"></span><span id="menroll_e_device_certifcaterequest_error"></span>**MENROLL\_E\_DEVICE\_CERTIFCATEREQUEST\_ERROR**
</dt> <dd> <dl> <dt>

0x80180004
</dt> <dt>



The user has no permission for the certificate template or the certificate authority is unreachable.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_CONFIGMGRSERVER_ERROR"></span><span id="mregister_e_device_configmgrserver_error"></span>**MREGISTER\_E\_DEVICE\_CONFIGMGRSERVER\_ERROR**
</dt> <dd> <dl> <dt>

0x80190005
</dt> <dt>



There was a failure at the management server, such as a database access error.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_CONFIGMGRSERVER_ERROR"></span><span id="menroll_e_device_configmgrserver_error"></span>**MENROLL\_E\_DEVICE\_CONFIGMGRSERVER\_ERROR**
</dt> <dd> <dl> <dt>

0x80180005
</dt> <dt>



There was a failure at the management server, such as a database access error.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_INTERNALSERVICE_ERROR"></span><span id="mregister_e_device_internalservice_error"></span>**MREGISTER\_E\_DEVICE\_INTERNALSERVICE\_ERROR**
</dt> <dd> <dl> <dt>

0x80190006
</dt> <dt>



There was an unhandled exception on the server.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_INTERNALSERVICE_ERROR"></span><span id="menroll_e_device_internalservice_error"></span>**MENROLL\_E\_DEVICE\_INTERNALSERVICE\_ERROR**
</dt> <dd> <dl> <dt>

0x80180006
</dt> <dt>



There was an unhandled exception on the server.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_INVALIDSECURITY_ERROR"></span><span id="mregister_e_device_invalidsecurity_error"></span>**MREGISTER\_E\_DEVICE\_INVALIDSECURITY\_ERROR**
</dt> <dd> <dl> <dt>

0x80190007
</dt> <dt>



There was an unhandled exception on the server.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_INVALIDSECURITY_ERROR"></span><span id="menroll_e_device_invalidsecurity_error"></span>**MENROLL\_E\_DEVICE\_INVALIDSECURITY\_ERROR**
</dt> <dd> <dl> <dt>

0x80180007
</dt> <dt>



There was an unhandled exception on the server.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_UNKNOWN_ERROR"></span><span id="mregister_e_device_unknown_error"></span>**MREGISTER\_E\_DEVICE\_UNKNOWN\_ERROR**
</dt> <dd> <dl> <dt>

0x80190008
</dt> <dt>



Unknown server error.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_UNKNOWN_ERROR"></span><span id="menroll_e_device_unknown_error"></span>**MENROLL\_E\_DEVICE\_UNKNOWN\_ERROR**
</dt> <dd> <dl> <dt>

0x80180008
</dt> <dt>



Unknown server error.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_REGISTRATION_IN_PROGRESS"></span><span id="mregister_e_registration_in_progress"></span>**MREGISTER\_E\_REGISTRATION\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

0x80190009
</dt> <dt>



Another enrollment operation is currently underway.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_ENROLLMENT_IN_PROGRESS"></span><span id="menroll_e_enrollment_in_progress"></span>**MENROLL\_E\_ENROLLMENT\_IN\_PROGRESS**
</dt> <dd> <dl> <dt>

0x80180009
</dt> <dt>



Another enrollment operation is currently underway.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_ALREADY_REGISTERED"></span><span id="mregister_e_device_already_registered"></span>**MREGISTER\_E\_DEVICE\_ALREADY\_REGISTERED**
</dt> <dd> <dl> <dt>

0x8019000A
</dt> <dt>



No longer used.

**Windows 8.1:** The device is already enrolled.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_ALREADY_ENROLLED"></span><span id="menroll_e_device_already_enrolled"></span>**MENROLL\_E\_DEVICE\_ALREADY\_ENROLLED**
</dt> <dd> <dl> <dt>

0x8018000A
</dt> <dt>



The device is already enrolled.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_NOT_REGISTERED"></span><span id="mregister_e_device_not_registered"></span>**MREGISTER\_E\_DEVICE\_NOT\_REGISTERED**
</dt> <dd> <dl> <dt>

0x8019000B
</dt> <dt>



No longer used.

**Windows 8.1:** The device is not enrolled.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_NOT_ENROLLED"></span><span id="menroll_e_device_not_enrolled"></span>**MENROLL\_E\_DEVICE\_NOT\_ENROLLED**
</dt> <dd> <dl> <dt>

0x8018000B
</dt> <dt>



The device is not enrolled.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DISCOVERY_REDIRECTED"></span><span id="mregister_e_discovery_redirected"></span>**MREGISTER\_E\_DISCOVERY\_REDIRECTED**
</dt> <dd> <dl> <dt>

0x8019000C
</dt> <dt>



No longer used.

**Windows 8.1:** Redirection is needed.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DEVICE_NOT_AD_REGISTERED_ERROR"></span><span id="mregister_e_device_not_ad_registered_error"></span>**MREGISTER\_E\_DEVICE\_NOT\_AD\_REGISTERED\_ERROR**
</dt> <dd> <dl> <dt>

0x8019000D
</dt> <dt>



No longer used.

**Windows 8.1:** The device is not registered with Active Directory.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DISCOVERY_SEC_CERT_DATE_INVALID"></span><span id="menroll_e_discovery_sec_cert_date_invalid"></span>**MENROLL\_E\_DISCOVERY\_SEC\_CERT\_DATE\_INVALID**
</dt> <dd> <dl> <dt>

0x8018000D
</dt> <dt>



During discovery the sec cert date was invalid.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_DISCOVERY_FAILED"></span><span id="mregister_e_discovery_failed"></span>**MREGISTER\_E\_DISCOVERY\_FAILED**
</dt> <dd> <dl> <dt>

0x8019000E
</dt> <dt>



No longer used.

**Windows 8.1:** Discovery failed; redirection is needed.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PASSWORD_NEEDED"></span><span id="menroll_e_password_needed"></span>**MENROLL\_E\_PASSWORD\_NEEDED**
</dt> <dd> <dl> <dt>

0x8018000E
</dt> <dt>



A password is needed, but was not supplied.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_WAB_ERROR"></span><span id="menroll_e_wab_error"></span>**MENROLL\_E\_WAB\_ERROR**
</dt> <dd> <dl> <dt>

0x8018000F
</dt> <dt>



An error occurred during WAB enrollment.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_CONNECTIVITY"></span><span id="menroll_e_connectivity"></span>**MENROLL\_E\_CONNECTIVITY**
</dt> <dd> <dl> <dt>

0x80180010
</dt> <dt>



A network error occurred, such as DNS or a network timeout.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_S_ENROLLMENT_SUSPENDED"></span><span id="menroll_s_enrollment_suspended"></span>**MENROLL\_S\_ENROLLMENT\_SUSPENDED**
</dt> <dd> <dl> <dt>

0x00180011
</dt> <dt>



Enrollment was suspended. No longer supported.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_INVALIDSSLCERT"></span><span id="menroll_e_invalidsslcert"></span>**MENROLL\_E\_INVALIDSSLCERT**
</dt> <dd> <dl> <dt>

0x80180012
</dt> <dt>



The SSL cert was not valid.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICECAPREACHED"></span><span id="menroll_e_devicecapreached"></span>**MENROLL\_E\_DEVICECAPREACHED**
</dt> <dd> <dl> <dt>

0x80180013
</dt> <dt>



The user has already enrolled too many devices. Delete or unenroll old ones to fix this error. Note that the user can resolve this error without admin assistance.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICENOTSUPPORTED"></span><span id="menroll_e_devicenotsupported"></span>**MENROLL\_E\_DEVICENOTSUPPORTED**
</dt> <dd> <dl> <dt>

0x80180014
</dt> <dt>



A specific platform (e.g. Windows) or version is not supported. The general fix for this error is to upgrade the device.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_NOTSUPPORTED"></span><span id="menroll_e_notsupported"></span>**MENROLL\_E\_NOTSUPPORTED**
</dt> <dd> <dl> <dt>

0x80180015
</dt> <dt>



Mobile device management is generally not supported for this device - the user may call the admin, but will be unlikely to resolve this issue.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MREGISTER_E_NOTELIGIBLETORENEW"></span><span id="mregister_e_noteligibletorenew"></span>**MREGISTER\_E\_NOTELIGIBLETORENEW**
</dt> <dd> <dl> <dt>

0x80180016
</dt> <dt>



The device is attempting to renew, but the server rejected the request. Check time on device. The user may be able to resolve this error by re-enrolling.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_INMAINTENANCE"></span><span id="menroll_e_inmaintenance"></span>**MENROLL\_E\_INMAINTENANCE**
</dt> <dd> <dl> <dt>

0x80180017
</dt> <dt>



Account is in maintenance; retry later. The user can retry later. However, the user may choose to call the admin to determine the maintenance schedule.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_USERLICENSE"></span><span id="menroll_e_userlicense"></span>**MENROLL\_E\_USERLICENSE**
</dt> <dd> <dl> <dt>

0x80180018
</dt> <dt>



The license of user is in bad state blocking enrollment; the user will need to call the admin.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_ENROLLMENTDATAINVALID"></span><span id="menroll_e_enrollmentdatainvalid"></span>**MENROLL\_E\_ENROLLMENTDATAINVALID**
</dt> <dd> <dl> <dt>

0x80180019
</dt> <dt>



The server rejected the Enrollment Data; the server may not be configured correctly.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_INSECUREREDIRECT"></span><span id="menroll_e_insecureredirect"></span>**MENROLL\_E\_INSECUREREDIRECT**
</dt> <dd> <dl> <dt>

0x8018001A
</dt> <dt>



The server requested HTTP rather than HTTPS but it was not accepted.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PLATFORM_WRONG_STATE"></span><span id="menroll_e_platform_wrong_state"></span>**MENROLL\_E\_PLATFORM\_WRONG\_STATE**
</dt> <dd> <dl> <dt>

0x8018001B
</dt> <dt>



An invalid operation was attempted, such trying to enroll the same device twice or unenroll an unknown device.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PLATFORM_LICENSE_ERROR"></span><span id="menroll_e_platform_license_error"></span>**MENROLL\_E\_PLATFORM\_LICENSE\_ERROR**
</dt> <dd> <dl> <dt>

0x8018001C
</dt> <dt>



The version of Windows installed on the client does not support this enrollment type.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PLATFORM_UNKNOWN_ERROR"></span><span id="menroll_e_platform_unknown_error"></span>**MENROLL\_E\_PLATFORM\_UNKNOWN\_ERROR**
</dt> <dd> <dl> <dt>

0x8018001D
</dt> <dt>



An unknown error occurred on the client.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_CERTSTORE"></span><span id="menroll_e_prov_csp_certstore"></span>**MENROLL\_E\_PROV\_CSP\_CERTSTORE**
</dt> <dd> <dl> <dt>

0x8018001E
</dt> <dt>



Provisioning failed in the certificate store CSP.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_W7"></span><span id="menroll_e_prov_csp_w7"></span>**MENROLL\_E\_PROV\_CSP\_W7**
</dt> <dd> <dl> <dt>

0x8018001F
</dt> <dt>



Provisioning failed in a W7/DMAcc CPP.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_DMCLIENT"></span><span id="menroll_e_prov_csp_dmclient"></span>**MENROLL\_E\_PROV\_CSP\_DMCLIENT**
</dt> <dd> <dl> <dt>

0x80180020
</dt> <dt>



Provisioning failed in a DM client CSP.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_PFW"></span><span id="menroll_e_prov_csp_pfw"></span>**MENROLL\_E\_PROV\_CSP\_PFW**
</dt> <dd> <dl> <dt>

0x80180021
</dt> <dt>



Provisioning failed in a Passport for Work CSP.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_MISC"></span><span id="menroll_e_prov_csp_misc"></span>**MENROLL\_E\_PROV\_CSP\_MISC**
</dt> <dd> <dl> <dt>

0x80180022
</dt> <dt>



Provisioning failed in a CSP not listed above.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_UNKNOWN"></span><span id="menroll_e_prov_unknown"></span>**MENROLL\_E\_PROV\_UNKNOWN**
</dt> <dd> <dl> <dt>

0x80180023
</dt> <dt>



Provisioning failed, but a specific CSP is not indicated.

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_SSLCERTNOTFOUND"></span><span id="menroll_e_prov_sslcertnotfound"></span>**MENROLL\_E\_PROV\_SSLCERTNOTFOUND**
</dt> <dd> <dl> <dt>

0x80180024
</dt> <dt>



When attempting to bind the public cert/private key, the public cert was not found either: when attempting to bind the public cert/private key, or when looking into provisioning payload (perhaps targeting the wrong store).

**Windows 8.1:** This constant is not available before Windows 10.


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_PROV_CSP_APPMGMT"></span><span id="menroll_e_prov_csp_appmgmt"></span>**MENROLL\_E\_PROV\_CSP\_APPMGMT**
</dt> <dd> <dl> <dt>

0x80180025
</dt> <dt>



Provisioning failed in the EnterpriseAppManagement CSP.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_DEVICE_MANAGEMENT_BLOCKED"></span><span id="menroll_e_device_management_blocked"></span>**MENROLL\_E\_DEVICE\_MANAGEMENT\_BLOCKED**
</dt> <dd> <dl> <dt>

0x80180026
</dt> <dt>



Mobile Device Management (MDM) was blocked, possibly by Group Policy or the [**SetManagedExternally**](/windows/desktop/api/MDMRegistration/nf-mdmregistration-setmanagedexternally) function.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_CERTPOLICY_PRIVATEKEYCREATION_FAILED"></span><span id="menroll_e_certpolicy_privatekeycreation_failed"></span>**MENROLL\_E\_CERTPOLICY\_PRIVATEKEYCREATION\_FAILED**
</dt> <dd> <dl> <dt>

0x80180027
</dt> <dt>



Failed to create the private key.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_CERTAUTH_FAILED_TO_FIND_CERT"></span><span id="menroll_e_certauth_failed_to_find_cert"></span>**MENROLL\_E\_CERTAUTH\_FAILED\_TO\_FIND\_CERT**
</dt> <dd> <dl> <dt>

0x80180028
</dt> <dt>



Certificate Authentication was requested, but failed find a certificate to use.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_EMPTY_MESSAGE"></span><span id="menroll_e_empty_message"></span>**MENROLL\_E\_EMPTY\_MESSAGE**
</dt> <dd> <dl> <dt>

0x80180029
</dt> <dt>



The server responded with HTTP 200, but the message was empty.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_USER_CANCELED_"></span><span id="menroll_e_user_canceled_"></span>**MENROLL\_E\_USER\_CANCELED** 
</dt> <dd> <dl> <dt>

0x80180030
</dt> <dt>



The user canceled the operation.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> <dt>

<span id="MENROLL_E_MDM_NOT_CONFIGURED"></span><span id="menroll_e_mdm_not_configured"></span>**MENROLL\_E\_MDM\_NOT\_CONFIGURED**
</dt> <dd> <dl> <dt>

0x80180031
</dt> <dt>



Mobile Device Management (MDM) is not configured.

> [!Note]  
> This constant is not available before Windows 10, version 1709.

 


</dt> </dl> </dd> </dl>

## Requirements

| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                       |
| Minimum supported server<br/> | None supported<br/>                                                                    |
| Header<br/>                   | <dl> <dt>MDMRegistration.h</dt> </dl> |



 

 





