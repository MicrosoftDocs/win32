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




| Attribute | Type | Required | Description | Possible Values | 
|-----------|------|----------|-------------|-----------------|
| <strong>Style</strong> | <a href="linelayoutstyletype-simple-type.md"><strong>LineLayoutStyleType</strong></a> simpleType | Required | Specifies the type of line to be drawn. | <ul><li>None</li><li>Solid</li><li>Dash</li><li>Dot</li><li>DashDot</li><li>DashDotDot</li><li>Double</li></ul> | 
| <strong>Color</strong> | <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType | Optional | Color of the element. | A hexadecimal RGB value. Matches the following regular expression: #[0-9a-zA-Z]{6}. For example, #4a79B5.<br /> | 
| <strong>SpacingBefore</strong> | <strong>xs:nonNegativeInteger</strong> | Optional | Spacing before the element. | Any non-negative integer. | 
| <strong>SpacingBetween</strong> | <strong>xs:nonNegativeInteger</strong> | Optional | Spacing between this element and surrounding elements. | Any non-negative integer. | 




 

## Element Information



|  Element     | Value                                                     |
|--------------|-------------------------------------------------------------------|
| Element type | [**HorizontalType complexType**](horizontaltype-complex-type.md) |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                        |
| Schema name  | Journal Reader                                                    |



 

 

 




