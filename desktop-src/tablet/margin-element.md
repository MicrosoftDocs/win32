---
description: Defines the margin lines drawn on the page.
ms.assetid: c3047706-affd-4feb-9d48-cfb4c7dd6fa0
title: Margin Element
ms.topic: reference
ms.date: 05/31/2018
---

# Margin Element

Defines the margin lines drawn on the page.

## Definition

``` syntax
<xs:complexType name="MarginType">
   <xs:attribute name="Style" use="required" type="LineLayoutStyleType" />
   <xs:attribute name="Color" type="ColorType" />
   <xs:attribute name="Type" type="MarginTypeType" />
   <xs:attribute name="Spacing" type="xs:positiveInteger" />
</xs:complexType>
```

## Parent Elements

None.

## Child Elements

None..

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
<td><strong>Type</strong></td>
<td><a href="margintypetype-simple-type.md"><strong>MarginTypeType</strong></a> simpleType</td>
<td>Optional</td>
<td>Indicates Left or Right margin.</td>
<td><ul>
<li>Left</li>
<li>Right</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Spacing</strong></td>
<td><strong>xs:nonNegativeInteger</strong></td>
<td>Optional</td>
<td>Spacing between edge of page and margin.</td>
<td>Any non-negative integer.</td>
</tr>
</tbody>
</table>



 

## Element Information



|              |                                                           |
|--------------|-----------------------------------------------------------|
| Element type | [**MarginType**](margintype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                |
| Schema name  | Journal Reader                                            |



 

 

 




