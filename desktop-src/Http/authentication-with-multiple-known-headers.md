---
title: Authentication with Multiple Known Headers
description: The HTTP\_MULTIPLE\_KNOWN\_HEADERS structure enables server applications to send multiple authentication challenges to the client.
ms.assetid: d517fd61-9547-4e1c-b0fd-1eb3d0098db2
ms.topic: article
ms.date: 05/31/2018
---

# Authentication with Multiple Known Headers

The [**HTTP\_MULTIPLE\_KNOWN\_HEADERS**](/windows/desktop/api/Http/ns-http-http_multiple_known_headers) structure enables server applications to send multiple authentication challenges to the client. Applications can challenge the client with a single authentication scheme by supplying the **HttpHeaderWwwAuthenticate** enumeration type in the **KnownHeaders** member of the [**HTTP\_RESPONSE\_HEADERS**](/windows/desktop/api/Http/ns-http-http_response_headers) structure contained in [**HTTP\_RESPONSE**](http-response.md). However, when the server challenges with multiple authentication schemes, the application uses the [**HTTP\_MULTIPLE\_KNOWN\_HEADERS**](/windows/desktop/api/Http/ns-http-http_multiple_known_headers) structure to provide the authentication types.

When the **HTTP\_RESPONSE\_INFO\_FLAGS\_PRESERVE\_ORDER** flag is present, HTTP sends the authentication headers in the specified order. If the flag is not present, HTTP orders the authentication schemes from strongest to weakest as follows:

1.  Negotiate
2.  NTLM
3.  Digest
4.  Basic

If the authentication scheme is not one of these schemes, the application must specify the **HTTP\_RESPONSE\_INFO\_FLAGS\_PRESERVE\_ORDER** flag.

The **KnownHeader** member of [**HTTP\_MULTIPLE\_KNOWN\_HEADERS**](/windows/desktop/api/Http/ns-http-http_multiple_known_headers) points to an array of [**HTTP\_KNOWN\_HEADER**](/windows/desktop/api/Http/ns-http-http_known_header) structures. The **pRawValue** member of the **HTTP\_KNOWN\_HEADER** structure must point to a string that specifies the scheme name. HTTP parses the string to determine the scheme and performs one of the following actions:

-   If the string contains an unknown authentication type, or if the authentication type is not enabled on the configuration group (either the URL group or server session) associated with the request, the HTTP Server API appends the string in **pRawValue** to the WWW-Authenticate header. For example, if the application specifies an unsupported authentication scheme, and **pRawValue** contains the string "CustomAuthString", the following text is appended to the authentication header:

    WWW-Authenticate: CustomAuthSchemeCRLF

    If the application does not have Basic authentication enabled, and **pRawValue** contains the string "Basic realm="BasicRealm"", the authentication header contains the following text:

    WWW-Authenticate: Basic realm="BasicRealm"

-   If the string contains a known authentication type and is present on the configuration group (either the URL group or the server session) associated with the request, the HTTP Server API generates the WWW-Authenticate header. For example if the string specified in **pRawValue** is "Digest", and Digest is enabled on the server session, the HTTP Server API appends the following text to the authentication header:

    WWW-Authenticate: Digest realm="testrealm@host.com"

If the scheme in the **pRawValue** member of [**HTTP\_KNOWN\_HEADER**](/windows/desktop/api/Http/ns-http-http_known_header) is Negotiate or NTLM, the authentication scheme name is sufficient. If the specified scheme is Basic, the realm name is appended to the scheme name; the application doesn't need to supply the realm name in **pRawValue**. If the specified scheme is Digest, HTTP calls [**AcceptSecurityContext**](../SecAuthN/acceptsecuritycontext--general.md) to generate the challenge that is appended to the scheme name. The parameters for Basic (realm) and Digest (realm and domain name) scheme are obtained from the corresponding configuration group authentication information.

When the application sends multiple authentication challenges to the client in Unknown request headers, the HTTP Server API sends these to the client without intervention. However this usage is not recommended.

 

 




