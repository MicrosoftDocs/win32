---
title: Index
description: Creates a graphical index that displays a specified index (.hhk) file.
ms.assetid: '29669B4F-E200-4557-A7E9-0E3245B443A3'
---

# Index

Creates a graphical index that displays a specified index (.hhk) file.

This command can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Syntax

``` syntax
<PARAM name="Command" value="Index">
<PARAM name="Item1"   value="<i>.hhk file path</i>">
```

## Properties

<dl> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the Index command.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the index (.hhk) file path.

</dd> </dl>

## Example


```
<OBJECT
   id=MyControl
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="Hhctrl.ocx#Version=5,02,3790,1194"
   width=100%
   height=100%
>
   <PARAM name="Command" value="Index">
   <PARAM name="Item1" value="c:\Index Files\MyIndex.hhk">
</OBJECT>
```



## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




