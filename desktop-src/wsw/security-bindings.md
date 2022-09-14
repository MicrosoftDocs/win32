---
title: Security Bindings
description: A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security.
ms.assetid: 3e50e0fb-a7ca-4615-ac4c-5d93988e6460
keywords:
- Security Bindings Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Bindings

A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security. The security token contains information that vouches for the right to access resources. It may also have an associated cryptographic key for performing signatures and encryption.


Each security binding contains its own collection of optional [security binding settings](security-binding-settings.md) that are scoped to the security token it defines. It also contains [security credentials](security-credentials.md), representing the security evidence (such as username and passwords, or certificates) needed to create security tokens.

The following callbacks are part of the security binding:

-   [**WS\_VALIDATE\_SAML\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_validate_saml_callback)

The following enumerations are part of the security binding:

-   [**WS\_MESSAGE\_SECURITY\_USAGE**](/windows/desktop/api/WebServices/ne-webservices-ws_message_security_usage)
-   [**WS\_SAML\_AUTHENTICATOR\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_saml_authenticator_type)
-   [**WS\_SECURITY\_BINDING\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_type)
-   [**WS\_SECURITY\_KEY\_HANDLE\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_security_key_handle_type)

The following functions are part of the security binding:

-   [**WsCreateXmlSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wscreatexmlsecuritytoken)
-   [**WsFreeSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wsfreesecuritytoken)
-   

The following structures are part of the security binding:

-   [**WS\_CAPI\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/desktop/api/WebServices/ns-webservices-ws_capi_asymmetric_security_key_handle)
-   [**WS\_CERT\_SIGNED\_SAML\_AUTHENTICATOR**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_signed_saml_authenticator)
-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding)
-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding)
-   [**WS\_NAMEDPIPE\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_namedpipe_sspi_transport_security_binding)
-   [**WS\_NCRYPT\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/desktop/api/WebServices/ns-webservices-ws_ncrypt_asymmetric_security_key_handle)
-   [**WS\_RAW\_SYMMETRIC\_SECURITY\_KEY\_HANDLE**](/windows/desktop/api/WebServices/ns-webservices-ws_raw_symmetric_security_key_handle)
-   [**WS\_SAML\_AUTHENTICATOR**](/windows/desktop/api/WebServices/ns-webservices-ws_saml_authenticator)
-   [**WS\_SAML\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_saml_message_security_binding)
-   [**WS\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding)
-   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding)
-   [**WS\_SECURITY\_KEY\_HANDLE**](/windows/desktop/api/WebServices/ns-webservices-ws_security_key_handle)
-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding)
-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding)
-   [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding)

 

 




