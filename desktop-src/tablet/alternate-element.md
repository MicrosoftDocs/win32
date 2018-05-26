---
Description: Contains a recognition alternate for an InkWord. The alternates are ordered by the recognizers confidence in the alternate, with highest first.
ms.assetid: 6ec78ac9-c10c-4227-bead-5ddfc48ce27e
title: Alternate Element
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Alternate Element

Contains a recognition alternate for an [**InkWord**](inkword-element.md). The alternates are ordered by the recognizer's confidence in the alternate, with highest first.

## Definition

``` syntax
<xs:element name="Alternate" type="xs:string" minOccurs="0" maxOccurs="unbounded" />
```

## Parent Elements

[**AlternateList**](alternatelist-element.md)

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



 

## Requirements



|                   |                                                                                     |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wingdi.h</dt> </dl> |



 

 




