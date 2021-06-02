---
description: specifies a prefix that is on-link to interface \#4.
ms.assetid: cc3aa99d-cf45-460c-bdc1-3e9a19806fe4
title: IPv6 Site Prefixes
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Site Prefixes

The ipv6 rtu command allows published on-link prefixes to be configured with a site prefix length. If specified, the site prefix length is put into a prefix information option in router advertisements. For example:

``` syntax
ipv6 rtu 2002:836b:9820:2::/64 4 pub life 1800 spl 48
```

specifies a prefix that is on-link to interface \#4. The prefix is published, meaning that it is included in router advertisements if interface \#4 is an advertising interface. The lifetime in the prefix information option is 1800 seconds (30 minutes). The site prefix length in the prefix information option is 48.

The receipt of a prefix information option that specifies a site prefix causes an entry to be created in the site prefix table, which can be displayed by using the ipv6 spt command. The site prefix table is used to remove inappropriate site-local addresses from those returned by the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) and related functions.

## Related topics

<dl> <dt>

[IPv6 Link-local and Site-local Addresses](link-local-and-site-local-addresses-2.md)
</dt> <dt>

[Netsh.exe](netsh-exe.md)
</dt> </dl>

 

 



