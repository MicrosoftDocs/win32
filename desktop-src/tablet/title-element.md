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




| Attribute | Type | Required | Description | Possible Values | 
|-----------|------|----------|-------------|-----------------|
| <strong>Style</strong> | <strong>xs:string</strong> | Required | Specifies the type of border surrounding the title of the note. | <ul><li>None</li><li>SolidSquare</li><li>OutlineSquare</li><li>SolidRoundRect</li><li>OutlineRoundRect</li><li>SolidRoundRectDottedBaseline</li></ul> | 
| <strong>DateStyle</strong> | <strong>xs:string</strong> | Required | Defines whether the title includes a date or not. | <ul><li>None</li><li>Short</li></ul> | 
| <strong>Color</strong> | <a href="colortype-simple-type.md"><strong>ColorType simpleType</strong></a> | Optional | Specifies the color of the background. | See <a href="colortype-simple-type.md"><strong>ColorType simpleType</strong></a>. | 




 

## Element Information



| Element      | Value                                                   |
|--------------|---------------------------------------------------------|
| Element type | [**TitleType**](titletype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink              |
| Schema name  | Journal Reader                                          |



 

 

 



