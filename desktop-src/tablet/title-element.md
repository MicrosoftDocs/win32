---
description: Contains title information about the Journal note.
ms.assetid: efeed3a6-de5e-4698-9dc3-d0acb3d13dee
title: Title Element
ms.topic: reference
ms.date: 05/31/2018
---

# Title Element

Contains title information about the Journal note.

## Definition

``` syntax
<xs:element name="Title" type="TitleType" minOccurs="0" />
```

## Parent Elements

[**Stationery**](stationery-element.md)

## Child Elements

[**TitleArea**](titlearea-element.md)

## Attributes



<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
<th>Possible Values</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Style</strong></td>
<td><strong>xs:string</strong></td>
<td>Required</td>
<td>Specifies the type of border surrounding the title of the note.</td>
<td><ul>
<li>None</li>
<li>SolidSquare</li>
<li>OutlineSquare</li>
<li>SolidRoundRect</li>
<li>OutlineRoundRect</li>
<li>SolidRoundRectDottedBaseline</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>DateStyle</strong></td>
<td><strong>xs:string</strong></td>
<td>Required</td>
<td>Defines whether the title includes a date or not.</td>
<td><ul>
<li>None</li>
<li>Short</li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Color</strong></td>
<td><a href="colortype-simple-type.md"><strong>ColorType simpleType</strong></a></td>
<td>Optional</td>
<td>Specifies the color of the background.</td>
<td>See <a href="colortype-simple-type.md"><strong>ColorType simpleType</strong></a>.</td>
</tr>
</tbody>
</table>



 

## Element Information



|              |                                                         |
|--------------|---------------------------------------------------------|
| Element type | [**TitleType**](titletype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink              |
| Schema name  | Journal Reader                                          |



 

 

 



