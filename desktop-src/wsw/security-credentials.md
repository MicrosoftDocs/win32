---
title: Security Credentials
description: Security credentials are a piece of evidence that a communicating party possesses that can be used to create or obtain a security token.
ms.assetid: 70e260ce-9e45-436f-b6d1-b650a5c9c0e9
keywords:
- Security Credentials Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Credentials

Security credentials are a piece of evidence that a communicating party possesses that can be used to create or obtain a security token. Thus, credentials are typically longer-lived than security tokens, and a security token can be viewed as the runtime manifestation of the security credentials. Example of credentials include a machine certificate (which can be converted into an X.509 security token at runtime) or a username/password pair for a domain (which can be used to obtain a Kerberos security token).


Credentials are specified as part of the [security bindings](security-bindings.md).

The following API elements are used with security credentials.

| Callback                                                                  | Description                                              |
|---------------------------------------------------------------------------|----------------------------------------------------------|
| [**WS\_GET\_CERT\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_get_cert_callback)                   | Provides a certificate to the security runtime.          |
| [**WS\_VALIDATE\_PASSWORD\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_validate_password_callback) | Validates a username/password pair on the receiver side. |



 



| Enumeration                                                                                           | Description                                                   |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| [**WS\_CERT\_CREDENTIAL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_cert_credential_type)                                         | The type of the certificate credential.                       |
| [**WS\_USERNAME\_CREDENTIAL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_username_credential_type)                                 | The type of the username/password credential.                 |
| [**WS\_WINDOWS\_INTEGRATED\_AUTH\_CREDENTIAL\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_windows_integrated_auth_credential_type) | The type of the Windows Integrated Authentication credential. |



 



| Structure                                                                                                   | Description                                                                                                           |
|-------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| [**WS\_CERT\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_credential)                                                          | The abstract base type for all certificate credential types.                                                          |
| [**WS\_CUSTOM\_CERT\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_custom_cert_credential)                                           | The type for specifying a certificate credential that is to be supplied by a callback to the application.             |
| [**WS\_DEFAULT\_WINDOWS\_INTEGRATED\_AUTH\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_default_windows_integrated_auth_credential) | Type for supplying a Windows Integrated Authentication credential based on the current thread token.                  |
| [**WS\_OPAQUE\_WINDOWS\_INTEGRATED\_AUTH\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_opaque_windows_integrated_auth_credential)   | Type for supplying a Windows Integrated Authentication credential.                                                    |
| [**WS\_STRING\_USERNAME\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_string_username_credential)                                   | The type for supplying a username/password pair as strings.                                                           |
| [**WS\_STRING\_WINDOWS\_INTEGRATED\_AUTH\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_string_windows_integrated_auth_credential)   | Type for supplying a Windows credential as username, password, domain strings.                                        |
| [**WS\_SUBJECT\_NAME\_CERT\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_subject_name_cert_credential)                              | The type for specifying a certificate credential using the certificate's subject name, store location and store name. |
| [**WS\_THUMBPRINT\_CERT\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_thumbprint_cert_credential)                                   | The type for specifying a certificate credential using the certificate's thumbprint, store location and store name.   |
| [**WS\_USERNAME\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_username_credential)                                                  | The abstract base type for all username/password credentials.                                                         |
| [**WS\_WINDOWS\_INTEGRATED\_AUTH\_CREDENTIAL**](/windows/desktop/api/WebServices/ns-webservices-ws_windows_integrated_auth_credential)                  | The abstract base type for all credential types used with Windows Integrated Authentication.                          |



 

 

 




