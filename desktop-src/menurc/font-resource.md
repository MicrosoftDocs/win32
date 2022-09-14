---
title: FONT resource
description: Defines a file that contains a font.
ms.assetid: 0e19edd5-6cfc-44e6-add4-7413eb94867a
keywords:
- FONT resource Menus and Other Resources
topic_type:
- apiref
api_name:
- FONT
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# FONT resource

Defines a file that contains a font.

``` syntax
nameID FONT filename
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique 16-bit unsigned integer value identifying the resource.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Name of the file that contains the resource. The name must be a valid file name; it must be a full path if the file is not in the current working directory. The path should be a quoted string.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following example defines a single font resource:

``` syntax
5 FONT  "cmroman.fnt"
```

 

 




