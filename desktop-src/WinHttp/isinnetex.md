---
description: Determines if an IP address is in a specific subnet.
ms.assetid: 2fbfad9c-86b1-44c3-860b-a5c98ac6c2e9
title: isInNetEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- isInNetEx
api_type: 
- NA
api_location: 
---

# isInNetEx function

Determines if an IP address is in a specific subnet.

## Parameters

<dl> <dt>

*IPaddress* 
</dt> <dd>

A string containing IPv6/IPv4 addresses.

</dd> <dt>

*IPprefix* 
</dt> <dd>

A string containing colon delimited IP prefix with top n bits specified in the bit field (i.e. 3ffe:8311:ffff::/48 or 123.112.0.0/16).

</dd> </dl>

## Return value

TRUE if the host is in the same subnet; otherwise, FALSE.

Also returns FALSE if the prefix is not in the correct format or if addresses and prefixes of different types are used in the comparison (i.e. IPv4 prefix and an IPv6 address).

## Examples

``` syntax
isInNetEx(host, "198.95.249.79/32");
    true if the IP address of host matches exactly 198.95.249.79
```

``` syntax
isInNetEx(host, "198.95.0.0/16");
    true if the IP address of the host matches 198.95.*.*
```

``` syntax
isInNetEx(host, "3ffe:8311:ffff::/48");
    true if the IP address of the host matches 3ffe:8311:fff:*:*:*:*:*
```

## See also

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dt>

[IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)
</dt> </dl>

 

 



