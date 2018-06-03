---
title: Rich Edit Functions
description: .
ms.assetid: 5e913cb6-d561-447f-b33e-9160a8f46cda
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
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
<td>[<em>AutoCorrectProc</em>](/windows/desktop/api/Richedit/nc-richedit-autocorrectproc)<br/></td>
<td>The [<em>AutoCorrectProc</em>](/windows/desktop/api/Richedit/nc-richedit-autocorrectproc) function is an application-defined callback function that is used with the [<strong>EM_SETAUTOCORRECTPROC</strong>](em-setautocorrectproc.md) message.<br/></td>
</tr>
<tr class="even">
<td>[<em>EditStreamCallback</em>](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback)<br/></td>
<td>The [<em>EditStreamCallback</em>](/windows/desktop/api/Richedit/nc-richedit-editstreamcallback) function is an application defined callback function used with the [<strong>EM_STREAMIN</strong>](em-streamin.md) and [<strong>EM_STREAMOUT</strong>](em-streamout.md) messages. It is used to transfer a stream of data into or out of a rich edit control. The <strong>EDITSTREAMCALLBACK</strong> type defines a pointer to this callback function. <em>EditStreamCallback</em> is a placeholder for the application-defined function name. <br/></td>
</tr>
<tr class="odd">
<td>[<em>EditWordBreakProcEx</em>](/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex)<br/></td>
<td>The [<em>EditWordBreakProcEx</em>](/windows/desktop/api/Richedit/nc-richedit-editwordbreakprocex) function is an application defined callback function used with the [<strong>EM_SETWORDBREAKPROCEX</strong>](em-setwordbreakprocex.md) message. It determines the character index of the word break or the character class and word-break flags of the characters in the specified text. The <strong>EDITWORDBREAKPROCEX</strong> type defines a pointer to this callback function. <em>EditWordBreakProcEx</em> is a placeholder for the application-defined function name. <br/></td>
</tr>
<tr class="even">
<td>[<strong>GetMathAlphanumeric</strong>](/windows/desktop/api/Tom/)<br/></td>
<td>Retrieves the Unicode Transformation Format (UTF)-32 math alphanumeric character that corresponds to the specified Basic Multilingual Plane (BMP) character and math style. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>GetMathAlphanumericCode</strong>](/windows/desktop/api/Tom/)<br/></td>
<td>Retrieves the math style and the upright Basic Multilingual Plane (BMP) character code that corresponds to the specified trailing byte of a math surrogate pair.<br/></td>
</tr>
<tr class="even">
<td>[<em>HyphenateProc</em>](/windows/desktop/api/Richedit/nf-richedit-hyphenateproc)<br/></td>
<td>The [<em>HyphenateProc</em>](/windows/desktop/api/Richedit/nf-richedit-hyphenateproc) function is an application defined callback function used with the [<strong>EM_SETHYPHENATEINFO</strong>](em-sethyphenateinfo.md) message. It determines how hyphenation is done in a Microsoft Rich Edit control.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MathBuildDown</strong>](/windows/desktop/api/Tom/)<br/></td>
<td>Translates the built-up math, ruby, and other inline objects in the specified range to linear form.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MathBuildUp</strong>](/windows/desktop/api/Tom/)<br/></td>
<td>Converts the linear-format math in a range to a built-up form, or modifies the current built-up form. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MathTranslate</strong>](/windows/desktop/api/Tom/)<br/></td>
<td>Translates the math characters in the specified range.<br/></td>
</tr>
<tr class="even">
<td>[<strong>REExtendedRegisterClass</strong>](reextendedregisterclass.md)<br/></td>
<td>Registers two class names, REListBox20W and RECombobox20W, that could be used to create Rich Edit listbox or combobox windows. <br/>
<blockquote>
[!Note]<br />
Intended for internal use; not recommended for use in applications. This function may not be supported in future versions.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 





