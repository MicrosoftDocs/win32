---
description: This topic is not current. For the most current information, see the Print Schema Specification.
ms.assetid: 78df6acf-eb4e-46c1-bf1d-c0a99cf49bff
title: ParameterRef Elements
ms.topic: article
ms.date: 05/31/2018
---

# ParameterRef Elements

This topic is not current. For the most current information, see the [Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip).

ParameterRef elements specifically apply to Option elements, allowing the ability for that Option element to refer to a particular ParameterDef element. For these Option elements, a ScoredProperty element that characterizes the Option is not hard-coded in the PrintCapabilities document as a Value, but instead is variable. To enable this variability, these ScoredProperty elements contain a ParameterRef element. A ScoredProperty element may not contain both a Value element and a ParameterRef element. Option elements containing one or more ParameterRef elements are called parameterized Option elements.

The Print Schema Framework allows an Option element to contain any number of ScoredProperty elements that refer to Parameter elements, together with any number of ScoredProperty elements that contain Value elements. The Framework also allows any number of Feature elements to contain parameterized Option elements, and any number of parameterized Option elements are permitted for each Feature element. Also, the same parameter construct can be referred to by several different Option elements, Option elements that can belong to the same or different Feature elements.

## Related topics

<dl> <dt>

[Print Schema Specification](https://download.microsoft.com/download/D/E/C/DECA6E6B-3E81-48E7-B7EF-6D92A547D03C/print-schema-spec-2-0.zip)
</dt> </dl>

 

 



