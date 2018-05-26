---
Description: When the application is dealing with whole words, valid positions for the caret are marked by the value of the fWordStop member of the SCRIPT\_LOGATTR structure. This value is retrieved by making a call to ScriptBreak.
ms.assetid: c9bbfb51-727a-45ff-8450-774bc106f9f7
title: Using Word Break Points
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Word Break Points

When the application is dealing with whole words, valid positions for the caret are marked by the value of the **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/Usp10/ns-usp10-tag_script_logattr?branch=master) structure. This value is retrieved by making a call to [**ScriptBreak**](/windows/win32/Usp10/nf-usp10-scriptbreak?branch=master).

Valid positions for breaking lines between words are marked by the **fSoftBreak** value retrieved by [**ScriptBreak**](/windows/win32/Usp10/nf-usp10-scriptbreak?branch=master).

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



