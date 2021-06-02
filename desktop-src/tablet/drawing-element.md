---
description: Contains content that has been classified by the analyzer or the user as a drawing.
ms.assetid: 566542f3-b824-442d-9d8b-0064ebcf9b68
title: Drawing Element
ms.topic: reference
ms.date: 05/31/2018
---

# Drawing Element

Contains content that has been classified by the analyzer or the user as a drawing.

## Definition

``` syntax
<xs:element name="Drawing" type="DrawingType" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

[**GroupNode**](groupnode-element.md)

## Child Elements

[**ScalarTransform**](scalartransform-element.md)

[**CanReClassify**](canreclassify-element.md)

[**InkClass**](inkclass-element.md)

[**InkObject**](inkobject-element.md)

## Attributes



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

## Element Information



|              |                                                             |
|--------------|-------------------------------------------------------------|
| Element type | [**DrawingType**](drawingtype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                  |
| Schema name  | Journal Reader                                              |



 

 

 



