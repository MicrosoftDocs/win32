---
Description: TrueType font files include PANOSE numbers, which applications can use to choose a font that closely matches their specifications.
ms.assetid: 39fd56da-c744-432d-9623-92fc7d9bf5f5
title: Using PANOSE Numbers
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using PANOSE Numbers

TrueType font files include PANOSE numbers, which applications can use to choose a font that closely matches their specifications. The PANOSE system classifies faces by 10 different attributes. For more information about these attributes, see [**PANOSE**](/windows/win32/Wingdi/ns-wingdi-tagpanose?branch=master). A **PANOSE** structure is part of the [**OUTLINETEXTMETRIC**](/windows/win32/Wingdi/ns-wingdi-_outlinetextmetrica?branch=master) structure (whose values are filled in by calling the [**GetOutlineTextMetrics**](/windows/win32/Wingdi/nf-wingdi-getoutlinetextmetricsa?branch=master) function).

The PANOSE attributes are rated individually on a scale. The resulting values are concatenated to produce a number. Given this number for a font and a mathematical metric to measure distances in the PANOSE space, an application can determine the nearest neighbors.

 

 



