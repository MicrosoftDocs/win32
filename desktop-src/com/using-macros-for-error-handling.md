---
title: Using Macros for Error Handling
description: COM defines a number of macros that make it easier to work with HRESULT values.
ms.assetid: ad28eb80-cab9-4bec-9601-34660f6dcad4
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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
<td>[<strong>MAKE_HRESULT</strong>](/windows/desktop/api/dmerror/nf-dmerror-make_hresult)<br/></td>
<td>Returns an <strong>HRESULT</strong> given the severity bit, facility code, and error code that comprise the <strong>HRESULT</strong>.<br/>
<blockquote>
[!Note]<br />
Calling [<strong>MAKE_HRESULT</strong>](/windows/desktop/api/dmerror/nf-dmerror-make_hresult) for S_OK verification carries a performance penalty. You should not routinely use <strong>MAKE_HRESULT</strong> for successful results.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>MAKE_SCODE</strong>](/windows/desktop/api/Winerror/nf-winerror-make_scode)<br/></td>
<td>Returns an <strong>SCODE</strong> given the severity bit, facility code, and error code that comprise the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_CODE</strong>](/windows/desktop/api/Winerror/nf-winerror-hresult_code)<br/></td>
<td>Extracts the error code portion of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>HRESULT_FACILITY</strong>](/windows/desktop/api/Winerror/nf-winerror-hresult_facility)<br/></td>
<td>Extracts the facility code of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_SEVERITY</strong>](/windows/desktop/api/Winerror/nf-winerror-hresult_severity)<br/></td>
<td>Extracts the severity bit of the <strong>HRESULT</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCODE_CODE</strong>](/windows/desktop/api/Winerror/nf-winerror-scode_code)<br/></td>
<td>Extracts the error code portion of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCODE_FACILITY</strong>](/windows/desktop/api/Winerror/nf-winerror-scode_facility)<br/></td>
<td>Extracts the facility code of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCODE_SEVERITY</strong>](/windows/desktop/api/Winerror/nf-winerror-scode_severity)<br/></td>
<td>Extracts the severity field of the <strong>SCODE</strong>.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SUCCEEDED</strong>](/windows/desktop/api/Winerror/nf-winerror-succeeded)<br/></td>
<td>Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is zero and <strong>FALSE</strong> if it is one.<br/></td>
</tr>
<tr class="even">
<td>[<strong>FAILED</strong>](/windows/desktop/api/Winerror/nf-winerror-failed)<br/></td>
<td>Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is one and <strong>FALSE</strong> if it is zero.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IS_ERROR</strong>](/windows/desktop/api/Winerror/nf-winerror-is_error)<br/></td>
<td>Provides a generic test for errors on any status value. <br/></td>
</tr>
<tr class="even">
<td>[<strong>HRESULT_FROM_WIN32</strong>](/windows/desktop/api/Winerror/nf-winerror-hresult_from_win32)<br/></td>
<td>Maps a [system error code](https://msdn.microsoft.com/library/windows/desktop/ms681381) to an <strong>HRESULT</strong> value. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>HRESULT_FROM_NT</strong>](/windows/desktop/api/Winerror/nf-winerror-hresult_from_nt)<br/></td>
<td>Maps an NT status value to an <strong>HRESULT</strong> value.<br/></td>
</tr>
</tbody>
</table>



 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 





