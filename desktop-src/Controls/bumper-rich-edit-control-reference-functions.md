---
title: Rich Edit Functions
description: Rich Edit Functions
ms.assetid: 5e913cb6-d561-447f-b33e-9160a8f46cda
ms.topic: article
ms.date: 05/31/2018
---

# Rich Edit Functions

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="/windows/desktop/api/Richedit/nc-richedit-autocorrectproc"><em>AutoCorrectProc</em></a><br/></td>
<td>The <a href="/windows/desktop/api/Richedit/nc-richedit-autocorrectproc"><em>AutoCorrectProc</em></a> function is an application-defined callback function that is used with the <a href="em-setautocorrectproc.md"><strong>EM_SETAUTOCORRECTPROC</strong></a> message.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Richedit/nc-richedit-editstreamcallback"><em>EditStreamCallback</em></a><br/></td>
<td>The <a href="/windows/desktop/api/Richedit/nc-richedit-editstreamcallback"><em>EditStreamCallback</em></a> function is an application defined callback function used with the <a href="em-streamin.md"><strong>EM_STREAMIN</strong></a> and <a href="em-streamout.md"><strong>EM_STREAMOUT</strong></a> messages. It is used to transfer a stream of data into or out of a rich edit control. The <strong>EDITSTREAMCALLBACK</strong> type defines a pointer to this callback function. <em>EditStreamCallback</em> is a placeholder for the application-defined function name. <br/></td>
</tr>
<tr class="odd">
<td><a href="/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex"><em>EditWordBreakProcEx</em></a><br/></td>
<td>The <a href="/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex"><em>EditWordBreakProcEx</em></a> function is an application defined callback function used with the <a href="em-setwordbreakprocex.md"><strong>EM_SETWORDBREAKPROCEX</strong></a> message. It determines the character index of the word break or the character class and word-break flags of the characters in the specified text. The <strong>EDITWORDBREAKPROCEX</strong> type defines a pointer to this callback function. <em>EditWordBreakProcEx</em> is a placeholder for the application-defined function name. <br/></td>
</tr>
<tr class="even">
<td><a href="/previous-versions/windows/desktop/legacy/hh780353(v=vs.85)"><strong>GetMathAlphanumeric</strong></a><br/></td>
<td>Retrieves the Unicode Transformation Format (UTF)-32 math alphanumeric character that corresponds to the specified Basic Multilingual Plane (BMP) character and math style. <br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/hh780354(v=vs.85)"><strong>GetMathAlphanumericCode</strong></a><br/></td>
<td>Retrieves the math style and the upright Basic Multilingual Plane (BMP) character code that corresponds to the specified trailing byte of a math surrogate pair.<br/></td>
</tr>
<tr class="even">
<td><a href="/windows/desktop/api/Richedit/nf-richedit-hyphenateproc"><em>HyphenateProc</em></a><br/></td>
<td>The <a href="/windows/desktop/api/Richedit/nf-richedit-hyphenateproc"><em>HyphenateProc</em></a> function is an application defined callback function used with the <a href="em-sethyphenateinfo.md"><strong>EM_SETHYPHENATEINFO</strong></a> message. It determines how hyphenation is done in a Microsoft Rich Edit control.<br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/hh780443(v=vs.85)"><strong>MathBuildDown</strong></a><br/></td>
<td>Translates the built-up math, ruby, and other inline objects in the specified range to linear form.<br/></td>
</tr>
<tr class="even">
<td><a href="/previous-versions/windows/desktop/legacy/hh780445(v=vs.85)"><strong>MathBuildUp</strong></a><br/></td>
<td>Converts the linear-format math in a range to a built-up form, or modifies the current built-up form. <br/></td>
</tr>
<tr class="odd">
<td><a href="/previous-versions/windows/desktop/legacy/hh780446(v=vs.85)"><strong>MathTranslate</strong></a><br/></td>
<td>Translates the math characters in the specified range.<br/></td>
</tr>
<tr class="even">
<td><a href="reextendedregisterclass.md"><strong>REExtendedRegisterClass</strong></a><br/></td>
<td>Registers two class names, REListBox20W and RECombobox20W, that could be used to create Rich Edit listbox or combobox windows. <br/>
<blockquote>
[!Note]<br />
Intended for internal use; not recommended for use in applications. This function may not be supported in future versions.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

