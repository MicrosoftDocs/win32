---
title: Using Macros for Error Handling
description: COM defines a number of macros that make it easier to work with HRESULT values.
ms.assetid: 'ad28eb80-cab9-4bec-9601-34660f6dcad4'
---

# Using Macros for Error Handling

COM defines a number of macros that make it easier to work with **HRESULT** values.

The error handling macros are described in the following table.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Macro</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>MAKE_HRESULT</strong>](make-hresult-macro.md)<br/></td>
<td>Returns an <strong>HRESULT</strong> given the severity bit, facility code, and error code that comprise the <strong>HRESULT</strong>.<br/>
<blockquote>
[!Note]<br />
Calling [<strong>MAKE_HRESULT</strong>](make-hresult-macro.md) for S_OK verification carries a performance penalty. You should not routinely use <strong>MAKE_HRESULT</strong> for successful results.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>MAKE_SCODE</strong>](make-scode-macro.md)<br/></td>
<td>Returns an <strong>SCODE</strong> given the severity bit, facility code, and error code that comprise the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_CODE</strong>](hresult-code-macro.md)<br/></td>
<td>Extracts the error code portion of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>HRESULT_FACILITY</strong>](hresult-facility-macro.md)<br/></td>
<td>Extracts the facility code of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_SEVERITY</strong>](hresult-severity-macro.md)<br/></td>
<td>Extracts the severity bit of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCODE_CODE</strong>](scode-code-macro.md)<br/></td>
<td>Extracts the error code portion of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCODE_FACILITY</strong>](scode-facility-macro.md)<br/></td>
<td>Extracts the facility code of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCODE_SEVERITY</strong>](scode-severity-macro.md)<br/></td>
<td>Extracts the severity field of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SUCCEEDED</strong>](succeeded-macro.md)<br/></td>
<td>Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is zero and <strong>FALSE</strong> if it is one.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FAILED</strong>](failed-macro.md)<br/></td>
<td>Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is one and <strong>FALSE</strong> if it is zero.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IS_ERROR</strong>](is-error-macro.md)<br/></td>
<td>Provides a generic test for errors on any status value. <br/></td>
</tr>
<tr class="even">
<td>[<strong>HRESULT_FROM_WIN32</strong>](hresult-from-win32-macro.md)<br/></td>
<td>Maps a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381) to an <strong>HRESULT</strong> value. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_FROM_NT</strong>](hresult-from-nt-macro.md)<br/></td>
<td>Maps an NT status value to an <strong>HRESULT</strong> value.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 





