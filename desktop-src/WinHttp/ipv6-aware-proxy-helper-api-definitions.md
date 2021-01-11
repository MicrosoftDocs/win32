---
description: In order to take advantage of the IPv6 enabled functions, IT administrators must define within their WPAD script, a function called FindProxyForURLEx (url, host) which will replace the legacy FindProxyForUrl (url, host) function.
ms.assetid: e531a66d-5c50-4065-a12a-783fd4d1d310
title: IPv6-Aware Proxy Helper API Definitions
ms.topic: article
ms.date: 05/31/2018
---

# IPv6-Aware Proxy Helper API Definitions

In order to take advantage of the IPv6 enabled functions, IT administrators must define within their WPAD script, a function called FindProxyForURLEx (url, host) which will replace the legacy FindProxyForUrl (url, host) function. Only from the new FindProxyForURLEx function will administrators be able to execute the new functions.

We also attempted to simplify work for developers, by aligning our functions to return different types of IP addresses in the same order of preference as other networking components, specifically IPv6 addresses followed by IPv4 addresses (i.e. current behavior for Winsock’s getaddrinfo(..) function).

The following functions are extensions to the [Navigator Proxy Auto-Config (PAC) File Format specification](https://web.archive.org/web/20060424005037/wp.netscape.com/eng/mozilla/2.0/relnotes/demo/proxy-live.html) to enable WPAD scripts to handle IPv6 capable networks.

## Predefined Functions and Environment for the JavaScript Function FindProxyforURLEx

Hostname based conditions

<dl> <dt>

[**isResolvableEx**](isresolvableex.md)
</dt> <dd>

Determines if a given host string can resolve to an IP address.

</dd> <dt>

[**isInNetEx**](isinnetex.md)
</dt> <dd>

Determines if an IP address is in a specific subnet.

</dd> </dl>

Related utility functions

<dl> <dt>

[**dnsResolveEx**](dnsresolveex.md)
</dt> <dd>

Resolve a host string to its IP address.

</dd> <dt>

[**myIPAddressEx**](myipaddressex.md)
</dt> <dd>

Finds all the IP addresses for localhost.

</dd> <dt>

[**sortIpAddressList**](sortipaddresslist.md)
</dt> <dd>

Sorts a list of IP addresses.

</dd> <dt>

[**getClientVersion**](getclientversion.md)
</dt> <dd>

Gets the version of the WPAD processing engine.

</dd> </dl>

> [!Note]  
> This functionality requires Windows Internet Explorer 7 or greater.

 

 

 



