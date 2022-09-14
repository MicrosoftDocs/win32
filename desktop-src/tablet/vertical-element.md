---
description: Contains the information that describes the vertical component of the lines in the stationery used by the Journal note. Used, for example, when the note has grid lines.
ms.assetid: af6f485e-13df-41bb-b57a-10d8393b83e7
title: Vertical Element
ms.topic: reference
ms.date: 05/31/2018
---

# Vertical Element

Contains the information that describes the vertical component of the lines in the stationery used by the Journal note. Used, for example, when the note has grid lines.

## Definition

``` syntax
<xs:element name="Vertical" type="VerticalType" minOccurs="0" />
```

## Parent Elements

[**LineLayout**](linelayout-element.md)

## Child Elements

None.

## Attributes




| Attribute | Type | Required | Description | Possible Values | 
|-----------|------|----------|-------------|-----------------|
| <strong>Style</strong> | <a href="linelayoutstyletype-simple-type.md"><strong>LineLayoutStyleType</strong></a> simpleType | Required | Specifies the type of line to be drawn. | <ul><li>None</li><li>Solid</li><li>Dash</li><li>Dot</li><li>DashDot</li><li>DashDotDot</li><li>Double</li></ul> | 
| <strong>Color</strong> | <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType | Optional | Color of the element. | A hexadecimal RGB value. Matches the following regular expression: #[0-9a-zA-Z]{6}. For example, #4a79B5.<br /> | 
| <strong>SpacingBefore</strong> | <strong>xs:nonNegativeInteger</strong> | Optional | Spacing before the element. | Any non-negative integer. | 
| <strong>SpacingBetween</strong> | <strong>xs:nonNegativeInteger</strong> | Optional | Spacing between this element and surrounding elements. | Any non-negative integer. | 




 

## Element Information



|  Element     | Value                                                         |
|--------------|---------------------------------------------------------------|
| Element type | [**VerticalType**](verticaltype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                    |
| Schema name  | Journal Reader                                                |



 

 

 




