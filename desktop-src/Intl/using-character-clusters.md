---
description: Character clusters are glyph sequences that cannot be split between lines.
ms.assetid: ab852feb-9e26-429e-a02a-11fe0abdfafc
title: Using Character Clusters
ms.topic: article
ms.date: 05/31/2018
---

# Using Character Clusters

Character clusters are glyph sequences that cannot be split between lines. Some languages, for example Thai and Indic, restrict caret placement to points between clusters. This restriction applies to caret movement initiated with keyboard or mouse actions (hit testing).

Uniscribe provides cluster information in both the visual attributes contained in a [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr) structure, and the logical attributes contained in a [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure. After the application calls [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape), the cluster information is represented both by sequences of the same value in the **SCRIPT\_LOGATTR** array, and by the **fClusterStart** member in the **SCRIPT\_VISATTR** array.

[**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak) also retrieves the **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure to identify cluster positions.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



