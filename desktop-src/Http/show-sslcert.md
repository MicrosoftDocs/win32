---
title: show sslcert
description: Lists SSL server certificate bindings and the corresponding client certificate policies for an IP address and port.
ms.assetid: 8e20f55e-a357-4f9c-a24e-e234607c3196
keywords:
- show sslcert HTTP
topic_type:
- apiref
api_name:
- show sslcert
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# show sslcert

Lists SSL server certificate bindings and the corresponding client certificate policies for an IP address and port.

``` syntax
show sslcert [ipport=]IP Address:port
 
```

## Parameters

__\[ipport=\]__*IP Address:port*

Specifies the IPv4 or IPv6 address and port for which the SSL certificate bindings will be displayed. Not specifying an ipport lists all bindings.

## Examples

**show sslcert ipport=\[fe80::1\]:443**

**show sslcert ipport=1.1.1.1:443**

**show sslcert ipport=0.0.0.0:443**

**show sslcert ipport=\[::\]:443**

 

 




