---
title: Extended Protection
description: Extended protection is a mechanism to bind an outer secure channel such as SSL to inner channel authentication protocols such as Kerberos-APREQ and HTTP header authentication.
ms.assetid: 35e48846-05e5-4db9-a3b5-098b62815b66
keywords:
- Extended Protection Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Extended Protection

Extended protection is a mechanism to bind an outer secure channel such as SSL to inner channel authentication protocols such as Kerberos-APREQ and HTTP header authentication.

The concept of extended protection is defined in RFC2743.

Extended protection, when available, is configured automatically on the client but may require configuration on the server for non-default scenarios.

## Supported Configurations

Extended protection is supported when using [**WS\_HTTP\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding) with security bindings using Windows Integrated Authentication protocols such as [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) and [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding). It is configured via the following [**security properties**](/windows/desktop/api/WebServices/ns-webservices-ws_security_property):

-   [**WS\_SECURITY\_PROPERTY\_EXTENDED\_PROTECTION\_POLICY**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)
-   [**WS\_SECURITY\_PROPERTY\_EXTENDED\_PROTECTION\_SCENARIO**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)
-   [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id)

The following configurations involving extended protection are possible:

Client

-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding) is used with [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding). In this configuration the authentication binding is bound to the SSL connection via an extended protection token that is automatically extracted from the SSL connection.
-   No SSL is used and [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) is set. The authentication binding is bound via the Server Principal Name (SPN), which is autonatically determined from the [**WS\_ENDPOINT\_ADDRESS**](/windows/desktop/api/WebServices/ns-webservices-ws_endpoint_address).

Server

-   [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding) is used with [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding). In this configuration the authentication binding is bound to the SSL connection via an extended protection token that is extracted from the SSL connection and validated automatically.
-   No SSL is used and [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) is set. The authentication binding is bound via the Server Principal Name (SPN), which must be provided via [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id). When a message is received, the SPN is extracted and validated for an exact match with the provided service names. Not providing SPNs is the equivalent of setting [**WS\_EXTENDED\_PROTECTION\_POLICY\_NEVER**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_policy).
-   No SSL is used, [**WS\_EXTENDED\_PROTECTION\_SCENARIO\_BOUND\_SERVER**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_scenario) is specified and [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) is used. In this configuration, [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id) must not be set. No SPN check is performed beyond what is done as part of the Kerberos protocol.
-   [**WS\_EXTENDED\_PROTECTION\_SCENARIO\_TERMINATED\_SSL**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_scenario) is specified and either [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) or [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) is used. [**WS\_SECURITY\_PROPERTY\_SERVICE\_IDENTITIES**](/windows/desktop/api/WebServices/ne-webservices-ws_security_property_id) must be set.

## Supported Platforms

Extended protection is supported on platforms with support for it in the operating system. Windows 7 and Windows Server 2008 R2 provide built-in support. Other platforms may require an update.

If the server's operating system does not provide such support, any extended protection information sent by the client is ignored. As a result, clients using extended protection can communicate with such a server, but the security benefit is lost. On the client, [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) combined with [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding) only supports extended protection on Vista and above.

NOTE: Extended protection being unavailable does not prevent any particular configuration from being used.

## Interoperability

A default-configured server can communicate with SOAP clients regardless of whether they use extended protection or not. The one exception being Windows XP and Windows Server 2003 WWSAPI clients that have been updated to support extended protection and use both [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) and [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding). To support such clients [**WS\_EXTENDED\_PROTECTION\_POLICY\_NEVER**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_policy) must be specified by the server. Servers configured with **WS\_EXTENDED\_PROTECTION\_POLICY\_ALWAYS** will reject communication from clients that do not use extended protection. On the client, **WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING** combined with **WS\_SSL\_TRANSPORT\_SECURITY\_BINDING** will result in the message being sent using the HTTP chunked transfer encoding on Vista and above. This may cause interop issues with servers that do not support chunked transfer.

The following Enums/Constants are part of extended protection:

-   [**WS\_EXTENDED\_PROTECTION\_POLICY**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_policy)
-   [**WS\_EXTENDED\_PROTECTION\_SCENARIO**](/windows/desktop/api/WebServices/ne-webservices-ws_extended_protection_scenario)

The following stuctures are part of extended protection:

-   [**WS\_SERVICE\_SECURITY\_IDENTITIES**](/windows/desktop/api/WebServices/ns-webservices-ws_service_security_identities)

 

 




