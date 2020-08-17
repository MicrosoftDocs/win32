---
title: Proxy Servers and WinRM
description: Windows Remote Management (WinRM) uses HTTP and HTTPS to send messages between the client and server computers. In general, the WinRM client sends messages directly to the WinRM server. WinRM clients can be also configured to use a proxy server.
ms.assetid: f8137b3a-7704-4b21-a923-6e2692e18d90
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Proxy Servers and WinRM

Windows Remote Management (WinRM) uses HTTP and HTTPS to send messages between the client and server computers. In general, the WinRM client sends messages directly to the WinRM server. WinRM clients can be also configured to use a proxy server.

For more information, see the following sections:

-   [Configuring a Proxy Server for WinRM 2.0](#configuring-a-proxy-server-for-winrm-20)
    -   [HTTPS-Based Proxy Connections](#https-based-proxy-connections)
    -   [HTTP-Based Proxy Connections](#http-based-proxy-connections)
-   [Configuring a Proxy Server for WinRM 1.1 and Earlier](#configuring-a-proxy-server-for-winrm-11-and-earlier)

## Configuring a Proxy Server for WinRM 2.0

WinRM 2.0 supports a wide range of proxy configurations. For example, WinRM supports proxies for HTTP and HTTPS transports and for authenticated and unauthenticated proxy servers.

### HTTPS-Based Proxy Connections

For better security and connection-based affinity, HTTPS should be used as the transport mechanism.

If the proxy server requires authentication, the WinRM clients and servers must use HTTPS.

> [!Note]  
> Authentication to the proxy server is independent from the authentication to the destination server.

 

### HTTP-Based Proxy Connections

If no proxy server authentication is required, either HTTP or HTTPs can be used for transport. However, HTTP-based connections from a WinRM client to a WinRM server through a proxy server can be problematic.

The following issues might be encountered when using HTTP-based connections:

-   The proxy server does not support connection-based authentication, which can cause the authentication against the destination server to fail with an access denied error.
-   More than one set of credentials is needed to connect to the destination server and to the proxy server.
-   HTTP-based proxy servers might not support the ability to maintain the associated client-based and server-based connections. If the proxy does not strongly link a client to a server and maintain the TCP/IP connection, unauthenticated clients might gain access to data. Also, the lack of connection affinity might cause the authentication to fail against the server.

If HTTP must be used as the transport, the proxy server should support the following configuration to achieve a better WinRM response and to prevent access denied failures for WinRM clients:

-   Support for HTTP/1.1. HTTP/1.1 is more stringent in mapping connection affinity between client and server.
-   Connection-based authentication for Negotiate, Kerberos, and CredSSP authentication.

    Authentication of a request requires multiple round-trips between the client and server. Most negotiation for authentication is complete after the authenticating (WinRM) server sends a response to the client that is not a 401 response (Unauthorized). If the WinRM server returns a response to the client that is not a 401 response, the proxy should not close the connection.

    Multiple request/response pairs can be sent between client and server before the actual packet data is sent. WinRM 2.0 uses the Negotiate and Kerberos authentication schemes with encryption, which can add extra round-trips. Data cannot be sent to the server until the authentication is complete.

    The WinRM server returns a 200-level response that indicates that the authentication is complete. HTTP-based proxy servers might end the connection-based authentication affinity and close the TCP/IP connection after receiving the 200-level response from the WinRM server. The final round-trip from client to server does not include the original request packet. If the proxy server closes the connection, the server will attempt to re-authenticate the client and the client request might never be sent to the server. If the connection-based affinity is not maintained, authentication against the destination server can fail with an access denied error.

-   Connection persistence. The client TCP/IP connection to the proxy should continue to map to the same TCP/IP connection from the proxy to the server. Maintaining this connection helps to achieve a higher level of performance. If the connection is not maintained, every request must be re-authenticated, which might affect performance.

### Encryption and WinRM 2.0

WinRM 2.0 supports encryption over HTTP by using the Negotiate, Kerberos, and CredSSP authentication schemes. If a WinRM server supports HTTP and is accessed through a proxy, the WinRM server must enforce encryption and not allow unencrypted network traffic.

Under no circumstances should unencrypted HTTP requests be sent through proxy servers. When data must pass through a proxy server before being sent to the destination server, the following security issues are very important:

-   It is possible that a malicious proxy server could examine every request/response pair, including credentials.
-   If the TCP/IP connections are not strongly mapped between both the WinRM client and the proxy server and between the proxy server and the destination server, an unauthorized client could connect to the destination server by using the same authenticated connection from the proxy server to the destination server. The destination server might allow the unauthenticated client access to data. If encryption is enforced, the destination server sends an access denied message to the unauthenticated client.

Using encryption would mitigate these potential security issues.

## Configuring a Proxy Server for WinRM 1.1 and Earlier

If a proxy is required to reach the WinRM server, the WinRM client relies on the Windows HTTP services (WinHTTP) proxy configuration. By default, WinHTTP is not configured to use a proxy server. WinHTTP proxy configuration can be changed by using the [ProxyCfg.exe](/previous-versions/windows/desktop/ms761351(v=vs.85)) or [netsh](/previous-versions/windows/it-pro/windows-server-2003/cc785383(v=ws.10)) command-line utilities.

**WinRM 1.1 and Earlier:** WinRM does not use the Internet Explorer proxy settings.

 

 