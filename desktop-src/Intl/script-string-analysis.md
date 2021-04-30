---
description: Defines some or all of the character attributes, glyphs, advance widths, x and y positions, character-to-glyph mappings, and so forth, for a string.
ms.assetid: aa93d631-3cfc-449d-9d04-c1f851129c6c
title: SCRIPT_STRING_ANALYSIS (Usp10.h)
ms.topic: reference
ms.date: 05/31/2018
---

# SCRIPT\_STRING\_ANALYSIS

Defines some or all of the character attributes, glyphs, advance widths, x and y positions, character-to-glyph mappings, and so forth, for a string.


```C++
typedef void* SCRIPT_STRING_ANALYSIS;
```



## Remarks

This is an opaque structure that is allocated dynamically and retrieved by [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse). It is required for all other **ScriptString\*** functions, as well.

Since the analysis can be large, it is important for your application to call [**ScriptStringFree**](/windows/desktop/api/Usp10/nf-usp10-scriptstringfree) as soon as it has finished with the string.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                               |
| Redistributable<br/>          | Internet Explorer 5 or later onWindows Me/98/95<br/>                         |
| Header<br/>                   | <dl> <dt>Usp10.h</dt> </dl> |



## See also

<dl> <dt>

[Uniscribe](uniscribe.md)
</dt> <dt>

[Uniscribe Structures](uniscribe-structures.md)
</dt> <dt>

[**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse)
</dt> <dt>

[**ScriptStringFree**](script-string-analysis.md)
</dt> </dl>

 

 




