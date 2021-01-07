---
description: Microsoft Internet Explorer supports using IPv6 to connect and access IPv6-enabled sites (web servers and FTP servers, for example) when the following circumstances are met:The host machine running Internet Explorer must have IPv6 installed and enabled.When connecting to a host that is outside of the local subnet, the interface that provides the connectivity must have a routable IPv6 address assigned.When connecting to the IPv6 loopback address (::1) or to a link-local destination, a routable IPv6 address is not required.If the requested URL contains a name (www.contoso.com, for example), the Domain Name System (DNS) query for that name must return one or more IPv6 addresses.If the requested URL contains an IPv6 address (::1, for example), the IPv6 address must be surrounded by square brackets (https://\[::1\]). Scope IDs, sometimes called zone indexes, are supported as part of the IPv6 address. The scope ID is used to determine which network interface to use when sending the request on computers with multiple network interfaces. The scope ID is specified using the '%' character after the main IPv6 address (fe80::1%11, for example). However, the '%' character must be escaped in the URL used with Internet Explorer. For example, scope ID 11 on a link-local address would be specified as https://\[fe80::1%2511\] when using Internet Explorer. This ability to use IPv6 addresses in a URL is supported on Internet Explorer 7 and later.
ms.assetid: c3a8303a-50d6-4deb-a371-171ac0a7c5a9
title: Using Internet Explorer to Access IPv6 Websites
ms.topic: article
ms.date: 05/31/2018
---

# Using Internet Explorer to Access IPv6 Websites

Microsoft Internet Explorer supports using IPv6 to connect and access IPv6-enabled sites (web servers and FTP servers, for example) when the following circumstances are met:

-   The host machine running Internet Explorer must have IPv6 installed and enabled.
    -   When connecting to a host that is outside of the local subnet, the interface that provides the connectivity must have a routable IPv6 address assigned.
    -   When connecting to the IPv6 loopback address (::1) or to a link-local destination, a routable IPv6 address is not required.
-   If the requested URL contains a name (www.contoso.com, for example), the Domain Name System (DNS) query for that name must return one or more IPv6 addresses.
-   If the requested URL contains an IPv6 address (::1, for example), the IPv6 address must be surrounded by square brackets (https://\[::1\]). Scope IDs, sometimes called zone indexes, are supported as part of the IPv6 address. The scope ID is used to determine which network interface to use when sending the request on computers with multiple network interfaces. The scope ID is specified using the '%' character after the main IPv6 address (fe80::1%11, for example). However, the '%' character must be escaped in the URL used with Internet Explorer. For example, scope ID 11 on a link-local address would be specified as https://\[fe80::1%2511\] when using Internet Explorer. This ability to use IPv6 addresses in a URL is supported on Internet Explorer 7 and later.

> [!Note]  
> If Internet Explorer is configured to use a proxy server, the proxy server must have an IPv6 address assigned and the proxy server must able to proxy IPv6 addresses. The proxy server would be used to connect to an external host using IPv6. The proxy server would normally be bypassed for the IPv6 loopback address and IPv6 link-local addresses.

 

 

 



