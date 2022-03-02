---
title: delete sslcert
description: Deletes SSL server certificate bindings and the corresponding client certificate policies for an IP address and port.
ms.assetid: 2adea7a8-f31f-4c02-8279-7d452e36cd9b
keywords:
- delete sslcert HTTP
topic_type:
- apiref
api_name:
- delete sslcert
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# delete sslcert

Deletes SSL server certificate bindings and the corresponding client certificate policies for an IP address and port.

``` syntax
delete sslcert [ipport=]IP Address:port
 
```

## Parameters

__\[ipport=\]__*IP Address:port*

Specifies the IPv4 or IPv6 address and port for which the SSL certificate bindings will be deleted.

## Examples

**delete sslcert ipport=1.1.1.1:443**

**delete sslcert ipport=0.0.0.0:443**

**delete sslcert ipport=\[::\]:443**
