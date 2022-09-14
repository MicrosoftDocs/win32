---
title: IP Version 6 Support
description: Starting with IE7 and above, WinINet supports IPv6 literals in the hostname, and the authority component of the URI.
ms.assetid: cbbb9f93-15b0-4017-ac39-8a396203532e
keywords:
- IP Version 6 Support
ms.topic: article
ms.date: 05/31/2018
---

# IP Version 6 Support

Starting with IE7 and above, WinINet supports IPv6 literals in the hostname, and the authority component of the URI. WinINet also supports the use of IPv6 literals in relevant portions of the HTTP protocol, such as in the Location header.

## Hostname IPv6 Literals and URI Components

WinINet implements IPv6 literals according to the specifications in RFC 3513. As specified in this RFC, IPv6 literals in a URI must be enclosed in brackets. For example, https://\[::1\]/ is a valid IPv6 URI; the form without brackets (https://::1/) is not valid. Hostname IPv6 literals that are not part of the URI, however, do not need to be enclosed in the brackets; either form is acceptable to WinINet. For example, both "::1" and "\[::1\]" are acceptable forms of IPv6 hostname literals. Other APIs, such as the WinSock API, will also accept both forms. Thus applications should be prepared to handle both forms of IPv6 hostname literals.

## Scope ID

The IPv6 literal address in the URI may include a scope ID. A scope ID can be an interface ID such as \[FE80::1%1\]. The URI standard, documented in RFC 3986, does not define the syntax for the scope ID, and the URI is considered non-uniform when the scope ID is present. However, WinINet accepts a scope ID in the authority component of the URI, and in the hostname IPv6 literal.

The percent character (%) in the IPv6 literal address must be percent escaped when present in the URI. For example, the scope ID FE80::2%3, must appear in the URI as "https://\[FE80::2%253\]/", where %25 is the hex encoded percent character (%). If the application retrieves the URI from a Unicode API, such as the Winsock [**WSAAddressToString**](/windows/desktop/api/winsock2/nf-winsock2-wsaaddresstostringa) API, the application must add the escaped version of the percent character (%) in the hostname of the URI. To create the escaped version of the URI, applications call [**InternetCreateUrl**](/windows/desktop/api/Wininet/nf-wininet-internetcreateurla) with the *dwFlags* parameter set to **ICU\_ESCAPE\_AUTHORITY**, and the IPv6 hostname specified in the URL components structure specified in the *lpUrlComponents* parameter.

For all sockets operations, WinINet uses the scope ID. However, because the scope ID has only local host significance, it is not sent as part of the HTTP protocol headers in the request. For example, the call to [**InternetOpenUrl**](/windows/desktop/api/Wininet/nf-wininet-internetopenurla) is called with the following URL in the *lpszUrl* parameter.

``` syntax
https://[fec0::2%251]:80/path.htm
```

The scope ID portion of the URL is removed by WinINet when the HTTP request is sent for this URL. The request contains the following headers:

``` syntax
GET path.htm HTTP/1.1
Host: [fec0::2]
```

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

 

 