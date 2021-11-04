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




| Attribute | Type | Required | Description | Possible Values | 
|-----------|------|----------|-------------|-----------------|
| <strong>Style</strong> | <a href="linelayoutstyletype-simple-type.md"><strong>LineLayoutStyleType</strong></a> simpleType | Required | Specifies the type of line to be drawn. | <ul><li>None</li><li>Solid</li><li>Dash</li><li>Dot</li><li>DashDot</li><li>DashDotDot</li><li>Double</li></ul> | 
| <strong>Color</strong> | <a href="colortype-simple-type.md"><strong>ColorType</strong></a> simpleType | Optional | Color of the element. | A hexadecimal RGB value. Matches the following regular expression: #[0-9a-zA-Z]{6}. For example, #4a79B5.<br /> | 
| <strong>Type</strong> | <a href="margintypetype-simple-type.md"><strong>MarginTypeType</strong></a> simpleType | Optional | Indicates Left or Right margin. | <ul><li>Left</li><li>Right</li></ul> | 
| <strong>Spacing</strong> | <strong>xs:nonNegativeInteger</strong> | Optional | Spacing between edge of page and margin. | Any non-negative integer. | 




 

## Element Information



|  Element     | Value                                                     |
|--------------|-----------------------------------------------------------|
| Element type | [**MarginType**](margintype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                |
| Schema name  | Journal Reader                                            |



 

 

 




