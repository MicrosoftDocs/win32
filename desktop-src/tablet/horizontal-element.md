---
description: Contains formatting information for the horizontal lines used for the stationery in a Journal note.
ms.assetid: e3c9e7a8-8de6-4871-b386-2186883f2ee7
title: Horizontal Element
ms.topic: reference
ms.date: 05/31/2018
---

# Horizontal Element

Contains formatting information for the horizontal lines used for the stationery in a Journal note.

## Definition

``` syntax
<xs:element name="Horizontal" type="HorizontalType" minOccurs="0" />
```

## Parent Elements

[**LineLayout**](linelayout-element.md)

## Child Elements

None.

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
<td><a href="linelayoutstyletype-simple-type.md"><strong>LineLayoutStyleType</strong></a> simpleType</td>
<td>Required</td>
<td>Specifies the type of line to be drawn.</td>
<td><ul>
<li>None</li>
<li>Solid</li>
<li>Dash</li>
<li>Dot</li>
<li>DashDot</li>
<li>DashDotDot</li>
<li>Double</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Color</strong></td>
<td><a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType</td>
<td>Optional</td>
<td>Color of the element.</td>
<td>A hexadecimal RGB value. Matches the following regular expression: #[0-9a-zA-Z]{6}. For example, #4a79B5.<br/></td>
</tr>
<tr class="odd">
<td><strong>SpacingBefore</strong></td>
<td><strong>xs:nonNegativeInteger</strong></td>
<td>Optional</td>
<td>Spacing before the element.</td>
<td>Any non-negative integer.</td>
</tr>
<tr class="even">
<td><strong>SpacingBetween</strong></td>
<td><strong>xs:nonNegativeInteger</strong></td>
<td>Optional</td>
<td>Spacing between this element and surrounding elements.</td>
<td>Any non-negative integer.</td>
</tr>
</tbody>
</table>



 

## Element Information



|  Element     | Value                                                     |
|--------------|-------------------------------------------------------------------|
| Element type | [**HorizontalType complexType**](horizontaltype-complex-type.md) |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                        |
| Schema name  | Journal Reader                                                    |



 

 

 




