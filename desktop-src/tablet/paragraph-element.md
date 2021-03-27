---
description: Contains a paragraph.
ms.assetid: 60322907-3902-49a9-91a9-e00b0a714c00
title: Paragraph Element (Windows.ui.xaml.documents.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Paragraph
api_type: 
- HeaderDef
api_location: 
- windows.ui.xaml.documents.h
---

# Paragraph Element

Contains a paragraph.

## Definition

``` syntax
<xs:element name="Paragraph" type="ParagraphType" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**Content**](content-element--journal-reader.md)

[**GroupNode**](groupnode-element.md)

## Child Elements

[**Line**](line-element.md)

[**ParagraphLineMetrics**](paragraphlinemetrics-element.md)

## Attributes



| Attribute       | Type                      | Required | Description                                                                             | Possible Values           |
|-----------------|---------------------------|----------|-----------------------------------------------------------------------------------------|---------------------------|
| **Left**        | **xs:integer**            | Required | The distance from the origin to the leftmost point in the bounding box for the element. | Any integer.              |
| **Top**         | **xs:integer**            | Required | The distance from the origin to the topmost point in the bounding box for the element.  | Any integer.              |
| **Width**       | **xs:nonNegativeInteger** | Required | The width of the bounding box for the element.                                          | Any non-negative integer. |
| **Height**      | **xs:nonNegativeInteger** | Required | The height of the bounding box for the element.                                         | Any non-negative integer. |
| **BlockNumber** | **xs:nonNegativeInteger** | Required | Block number.                                                                           | Any non-negative integer. |
| **LineNumber**  | **xs:nonNegativeInteger** | Required | The line on which the paragraph begins.                                                 | Any non-negative integer. |



 

## Element Information



|              |                                                                 |
|--------------|-----------------------------------------------------------------|
| Element type | [**ParagraphType**](paragraphtype-complex-type.md) complexType |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink                      |
| Schema name  | Journal Reader                                                  |



 

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Windows.ui.xaml.documents.h</dt> </dl> |



 

 




