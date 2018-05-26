---
Description: For an application dealing with unformatted text, Uniscribe provides the ScriptString\* functions.
ms.assetid: bfbba5df-ce06-4012-a7b1-55d8ea580942
title: Using the ScriptString Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the ScriptString Functions

For an application dealing with unformatted text, Uniscribe provides the **ScriptString\*** functions. These functions are similar to [**ExtTextOut**](gdi.ExtTextOut), [**DrawText**](gdi.DrawText), and [**GetTextExtent**](CDC::GetTextExtent), but they provide full complex script support, including caret placement. These functions are similar to the other Uniscribe functions, but are tailored to the simpler requirements of plain text processing.

The following table details the **ScriptString\*** functions and any counterparts in the other Uniscribe functions.



<table>
<thead>
<tr class="header">
<th>Function</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>ScriptStringAnalyse</strong>](/windows/win32/Usp10/nf-usp10-scriptstringanalyse?branch=master)</td>
<td>Analyzes plain text. This function corresponds to the following functions:<br/> <dl>[<strong>ScriptItemize</strong>](/windows/win32/Usp10/nf-usp10-scriptitemize?branch=master)<br />
[<strong>ScriptShape</strong>](/windows/win32/Usp10/nf-usp10-scriptshape?branch=master)<br />
[<strong>ScriptPlace</strong>](/windows/win32/Usp10/nf-usp10-scriptplace?branch=master)<br />
[<strong>ScriptBreak</strong>](/windows/win32/Usp10/nf-usp10-scriptbreak?branch=master)<br />
[<strong>ScriptGetCMap</strong>](/windows/win32/Usp10/nf-usp10-scriptgetcmap?branch=master)<br />
[<strong>ScriptJustify</strong>](/windows/win32/Usp10/nf-usp10-scriptjustify?branch=master)<br />
[<strong>ScriptLayout</strong>](/windows/win32/Usp10/nf-usp10-scriptlayout?branch=master)<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringCPtoX</strong>](/windows/win32/Usp10/nf-usp10-scriptstringcptox?branch=master)</td>
<td>Retrieves the x coordinate for a character position. This function corresponds to [<strong>ScriptCPtoX</strong>](/windows/win32/Usp10/nf-usp10-scriptcptox?branch=master).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringFree</strong>](/windows/win32/Usp10/nf-usp10-scriptstringfree?branch=master)</td>
<td>Frees a [<strong>SCRIPT_STRING_ANALYSIS</strong>](script-string-analysis.md) structure.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringGetLogicalWidths</strong>](/windows/win32/Usp10/nf-usp10-scriptstringgetlogicalwidths?branch=master)</td>
<td>Converts visual widths to logical widths. This function corresponds to [<strong>ScriptGetLogicalWidths</strong>](/windows/win32/Usp10/nf-usp10-scriptgetlogicalwidths?branch=master).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringGetOrder</strong>](/windows/win32/Usp10/nf-usp10-scriptstringgetorder?branch=master)</td>
<td>Maps character glyph positions in a similar way to [GetCharacterPlacement](gdi.getcharacterplacement), for legacy use only. This function does not work well with scripts that generate more than one glyph per code point.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringOut</strong>](/windows/win32/Usp10/nf-usp10-scriptstringout?branch=master)</td>
<td>Displays plain text. This function corresponds to [<strong>ScriptTextOut</strong>](/windows/win32/Usp10/nf-usp10-scripttextout?branch=master).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pcOutChars</strong>](/windows/win32/Usp10/nf-usp10-scriptstring_pcoutchars?branch=master)</td>
<td>Returns a pointer to the length of a clipped plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptString_pLogAttr</strong>](/windows/win32/Usp10/nf-usp10-scriptstring_plogattr?branch=master)</td>
<td>Returns a pointer to the logical attributes buffer for an analyzed plain text string.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pSize</strong>](/windows/win32/Usp10/nf-usp10-scriptstring_psize?branch=master)</td>
<td>Returns a pointer to the size (width and height) for an analyzed plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringValidate</strong>](/windows/win32/Usp10/nf-usp10-scriptstringvalidate?branch=master)</td>
<td>Identifies code point sequences not valid in the given script. This function is different from [<strong>ScriptGetCMap</strong>](/windows/win32/Usp10/nf-usp10-scriptgetcmap?branch=master), which identifies code points not present in a font.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringXtoCP</strong>](/windows/win32/Usp10/nf-usp10-scriptstringxtocp?branch=master)</td>
<td>Converts an x coordinate to a character position. This function corresponds to [<strong>ScriptXtoCP</strong>](/windows/win32/Usp10/nf-usp10-scriptxtocp?branch=master).</td>
</tr>
</tbody>
</table>



 

To only display plain text without any modifications, an application should call [**ScriptStringAnalyse**](/windows/win32/Usp10/nf-usp10-scriptstringanalyse?branch=master), [**ScriptStringOut**](/windows/win32/Usp10/nf-usp10-scriptstringout?branch=master), and then [**ScriptStringFree**](/windows/win32/Usp10/nf-usp10-scriptstringfree?branch=master). The other functions are used to modify the plain text before display.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




