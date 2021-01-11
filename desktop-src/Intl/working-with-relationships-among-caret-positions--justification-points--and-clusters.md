---
description: The following table shows the various methods that the application can use to handle the caret, justification, and clusters.
ms.assetid: 950a24b4-62ab-4eaf-ac15-87434d3c28c0
title: Working with Relationships Among Caret Positions, Justification Points, and Clusters
ms.topic: article
ms.date: 05/31/2018
---

# Working with Relationships Among Caret Positions, Justification Points, and Clusters

The following table shows the various methods that the application can use to handle the caret, justification, and clusters.



| Task                             | Uniscribe support                                                                                                                                                                                                                                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Caret move by character cluster  | The *pwLogClust* parameter of the [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) functionThe **fClusterStart** member of the [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr) structure<br/> The **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure<br/> |
| Line breaking between characters | The *pwLogClust* parameter of the [**ScriptShape**](/windows/desktop/api/Usp10/nf-usp10-scriptshape) functionThe **fClusterStart** member of the [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr) structure<br/> The **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure<br/> |
| Caret move by word               | The **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure                                                                                                                                                                                            |
| Line breaking between words      | The **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure                                                                                                                                                                                            |
| Justification                    | The **uJustification** member of the [**SCRIPT\_VISATTR**](/windows/win32/api/usp10/ns-usp10-script_visattr) structure                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




