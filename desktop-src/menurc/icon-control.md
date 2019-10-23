---
title: ICON control
description: Defines an icon control. This control is an icon displayed in a dialog box.
ms.assetid: fd2e1e7a-f386-4fdc-8b05-afce19dd3e8d
keywords:
- ICON control Menus and Other Resources
topic_type:
- apiref
api_name:
- ICON
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ICON control

Defines an icon control. This control is an icon displayed in a dialog box.

The **ICON** control statement, which you can use only in a [**DIALOGEX**](dialogex-resource.md) statement, defines the icon-resource identifier, icon-control identifier, position, and attributes of a control.

``` syntax
ICON text, id, x, y [, width, height, style [, extended-style]]
```

<dl> <dt>

<span id="text"></span><span id="TEXT"></span>*text*
</dt> <dd>

Name of an icon (not a file name) defined elsewhere in the resource file.

</dd> <dt>

<span id="width"></span><span id="WIDTH"></span>*width*
</dt> <dd>

This value is ignored and should be set to zero.

</dd> <dt>

<span id="height"></span><span id="HEIGHT"></span>*height*
</dt> <dd>

This value is ignored and should be set to zero.

</dd> <dt>

<span id="style"></span><span id="STYLE"></span>*style*
</dt> <dd>

Control style. This parameter is optional. The only value that can be specified is the **SS\_ICON** style. This is the default style whether this parameter is specified or not.

</dd> </dl>

For more information about the general syntax of a control statement, see [Common Control Parameters](common-control-parameters.md).

## Examples

This example defines an icon control whose icon identifier is 901 and whose name is myicon:

``` syntax
ICON "myicon", 901, 30, 30
```

## See also

<dl> <dt>

[**ICON**](icon-resource.md)
</dt> </dl>

 

 




