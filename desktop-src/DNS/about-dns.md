---
title: About DNS
description: Domain Name System (DNS) is an industry-standard protocol used to locate computers on an IP-based network. Users can remember display names, such as www.microsoft.com easier than number-based addresses, such as 207.46.131.137.
ms.assetid: 3a899ba4-4338-4119-aa68-a969d196c4f5
keywords:
- About Domain Name System DNS
- Domain Name System DNS , about
- Domain Name System DNS , described
ms.topic: article
ms.date: 05/31/2018
---

# About DNS

Domain Name System (DNS) is an industry-standard protocol used to locate computers on an IP-based network. Users can remember display names, such as `www.microsoft.com` easier than number-based addresses, such as 207.46.131.137.

IP networks, such as the Internet and Windows networks, rely on number-based addresses to transmit data throughout the network; therefore, it is necessary to translate display names (such as `www.microsoft.com`) into numeric addresses that the network can recognize (such as 207.46.131.137). DNS is the service of choice in Windows to locate such resources and translate them into IP addresses.

DNS is the primary locator service for Active Directory, and therefore, DNS can be considered a base service for both Windows and Active Directory. Windows provides functions that enable application programmers to use DNS functions such as programmatically making DNS queries, comparing records, and looking up names.

Many DNS functions are actually function types, in that there is a base name for the function, but its use depends on character encoding. For example, the [**DnsQuery**](/windows/desktop/api/Windns/nf-windns-dnsquery_a) function is listed in the function reference of the DNS Application Programming Interface (API) as **DnsQuery**, but its use in applications depends on whether the character encoding is ANSI (designated by appending \_A to the function type name), Unicode (designated by appending \_W to the function type name), or UTF-8 (designated by appending \_UTF to the function type name). Therefore, the function call for the **DnsQuery** function would actually be one of the following:

DnsQuery\_A (\_A for ANSI encoding)

DnsQuery\_W (\_W for Unicode encoding)

DnsQuery\_UTF8 (\_UTF8 for UTF-8 encoding)

All functions that require this convention clearly state this requirement within the first few sentences of their function definition. Use the proper function name; for example, you cannot simply call [**DnsQuery**](/windows/desktop/api/Windns/nf-windns-dnsquery_a) instead of DnsQuery\_A.

 

 




