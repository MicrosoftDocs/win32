---
description: When developing an application that uses Microsoft Windows HTTP Services (WinHTTP), it is important to understand the following concepts and terminology that relate to networking in general and the HTTP protocol in particular.
ms.assetid: 6ea0c16f-1233-4580-97bb-14e224646857
title: Network Terminology (WinHTTP)
ms.topic: article
ms.date: 05/31/2018
---

# Network Terminology (WinHTTP)

When developing an application that uses Microsoft Windows HTTP Services (WinHTTP), it is important to understand the following concepts and terminology that relate to networking in general and the HTTP protocol in particular.

-   [HTTP Transactions](#http-transactions)
-   [Proxy Servers](#proxy-servers)
-   [Synchronous and Asynchronous Modes](#synchronous-and-asynchronous-modes)
-   [Authentication](#authentication)

## HTTP Transactions

When you work with HTTP transactions, you are exchanging information with another computer elsewhere on a network. The information exchanged can be a file that contains text or multimedia, or it can be the results of a database query. A piece of information exchanged over a network is called a *resource*. Normally the computer that sends a resource is the server and the computer that receives that resource is a client. However, it is also possible for a client to post data to a server. Sometimes an HTTP transaction involves a middle-tier server. A middle-tier server gathers several resources from other servers, compiles the information into one resource, and sends that resource to the client.

The process of obtaining a resource using the HTTP protocol requires that a series of messages be exchanged between the client and the server. The client begins the transaction by sending a message that requests a resource. This message is called an HTTP request, or sometimes just a request. An HTTP request consists of the following components.

-   Method, Uniform Resource Identifier (URI), protocol version number
-   Headers
-   Entity body

When a server receives a request, it responds by sending a message back to the client. The message sent by the server is called an HTTP response. An HTTP response consists of the following components.

-   Protocol version number, status code, status text
-   Headers
-   Entity body

The response either indicates that the request cannot be processed, or provides requested information. Depending on the type of request, this can be information about a resource, such as its size and type, or can be some or all of the resource itself. The part of a response that includes some or all of the requested resource is called the "response data" or the "entity body,' and the response is not complete until all the response data is received.

For detailed information on HTTP transactions and the HTTP protocol, see [RFC 2616](https://www.ietf.org/rfc/rfc2616.txt), Hypertext Transfer Protocol — HTTP/1.1.

## Proxy Servers

Although a request sent by a client is eventually received by the target server, sometimes the transaction first passes through a proxy server. A proxy intercepts the request, and can even modify the request, before sending it on to the server. When the server responds, the response also passes through the proxy before it is forwarded on to the client. The proxy can modify the headers in this response.

By intercepting and translating network transactions, a proxy can:

-   Protect the client by monitoring potentially dangerous transactions.
-   Enable the client to communicate using protocols that might not be implemented by the client software.
-   Act as a gateway between a private network and a public network.

The WinHTTP API includes a proxy configuration tool that enables you to provide WinHTTP with information regarding any proxy servers that intercept your HTTP transactions. For information on using the proxy configuration tool, see [ProxyCfg.exe, a Proxy Configuration Tool](proxycfg-exe--a-proxy-configuration-tool.md).

## Synchronous and Asynchronous Modes

There are two programming models for obtaining resources over a network using WinHTTP—the synchronous and asynchronous models. In a synchronous model, a call to a function or method does not finish until the requested operation is complete or until an error occurs. For example, when your application requests a resource using WinHTTP synchronously, it does not continue with the next step until the requested data has been received.

An asynchronous model, on the other hand, allows an application to perform other tasks while it waits for the resource to be retrieved. If another WinHTTP function or method is called and a previous operation has not finished, the function returns an error. When using WinHTTP asynchronously, Component Object Model (COM) events and callback are available to notify an application of progress in an HTTP operation.

## Authentication

Authentication is the process by which an HTTP proxy or HTTP server validates a user's login information before it allows access to resources. Various authentication schemes are used on the Internet. Usually a user's name and password are compared against an authorized list, and if the system detects a match, access is granted to the extent specified in the permission list for the user.

WinHTTP functions support both server and proxy authentication for HTTP sessions. WinHTTP supports the following authentication schemes: Basic, Digest (see [RFC 2617](https://www.ietf.org/rfc/rfc2617.txt)), [NTLM Authentication](../com/ntlmssp.md), Negotiate/ [Kerberos](../com/kerberos-v5-protocol.md), and Microsoft Passport 1.4. For detailed information on authentication, as well as an example of using authentication in a Microsoft Visual C++ application, see [Authentication in WinHTTP](authentication-in-winhttp.md).

For information about security considerations regarding Basic and Passport authentication, see [WinHTTP Security Considerations](winhttp-security-considerations.md).

 

 
