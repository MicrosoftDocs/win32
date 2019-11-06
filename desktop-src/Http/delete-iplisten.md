---
title: delete iplisten
description: Specifies an IPv4 or IPv6 address to be deleted from the IP listen list.
ms.assetid: 1d0935a5-77de-4fdf-8d3b-88c8578bd5c7
keywords:
- delete iplisten HTTP
topic_type:
- apiref
api_name:
- delete iplisten
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# delete iplisten

Specifies an IPv4 or IPv6 address to be deleted from the IP listen list.

``` syntax
delete iplisten [ address=] IPAddress
 
```

## Parameters

<dl> <dt>

<span id="_address___IPAddress"></span><span id="_address___ipaddress"></span><span id="_ADDRESS___IPADDRESS"></span>**\[address=\]** *IPAddress*
</dt> <dd>

Specifies the IPv4 or IPv6 address to be deleted from the IP listen list.

</dd> </dl>

## Remarks

Deletes an IP address to the IP listen list. This does not include the port number. The IP listen list is used to scope the list of addresses to which the HTTP service binds. "0.0.0.0" means any IPv4 address and "::" means any IPv6 address.

## Examples

**delete iplisten address=fe80::1**

**delete iplisten address=1.1.1.1**

**delete iplisten address=0.0.0.0**

**delete iplisten address=::**

 

 




