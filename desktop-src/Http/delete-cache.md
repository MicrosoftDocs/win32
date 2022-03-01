---
title: delete cache
description: Flushes the entire URL cache or deletes entries according to the specified URL.
ms.assetid: 499ce0f9-01db-4648-89f7-1ecafd25a805
keywords:
- delete cache HTTP
topic_type:
- apiref
api_name:
- delete cache
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# delete cache

Flushes the entire URL cache or deletes entries according to the specified URL.

``` syntax
delete cache [url=]string [[recursive=]{yes|no}]
 
```

## Parameters

<dl> <dt>

<span id="_url__string"></span><span id="_URL__STRING"></span>__\[url=\]__*string*
</dt> <dd>

Required. Specifies the fully qualified URL.

</dd> </dl>

<dl> <dt>

<span id="_recursive___yes_no_"></span><span id="_RECURSIVE___YES_NO_"></span>**\[recursive=\]{yes\|no}**
</dt> <dd>

If yes, removes all entries under the specified URL.

</dd> </dl>

## Examples

**delete cache url=https://www.contoso.com:80/myresource/ recursive=yes**

 

 




