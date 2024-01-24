---
description: Lists the enumerations used in authentication APIs.
ms.assetid: e27888e5-d01a-4fdd-8c7d-9849c0f90eb5
title: Authentication Enumerations
ms.topic: article
ms.date: 05/31/2018
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
| [**CRED\_MARSHAL\_TYPE**](/windows/desktop/api/WinCred/ne-wincred-cred_marshal_type)       | Contains the types of credential that can be marshaled by [**CredMarshalCredential**](/windows/desktop/api/WinCred/nf-wincred-credmarshalcredentiala) or unmarshaled by [**CredUnmarshalCredential**](/windows/desktop/api/WinCred/nf-wincred-credunmarshalcredentiala).<br/> |
| [**CRED\_PROTECTION\_TYPE**](/windows/desktop/api/WinCred/ne-wincred-cred_protection_type) | Specifies the security context in which credentials are encrypted when using the [**CredProtect**](/windows/desktop/api/WinCred/nf-wincred-credprotecta) function.<br/>                                                                  |



 

## LSA Enumerations

LSA uses the following enumerations.



| Enumeration                                                                                   | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**KERB\_LOGON\_SUBMIT\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-kerb_logon_submit_type)                                   | Lists the type of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**KERB\_PROFILE\_BUFFER\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-kerb_profile_buffer_type)                               | Lists the type of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**KERB\_PROTOCOL\_MESSAGE\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-kerb_protocol_message_type)                           | Lists the types of messages which can be sent to the [*Kerberos*](/windows/desktop/SecGloss/k-gly) authentication package by calling [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage).<br/> |
| [**LSA\_FOREST\_TRUST\_COLLISION\_RECORD\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-lsa_forest_trust_collision_record_type) | Defines the types of collision that can occur between LSA forest trust records.<br/>                                                                                                                                                                           |
| [**LSA\_FOREST\_TRUST\_RECORD\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-lsa_forest_trust_record_type)                      | Defines the type of an LSA forest trust record.<br/>                                                                                                                                                                                                           |
| [**LSA\_TOKEN\_INFORMATION\_TYPE**](/windows/desktop/api/Ntsecpkg/ne-ntsecpkg-lsa_token_information_type)                           | Specifies the levels of information that can be included in a logon token.<br/>                                                                                                                                                                                |
| [**MSV1\_0\_LOGON\_SUBMIT\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-msv1_0_logon_submit_type)                              | Lists the kind of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**MSV1\_0\_PROFILE\_BUFFER\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-msv1_0_profile_buffer_type)                          | Lists the kind of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**MSV1\_0\_PROTOCOL\_MESSAGE\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-msv1_0_protocol_message_type)                      | Lists the types of messages which can be sent to the [MSV1\_0 Authentication Package](msv1-0-authentication-package.md) by calling [**LsaCallAuthenticationPackage**](/windows/desktop/api/Ntsecapi/nf-ntsecapi-lsacallauthenticationpackage).<br/>                                                 |
| [**POLICY\_DOMAIN\_INFORMATION\_CLASS**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-policy_domain_information_class)                 | Defines the type of policy domain information.<br/>                                                                                                                                                                                                            |
| [**SECURITY\_LOGON\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-security_logon_type)                                          | Indicates the type of logon requested by a logon process.<br/>                                                                                                                                                                                                 |



 

## Network Provider Enumerations

Network Provider uses the following enumerations.



| Enumeration                                                                       | Description                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SECPKG\_EXTENDED\_INFORMATION\_CLASS**](/windows/desktop/api/Ntsecpkg/ne-ntsecpkg-secpkg_extended_information_class) | Enumeration type that specifies the type of information to set or get for a [*security package*](/windows/desktop/SecGloss/s-gly).<br/> |
| [**SECPKG\_NAME\_TYPE**](/windows/desktop/api/Ntsecpkg/ne-ntsecpkg-secpkg_name_type)                                    | Enumeration value that specifies the type of name specified for an account.<br/>                                                                                                     |



 

## Credential Security Support Provider (CredSSP) Enumerations

CredSSP uses the following enumerations.



| Enumeration                                          | Description                                                                                                  |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**CREDSPP\_SUBMIT\_TYPE**](/windows/win32/api/credssp/ne-credssp-credspp_submit_type) | Specifies the type of credentials specified by a [**CREDSSP\_CRED**](/windows/desktop/api/Credssp/ns-credssp-credssp_cred) structure.<br/> |



 

## Other Enumerations

Here are the other enumerations used by Authentication.



| Enumeration                                                   | Description                                                                                                                                                                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDENTITY\_TYPE**](/windows/win32/api/identitycommon/ne-identitycommon-identity_type)                       | Specifies the type of identities to enumerate.<br/>                                                                                                                                                                  |
| [**PKU2U\_LOGON\_SUBMIT\_TYPE**](/windows/desktop/api/Ntsecapi/ne-ntsecapi-pku2u_logon_submit_type) | Indicates the type of logon message passed in a [**PKU2U\_CERTIFICATE\_S4U\_LOGON**](/windows/desktop/api/Ntsecapi/ns-ntsecapi-pku2u_certificate_s4u_logon) structure.<br/>                                                                                |
| [**SECPKG\_ATTR\_LCT\_STATUS**](/windows/desktop/api/Sspi/ne-sspi-secpkg_attr_lct_status)   | Indicates whether the token from the most recent call to the [**InitializeSecurityContext**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function is the last token from the client.<br/>                               |
| [**SECPKG\_CRED\_CLASS**](/windows/desktop/api/Sspi/ne-sspi-secpkg_cred_class)              | Indicates the type of credential used in a client context. The [**SECPKG\_CRED\_CLASS**](/windows/desktop/api/Sspi/ne-sspi-secpkg_cred_class) enumeration is used in the [**SecPkgContext\_CredInfo**](/windows/desktop/api/Sspi/ns-sspi-secpkgcontext_credinfo) structure.<br/> |



 

 

