---
title: Security Overview
description: The security framework in Windows Web Services API (WWSAPI) provides Message integrity, confidentiality, replay detection and server authentication using transport security.
ms.assetid: 2681bffc-ba07-4822-b265-2bf7f95297d4
keywords:
- Security Overview Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Security Overview

The security framework in Windows Web Services API (WWSAPI) provides:

-   Message integrity, confidentiality, replay detection and server authentication using transport security.
-   Client authentication such as security token validation, certificate trust and revocation checks, etc using SOAP message security or transport security.

## The Security Programming Model

Security is associated with [communication channels](channel-layer-overview.md). Securing a channel consists of the following steps.

-   Create and initialize one or more [**security bindings**](/windows/desktop/api/WebServices/ns-webservices-ws_security_binding) appropriate for the application's security requirements.
-   Create a [**security description**](/windows/desktop/api/WebServices/ns-webservices-ws_security_description) containing those security bindings.
-   Create a [**channel**](/windows/desktop/api/WebServices/nf-webservices-wscreatechannel) or [**service proxy**](/windows/desktop/api/WebServices/nf-webservices-wscreateserviceproxy) (on the client side), or create a [**listener**](/windows/desktop/api/WebServices/nf-webservices-wscreatelistener) or [**service host**](/windows/desktop/api/WebServices/nf-webservices-wscreateservicehost) (on the server side) passing in that security description.
-   Do the normal channel programming steps of Open, Accept, Send, Receive, Close etc.

Messages sent and received on the channel are secured automatically by the runtime according the supplied security description. Optionally, these steps can be fine-tuned by specifying one or more [channel-wide security settings](security-channel-settings.md) in the security description or [binding-wide security settings](security-binding-settings.md) in a security binding.

Any required authorization of sender identities must be done by the application using the [security processing results](security-processing-results.md) attached to each received message. Authorization steps are not specified in the security description, nor are performed automatically by the runtime.

Errors in the security description, such as unsupported bindings, inapplicable properties/fields, lack of required properties/fields or invalid property/field values, will cause channel or listener creation to fail.

## Selecting Security Bindings

When designing security for an application, the primary decision is the selection of the security bindings to be included in the security description. The following are some guidelines for choosing security bindings suitable for an application's security scenario. A useful heuristic is to first understand what security credential types (such as [**X.509 certificates**](/windows/desktop/api/WebServices/ns-webservices-ws_cert_credential), [**Windows domain username/passwords**](/windows/desktop/api/WebServices/ns-webservices-ws_windows_integrated_auth_credential), [**application defined username/passwords**](/windows/desktop/api/WebServices/ns-webservices-ws_username_credential)) will be available to the application, and to then choose a security binding that can use that credential type.

-   Transport security, where security is applied at the transport byte stream level (below the SOAP message boundaries), is the first option to consider.
    -   For Internet scenarios, and for those Intranet scenarios where an X.509 certificate can be deployed at the server, the application may use [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding). The following example illustrates this option. Client: [HttpClientWithSslExample](httpclientwithsslexample.md) Server: [HttpServerWithSslExample](httpserverwithsslexample.md).

        If client authentication via HTTP header authentication is desired, a [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) can be added to provide that functionality.

    -   For Intranet scenarios where Windows Integrated Authentication protocols such as Kerberos, NTLM and SPNEGO are appropriate, the application may use [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding). The following example illustrates this option: Client: [RequestReplyTcpClientWithWindowsTransportSecurityExample](requestreplytcpclientwithwindowstransportsecurityexample.md) Server: [RequestReplyTcpServerWithWindowsTransportSecurityExample](requestreplytcpserverwithwindowstransportsecurityexample.md).

        Client over named pipes: [RequestReplyNamedPipesClientWithWindowsTransportSecurityExample](requestreplynamedpipesclientwithwindowstransportsecurityexample.md)

        Server over named pipes: [RequestReplyNamedPipesServerWithWindowsTransportSecurityExample](requestreplynamedpipesserverwithwindowstransportsecurityexample.md)

    -   For local machine scenarios where Windows Integrated Authentication protocols such as Kerberos, NTLM and SPNEGO are appropriate, the application may use [**WS\_TCP\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_tcp_sspi_transport_security_binding) or [**WS\_NAMEDPIPE\_SSPI\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_namedpipe_sspi_transport_security_binding). The[**WS\_NAMEDPIPE\_CHANNEL\_BINDING**](/windows/desktop/api/WebServices/ne-webservices-ws_channel_binding) is preferred in such scenarios because it guarantees that traffic will not leave the machine (this is the property of **WS\_NAMEDPIPE\_CHANNEL\_BINDING**).

-   Mixed-mode security, where transport security protects the connection and a WS-Security header in the SOAP message provides client authentication, is the next option to consider. The following bindings are used in conjunction with one of the transport security bindings described in the previous section.
    -   When the client is authenticated by an application-level username/password pair, the application can use a [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding) to provide the authentication data. The following examples illustrate the usage of this binding in conjunction with a [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding):
        -   Client: [HttpClientWithUsernameOverSslExample](httpclientwithusernameoversslexample.md)
        -   Server: [HttpServerWithUsernameOverSslExample](httpserverwithusernameoversslexample.md)
    -   When the client is authenticated by a Kerberos ticket, the application can use a [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) to provide the authentication data.
    -   When using a [security context](security-context.md), the client first establishes a security context with the server and then uses that context to authenticate messages. To enable this functionality, the security description must contain a [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding). Once established, security contexts can be transmitted by means of lightweight tokens, which avoids having to send the potentially large and computationally expensive client credentials with every message.
    -   In a [federated security](federation.md) scenario, the client first obtains a security token issued by a security token service (STS), and then presents the issued token to a service. Client-side: To obtain the security token from the STS, the application may use [**WsRequestSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wsrequestsecuritytoken). Alternatively, the application may use a client side security token provider library such as CardSpace or LiveID, and then use their output to locally create a security token using [**WsCreateXmlSecurityToken**](/windows/desktop/api/WebServices/nf-webservices-wscreatexmlsecuritytoken). Either way, once the security token is available to the client, it may be presented to the service using a security description containing a [**WS\_XML\_TOKEN\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_xml_token_message_security_binding). Server-side: If the security token issued by the STS is a SAML token, then the server may use a security description with a [**WS\_SAML\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_saml_message_security_binding).
        > [!Note]  
        > Windows 7 and Windows Server 2008 R2: WWSAPI only supports [Ws-Trust](http://specs.xmlsoap.org/ws/2005/02/trust/WS-Trust.pdf) and [Ws-SecureConversation](http://specs.xmlsoap.org/ws/2005/02/sc/WS-SecureConversation.pdf) as defined by [Lightweight Web Services Security Profile (LWSSP)](/openspecs/windows_protocols/ms-lwssp/376af2f8-f4fe-4577-bfd5-370ac12cac2e). For details regarding Microsoft's implementation please see the [MESSAGE Syntax](/openspecs/windows_protocols/ms-lwssp/d4f0f509-e14a-47b5-81e8-ade06a51d1ed) section of LWSSP.

         
-   The final option to consider is using authentication bindings without using a protection binding such as [**WS\_SSL\_TRANSPORT\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_ssl_transport_security_binding). This will result in the credentials being transmitted in clear text and can have security implications. The use of this option should be carefully evaluated to ensure that there are no vulnerabilities as a result. An example of a potential use is exchanging messages between back-end servers over a secure private network. The following configurations support this option.

    -   [**WS\_HTTP\_HEADER\_AUTH\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_http_header_auth_security_binding) supports this option in all configurations.
    -   [**WS\_USERNAME\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_username_message_security_binding) supports this option on the server when using HTTP as transport.
    -   [**WS\_KERBEROS\_APREQ\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_kerberos_apreq_message_security_binding) supports this option on the server when using HTTP as transport.
    -   [**WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_security_context_message_security_binding) supports this option on the server when using HTTP as transport.
    -   [**WS\_SAML\_MESSAGE\_SECURITY\_BINDING**](/windows/desktop/api/WebServices/ns-webservices-ws_saml_message_security_binding) supports this option on the server when using HTTP as transport.

    Enabling this option requires explicitly setting the [**WS\_PROTECTION\_LEVEL**](/windows/desktop/api/WebServices/ne-webservices-ws_protection_level) to a value other than **WS\_PROTECTION\_LEVEL\_SIGN\_AND\_ENCRYPT**.

## Channels and Security

As noted above, security is scoped to channels. Moreover, channel operations map to security steps consistently across all security bindings.

-   Channel create: The set of security bindings specified in the security description is validated and remains fixed for the channel thereafter. The shape of the channel stack, including any side-channels to be used for WS-Trust based negotiations, is also determined.
-   Channel open: Any credentials that are supplied as part of security bindings are loaded, and security sessions are established. In general, an open channel contains 'live' security state. Opening a client channel also specifies the server's endpoint address against which server authentication will be done by the runtime.
-   Between channel open and close: Messages can be securely sent and received during this phase.
-   Message send: Security context tokens are obtained or renewed as needed and security is applied to each transmitted message according to the security description. Errors that are encountered when applying security are returned to the application as send errors.
-   Message receive: Security is verified on each received message according to the security description. Any message security verification errors are returned to the application as receive errors. These per-message errors do not affect the channel state or subsequent receives. The application may discard a failed receive and restart a receive for another message.
-   Channel abort: The channel may be aborted at any time to halt all I/O on the channel. On abort, the channel will go into a faulted state and will not allow any more sends or receives. However, the channel may still retain some 'live' security state, so a subsequent channel close will be necessary to dispose all state cleanly.
-   Channel close: The security state created at open is disposed and sessions are torn down. Security context tokens are cancelled. The channel stack remains, but contains no 'live' security state or loaded credentials.
-   Channel free: The channel stack built at create, together with all security resources, are freed.

## Security APIs

The API documentation for security is grouped into the following topics.

-   [Security Description](security-description.md)
    -   [Security Channel Settings](security-channel-settings.md)
    -   [Security Bindings](security-bindings.md)
        -   [Security Credentials](security-credentials.md)
        -   [Security Binding Settings](security-binding-settings.md)
-   [Federation](federation.md)
-   [Security Context](security-context.md)
-   [Endpoint Identity](endpoint-identity.md)
-   [Security Processing Results](security-processing-results.md)

## Security

When using the WWSAPI Security API, applications face several security risks:

<dl> <dt>

<span id="Accidental_misconfiguration"></span><span id="accidental_misconfiguration"></span><span id="ACCIDENTAL_MISCONFIGURATION"></span>Accidental misconfiguration
</dt> <dd>

WWSAPI supports a range of security-related configuration options. See for example [**WS\_SECURITY\_BINDING\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_property_id). Some of these options, such as **WS\_SECURITY\_BINDING\_PROPERTY\_ALLOW\_ANONYMOUS\_CLIENTS** allow the application to lower the default level of security provided by the various Security Bindings. The use of such options should be carefully evaluated to ensure that there are no resulting attack vectors.

Additionally, as described above, WWSAPI allows an application to deliberately disable certain steps required to fully secure a message exchange, such as allowing to disable encryption even though security credentials are transmitted. This is allowed to enable certain specific scenarios and should not be used for general communication. The [**WS\_PROTECTION\_LEVEL**](/windows/desktop/api/WebServices/ne-webservices-ws_protection_level) must be specifically lowered to enable this scenarios, and applications should not change that value unless absolutely necessary, as doing so will disable many checks that are designed to ensure a secure configuration.

</dd> <dt>

<span id="Storing_confidential_information_in_memory"></span><span id="storing_confidential_information_in_memory"></span><span id="STORING_CONFIDENTIAL_INFORMATION_IN_MEMORY"></span>Storing confidential information in memory
</dt> <dd>

Confidential information, such as passwords, that is stored in memory is vulnerable to being extracted by a privileged attacker by means of, for example, the page file. WWSAPI makes a copy of provided credentials and encrypts that copy, leaving the original data unprotected. It is the application's responsibility to protect the original instance. Additionally, the encrypted copy is briefly decrypted while being used, opening up a window to extract it.

</dd> <dt>

<span id="Denial_of_service"></span><span id="denial_of_service"></span><span id="DENIAL_OF_SERVICE"></span>Denial of service
</dt> <dd>

Security processing can consume significant resources. Every additional security binding increases those costs. WWSAPI aborts security processing as soon as a security verification failure is encountered, but certain checks such as authorization decisions may not take place until after significant work has been performed.

While a message is processed on the server, security state is stored on the message heap. The application can limit the memory consumption during security processing by reducing the size of that heap through WS\_MESSAGE\_PROPERTY\_HEAP\_PROPERTIES. Additionally, certain security bindings such as the WS\_SECURITY\_CONTEXT\_MESSAGE\_SECURITY\_BINDING can cause the server to allocate resources on behalf of the client. The limits for those resources can be configured by way of the following [**WS\_SECURITY\_BINDING\_PROPERTY\_ID**](/windows/desktop/api/WebServices/ne-webservices-ws_security_binding_property_id) values:

-   WS\_SECURITY\_BINDING\_PROPERTY\_SECURITY\_CONTEXT\_MAX\_PENDING\_CONTEXTS
-   WS\_SECURITY\_BINDING\_PROPERTY\_SECURITY\_CONTEXT\_MAX\_ACTIVE\_CONTEXTS
-   WS\_SECURITY\_BINDING\_PROPERTY\_SECURITY\_CONTEXT\_RENEWAL\_INTERVAL
-   WS\_SECURITY\_BINDING\_PROPERTY\_SECURITY\_CONTEXT\_ROLLOVER\_INTERVAL

Setting those limits to low values reduces the maximum memory consumption but can lead to legitimate clients being rejected when the quota is reached.

</dd> </dl>

 

 