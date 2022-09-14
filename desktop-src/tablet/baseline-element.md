---
description: Provides (x, y) information for the starting and ending points of the baseline of a paragraph in the Journal document. The coordinate space used for these values is HIMETRIC.
ms.assetid: ff6a97ad-0e48-4128-8f94-24802b6ddc05
title: Baseline Element
ms.topic: reference
ms.date: 05/31/2018
---

# Baseline Element

Provides (x, y) information for the starting and ending points of the baseline of a paragraph in the Journal document. The coordinate space used for these values is **HIMETRIC**.

## Definition

``` syntax
<xs:element name="Baseline" type="BaseLineType" />
```

## Parent Elements

[**ParagraphLineMetrics**](paragraphlinemetrics-element.md)

## Child Elements

None.

## Attributes



| Attribute  | Type                      | Required | Description                                                      | Possible Values           |
|------------|---------------------------|----------|------------------------------------------------------------------|---------------------------|
| **StartX** | **xs:nonNegativeInteger** | Required | The X value for the point marking the beginning of the baseline. | Any non-negative integer. |
| **StartY** | **xs:nonNegativeInteger** | Required | The Y value for the point marking the beginning of the baseline. | Any non-negative integer. |
| **EndX**   | **xs:nonNegativeInteger** | Required | The X value for the point marking the end of the baseline.       | Any non-negative integer. |



 

## Element Information



|                  | Value                                                         |
|------------------|---------------------------------------------------------------|
| **Element type** | [**BaselineType**](baselinetype-complex-type.md) complexType |
| **Namespace**    | urn:schemas-microsoft-com:tabletpc:richink                    |
| **Schema name**  | Journal Reader                                                |



 

 

 



