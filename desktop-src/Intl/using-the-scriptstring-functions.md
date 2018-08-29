---
Description: For an application dealing with unformatted text, Uniscribe provides the ScriptString\* functions.
ms.assetid: bfbba5df-ce06-4012-a7b1-55d8ea580942
title: Using the ScriptString Functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using the ScriptString Functions

For an application dealing with unformatted text, Uniscribe provides the **ScriptString\*** functions. These functions are similar to [**ExtTextOut**](https://msdn.microsoft.com/en-us/library/Dd162713(v=VS.85).aspx), [**DrawText**](https://msdn.microsoft.com/en-us/library/Dd162498(v=VS.85).aspx), and [**GetTextExtent**](CDC::GetTextExtent), but they provide full complex script support, including caret placement. These functions are similar to the other Uniscribe functions, but are tailored to the simpler requirements of plain text processing.

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
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse"><strong>ScriptStringAnalyse</strong></a></td>
<td>Analyzes plain text. This function corresponds to the following functions:<br/> <dl><a href="/windows/desktop/api/Usp10/nf-usp10-scriptitemize"><strong>ScriptItemize</strong></a><br />
[<strong>ScriptShape</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptshape)<br />
[<strong>ScriptPlace</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptplace)<br />
[<strong>ScriptBreak</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptbreak)<br />
[<strong>ScriptGetCMap</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap)<br />
[<strong>ScriptJustify</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptjustify)<br />
[<strong>ScriptLayout</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptlayout)<br />
</dl></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringcptox"><strong>ScriptStringCPtoX</strong></a></td>
<td>Retrieves the x coordinate for a character position. This function corresponds to <a href="/windows/desktop/api/Usp10/nf-usp10-scriptcptox"><strong>ScriptCPtoX</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringfree"><strong>ScriptStringFree</strong></a></td>
<td>Frees a <a href="script-string-analysis"><strong>SCRIPT_STRING_ANALYSIS</strong></a> structure.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringgetlogicalwidths"><strong>ScriptStringGetLogicalWidths</strong></a></td>
<td>Converts visual widths to logical widths. This function corresponds to <a href="/windows/desktop/api/Usp10/nf-usp10-scriptgetlogicalwidths"><strong>ScriptGetLogicalWidths</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringgetorder"><strong>ScriptStringGetOrder</strong></a></td>
<td>Maps character glyph positions in a similar way to <a href="https://msdn.microsoft.com/en-us/library/Dd144860(v=VS.85).aspx">GetCharacterPlacement</a>, for legacy use only. This function does not work well with scripts that generate more than one glyph per code point.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringout"><strong>ScriptStringOut</strong></a></td>
<td>Displays plain text. This function corresponds to <a href="/windows/desktop/api/Usp10/nf-usp10-scripttextout"><strong>ScriptTextOut</strong></a>.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstring_pcoutchars"><strong>ScriptString_pcOutChars</strong></a></td>
<td>Returns a pointer to the length of a clipped plain text string.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstring_plogattr"><strong>ScriptString_pLogAttr</strong></a></td>
<td>Returns a pointer to the logical attributes buffer for an analyzed plain text string.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstring_psize"><strong>ScriptString_pSize</strong></a></td>
<td>Returns a pointer to the size (width and height) for an analyzed plain text string.</td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringvalidate"><strong>ScriptStringValidate</strong></a></td>
<td>Identifies code point sequences not valid in the given script. This function is different from [<strong>ScriptGetCMap</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap), which identifies code points not present in a font.</td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Usp10/nf-usp10-scriptstringxtocp"><strong>ScriptStringXtoCP</strong></a></td>
<td>Converts an x coordinate to a character position. This function corresponds to <a href="/windows/desktop/api/Usp10/nf-usp10-scriptxtocp"><strong>ScriptXtoCP</strong></a>.</td>
</tr>
</tbody>
</table>



 

To only display plain text without any modifications, an application should call [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse), [**ScriptStringOut**](/windows/desktop/api/Usp10/nf-usp10-scriptstringout), and then [**ScriptStringFree**](/windows/desktop/api/Usp10/nf-usp10-scriptstringfree). The other functions are used to modify the plain text before display.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




