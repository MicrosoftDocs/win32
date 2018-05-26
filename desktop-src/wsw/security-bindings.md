---
title: Security Bindings
description: A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security.
ms.assetid: 3e50e0fb-a7ca-4615-ac4c-5d93988e6460
keywords:
- Security Bindings Web Services for Windows
- WWSAPI
- WWS
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Security Bindings

A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security. The security token contains information that vouches for the right to access resources. It may also have an associated cryptographic key for performing signatures and encryption.

## 

Each security binding contains its own collection of optional [security binding settings](security-binding-settings.md) that are scoped to the security token it defines. It also contains [security credentials](security-credentials.md), representing the security evidence (such as username and passwords, or certificates) needed to create security tokens.

The following callbacks are part of the security binding:

-   [**WS\_VALIDATE\_SAML\_CALLBACK**](/windows/win32/WebServices/nc-webservices-ws_validate_saml_callback?branch=master)

The following enumerations are part of the security binding:

-   [**WS\_MESSAGE\_SECURITY\_USAGE**](/windows/win32/WebServices/ne-webservices-ws_message_security_usage?branch=master)
-   [**WS\_SAML\_AUTHENTICATOR\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_saml_authenticator_type?branch=master)
-   [**WS\_SECURITY\_BINDING\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_security_binding_type?branch=master)
-   [**WS\_SECURITY\_KEY\_HANDLE\_TYPE**](/windows/win32/WebServices/ne-webservices-ws_security_key_handle_type?branch=master)

The following functions are part of the security binding:

-   [**WsCreateXmlSecurityToken**](/windows/win32/WebServices/nf-webservices-wscreatexmlsecuritytoken?branch=master)
-   [**WsFreeSecurityToken**](/windows/win32/WebServices/nf-webservices-wsfreesecuritytoken?branch=master)
-   

The following structures are part of the security binding:

-   [**WS\_CAPI\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/win32/WebServices/ns-webservices-_ws_capi_asymmetric_security_key_handle?branch=master)
-   [**WS\_CERT\_SIGNED\_SAML\_AUTHENTICATOR**](/windows/win32/WebServices/ns-webservices-_ws_cert_signed_saml_authenticator?branch=master)
-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_http_header_auth_security_binding?branch=master)
-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_kerberos_apreq_message_security_binding?branch=master)
-   [**WS\_NAMEDPIPE\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_namedpipe_sspi_transport_security_binding?branch=master)
-   [**WS\_NCRYPT\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/win32/WebServices/ns-webservices-_ws_ncrypt_asymmetric_security_key_handle?branch=master)
-   [**WS\_RAW\_SYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/win32/WebServices/ns-webservices-_ws_raw_symmetric_security_key_handle?branch=master)
-   [**WS\_SAML\_AUTHENTICATOR**](/windows/win32/WebServices/ns-webservices-_ws_saml_authenticator?branch=master)
-   [**WS\_SAML\_MESSAGE\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_saml_message_security_binding?branch=master)
-   [**WS\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_security_binding?branch=master)
-   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_security_context_message_security_binding?branch=master)
-   [**WS\_SECURITY\_KEY\_HANDLE**](/windows/win32/WebServices/ns-webservices-_ws_security_key_handle?branch=master)
-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_ssl_transport_security_binding?branch=master)
-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_tcp_sspi_transport_security_binding?branch=master)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_username_message_security_binding?branch=master)
-   [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/win32/WebServices/ns-webservices-_ws_xml_token_message_security_binding?branch=master)

 

 




