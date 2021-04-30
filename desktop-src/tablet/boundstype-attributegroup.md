---
description: Defines an attribute group that is used by a variety of elements in a Journal XML file. It contains attributes used to define the bounds (left, top, height, and width) of an element in the document.
ms.assetid: 7841aa65-fb35-4909-a34e-3c883555f764
title: BoundsType Attribute Group
ms.topic: reference
ms.date: 05/31/2018
---

# BoundsType Attribute Group

Defines an attribute group that is used by a variety of elements in a Journal XML file. It contains attributes used to define the bounds (left, top, height, and width) of an element in the document.

## Definition

``` syntax
<xs:attributeGroup name="BoundsType">
  <xs:attribute name="Left" use="required" type="xs:integer" />
  <xs:attribute name="Top" use="required" type="xs:integer" />
  <xs:attribute name="Width" use="required" type="xs:nonNegativeInteger" />
  <xs:attribute name="Height" use="required" type="xs: nonNegativeInteger" />
</xs:attributeGroup>
```

## Child Elements

None.

## Attributes



| Attribute  | Type                      | Required | Description                                                                                        | PossibleValues                       |
|------------|---------------------------|----------|----------------------------------------------------------------------------------------------------|--------------------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element.<br/> | Any integer.<br/>              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.<br/>  | Any integer.<br/>              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.<br/>                                          | Any non-negative integer.<br/> |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.<br/>                                         | Any non-negative integer.<br/> |



 

## Type Information



|             |                                            |
|-------------|--------------------------------------------|
| Namespace   | urn:schemas-microsoft-com:tabletpc:richink |
| Schema name | Journal Reader                             |



 

## Remarks

**Left** and **Top** can be negative because the origin is defined by the margins, not the page.

 

 




