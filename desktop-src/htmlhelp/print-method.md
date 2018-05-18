---
title: Print Method
description: Use the Print method to print one or more topics in a specified contents (.hhc) file.
ms.assetid: 'E828EDFC-8553-4c91-A7A6-1AF140C51AA6'
---

# Print Method

Use the Print method to print one or more topics in a specified contents (.hhc) file.

This method can be used with either a compiled help (.chm) file or uncompiled HTML files.

## Applies to

[Contents](contents.md)

## Syntax

``` syntax
Print() 
```

## Parameters

The Print method takes no parameters.

## Example

The following example shows how to use the Print method to invoke the [Contents](contents.md) command.

The code for the [Contents](contents.md) command:


```
<OBJECT
   id=test2
   type="application/x-oleobject"
   classid="clsid:52a2aaae-085d-4187-97ea-8c30db990436"
   codebase="hhctrl.ocx#Version=5,02,3790,1194"
   width=55%
   height=45%
>
   <PARAM name="Command" value="Contents">
   <PARAM name="Item1" value="methods.hhc">
</OBJECT>
```



The JavaScript code to call the Print method:


```
<a href=JavaScript:test2.Print()>Print Contents</a>
```



## Related topics

<dl> <dt>

[About Methods](about-methods.md)
</dt> </dl>

 

 




