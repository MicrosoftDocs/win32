---
Description: 'The secure socket extensions to Winsock allow a socket application to control the security of their traffic over a network.'
ms.assetid: '023a9f96-814f-40c3-a186-ae0a0c9baef2'
title: Winsock Secure Socket Extensions
---

# Winsock Secure Socket Extensions

The secure socket extensions to Winsock allow a socket application to control the security of their traffic over a network. These extensions allow an application to provide security policy and requirements for their network traffic, and query the security settings applied. For example, an application can use these extensions to query the peer security token that can be used to perform application level access checks.

The secure socket extensions are intended to integrate the services provided by IPsec and other security protocols with the Winsock framework. Prior to Windows Vista, on Windows Server 2003 and Windows XP, IPsec has been configured by an administrator via local and domain policies. On Windows Vista, the secure socket extensions instead allow applications to entirely or partially configure and control the security of their network traffic at the socket level.

Applications can already secure network traffic by using public APIs, such as IPsec management, Windows Filtering Platform and Security Support Provider Interface (SSPI). However, using these APIs may make the application more difficult to develop, and may make it more difficult to configure and deploy. The Winsock secure socket extensions have been designed to simplify the development of network applications that require secure network traffic by letting Winsock handle most of the complexity.

These secure socket extensions are available on Windows Vista and later.

## Secure Socket Functions

The secure socket extension functions are as follows:

-   [**WSADeleteSocketPeerTargetName**](wsadeletesocketpeertargetname.md)
-   [**WSAImpersonateSocketPeer**](wsaimpersonatesocketpeer.md)
-   [**WSAQuerySocketSecurity**](wsaquerysocketsecurity.md)
-   [**WSARevertImpersonation**](wsarevertimpersonation.md)
-   [**WSASetSocketPeerTargetName**](wsasetsocketpeertargetname.md)
-   [**WSASetSocketSecurity**](wsasetsocketsecurity.md)

> [!Note]  
> The secure socket functions currently support only the IPsec protocol and are available on Windows Vista and later.

 

The structures and enumerations used by the secure socket functions are as follows:

-   [**SOCKET\_PEER\_TARGET\_NAME**](socket-peer-target-name.md)
-   [**SOCKET\_SECURITY\_PROTOCOL**](socket-security-protocol.md)
-   [**SOCKET\_SECURITY\_QUERY\_INFO**](socket-security-query-info.md)
-   [**SOCKET\_SECURITY\_QUERY\_TEMPLATE**](socket-security-query-template.md)
-   [**SOCKET\_SECURITY\_SETTINGS**](socket-security-settings.md)
-   [**SOCKET\_SECURITY\_SETTINGS\_IPSEC**](socket-security-settings-ipsec.md)

The secure socket functions are simple to use for normal applications and are flexible enough for applications that need a high degree of control over their security. These functions make it possible to keep the underlying security mechanism hidden from the application. An application can specify generic security requirements and let the administrator control the security protocol that is used to support the requirements. While it is possible to extend these functions to add other security protocols, currently only IPsec integrates with the secure socket functions.

The [**WSASetSocketSecurity**](wsasetsocketsecurity.md) function allows an application to enable security and apply security settings before a connection is established.

The [**WSASetSocketPeerTargetName**](wsasetsocketpeertargetname.md) function allows an application to specify the target name corresponding to a peer entity. The selected security protocol will use this information when authenticating the peer. This feature addresses concerns about trusted man-in-the-middle attacks.

The [**WSADeleteSocketPeerTargetName**](wsadeletesocketpeertargetname.md) function is used to delete a previously specified peer name for a socket.

After a connection is established, the [**WSAQuerySocketSecurity**](wsaquerysocketsecurity.md) function allows an application to query the security properties of the connection, which can include the peer access or computer access token.

After a connection is established, the [**WSAImpersonateSocketPeer**](wsaimpersonatesocketpeer.md) function allows an application to impersonate the security principal corresponding to a socket peer in order to perform application-level authorization.

The [**WSARevertImpersonation**](wsarevertimpersonation.md) allows an application to terminate the impersonation of a socket peer.

## Secure Socket Architecture

![basic architecture of the winsock secure socket extensions](images/ss-arch.png)

-   An application calls the secure socket functions to set or query security settings for a socket.
-   The secure socket functions are a set of type-safe extension functions that wrap calls to the [**WSAIoctl**](wsaioctl-2.md) function using newly-defined values for the *dwIoControlCode* parameter available on Windows Vista and later. These IOCTLs are handled by the network stack.
-   The network stack will direct the call to [Application Layer Enforcement (ALE)](fwp.application_layer_enforcement__ale_) along with the endpoint handle. For the [**WSADeleteSocketPeerTargetName**](wsadeletesocketpeertargetname.md), [**WSASetSocketPeerTargetName**](wsasetsocketpeertargetname.md), and [**WSASetSocketSecurity**](wsasetsocketsecurity.md) functions, ALE will configure the application's settings on the local endpoint. For the [**WSAQuerySocketSecurity**](wsaquerysocketsecurity.md) function, ALE will read the requested information from applicable local and remote endpoints.
-   Based on socket events, Application Layer Enforcement (ALE) enforces policies for the secure socket architecture using the Windows Filtering Platform. For more information, see [About Windows Filtering Platform](fwp.about_windows_filtering_platform) and [Application Layer Enforcement (ALE)](fwp.application_layer_enforcement__ale_).

## Related topics

<dl> <dt>

[About Windows Filtering Platform](fwp.about_windows_filtering_platform)
</dt> <dt>

[Advanced Winsock Samples Using Secure Socket Extensions](advanced-winsock-samples-using-secure-socket-extensions.md)
</dt> <dt>

[Application Layer Enforcement (ALE)](fwp.application_layer_enforcement__ale_)
</dt> <dt>

[IPsec Configuration](fwp.ipsec_configuration)
</dt> <dt>

[IPsec Functions](fwp.fwp_ipsec_functions)
</dt> <dt>

[Secure Winsock Programming](secure-winsock-programming.md)
</dt> <dt>

[Security Support Provider Interface (SSPI)](rpc.security_support_provider_interface_sspi_)
</dt> <dt>

[Using Secure Socket Extensions](using-secure-socket-extensions.md)
</dt> <dt>

[Windows Filtering Platform](fwp.windows_firewall_start_page)
</dt> <dt>

[Windows Filtering Platform API Functions](fwp.fwp_functions)
</dt> </dl>

 

 



