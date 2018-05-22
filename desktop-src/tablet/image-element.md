---
Description: 'Contains encoded binary data for an image in the Journal document, if present.'
ms.assetid: '98ee234f-13b8-4da4-ac64-60943e76a3ba'
title: Image Element
---

# Image Element

Contains encoded binary data for an image in the Journal document, if present.

## Definition

``` syntax
 Copy Code<xs:element name="Image" type="ImageType" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

[**GroupNode**](groupnode-element.md)

## Child Elements

None.

## Attributes



| Attribute  | Type                      | Required | Description                                                                             | Possible Values           |
|------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**   | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**    | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**  | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height** | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |



 

## Element Information



|              |                                                         |
|--------------|---------------------------------------------------------|
| Element type | [**ImageType**](imagetype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink              |
| Schema name  | Journal Reader                                          |



 

## See also

<dl> <dt>

[**Background**](background-element.md)
</dt> </dl>

 

 



