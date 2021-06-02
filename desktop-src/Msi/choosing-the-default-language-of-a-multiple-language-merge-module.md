---
description: The default language for a merge module is the language that is listed in the ModuleSignature Table of the module before language transforms are applied. This is also the first language that is listed in the Template Summary Property.
ms.assetid: 4d795727-684c-4dc1-8b46-d72b69c455c3
title: Choosing the Default Language of a Multiple Language Merge Module
ms.topic: article
ms.date: 05/31/2018
---

# Choosing the Default Language of a Multiple Language Merge Module

The default language for a merge module is the language that is listed in the [ModuleSignature Table](modulesignature-table.md) of the module before language transforms are applied. This is also the first language that is listed in the [**Template Summary**](template-summary.md) Property.

The default language for the module should be one of the most specific languages that you support, because the default language is always checked first, and if it satisfies the requested language, it is used even if another language is a better match. For example, if a module supports 1033 and 0, 1033 should be the default language. If 0 were the default language, it would always satisfy any request, and the 1033 transform would never be used, even if 1033 is the exact language requested.

 

 



