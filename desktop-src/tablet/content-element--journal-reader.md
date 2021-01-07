---
description: Contains the content for a Journal page.
ms.assetid: 1df78a17-1cd4-4e98-aed1-b09d2b357703
title: Content Element [Journal Reader]
ms.topic: reference
ms.date: 05/31/2018
---

# Content Element \[Journal Reader\]

Contains the content for a Journal page.

## Definition

``` syntax
<xs:element name="Content" type="ContentType" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**JournalPage**](journalpage-element.md)

## Child Elements

[**GroupNode**](groupnode-element.md)

[**Paragraph**](paragraph-element.md)

[**Drawing**](drawing-element.md)

[**Text**](text-element.md)

[**Image**](image-element.md)

[**Flag**](flag-element.md)

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
<th>PossibleValues</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Type</strong></td>
<td><a href="contenttype-complex-type.md"><strong>ContentType complexType</strong></a></td>
<td>Required</td>
<td>If the type is &quot;Inert&quot;, then the content cannot be modified.<br/></td>
<td><ul>
<li>Normal</li>
<li>Inert</li>
</ul></td>
</tr>
</tbody>
</table>



 

## Element Information



|              |                                                             |
|--------------|-------------------------------------------------------------|
| Element type | [**ContentType**](contenttype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                  |
| Schema name  | Journal Reader                                              |



 

 

 




