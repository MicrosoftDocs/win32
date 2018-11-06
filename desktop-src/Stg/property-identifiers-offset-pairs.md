---
title: Property Identifiers/Offset Pairs
description: Following the Count of Properties property set value is an array of Property Identifiers/Offset Pairs property set values.
ms.assetid: 341608a1-3ab1-4fa9-ab9a-4124c63c78a7
ms.topic: article
ms.date: 05/31/2018
---

# Property Identifiers/Offset Pairs

Following the Count of Properties property set value is an array of Property Identifiers/Offset Pairs property set values. Property Identifiers are 32-bit values that uniquely identify a property within a section. The Offset Pairs indicate the distance from the start of the section to the start of the property Type/Value Pair. Because the offsets are relative to the section, sections can be copied as an array of bytes.

Property identifiers are not sorted in any particular order. Properties can be omitted from the stored property set; readers must not rely on a specific order or range of property identifiers.

 

 




