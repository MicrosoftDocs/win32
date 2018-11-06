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
ms.topic: article
ms.date: 05/31/2018
---

# show urlacl

Lists DACLs for the specified reserved URL or all reserved URLs.

``` syntax
show urlacl [url=]string
 
```

## Parameters

<dl> <dt>

<span id="_url__string"></span><span id="_URL__STRING"></span>**\[url=\]***string*
</dt> <dd>

Specifies the fully qualified URL. If unspecified, implies all URLs.

</dd> </dl>

## Examples

**show urlacl url=http://+:80/MyUrl**

**show urlacl url=http://www.contoso.com:80/MyUrl**

 

 




