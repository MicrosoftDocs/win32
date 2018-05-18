---
Description: 'For an application dealing with unformatted text, Uniscribe provides the ScriptString\* functions.'
ms.assetid: 'bfbba5df-ce06-4012-a7b1-55d8ea580942'
title: Using the ScriptString Functions
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
<td>[<strong>ScriptStringAnalyse</strong>](scriptstringanalyse.md)</td>
<td>Analyzes plain text. This function corresponds to the following functions:<br/> <dl>[<strong>ScriptItemize</strong>](scriptitemize.md)<br />
[<strong>ScriptShape</strong>](scriptshape.md)<br />
[<strong>ScriptPlace</strong>](scriptplace.md)<br />
[<strong>ScriptBreak</strong>](scriptbreak.md)<br />
[<strong>ScriptGetCMap</strong>](scriptgetcmap.md)<br />
[<strong>ScriptJustify</strong>](scriptjustify.md)<br />
[<strong>ScriptLayout</strong>](scriptlayout.md)<br />
</dl></td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringCPtoX</strong>](scriptstringcptox.md)</td>
<td>Retrieves the x coordinate for a character position. This function corresponds to [<strong>ScriptCPtoX</strong>](scriptcptox.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringFree</strong>](scriptstringfree.md)</td>
<td>Frees a [<strong>SCRIPT_STRING_ANALYSIS</strong>](script-string-analysis.md) structure.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringGetLogicalWidths</strong>](scriptstringgetlogicalwidths.md)</td>
<td>Converts visual widths to logical widths. This function corresponds to [<strong>ScriptGetLogicalWidths</strong>](scriptgetlogicalwidths.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringGetOrder</strong>](scriptstringgetorder.md)</td>
<td>Maps character glyph positions in a similar way to [GetCharacterPlacement](gdi.getcharacterplacement), for legacy use only. This function does not work well with scripts that generate more than one glyph per code point.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringOut</strong>](scriptstringout.md)</td>
<td>Displays plain text. This function corresponds to [<strong>ScriptTextOut</strong>](scripttextout.md).</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pcOutChars</strong>](scriptstring-pcoutchars.md)</td>
<td>Returns a pointer to the length of a clipped plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptString_pLogAttr</strong>](scriptstring-plogattr.md)</td>
<td>Returns a pointer to the logical attributes buffer for an analyzed plain text string.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptString_pSize</strong>](scriptstring-psize.md)</td>
<td>Returns a pointer to the size (width and height) for an analyzed plain text string.</td>
</tr>
<tr class="even">
<td>[<strong>ScriptStringValidate</strong>](scriptstringvalidate.md)</td>
<td>Identifies code point sequences not valid in the given script. This function is different from [<strong>ScriptGetCMap</strong>](scriptgetcmap.md), which identifies code points not present in a font.</td>
</tr>
<tr class="odd">
<td>[<strong>ScriptStringXtoCP</strong>](scriptstringxtocp.md)</td>
<td>Converts an x coordinate to a character position. This function corresponds to [<strong>ScriptXtoCP</strong>](scriptxtocp.md).</td>
</tr>
</tbody>
</table>



 

To only display plain text without any modifications, an application should call [**ScriptStringAnalyse**](scriptstringanalyse.md), [**ScriptStringOut**](scriptstringout.md), and then [**ScriptStringFree**](scriptstringfree.md). The other functions are used to modify the plain text before display.

## Related topics

<dl> <dt>

[Using Uniscribe](using-uniscribe.md)
</dt> </dl>

 

 




