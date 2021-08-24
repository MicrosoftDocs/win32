---
description: Implementing IAMErrorLog
ms.assetid: 0a380854-f3a9-4077-a481-dda67737d4c8
title: Implementing IAMErrorLog
ms.topic: article
ms.date: 05/31/2018
---

# Implementing IAMErrorLog

\[This API is not supported and may be altered or unavailable in the future.\]

The [**IAMErrorLog**](iamerrorlog.md) interface contains a single method, [**LogError**](iamerrorlog-logerror.md). The parameters to the method contain information about the error that occurred.


```C++
STDMETHODIMP LogError(
    LONG Severity,          // Reserved. Do not use.
    BSTR ErrorString,       // Description.
    LONG ErrorCode,         // Error code.
    HRESULT hresult,        // HRESULT that caused the error.
    VARIANT *pExtraInfo);   // Extra information about the error.
```



The error code and the error string are defined by DirectShow Editing Services. For a list of errors, see [Rendering Errors](rendering-errors.md).

The *pExtraInfo* parameter contains a pointer to a VARIANT type that holds additional information about the error. The data type and contents of the VARIANT depend on the specific error that occurred. For example, if the error was caused by an incorrect file name, the VARIANT is a string with the bad file name. Some errors do not have extra information, so *pExtraInfo* might be **NULL**. The following code shows how to test the **vt** member of the VARIANT, which indicates the data type, and format a message accordingly.


```C++
if( pExtraInfo )    // Report extra information, if any. 
{                           
    printf("\tExtra info: ");
    if( pExtraInfo->vt == VT_BSTR )      // Extra info is a BSTR.
    {
        UINT len = SysStringLen(pExtraInfo->bstrVal);
        char *szExtra = new char[len];
        if (szExtra != NULL)
        {
            // Note - If the BSTR contains embedded NULL characters, this
            // will only pick up the first sub-string.
            WideCharToMultiByte(CP_ACP, 0, pExtraInfo->bstrVal, -1, 
                szExtra, len, 0, 0);
            printf("%s\n", szExtra);
            delete [] szExtra;
        }
    } 
    else if( pExtraInfo->vt == VT_I4 )   // Extra info is an integer.
        printf("%d\n", pExtraInfo->lVal);

    else if( pExtraInfo->vt == VT_R8 )   // Extra info is floating-point.
        printf("%f\n", pExtraInfo->dblVal);
}
```



> [!Note]  
> Do not free the VARIANT pointed to by
>
> 
>
> 
| 
|
| <pre><code>pExtraInfo</code></pre> | 

>
> 
>
> . Also, the VARIANT becomes invalid after the method returns, so do not reference it later.

 

## Related topics

<dl> <dt>

[Logging Errors](logging-errors.md)
</dt> </dl>

 

 



