---
title: Extended Protection
description: Extended protection is a mechanism to bind an outer secure channel such as SSL to inner channel authentication protocols such as Kerberos-APREQ and HTTP header authentication.
ms.assetid: '35e48846-05e5-4db9-a3b5-098b62815b66'
keywords: ["Extended Protection Native-Web-Services", "WWSAPI", "WWS"]
---

# Extended Protection

Extended protection is a mechanism to bind an outer secure channel such as SSL to inner channel authentication protocols such as Kerberos-APREQ and HTTP header authentication.

The concept of extended protection is defined in RFC2743.

Extended protection, when available, is configured automatically on the client but may require configuration on the server for non-default scenarios.

## Supported Configurations

Extended protection is supported when using [**WS\_HTTP\_CHANNEL\_BINDING**](ws-channel-binding.md) with security bindings using Windows Integrated Authentication protocols such as [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md) and [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md). It is configured via the following [**security properties**](ws-security-property.md):

-   [**WS\_SECURITY\_PROPERTY\_EXTENDED\_PROTECTION\_POLICY**](ws-security-property-id.md)
-   [**WS\_SECURITY\_PROPERTY\_EXTENDED\_PROTECTION\_SCENARIO**](ws-security-property-id.md)
-   [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](ws-security-property-id.md)

The following configurations involving extended protection are possible:

Client

-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](ws-ssl-transport-security-binding.md) is used with [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md). In this configuration the authentication binding is bound to the SSL connection via an extended protection token that is automatically extracted from the SSL connection.
-   No SSL is used and [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md) is set. The authentication binding is bound via the Server Principal Name (SPN), which is autonatically determined from the [**WS\_ENDPOINT\_ADDRESS**](ws-endpoint-address.md).

Server

-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](ws-ssl-transport-security-binding.md) is used with [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md). In this configuration the authentication binding is bound to the SSL connection via an extended protection token that is extracted from the SSL connection and validated automatically.
-   No SSL is used and [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md) is set. The authentication binding is bound via the Server Principal Name (SPN), which must be provided via [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](ws-security-property-id.md). When a message is received, the SPN is extracted and validated for an exact match with the provided service names. Not providing SPNs is the equivalent of setting [**WS\_EXTENDED\_PROTECTION\_POLICY\_NEVER**](ws-extended-protection-policy.md).
-   No SSL is used, [**WS\_EXTENDED\_PROTECTION\_SCENARIO\_BOUND\_SERVER**](ws-extended-protection-scenario.md) is specified and [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) is used. In this configuration, [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](ws-security-property-id.md) must not be set. No SPN check is performed beyond what is done as part of the Kerberos protocol.
-   [**WS\_EXTENDED\_PROTECTION\_SCENARIO\_TERMINATED\_SSL**](ws-extended-protection-scenario.md) is specified and either [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](ws-http-header-auth-security-binding.md) is used. [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](ws-security-property-id.md) must be set.

## Supported Platforms

Extended protection is supported on platforms with support for it in the operating system. Windows 7 and Windows Server 2008 R2 provide built-in support. Other platforms may require an update.

If the server's operating system does not provide such support, any extended protection information sent by the client is ignored. As a result, clients using extended protection can communicate with such a server, but the security benefit is lost. On the client, [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) combined with [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](ws-ssl-transport-security-binding.md) only supports extended protection on Vista and above.

NOTE: Extended protection being unavailable does not prevent any particular configuration from being used.

## Interoperability

A default-configured server can communicate with SOAP clients regardless of whether they use extended protection or not. The one exception being Windows XP and Windows Server 2003 WWSAPI clients that have been updated to support extended protection and use both [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](ws-kerberos-apreq-message-security-binding.md) and [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](ws-ssl-transport-security-binding.md). To support such clients [**WS\_EXTENDED\_PROTECTION\_POLICY\_NEVER**](ws-extended-protection-policy.md) must be specified by the server. Servers configured with **WS\_EXTENDED\_PROTECTION\_POLICY\_ALWAYS** will reject communication from clients that do not use extended protection. On the client, **WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING** combined with **WS\_SSL\_TRANSPORT\_SECURITY\_BINDING** will result in the message being sent using the HTTP chunked transfer encoding on Vista and above. This may cause interop issues with servers that do not support chunked transfer.

The following Enums/Constants are part of extended protection:

-   [**WS\_EXTENDED\_PROTECTION\_POLICY**](ws-extended-protection-policy.md)
-   [**WS\_EXTENDED\_PROTECTION\_SCENARIO**](ws-extended-protection-scenario.md)

The following stuctures are part of extended protection:

-   [**WS\_SERVICE\_SECURITY\_IDENTITIES**](ws-service-security-identities.md)

 

 




