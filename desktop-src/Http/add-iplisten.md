---
title: add iplisten
description: Specifies an IPv4 or IPv6 address to be added to the IP listen list.
ms.assetid: 38253818-c029-4a46-ab52-095cbfdeeaf4
keywords:
- add iplisten HTTP
topic_type:
- apiref
api_name:
- add iplisten
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# add iplisten

Specifies an IPv4 or IPv6 address to be added to the IP listen list.

``` syntax
add iplisten [ ipaddress=] IPAddress
 
```

## Parameters

**\[ ipaddress=\]** *IPAddress*

Specifies the IPv4 or IPv6 address to be added to the IP listen list.

## Remarks

Adds a new IP address to the IP listen list. This does not include the port number. The IP listen list is used to scope the list of addresses to which the HTTP service binds. "0.0.0.0" means any IPv4 address and "::" means any IPv6 address.

## Examples

**add iplisten ipaddress=fe80::1**

**add iplisten ipaddress=1.1.1.1**

**add iplisten ipaddress=0.0.0.0**

**add iplisten ipaddress=::**

 

 




