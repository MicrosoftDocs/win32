---
title: Authentication (HTTP Server API)
description: Starting with version 2.0, the HTTP Server API performs server side authentication for the application.
ms.assetid: e8e41e8e-1b10-4747-b18e-763e0752ade4
ms.topic: article
ms.date: 05/31/2018
---

# Authentication (HTTP Server API)

Some server applications require client authentication to access resources and service HTTP requests. Starting with version 2.0, the HTTP Server API performs server side authentication for the application. In the HTTP Server API version 1.0, the server application had to implement its own authentication. Some advantages of authentication performed by the HTTP Server API include:

-   Applications can run under low privileges, thus reducing security risks.
-   Authentication is performed in kernel mode, thus reducing transitions from user mode to kernel mode during authentication.
-   Authentication performed in kernel mode allows server applications to run on different user accounts. In version 1.0, all applications on the machine must run under the same user account to authenticate on the Service Principle Name (SPN).
-   The NTLM authentication handshake is not reset if a worker process is recycled while the handshake is in process.

To take advantage of the version 2.0 authentication, the application enables the authentication schemes that the HTTP Server API applies to the URLs for which the application has registered. Authentication can be enabled on the server session or URL group. The URL group inherits the authentication schemes enabled by the server session if none are set on the URL group. The HTTP Server API supports the following schemes:

-   Negotiate
-   NTLM
-   Digest
-   Basic

The server application can also implement authentication schemes not supported by the HTTP Server API. The HTTP Server API sends requests to the application for authentication schemes that are not supported, or for schemes that have not been enabled by the application.

### Enabling Authentication

The server application enables and configures authentication on the server session or URL group with the [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty) or [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty) functions as follows:

1.  The application enables authentication by specifying **HttpServerAuthenticationProperty** in the *Property* parameter of [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty) or [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty).
2.  The application specifies the configuration parameters in the [**HTTP\_SERVER\_AUTHENTICATION\_INFO**](/windows/desktop/api/Http/ns-http-http_server_authentication_info) structure in the *pPropertyInformation* parameter of [**HttpSetServerSessionProperty**](/windows/desktop/api/Http/nf-http-httpsetserversessionproperty) or [**HttpSetUrlGroupProperty**](/windows/desktop/api/Http/nf-http-httpseturlgroupproperty). The application specifies the authentication schemes enabled, whether NTLM credential caching is disabled, and supplies the Basic and Digest parameters in the **HTTP\_SERVER\_AUTHENTICATION\_INFO** structure.

### Authentication Procedure

To initiate HTTP Server authentication, the application enables the authentication property before the first request arrives on the request queue. The following steps are the common processing flow for authenticating a request.

1.  The application enables authentication. See the preceding "Enabling Authentication" section.
    > [!Note]  
    > The client sends an unauthenticated request. The HTTP Server API passes the request to the server application and allows it to generate the initial 401 challenge. The HTTP Server API includes the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure embedded with the [**HTTP\_REQUEST**](/previous-versions/windows/desktop/legacy/aa364545(v=vs.85)) structure. The **AuthStatus** member indicates **HttpAuthStatusNotAuthenticated**

     

2.  The application examines the **AuthStatus** member of the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure to determine if the request has been authenticated. If the request has not been authenticated, the application can service the request as anonymous or send an initial 401 authentication challenge.
3.  If the application services the request as anonymous, it handles the request and sends the final response to the client application, just as if the authentication was not involved.
4.  If instead the application requires authentication, it sends the initial 401 challenge with one or more WWW-Authenticate headers indicating the available schemes to the client. The application should use the [**HTTP\_MULTIPLE\_KNOWN\_HEADERS**](/windows/desktop/api/Http/ns-http-http_multiple_known_headers) structure to build the required set of headers when more than one authentication header is sent in the response.
    > [!Note]
    >
    > The client resends the request with the authorization header for a scheme selected from the set of available schemes indicated by the server application in initial 401 response.
    >
    > The HTTP Server API examines the authorization request authorization header to determine if the scheme is enabled. If it is, then the HTTP Server API performs authentication and handles all interim request/401-response exchanges, until the authentication handshake is finalized.
    >
    > When The HTTP Server API completes the authentication attempt, it sends the request to the application with the results of the authentication attempt in the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure that is returned with the request. If the authentication attempt fails for one of the following reasons, the HTTP Server API does not pass the request to the application:
    >
    > -   If the authentication handshake fails due to an internal HTTP Server API error such as a memory allocation failure, the HTTP Server API generates a 503 (service unavailable) response and sends back to client.
    > -   If a malformed authorization header such as a header without a scheme name, or malformed Base64 encoding of client credentials encountered, the HTTP Server API generates a 400 (bad request) response and sends back to client.

     

5.  The server application examines the **AuthStatus** member of the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure to determine if authentication was successful. When authentication fails, the HTTP Server API includes the error returned from [AcceptSecurityContext](/previous-versions/windows/embedded/ms937012(v=msdn.10)) in the **SecStatus** member of the **HTTP\_REQUEST\_AUTH\_INFO** structure. If the authentication attempt fails due to bad credentials, the application can generate another 401 challenge with the desired WWW-Authenticate header, or may decided to service the request as anonymous.
6.  If authentication was successful, the application uses the token provided in the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure to impersonate the client and to access resources. The access token handle returned to the application is valid as long as the request ID is valid, which is typically until the application completes the response to the request. The token may, however, expire during this period and the application may need to send another 401 challenge to the client.
7.  The application sends the final 200 OK response, and it must close the handle to the access token.
    > [!Note]  
    > The HTTP Server API appends the mutual authentication data to the final 200 OK response, if one was generated during the authentication handshake.

     

### NTLM NULL Sessions

Note that an NTLM NULL session indicated in the final security context, is not treated as authenticated. In this case, the request is sent to the application with an HttpAuthStatusFailure error in the [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure and the application can send another 401 challenge.

### Preemptive Authentication

According to the HTTP protocol, after the client has established authentication for a resource, it can preemptively send the corresponding authorization header with subsequent consecutive requests for the resource without waiting for a 401 challenge from the server. If the scheme indicated in the Authorization header is still enabled by the application and supported by the HTTP Server API, the HTTP Server attempts authentication without sending the request to the application. When this type of authenticated request is received by the application, it can choose to discard the request and regenerate the initial 401 challenge or service the request as authenticated.

### Mutual Authentication

Mutual authentication data is generated when the negotiate scheme is used during handshake and it is resolved to Kerberos, and client has asked for mutual authentication. The mutual authentication data is automatically inserted by HTTP Server API in the final 200 OK response sent by the server application. By default HTTP Server API does not pass the Mutual authentication data to the server application, since it automatically handles the sending of it. However, if server application enables the ReceiveMutualAuth flag in the [**HTTP\_SERVER\_AUTHENTICATION\_INFO**](/windows/desktop/api/Http/ns-http-http_server_authentication_info) structure in configuration, the mutual authentication data is passed to the application in [**HTTP\_REQUEST\_AUTH\_INFO**](/windows/desktop/api/Http/ns-http-http_request_auth_info) structure embedded with the authenticated [**HTTP\_REQUEST**](/previous-versions/windows/desktop/legacy/aa364545(v=vs.85)). In this case application should send the mutual authentication data with the final 200 OK response. In the case where multiple sites are served by a single computer, all sites on the computer use the credentials for the Local Machine Account in the domain for mutual authentication.

 

 
