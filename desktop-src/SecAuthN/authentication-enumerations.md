---
Description: 'Lists the enumerations used in authentication APIs.'
ms.assetid: 'e27888e5-d01a-4fdd-8c7d-9849c0f90eb5'
title: Authentication Enumerations
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
| [**CRED\_MARSHAL\_TYPE**](cred-marshal-type.md)       | Contains the types of credential that can be marshaled by [**CredMarshalCredential**](credmarshalcredential.md) or unmarshaled by [**CredUnmarshalCredential**](credunmarshalcredential.md).<br/> |
| [**CRED\_PROTECTION\_TYPE**](cred-protection-type.md) | Specifies the security context in which credentials are encrypted when using the [**CredProtect**](credprotect.md) function.<br/>                                                                  |



 

## LSA Enumerations

LSA uses the following enumerations.



| Enumeration                                                                                   | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**KERB\_LOGON\_SUBMIT\_TYPE**](kerb-logon-submit-type.md)                                   | Lists the type of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**KERB\_PROFILE\_BUFFER\_TYPE**](kerb-profile-buffer-type.md)                               | Lists the type of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**KERB\_PROTOCOL\_MESSAGE\_TYPE**](kerb-protocol-message-type.md)                           | Lists the types of messages which can be sent to the [*Kerberos*](https://msdn.microsoft.com/library/windows/desktop/ms721590#-security-kerberos-protocol-gly) authentication package by calling [**LsaCallAuthenticationPackage**](lsacallauthenticationpackage.md).<br/> |
| [**LSA\_FOREST\_TRUST\_COLLISION\_RECORD\_TYPE**](lsa-forest-trust-collision-record-type.md) | Defines the types of collision that can occur between LSA forest trust records.<br/>                                                                                                                                                                           |
| [**LSA\_FOREST\_TRUST\_RECORD\_TYPE**](lsa-forest-trust-record-type.md)                      | Defines the type of an LSA forest trust record.<br/>                                                                                                                                                                                                           |
| [**LSA\_TOKEN\_INFORMATION\_TYPE**](lsa-token-information-type.md)                           | Specifies the levels of information that can be included in a logon token.<br/>                                                                                                                                                                                |
| [**MSV1\_0\_LOGON\_SUBMIT\_TYPE**](msv1-0-logon-submit-type.md)                              | Lists the kind of logon being requested.<br/>                                                                                                                                                                                                                  |
| [**MSV1\_0\_PROFILE\_BUFFER\_TYPE**](msv1-0-profile-buffer-type.md)                          | Lists the kind of logon profile returned.<br/>                                                                                                                                                                                                                 |
| [**MSV1\_0\_PROTOCOL\_MESSAGE\_TYPE**](msv1-0-protocol-message-type.md)                      | Lists the types of messages which can be sent to the [MSV1\_0 Authentication Package](msv1-0-authentication-package.md) by calling [**LsaCallAuthenticationPackage**](lsacallauthenticationpackage.md).<br/>                                                 |
| [**POLICY\_DOMAIN\_INFORMATION\_CLASS**](policy-domain-information-class.md)                 | Defines the type of policy domain information.<br/>                                                                                                                                                                                                            |
| [**SECURITY\_LOGON\_TYPE**](security-logon-type.md)                                          | Indicates the type of logon requested by a logon process.<br/>                                                                                                                                                                                                 |



 

## Network Provider Enumerations

Network Provider uses the following enumerations.



| Enumeration                                                                       | Description                                                                                                                                                                                |
|-----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SECPKG\_EXTENDED\_INFORMATION\_CLASS**](secpkg-extended-information-class.md) | Enumeration type that specifies the type of information to set or get for a [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly).<br/> |
| [**SECPKG\_NAME\_TYPE**](secpkg-name-type.md)                                    | Enumeration value that specifies the type of name specified for an account.<br/>                                                                                                     |



 

## Credential Security Support Provider (CredSSP) Enumerations

CredSSP uses the following enumerations.



| Enumeration                                          | Description                                                                                                  |
|------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [**CREDSPP\_SUBMIT\_TYPE**](credspp-submit-type.md) | Specifies the type of credentials specified by a [**CREDSSP\_CRED**](credssp-cred.md) structure.<br/> |



 

## Other Enumerations

Here are the other enumerations used by Authentication.



| Enumeration                                                   | Description                                                                                                                                                                                                                |
|---------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IDENTITY\_TYPE**](identity-type.md)                       | Specifies the type of identities to enumerate.<br/>                                                                                                                                                                  |
| [**PKU2U\_LOGON\_SUBMIT\_TYPE**](pku2u-logon-submit-type.md) | Indicates the type of logon message passed in a [**PKU2U\_CERTIFICATE\_S4U\_LOGON**](pku2u-certificate-s4u-logon.md) structure.<br/>                                                                                |
| [**SECPKG\_ATTR\_LCT\_STATUS**](secpkg-attr-lct-status.md)   | Indicates whether the token from the most recent call to the [**InitializeSecurityContext**](initializesecuritycontext--general-.md) function is the last token from the client.<br/>                               |
| [**SECPKG\_CRED\_CLASS**](secpkg-cred-class.md)              | Indicates the type of credential used in a client context. The [**SECPKG\_CRED\_CLASS**](secpkg-cred-class.md) enumeration is used in the [**SecPkgContext\_CredInfo**](secpkgcontext-credinfo.md) structure.<br/> |



 

 

 




