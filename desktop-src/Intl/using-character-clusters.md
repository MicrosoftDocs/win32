---
Description: Character clusters are glyph sequences that cannot be split between lines.
ms.assetid: ab852feb-9e26-429e-a02a-11fe0abdfafc
title: Using Character Clusters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Character Clusters

Character clusters are glyph sequences that cannot be split between lines. Some languages, for example Thai and Indic, restrict caret placement to points between clusters. This restriction applies to caret movement initiated with keyboard or mouse actions (hit testing).

Uniscribe provides cluster information in both the visual attributes contained in a [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master) structure, and the logical attributes contained in a [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure. After the application calls [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master), the cluster information is represented both by sequences of the same value in the **SCRIPT\_LOGATTR** array, and by the **fClusterStart** member in the **SCRIPT\_VISATTR** array.

[**ScriptBreak**](/windows/win32/Usp10/nf-usp10-scriptbreak?branch=master) also retrieves the **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure to identify cluster positions.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



