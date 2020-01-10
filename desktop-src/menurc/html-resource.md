---
title: HTML resource
description: Defines an HTML file.
ms.assetid: d3cf8348-8c10-41d9-a061-cdce0e13abf4
keywords:
- HTML resource Menus and Other Resources
topic_type:
- apiref
api_name:
- HTML
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# HTML resource

Defines an HTML file.

``` syntax
nameID HTML filename
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a 16-bit unsigned integer value identifying the resource.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

The name of the HTML file. It must be a full or relative path if the file is not in the current working directory. The path should be a quoted string.

</dd> </dl>

## Examples

The following example defines an HTML resource:

``` syntax
ID_RESPONSE_ERROR_PAGE  HTML "res\\responseerorpage.htm"
```

 

 




