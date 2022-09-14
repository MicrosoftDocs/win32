---
description: Resolve a host string to its IP address
ms.assetid: 32d70f10-803b-484d-a9e0-d4c61a8d897f
title: dnsResolveEx function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- dnsResolveEx
api_type: 
- NA
api_location: 
---

# dnsResolveEx function

Resolve a host string to its IP address

## Parameters

<dl> <dt>

*host* 
</dt> <dd>

A string containing the HTTP host that is supplied to FindProxyForUrl.

</dd> </dl>

## Return value

A semi-colon delimited string containing IPv6 and IPv4 addresses or an empty string if host is not resolvable.

## Remarks

FindProxyforURLEx implementers should add code that breaks the string of semi-colon delimited IP addresses into separate addresses.

## Examples

``` syntax
dnsResolveEx("testmachine1");
    returns the string "fe80::380c:2e71:f5b9:a3b5%15;fe80::982d:a3b3:97ad:7dd0%9;2001:4898:28:7:982d:a3b3:97ad:7dd0;2001:4898:28:7:adfe:a643:8130:2fdc;fe80::5efe:10.70.92.74%13;3ffe:8311:ffff:f70f:0:5efe:10.70.92.74;10.70.92.74;3ffe:831f:4136:e37e:380c:2e71
```

## See also

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dt>

[IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)
</dt> </dl>

 

 



