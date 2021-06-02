---
description: Contains the confidence rating returned by the Journal ink analyzer for the InkWord.
ms.assetid: cb0ed0d0-5e2f-44a3-b72b-61cbfd22bae8
title: Confidence Element
ms.topic: reference
ms.date: 05/31/2018
---

# Confidence Element

Contains the confidence rating returned by the Journal ink analyzer for the [**InkWord**](inkword-element.md).

## Definition

``` syntax
<xs:element name="Confidence" type="xs:string" minOccurs="0" />
```

## Parent Elements

[**InkWord**](inkword-element.md)

## Values

Valid values for this field include "0", "1", and "2". 0 indicates Strong confidence, 1 indicates Intermediate confidence, and 2 indicates Poor confidence.

## Child Elements

None.

## Attributes

None.

## Element Information



|              |                                            |
|--------------|--------------------------------------------|
| Element type | **xs:string**                              |
| Namespace    | urn:schemas-microsoft-com:tabletpc:richink |
| Schema name  | Journal Reader                             |



 

 

 



