---
description: Contains the background for a JournalDocument element or JournalPage element.
ms.assetid: 48527c4e-50fb-4800-ac87-1646234783ba
title: Background Element
ms.topic: reference
ms.date: 05/31/2018
---

# Background Element

Contains the background for a [**JournalDocument**](journaldocument-element.md) element or [**JournalPage**](journalpage-element.md) element.

## Definition

``` syntax
<xs:element name="Background" type="BackgroundType" minOccurs="0" />
```

## Parent Elements

[**Stationery**](stationery-element.md)

## Child Elements

[**Image**](image-element.md)

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
<td>Specifies the style of the background.</td>
<td><ul>
<li>None</li>
<li>Solid</li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Color</strong></td>
<td><a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType</td>
<td>Optional</td>
<td>Specifies the color of the background.</td>
<td>See <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType.</td>
</tr>
</tbody>
</table>



 

## Element Information



|                  | Value                                                             |
|------------------|-------------------------------------------------------------------|
| **Element type** | [**BackgroundType**](backgroundtype-complex-type.md) complexType |
| **Namespace**    | urn:schemas-microsoft-com:tabletpc:richink                        |
| **Schema name**  | Journal Reader                                                    |



 

 

 



