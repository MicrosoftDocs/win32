---
title: show urlacl
description: Lists DACLs for the specified reserved URL or all reserved URLs.
ms.assetid: 8428583c-b420-408f-974f-670b6809fa3c
keywords:
- show urlacl HTTP
topic_type:
- apiref
api_name:
- show urlacl
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# show urlacl

Lists DACLs for the specified reserved URL or all reserved URLs.

``` syntax
show urlacl [url=]string
 
```

## Parameters

__\[url=\]__*string*

Specifies the fully qualified URL. If unspecified, implies all URLs.


## Examples

**show urlacl url=https://+:80/MyUrl**

**show urlacl url=https://www.contoso.com:80/MyUrl**

 

 




