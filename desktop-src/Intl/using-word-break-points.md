---
description: When the application is dealing with whole words, valid positions for the caret are marked by the value of the fWordStop member of the SCRIPT\_LOGATTR structure. This value is retrieved by making a call to ScriptBreak.
ms.assetid: c9bbfb51-727a-45ff-8450-774bc106f9f7
title: Using Word Break Points
ms.topic: article
ms.date: 05/31/2018
---

# Using Word Break Points

When the application is dealing with whole words, valid positions for the caret are marked by the value of the **fWordStop** member of the [**SCRIPT\_LOGATTR**](/windows/win32/api/usp10/ns-usp10-script_logattr) structure. This value is retrieved by making a call to [**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak).

Valid positions for breaking lines between words are marked by the **fSoftBreak** value retrieved by [**ScriptBreak**](/windows/desktop/api/Usp10/nf-usp10-scriptbreak).

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 



