---
title: BITMAP resource
description: Defines a bitmap that an application uses in its screen display or as an item in a menu or control.
ms.assetid: 2db2f7f0-735f-4aac-9813-c04a2f7788b2
keywords:
- BITMAP resource Menus and Other Resources
topic_type:
- apiref
api_name:
- BITMAP
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# BITMAP resource

Defines a bitmap that an application uses in its screen display or as an item in a menu or control.

``` syntax
nameID BITMAP filename
```

## Parameters

<dl> <dt>

<span id="nameID"></span><span id="nameid"></span><span id="NAMEID"></span>*nameID*
</dt> <dd>

Unique name or a 16-bit unsigned integer value identifying the resource.

</dd> <dt>

<span id="filename"></span><span id="FILENAME"></span>*filename*
</dt> <dd>

Name of the file that contains the resource. The name must be a valid file name; it must be a full path if the file is not in the current working directory. The path should be a quoted string.

</dd> </dl>

Certain attributes are also supported for backward compatibility. For more information, see [Common Resource Attributes](common-resource-attributes.md).

## Examples

The following example defines two bitmap resources:

``` syntax
disk1   BITMAP "disk.bmp"
12      BITMAP "diskette.bmp"
```

## See also

<dl> <dt>

[Using Bitmaps](/windows/desktop/gdi/using-bitmaps)
</dt> <dt>

[**LoadBitmap**](/windows/desktop/api/winuser/nf-winuser-loadbitmapa)
</dt> <dt>

[**LoadImage**](/windows/desktop/api/Winuser/nf-winuser-loadimagea)
</dt> </dl>

 

 