---
Description: The following table shows the various methods that the application can use to handle the caret, justification, and clusters.
ms.assetid: 950a24b4-62ab-4eaf-ac15-87434d3c28c0
title: Working with Relationships Among Caret Positions, Justification Points, and Clusters
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Working with Relationships Among Caret Positions, Justification Points, and Clusters

The following table shows the various methods that the application can use to handle the caret, justification, and clusters.



| Task                             | Uniscribe support                                                                                                                                                                                                                                                              |
|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Caret move by character cluster  | The *pwLogClust* parameter of the [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master) functionThe **fClusterStart** member of the [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master) structure<br/> The **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure<br/> |
| Line breaking between characters | The *pwLogClust* parameter of the [**ScriptShape**](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master) functionThe **fClusterStart** member of the [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master) structure<br/> The **fCharStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure<br/> |
| Caret move by word               | The **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure                                                                                                                                                                                            |
| Line breaking between words      | The **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure                                                                                                                                                                                            |
| Justification                    | The **uJustification** member of the [**SCRIPT\_VISATTR**](/windows/win32/Usp10/ns-usp10-tag_script_visattr?branch=master) structure                                                                                                                                                                                       |



 

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




