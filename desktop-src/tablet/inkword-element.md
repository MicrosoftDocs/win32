---
description: Contains information about a given ink word in the Journal note, including position, alternates, and the actual ink data.
ms.assetid: 1e197716-bf6c-4a28-ae66-38aa59d7371d
title: InkWord Element
ms.topic: reference
ms.date: 05/31/2018
---

# InkWord Element

Contains information about a given ink word in the Journal note, including position, alternates, and the actual ink data.

## Definition

``` syntax
<xs:element name="InkWord" type="InkWordType" />
```

## Parent Elements

[**GroupNode**](groupnode-element.md)

[**Line**](line-element.md)

## Child Elements

[**ScalarTransform**](scalartransform-element.md)

[**AlternateList**](alternatelist-element.md)

[**CanReClassify**](canreclassify-element.md)

[**Confidence**](confidence-element.md)

[**InkObject**](inkobject-element.md)

## Attributes



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

> [!WARNING]
> The ink word's internal coordinate mapping is English Metric Units and a multiplier of 2.54 will need to be used by your application to convert the Width and Height values to the HIMETRIC units used by the Tablet PC platform APIs.

 

## Element Information



|              |                                                             |
|--------------|-------------------------------------------------------------|
| Element type | [**InkWordType**](inkwordtype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                  |
| Schema name  | Journal Reader                                              |



 

 

 



