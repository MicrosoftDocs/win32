---
Description: Lists the enumerations used in authentication APIs.
ms.assetid: e27888e5-d01a-4fdd-8c7d-9849c0f90eb5
title: Authentication Enumerations
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authentication Enumerations

Authentication enumerations are categorized according to usage as follows:

-   [Credentials Management Enumerations](#credentials-management-enumerations)
-   [LSA Enumerations](#lsa-enumerations)
-   [Network Provider Enumerations](#network-provider-enumerations)
-   [Credential Security Support Provider (CredSSP) Enumerations](#credential-security-support-provider-credssp-enumerations)
-   [Other Enumerations](#other-enumerations)

## Credentials Management Enumerations

Credentials Management uses the following enumerations.



| Enumeration                                            | Description                                                                                                                                                                                               |
|--------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CRED\_MARSHAL\_TYPE**](/windows/win32/WinCred/ne-wincred-_cred_marshal_type?branch=master)       | Contains the types of credential that can be marshaled by [**CredMarshalCredential**](/windows/win32/WinCred/nf-wincred-credmarshalcredentiala?branch=master) or unmarshaled by [**CredUnmarshalCredential**](/windows/win32/WinCred/nf-wincred-credunmarshalcredentiala?branch=master).<br/> |
| [**CRED\_PROTECTION\_TYPE**](/windows/win32/WinCred/ne-wincred-_cred_protection_type?branch=master) | Specifies the security context in which credentials are encrypted when using the [**CredProtect**](/windows/win32/WinCred/nf-wincred-credprotecta?branch=master) function.<br/>                                                                  |



 

## LSA Enumerations

LSA uses the following enumerations.



| Enumeration                                                                                   | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**KERB\_LOGON\_SUBMIT\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_kerb_logon_submit_type?branch=master)                                   | Lists the type of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**KERB\_PROFILE\_BUFFER\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_kerb_profile_buffer_type?branch=master)                               | Lists the type of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**KERB\_PROTOCOL\_MESSAGE\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_kerb_protocol_message_type?branch=master)                           | Lists the types of messages which can be sent to the [*Kerberos*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-kerberos-protocol-gly) authentication package by calling [**LsaCallAuthenticationPackage**](/windows/win32/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage?branch=master).<br/> |
| [**LSA\_FOREST\_TRUST\_COLLISION\_RECORD\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-lsa_forest_trust_collision_record_type?branch=master) | Defines the types of collision that can occur between LSA forest trust records.<br/>                                                                                                                                                                           |
| [**LSA\_FOREST\_TRUST\_RECORD\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-lsa_forest_trust_record_type?branch=master)                      | Defines the type of an LSA forest trust record.<br/>                                                                                                                                                                                                           |
| [**LSA\_TOKEN\_INFORMATION\_TYPE**](/windows/win32/Ntsecpkg/ne-ntsecpkg-_lsa_token_information_type?branch=master)                           | Specifies the levels of information that can be included in a logon token.<br/>                                                                                                                                                                                |
| [**MSV1\_0\_LOGON\_SUBMIT\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_msv1_0_logon_submit_type?branch=master)                              | Lists the kind of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**MSV1\_0\_PROFILE\_BUFFER\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_msv1_0_profile_buffer_type?branch=master)                          | Lists the kind of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**MSV1\_0\_PROTOCOL\_MESSAGE\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_msv1_0_protocol_message_type?branch=master)                      | Lists the types of messages which can be sent to the [MSV1\_0 Authentication Package](msv1-0-authentication-package.md) by calling [**LsaCallAuthenticationPackage**](/windows/win32/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage?branch=master).<br/>                                                 |
| [**POLICY\_DOMAIN\_INFORMATION\_CLASS**](/windows/win32/Ntsecapi/ne-ntsecapi-_policy_domain_information_class?branch=master)                 | Defines the type of policy domain information.<br/>                                                                                                                                                                                                            |
| [**SECURITY\_LOGON\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_security_logon_type?branch=master)                                          | Indicates the type of logon requested by a logon process.<br/>                                                                                                                                                                                                 |



 

## Network Provider Enumerations

Network Provider uses the following enumerations.



| Enumeration                                                                       | Description                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SECPKG\_EXTENDED\_INFORMATION\_CLASS**](/windows/win32/Ntsecpkg/ne-ntsecpkg-_secpkg_extended_information_class?branch=master) | Enumeration type that specifies the type of information to set or get for a [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly).<br/> |
| [**SECPKG\_NAME\_TYPE**](/windows/win32/Ntsecpkg/ne-ntsecpkg-_secpkg_name_type?branch=master)                                    | Enumeration value that specifies the type of name specified for an account.<br/>                                                                                                     |



 

## Credential Security Support Provider (CredSSP) Enumerations

CredSSP uses the following enumerations.



| Enumeration                                          | Description                                                                                                  |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**CREDSPP\_SUBMIT\_TYPE**](/windows/win32/Credssp/ne-credssp-_credssp_submit_type?branch=master) | Specifies the type of credentials specified by a [**CREDSSP\_CRED**](/windows/win32/Credssp/ns-credssp-_credssp_cred?branch=master) structure.<br/> |



 

## Other Enumerations

Here are the other enumerations used by Authentication.



| Enumeration                                                   | Description                                                                                                                                                                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDENTITY\_TYPE**](/windows/win32/Identitycommon/ne-identitycommon-_identitytype?branch=master)                       | Specifies the type of identities to enumerate.<br/>                                                                                                                                                                  |
| [**PKU2U\_LOGON\_SUBMIT\_TYPE**](/windows/win32/Ntsecapi/ne-ntsecapi-_pku2u_logon_submit_type?branch=master) | Indicates the type of logon message passed in a [**PKU2U\_CERTIFICATE\_S4U\_LOGON**](/windows/win32/Ntsecapi/ns-ntsecapi-_pku2u_certificate_s4u_logon?branch=master) structure.<br/>                                                                                |
| [**SECPKG\_ATTR\_LCT\_STATUS**](/windows/win32/Sspi/ne-sspi-_secpkg_attr_lct_status?branch=master)   | Indicates whether the token from the most recent call to the [**InitializeSecurityContext**](/windows/win32/Sspi/?branch=master) function is the last token from the client.<br/>                               |
| [**SECPKG\_CRED\_CLASS**](/windows/win32/Sspi/ne-sspi-_secpkg_cred_class?branch=master)              | Indicates the type of credential used in a client context. The [**SECPKG\_CRED\_CLASS**](/windows/win32/Sspi/ne-sspi-_secpkg_cred_class?branch=master) enumeration is used in the [**SecPkgContext\_CredInfo**](/windows/win32/Sspi/ns-sspi-_secpkgcontext_credinfo?branch=master) structure.<br/> |



 

 

 




