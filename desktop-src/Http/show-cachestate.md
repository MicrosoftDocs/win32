---
title: show cachestate
description: Lists all resources and their associated properties that are cached in the HTTP response cache or displays a single resource and its associated properties.
ms.assetid: 9daa445e-dd2f-4b73-8938-58df931c015b
keywords:
- show cachestate HTTP
topic_type:
- apiref
api_name:
- show cachestate
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# show cachestate

Lists all resources and their associated properties that are cached in the HTTP response cache or displays a single resource and its associated properties.

``` syntax
show cachestate [[url=]string]
 
```

## Parameters

<dl> <dt>

<span id="__url__string_"></span><span id="__URL__STRING_"></span>**\[\[url=\]***string***\]**
</dt> <dd>

Fully qualified URL. If unspecified, implies all URLs. The URL can also be a prefix to registered URLs.

</dd> </dl>

## Examples

**show cachestate url=https://www.contoso.com:80/myresource**

 

 




