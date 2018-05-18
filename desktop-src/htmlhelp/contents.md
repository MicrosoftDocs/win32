---
title: Contents
description: Creates a graphical table of contents that displays a specified contents (.hhc) file.
ms.assetid: 'CFAC4EBC-FB2B-43cf-8AAA-48E2FE0C04E0'
---

# Contents

Creates a graphical table of contents that displays a specified contents (.hhc) file.

This command can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Syntax

``` syntax
<PARAM name="Command" value="Contents">
<PARAM name="Item1"   value="<i>.hhc file path</i>">
<PARAM name="Flags"   value="0x<i>n</i>,0x<i>n</i>">
```

## Properties

<dl> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>[Command](command-parameter.md)
</dt> <dd>

Calls the Contents command.

</dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>[Flags](flags-parameter.md)
</dt> <dd>

Specifies **ExWindow Styles** and **Window Styles** values for the selected window style attributes. The values are stored as hexadecimal numbers in the format 0x*n*.

We recommend that you use the HTML Help ActiveX Control Wizard to select window styles. The wizard automatically inserts the appropriate parameter values in the format 0x*n*.

</dd> <dt>

<span id="Item1"></span><span id="item1"></span><span id="ITEM1"></span>[Item1](item-parameter.md)
</dt> <dd>

Specifies the contents (.hhc) file path.

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
   <PARAM name="Command" value="Contents">
   <PARAM name="Item1" value="C:\toc.hhc">
   <PARAM name="Flags" value="0x4000,0x800035>
</OBJECT>
```



## Remarks

-   The **Flags** parameter will overwrite any **ExWindow Styles** and **Window Styles** parameter values that have been set in the specified contents (.hhc) file using the **Table of Contents** dialog box in HTML Help Workshop.

## Related topics

<dl> <dt>

[About Commands](about-commands.md)
</dt> </dl>

 

 




