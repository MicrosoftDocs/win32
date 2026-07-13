---
title: Using Macros for Error Handling
description: COM defines a number of macros that make it easier to work with HRESULT values.
ms.assetid: ad28eb80-cab9-4bec-9601-34660f6dcad4
ms.topic: concept-article
ms.date: 05/31/2018
---

# Using Macros for Error Handling

COM defines a number of macros that make it easier to work with **HRESULT** values.

The error handling macros are described in the following table.




| Macro | Description | 
|-------|-------------|
| [**MAKE_HRESULT**](/windows/desktop/api/dmerror/nf-dmerror-make_hresult)<br> | Returns an **HRESULT** given the severity bit, facility code, and error code that comprise the **HRESULT**.<br> **Note:** Calling [**MAKE_HRESULT**](/windows/desktop/api/dmerror/nf-dmerror-make_hresult) for S_OK verification carries a performance penalty. You should not routinely use **MAKE_HRESULT** for successful results.<br> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-make_scode"><strong>MAKE_SCODE</strong></a><br /> | Returns an <strong>SCODE</strong> given the severity bit, facility code, and error code that comprise the <strong>SCODE</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-hresult_code"><strong>HRESULT_CODE</strong></a><br /> | Extracts the error code portion of the <strong>HRESULT</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-hresult_facility"><strong>HRESULT_FACILITY</strong></a><br /> | Extracts the facility code of the <strong>HRESULT</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-hresult_severity"><strong>HRESULT_SEVERITY</strong></a><br /> | Extracts the severity bit of the <strong>HRESULT</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-scode_code"><strong>SCODE_CODE</strong></a><br /> | Extracts the error code portion of the <strong>SCODE</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-scode_facility"><strong>SCODE_FACILITY</strong></a><br /> | Extracts the facility code of the <strong>SCODE</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-scode_severity"><strong>SCODE_SEVERITY</strong></a><br /> | Extracts the severity field of the <strong>SCODE</strong>.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-succeeded"><strong>SUCCEEDED</strong></a><br /> | Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is zero and <strong>FALSE</strong> if it is one.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-failed"><strong>FAILED</strong></a><br /> | Tests the severity bit of the <strong>SCODE</strong> or <strong>HRESULT</strong>; returns <strong>TRUE</strong> if the severity is one and <strong>FALSE</strong> if it is zero.<br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-is_error"><strong>IS_ERROR</strong></a><br /> | Provides a generic test for errors on any status value. <br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-hresult_from_win32"><strong>HRESULT_FROM_WIN32</strong></a><br /> | Maps a <a href="/windows/desktop/Debug/system-error-codes">system error code</a> to an <strong>HRESULT</strong> value. <br /> | 
| <a href="/windows/desktop/api/Winerror/nf-winerror-hresult_from_nt"><strong>HRESULT_FROM_NT</strong></a><br /> | Maps an NT status value to an <strong>HRESULT</strong> value.<br /> | 




 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

