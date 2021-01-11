---
description: TrueType font files include PANOSE numbers, which applications can use to choose a font that closely matches their specifications.
ms.assetid: 39fd56da-c744-432d-9623-92fc7d9bf5f5
title: Using PANOSE Numbers
ms.topic: article
ms.date: 05/31/2018
---

# Using PANOSE Numbers

TrueType font files include PANOSE numbers, which applications can use to choose a font that closely matches their specifications. The PANOSE system classifies faces by 10 different attributes. For more information about these attributes, see [**PANOSE**](/windows/win32/api/wingdi/ns-wingdi-panose). A **PANOSE** structure is part of the [**OUTLINETEXTMETRIC**](/windows/desktop/api/Wingdi/ns-wingdi-outlinetextmetrica) structure (whose values are filled in by calling the [**GetOutlineTextMetrics**](/windows/desktop/api/Wingdi/nf-wingdi-getoutlinetextmetricsa) function).

The PANOSE attributes are rated individually on a scale. The resulting values are concatenated to produce a number. Given this number for a font and a mathematical metric to measure distances in the PANOSE space, an application can determine the nearest neighbors.

 

 



