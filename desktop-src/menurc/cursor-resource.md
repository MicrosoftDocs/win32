---
title: CURSOR resource
description: Defines a bitmap that defines the shape of the cursor on the display screen or an animated cursor.
ms.assetid: c087abca-5502-4625-8c9b-464e1718571f
keywords:
- CURSOR resource Menus and Other Resources
topic_type:
- apiref
api_name:
- CURSOR
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# CURSOR resource

Defines a bitmap that defines the shape of the cursor on the display screen or an animated cursor.

``` syntax
nameID CURSOR filename
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a 16-bit unsigned integer identifying the resource.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Name of the file that contains the resource. The name must be a valid file name; it must be a full path if the file is not in the current working directory. The path should be a quoted string.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Remarks

Icon and cursor resources can contain more than one image.

## Examples

The following example defines two cursor resources; one by name (cursor1) and the other by number (2):

``` syntax
cursor1 CURSOR "bullseye.cur"
2       CURSOR "d:\\cursor\\arrow.cur" 
```

## See also

<dl> <dt>

[Using Cursors](./using-cursors.md)
</dt> </dl>

 

 