---
title: Error codes
description: Error codes returned by the Rights Management Services SDK 2.1 system.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'A02E4F40-5231-46F3-9BFB-0B4DFCD7AE30'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
topic_type:
- apiref
api_name:
- IPCERROR_USER_RIGHTS_NOT_SET
- IPCERROR_AD_ENTRY_NOT_FOUND
- IPCERROR_APPLICATION_AUTH_ERROR_AUTHENTICODE
- IPCERROR_BROKEN_CERT_CHAIN
- IPCERROR_CLOCK_ROLL_BACK_DETECTED
- IPCERROR_CRYPTO_OPERATION_UNSUPPORTED
- IPCERROR_DEBUGGER_DETECTED
- IPCERROR_LOCALE_NOT_FOUND
- IPCERROR_ILS_ERROR
- IPCERROR_SERVER_RESPONSE_NOT_VALID
- IPCERROR_OS_VERSION_NOT_TRUSTED
- IPCERROR_ISSUANCELICENSE_LENGTH_LIMIT_EXCEEDED
- IPCERROR_NEEDS_ONLINE
- IPCERROR_NEEDS_UI
- IPCERROR_NOT_BLOCK_ALIGNED
- IPCERROR_PROPERTY_ALREADY_SET
- IPCERROR_RIGHT_NOT_GRANTED
- IPCERROR_SAFEMODE_OS_DETECTED
- IPCERROR_SERVER_ERROR
- IPCERROR_MACHINE_NOT_TRUSTED
- IPCERROR_NEEDS_KEY_PARAMETER
- IPCERROR_LICENSE_INTERVAL_TIME_NOT_SET
- IPCERROR_CONTENT_KEY_NOT_SET
- IPCERROR_SIA_NOT_INSTALLED
- IPCERROR_TEMPLATE_NOT_ENABLED_FOR_USER
- IPCERROR_FILE_SYSTEM_FILE
- IPCERROR_FILE_IS_NOT_ENCRYPTED
- IPCERROR_FILE_ENCRYPT_BLOCKED
- IPCERROR_FILE_UPDATELICENSE_BLOCKED
- IPCERROR_FILE_PDFPROTECTOR_FORMAT_NOT_SUPPORTED
api_location:
- Ipcerror.h
api_type:
- HeaderDef
---

# Error codes

Error codes returned by the Rights Management Services SDK 2.1 system.

> [!Note]  
> This topic is for software developers that create applications using the RMS SDK. If you're a user who is receiving error codes, refer to the [Microsoft Support](https://support.microsoft.com) website.

 

For error condition processing, always use a call to [**IpcGetErrorMessageText**](ipcgeterrormessagetext.md) right after an SDK API call fails, so you get complete information about the nature of the error.

<dl> <dt>

<span id="IPCERROR_USER_RIGHTS_NOT_SET"></span><span id="ipcerror_user_rights_not_set"></span>**IPCERROR\_USER\_RIGHTS\_NOT\_SET**
</dt> <dd> <dl> <dt>

0x80040200
</dt> <dt>



Usage rights on this content are not set correctly. Contact your application support for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_AD_ENTRY_NOT_FOUND"></span><span id="ipcerror_ad_entry_not_found"></span>**IPCERROR\_AD\_ENTRY\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80040201
</dt> <dt>



No email address exists for the specified user in the Active Directory. Contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_APPLICATION_AUTH_ERROR_AUTHENTICODE"></span><span id="ipcerror_application_auth_error_authenticode"></span>**IPCERROR\_APPLICATION\_AUTH\_ERROR\_AUTHENTICODE**
</dt> <dd> <dl> <dt>

0x80040202
</dt> <dt>



This application is not trusted to consume rights managed content. The Authenticode signature for the application is not valid. Contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_BROKEN_CERT_CHAIN"></span><span id="ipcerror_broken_cert_chain"></span>**IPCERROR\_BROKEN\_CERT\_CHAIN**
</dt> <dd> <dl> <dt>

0x80040204
</dt> <dt>



A required certificate chain was not trusted.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_CLOCK_ROLL_BACK_DETECTED"></span><span id="ipcerror_clock_roll_back_detected"></span>**IPCERROR\_CLOCK\_ROLL\_BACK\_DETECTED**
</dt> <dd> <dl> <dt>

0x80040205
</dt> <dt>



This application cannot provide rights management functionality because the system clock has been set to a time that occurs in the past. Make sure that your computer's system clock is set correctly and try again.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_CRYPTO_OPERATION_UNSUPPORTED"></span><span id="ipcerror_crypto_operation_unsupported"></span>**IPCERROR\_CRYPTO\_OPERATION\_UNSUPPORTED**
</dt> <dd> <dl> <dt>

0x80040206
</dt> <dt>



This application cannot provide rights management functionality because the cryptographic algorithm requested by the server is not supported by this client. Contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_DEBUGGER_DETECTED"></span><span id="ipcerror_debugger_detected"></span>**IPCERROR\_DEBUGGER\_DETECTED**
</dt> <dd> <dl> <dt>

0x80040207
</dt> <dt>



The operation could not be completed because a debugger was detected.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_LOCALE_NOT_FOUND"></span><span id="ipcerror_locale_not_found"></span>**IPCERROR\_LOCALE\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x80040208
</dt> <dt>



Text for the specified language does not exist in this license.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_ILS_ERROR"></span><span id="ipcerror_ils_error"></span>**IPCERROR\_ILS\_ERROR**
</dt> <dd> <dl> <dt>

0x80040209
</dt> <dt>



An error occurred when trying to contact the Information Rights Management Service for your Microsoft account. Try again later, or contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_SERVER_RESPONSE_NOT_VALID"></span><span id="ipcerror_server_response_not_valid"></span>**IPCERROR\_SERVER\_RESPONSE\_NOT\_VALID**
</dt> <dd> <dl> <dt>

0x8004020A
</dt> <dt>



The data received from the server running AD RMS didn't match the expected format. Contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_OS_VERSION_NOT_TRUSTED"></span><span id="ipcerror_os_version_not_trusted"></span>**IPCERROR\_OS\_VERSION\_NOT\_TRUSTED**
</dt> <dd> <dl> <dt>

0x8004020B
</dt> <dt>



This operating system version is not trusted to perform the specified operation. Contact the content owner for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_ISSUANCELICENSE_LENGTH_LIMIT_EXCEEDED"></span><span id="ipcerror_issuancelicense_length_limit_exceeded"></span>**IPCERROR\_ISSUANCELICENSE\_LENGTH\_LIMIT\_EXCEEDED**
</dt> <dd> <dl> <dt>

0x8004020C
</dt> <dt>



Too many users have been granted access to this protected content. Reduce the number of users or replace users with user groups, and try again.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_NEEDS_ONLINE"></span><span id="ipcerror_needs_online"></span>**IPCERROR\_NEEDS\_ONLINE**
</dt> <dd> <dl> <dt>

0x8004020D
</dt> <dt>



The RMS Client 2.1 needs network access to complete the operation, but it cannot get network access because the application requested offline mode.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_NEEDS_UI"></span><span id="ipcerror_needs_ui"></span>**IPCERROR\_NEEDS\_UI**
</dt> <dd> <dl> <dt>

0x8004020E
</dt> <dt>



The RMS Client 2.1 needs to display a window to complete the operation, but it cannot display a window because the application requested silent mode.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_NOT_BLOCK_ALIGNED"></span><span id="ipcerror_not_block_aligned"></span>**IPCERROR\_NOT\_BLOCK\_ALIGNED**
</dt> <dd> <dl> <dt>

0x8004020F
</dt> <dt>



The data passed to the RMS Client 2.1 was not a multiple of the cipher block size. Contact your application support for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_PROPERTY_ALREADY_SET"></span><span id="ipcerror_property_already_set"></span>**IPCERROR\_PROPERTY\_ALREADY\_SET**
</dt> <dd> <dl> <dt>

0x80040210
</dt> <dt>



The application attempted to set a property that has already been set.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_RIGHT_NOT_GRANTED"></span><span id="ipcerror_right_not_granted"></span>**IPCERROR\_RIGHT\_NOT\_GRANTED**
</dt> <dd> <dl> <dt>

0x80040211
</dt> <dt>



You have not been granted the rights necessary to complete the specified operation. Contact the content owner for additional rights.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_SAFEMODE_OS_DETECTED"></span><span id="ipcerror_safemode_os_detected"></span>**IPCERROR\_SAFEMODE\_OS\_DETECTED**
</dt> <dd> <dl> <dt>

0x80040212
</dt> <dt>



The RMS Client 2.1 cannot be started when the operating system is in safe mode. Try the operation again when the operating system is in normal mode.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_SERVER_ERROR"></span><span id="ipcerror_server_error"></span>**IPCERROR\_SERVER\_ERROR**
</dt> <dd> <dl> <dt>

0x80040214
</dt> <dt>



An error occurred while trying to contact the Active Directory Rights Management Services server. Try again later or contact your administrator.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_MACHINE_NOT_TRUSTED"></span><span id="ipcerror_machine_not_trusted"></span>**IPCERROR\_MACHINE\_NOT\_TRUSTED**
</dt> <dd> <dl> <dt>

0x80040215
</dt> <dt>



This computer does not have the rights required to perform the specified operation. Update the rights on this computer or contact your administrator.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_NEEDS_KEY_PARAMETER"></span><span id="ipcerror_needs_key_parameter"></span>**IPCERROR\_NEEDS\_KEY\_PARAMETER**
</dt> <dd> <dl> <dt>

0x80040216
</dt> <dt>



The application must provide a key handle to access the requested information. Contact your application support for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_LICENSE_INTERVAL_TIME_NOT_SET"></span><span id="ipcerror_license_interval_time_not_set"></span>**IPCERROR\_LICENSE\_INTERVAL\_TIME\_NOT\_SET**
</dt> <dd> <dl> <dt>

0x80040217
</dt> <dt>



License interval time on this content is not set. Contact your application support for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_CONTENT_KEY_NOT_SET"></span><span id="ipcerror_content_key_not_set"></span>**IPCERROR\_CONTENT\_KEY\_NOT\_SET**
</dt> <dd> <dl> <dt>

0x80040218
</dt> <dt>



Content key on the license used by this content is not set. Contact your application support for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_SIA_NOT_INSTALLED"></span><span id="ipcerror_sia_not_installed"></span>**IPCERROR\_SIA\_NOT\_INSTALLED**
</dt> <dd> <dl> <dt>

0x80040219
</dt> <dt>



Microsoft Online Services Sign-in Assistant is not installed on this machine. Contact your administrator for further investigation.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_TEMPLATE_NOT_ENABLED_FOR_USER"></span><span id="ipcerror_template_not_enabled_for_user"></span>**IPCERROR\_TEMPLATE\_NOT\_ENABLED\_FOR\_USER**
</dt> <dd> <dl> <dt>

0x8004021A
</dt> <dt>



Azure Rights Management Service has not granted you rights to modify the usage policy for this content. Contact your administrator for more details.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_FILE_SYSTEM_FILE"></span><span id="ipcerror_file_system_file"></span>**IPCERROR\_FILE\_SYSTEM\_FILE**
</dt> <dd> <dl> <dt>

0x80041000
</dt> <dt>



The specified file is a Windows system file.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_FILE_IS_NOT_ENCRYPTED"></span><span id="ipcerror_file_is_not_encrypted"></span>**IPCERROR\_FILE\_IS\_NOT\_ENCRYPTED**
</dt> <dd> <dl> <dt>

0x80041001
</dt> <dt>



This file is not encrypted by Active Directory Rights Management Services.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_FILE_ENCRYPT_BLOCKED"></span><span id="ipcerror_file_encrypt_blocked"></span>**IPCERROR\_FILE\_ENCRYPT\_BLOCKED**
</dt> <dd> <dl> <dt>

0x80041002
</dt> <dt>



Encryption of this file format is blocked by your administrators.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_FILE_UPDATELICENSE_BLOCKED"></span><span id="ipcerror_file_updatelicense_blocked"></span>**IPCERROR\_FILE\_UPDATELICENSE\_BLOCKED**
</dt> <dd> <dl> <dt>

0x80041003
</dt> <dt>



Updating the policy on an already encrypted file is blocked by your administrator.


</dt> </dl> </dd> <dt>

<span id="IPCERROR_FILE_PDFPROTECTOR_FORMAT_NOT_SUPPORTED"></span><span id="ipcerror_file_pdfprotector_format_not_supported"></span>**IPCERROR\_FILE\_PDFPROTECTOR\_FORMAT\_NOT\_SUPPORTED**
</dt> <dd> <dl> <dt>

0x80041004
</dt> <dt>



The PDF Protector does not support the specified file for native protection.


</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                          |
| Header<br/>                   | <dl> <dt>Ipcerror.h (include Msipc.h)</dt> </dl> |



 

 





