---
description: Gets the version of the WPAD processing engine.
ms.assetid: f9e9a867-d491-4d46-bbd8-c0c3d8d5b3d6
title: getClientVersion function
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

# getClientVersion function

Gets the version of the WPAD processing engine.

## Parameters

<dl> <dt>

*IpAddressList* 
</dt> <dd>

A semi-colon delimited string containing IP addresses.

</dd> </dl>

## Return value

A list of sorted semi-colon delimited IP addresses or an empty string if unable to sort the IP Address list.

## Remarks

Currently this function returns version 1.0.

Microsoft added this function to allow IT administrators to update their WPAD scripts to use different versions of the WPAD processing engine without causing breaks to their existing deployment. For example, if Microsoft added a function to the 2.0 version of the WPAD engine, then administrators can check the version before attempting to call that function. This allows their script to work with client running versions 1.0 and 2.0 of the WPAD engine.

## Examples

``` syntax
getClientVersion();
    returns the appropriate versions number of the WPAD engine.
```

## See also

<dl> <dt>

[IPv6-Aware Proxy Helper API Definitions](ipv6-aware-proxy-helper-api-definitions.md)
</dt> <dt>

[IPv6 Extensions to Navigator Auto-Config File Format](ipv6-extensions-to-navigator-auto-config-file-format.md)
</dt> </dl>

 

 



