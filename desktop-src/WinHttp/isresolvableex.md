---
description: Determines if a given host string can resolve to an IP address.
ms.assetid: 83e52ca7-2ea0-419d-b09d-9301c1982b98
title: isResolvableEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- isResolvableEx
api_type: 
- NA
api_location: 
---

# isResolvableEx function

Determines if a given host string can resolve to an IP address.

## Parameters

<dl> <dt>

*host* 
</dt> <dd>

A string containing the HTTP host that is supplied to FindProxyForUrl.

</dd> </dl>

## Return value

TRUE if the host is resolvable to a IPv4 or IPv6 address; otherwise, FALSE.

## Examples

``` syntax
isResolvableEx(host);
    true if the hostname can be resolved to and IP address 
```

``` syntax
isResolvableEx(host); 
    false if the hostname cannot be resolved to an IP address 
```

## See also

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dt>

[IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)
</dt> </dl>

 

 



