---
title: Resource Records
description: Learn about resource records. A resource record is the unit of information entry in DNS zone files, which used to resolve all DNS queries.
ms.assetid: 'c64907c2-ebd3-4550-9454-13f51a6d7ca6'
ms.topic: article
ms.date: 05/31/2018
---

# Resource Records

A resource record, commonly referred to as an RR, is the unit of information entry in DNS zone files; RRs are the basic building blocks of host-name and IP information and are used to resolve all DNS queries. Resource records exist as many types to provide extended name-resolution services.

Different types of RRs have different formats, as they contain different data. In general, however, many RRs share a common format, as the following address resource records example illustrates. The following fictional example explains the fields found in an A resource record:

``` syntax
microsoft.com. 600 IN A 150.150.150.1
```

-   The first field (microsoft.com) denotes the owner.
-   The second field (600) is the time-to-live (TTL) parameter, in seconds.
-   The third field (IN) is the class field that represents the protocol family, which is almost always IN, for Internet class.
-   The fourth field (A) is the type of resource the RR is representing.
-   The fifth field (150.150.150.1) is the resource data, or RDATA. This field is a variable type that provides information appropriate for the type of resource; in this case, it's a 32-bit IP address.

The following resource record types are commonly used in DNS:

-   Start of authority (SOA)
-   Name server (NS)
-   [*Pointer record*](p-gly.md) (PTR)
-   Address (A)
-   IPv6 Address (AAAA)
-   Mail exchange (MX)
-   [*Canonical name*](c-gly.md) (CNAME)
-   Windows Internet Naming Service (WINS)
-   WINS Reverse Look up (WINSR)

There are many other resource record types in DNS. For more information, see [DNS WMI Provider Reference](dns-wmi-provider-reference.md).

 

 




