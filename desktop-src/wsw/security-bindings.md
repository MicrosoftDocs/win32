---
title: Security Bindings
description: A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security.
ms.assetid: '3e50e0fb-a7ca-4615-ac4c-5d93988e6460'
keywords: ["Security Bindings Web Services for Windows", "WWSAPI", "WWS"]
---

# Security Bindings

A security binding is the specification of a security token, and tells the runtime how to obtain and use a security token for channel security. The security token contains information that vouches for the right to access resources. It may also have an associated cryptographic key for performing signatures and encryption.

## 

Each security binding contains its own collection of optional [security binding settings](security-binding-settings.md) that are scoped to the security token it defines. It also contains [security credentials](security-credentials.md), representing the security evidence (such as username and passwords, or certificates) needed to create security tokens.

The following callbacks are part of the security binding:

-   [**WS\_VALIDATE\_SAML\_CALLBACK**](ws-validate-saml-callback.md)

The following enumerations are part of the security binding:

-   [**WS\_MESSAGE\_SECURITY\_USAGE**](ws-message-security-usage.md)
-   [**WS\_SAML\_AUTHENTICATOR\_TYPE**](ws-saml-authenticator-type.md)
-   [**WS\_SECURITY\_BINDING\_TYPE**](ws-security-binding-type.md)
-   [**WS\_SECURITY\_KEY\_HANDLE\_TYPE**](ws-security-key-handle-type.md)

The following functions are part of the security binding:

-   [**WsCreateXmlSecurityToken**](wscreatexmlsecuritytoken.md)
-   [**WsFreeSecurityToken**](wsfreesecuritytoken.md)
-   

The following structures are part of the security binding:

-   [**WS\_CAPI\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](ws-capi-asymmetric-security-key-handle.md)
-   [**WS\_CERT\_SIGNED\_SAML\_AUTHENTICATOR**](ws-cert-signed-saml-authenticator.md)
-   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md)
-   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md)
-   [**WS\_NAMEDPIPE\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](ws-namedpipe-sspi-transport-security-binding.md)
-   [**WS\_NCRYPT\_ASYMMETRIC\_SECURITY\_KEY\_HANDLE**](ws-ncrypt-asymmetric-security-key-handle.md)
-   [**WS\_RAW\_SYMMETRIC\_SECURITY\_KEY\_HANDLE**](ws-raw-symmetric-security-key-handle.md)
-   [**WS\_SAML\_AUTHENTICATOR**](ws-saml-authenticator.md)
-   [**WS\_SAML\_MESSAGE\_SECURITY\_BINDING**](ws-saml-message-security-binding.md)
-   [**WS\_SECURITY\_BINDING**](ws-security-binding.md)
-   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](ws-security-context-message-security-binding.md)
-   [**WS\_SECURITY\_KEY\_HANDLE**](ws-security-key-handle.md)
-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](ws-ssl-transport-security-binding.md)
-   [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](ws-tcp-sspi-transport-security-binding.md)
-   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](ws-username-message-security-binding.md)
-   [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](ws-xml-token-message-security-binding.md)

 

 




