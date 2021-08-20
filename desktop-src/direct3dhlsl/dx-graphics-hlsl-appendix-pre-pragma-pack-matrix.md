---
title: pack_matrix pragma Directive
description: Pragma directive that specifies packing alignment for matrices.
ms.assetid: e77dc007-d915-4d78-9fff-d44d4999e4da
keywords:
- pack_matrix pragma Directive HLSL
topic_type:
- apiref
api_name:
- pack_matrix pragma Directive
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# pack\_matrix pragma Directive

Pragma directive that specifies packing alignment for matrices.



| \#pragma pack\_matrix( *alignment* ) |
|--------------------------------------|



 

## Parameters



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="alignment"></span><span id="ALIGNMENT"></span><em>alignment</em><br/></td>
<td>Alignment to set for matrices. This parameter can take one of the values listed in the following table. <br/> 
<table>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>column_major</td>
<td>Default. Sets the matrix packing alignment to column major.</td>
</tr>
<tr class="even">
<td>row_major</td>
<td>Sets the matrix packing alignment to row major.</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

## Examples

The following example sets the matrix packing alignment to row major.


```
#pragma pack_matrix( row_major )
```



## See also

<dl> <dt>

[Preprocessor Directives (DirectX HLSL)](dx-graphics-hlsl-appendix-preprocessor.md)
</dt> <dt>

[\#pragma Directive (DirectX HLSL)](dx-graphics-hlsl-appendix-pre-pragma.md)
</dt> </dl>

 

 





