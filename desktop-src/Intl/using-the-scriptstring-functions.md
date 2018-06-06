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

For an application dealing with unformatted text, Uniscribe provides the **ScriptString\*** functions. These functions are similar to [**ExtTextOut**](https://msdn.microsoft.com/74f8fcb8-8ad4-47f2-a330-fa56713bdb37), [**DrawText**](https://msdn.microsoft.com/fe412280-d797-4abd-8a29-107a9cd96145), and [**GetTextExtent**](CDC::GetTextExtent), but they provide full complex script support, including caret placement. These functions are similar to the other Uniscribe functions, but are tailored to the simpler requirements of plain text processing.

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
<td>[<strong>ScriptStringAnalyse</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse)</td>
<td>Analyzes plain text. This function corresponds to the following functions:<br/> <dl>[<strong>ScriptItemize</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptitemize)<br />
[<strong>ScriptShape</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptshape)<br />
[<strong>ScriptPlace</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptplace)<br />
[<strong>ScriptBreak</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptbreak)<br />
[<strong>ScriptGetCMap</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap)<br />
[<strong>ScriptJustify</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptjustify)<br />
[<strong>ScriptLayout</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptlayout)<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringCPtoX</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringcptox)</td>
<td>Retrieves the x coordinate for a character position. This function corresponds to [<strong>ScriptCPtoX</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptcptox).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringFree</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringfree)</td>
<td>Frees a [<strong>SCRIPT_STRING_ANALYSIS</strong>](script-string-analysis.md) structure.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringGetLogicalWidths</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringgetlogicalwidths)</td>
<td>Converts visual widths to logical widths. This function corresponds to [<strong>ScriptGetLogicalWidths</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptgetlogicalwidths).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringGetOrder</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringgetorder)</td>
<td>Maps character glyph positions in a similar way to [GetCharacterPlacement](https://msdn.microsoft.com/80d3f4b3-503b-4abb-826c-e5c09972ba2f), for legacy use only. This function does not work well with scripts that generate more than one glyph per code point.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringOut</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringout)</td>
<td>Displays plain text. This function corresponds to [<strong>ScriptTextOut</strong>](/windows/desktop/api/Usp10/nf-usp10-scripttextout).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pcOutChars</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstring_pcoutchars)</td>
<td>Returns a pointer to the length of a clipped plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptString_pLogAttr</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstring_plogattr)</td>
<td>Returns a pointer to the logical attributes buffer for an analyzed plain text string.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pSize</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstring_psize)</td>
<td>Returns a pointer to the size (width and height) for an analyzed plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringValidate</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringvalidate)</td>
<td>Identifies code point sequences not valid in the given script. This function is different from [<strong>ScriptGetCMap</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptgetcmap), which identifies code points not present in a font.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringXtoCP</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptstringxtocp)</td>
<td>Converts an x coordinate to a character position. This function corresponds to [<strong>ScriptXtoCP</strong>](/windows/desktop/api/Usp10/nf-usp10-scriptxtocp).</td>
</tr>
</tbody>
</table>



 

To only display plain text without any modifications, an application should call [**ScriptStringAnalyse**](/windows/desktop/api/Usp10/nf-usp10-scriptstringanalyse), [**ScriptStringOut**](/windows/desktop/api/Usp10/nf-usp10-scriptstringout), and then [**ScriptStringFree**](/windows/desktop/api/Usp10/nf-usp10-scriptstringfree). The other functions are used to modify the plain text before display.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




