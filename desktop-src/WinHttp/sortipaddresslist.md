---
description: Sorts a list of IP addresses.
ms.assetid: 1266d6f3-e9f5-4e6b-9431-7329df156f0a
title: sortIpAddressList function
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

# sortIpAddressList function

Sorts a list of IP addresses.

## Parameters

<dl> <dt>

*IpAddressList* 
</dt> <dd>

A semi-colon delimited string containing IP addresses.

</dd> </dl>

## Return value

A list of sorted semi-colon delimited IP addresses or an empty string if unable to sort the IP Address list.

## Remarks

FindProxyforURLEx implementers should add code that breaks the string of semi-colon delimited IP addresses into separate addresses.

## Examples

``` syntax
sortIpAddressList(2001:4898:28:3:201:2ff:feea:fc14; 
                  157.59.139.22; 
                  fe80::5efe:157.59.139.22");
    returns "fe80::5efe:157.59.139.22;2001:4898:28:3:201:2ff:feea:fc14;157.59.139.22" 
    A list of sorted IP addresses. If there both IPv6 and IPv4 IP addresses are passed as input to this function, then the sorted IPv6 addresses are followed by sorted IPv4 addresses
```

## See also

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dt>

[IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)
</dt> </dl>

 

 



