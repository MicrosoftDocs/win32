---
Description: Retrieves the response entity body as an IStream.
ms.assetid: e12a9338-5e0c-4672-bbc6-31375b872e94
title: IWinHttpRequestResponseStream property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWinHttpRequest::ResponseStream property

The **ResponseStream** property retrieves the response entity body as an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034).

This property is read-only.

## Syntax


```C++
HRESULT get_ResponseStream(
  [out, retval] VARIANT *Body
);
```

<span codelanguage="JScript"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>JScript</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>vtResponseStream = WinHttpRequest.ResponseStream</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A **Variant** that receives a pointer to an [**IUnknown**](_com_iunknown) interface that can be queried for an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) interface. This stream returns the raw data as received directly from the server.

## Error codes

The return value is **S\_OK** on success or an error value otherwise.

It will be **E\_PENDING** if the previous [**Send**](iwinhttprequest-send.md) operation is not complete.

## Remarks

Call [**QueryInterface**](_com_iunknown_queryinterface) on the returned pointer to obtain a pointer to an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034) interface. This property returns the response data as an **IStream**. This property can only be invoked after the [**Send**](iwinhttprequest-send.md) method has been called.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Examples

The following example shows how to open an HTTP connection, send an HTTP request, and read the response as an [**IStream**](https://msdn.microsoft.com/library/windows/desktop/aa380034). The data from the **IStream** is written to the file Temp1.gif.


```C++
#include <windows.h>
#include <stdio.h>
#include <objbase.h>

#include "httprequest.h"

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")

// IID for IWinHttpRequest.
const IID IID_IWinHttpRequest =
{
  0x06f29373,
  0x5c5a,
  0x4b54,
  {0xb0, 0x25, 0x6e, 0xf1, 0xbf, 0x8a, 0xbf, 0x0e}
};

#define Trace(_s) fprintf(stderr, _s) 
#define TraceErr(_s, _hr) fprintf(stderr, _s, _hr) 
#define Check(_hr,_s) if (FAILED(_hr)) { fprintf(stderr, _s ## " 0x%08lx\n", _hr); return -1; }

int main(int argc, char* argv[])
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    // Variable for return value.
    HRESULT    hr;

    // Initialize COM.
    hr = CoInitialize( NULL );

    IWinHttpRequest *  pIWinHttpRequest = NULL;

    BSTR            bstrResponse = NULL;
    VARIANT         varFalse;
    VARIANT         varEmpty;
    VARIANT            varResponse;

    VariantInit(&amp;varResponse);
    
    CLSID           clsid;

    VariantInit(&amp;varFalse);
    V_VT(&amp;varFalse)   = VT_BOOL;
    V_BOOL(&amp;varFalse) = VARIANT_FALSE;

    VariantInit(&amp;varEmpty);
    V_VT(&amp;varEmpty) = VT_ERROR;

    hr = CLSIDFromProgID(L"WinHttp.WinHttpRequest.5.1", &amp;clsid);

    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(clsid, NULL, 
                              CLSCTX_INPROC_SERVER, 
                              IID_IWinHttpRequest, 
                              (void **)&amp;pIWinHttpRequest);
    }

    // ==== Get binary (.gif) file and write it to disk. =========
    if (SUCCEEDED(hr))
    {    // Open WinHttpRequest for synchronous access.
        BSTR bstrMethod = SysAllocString(L"GET");
        BSTR bstrUrl = SysAllocString(
            L"http://www.microsoft.com/library/homepage/images/ms-banner.gif");
        hr = pIWinHttpRequest->Open(bstrMethod, bstrUrl, varFalse);
        SysFreeString(bstrMethod);
        SysFreeString(bstrUrl);
    }
    if (SUCCEEDED(hr))
    {    // Send Request.
        hr = pIWinHttpRequest->Send(varEmpty);
    }
    if (SUCCEEDED(hr))
    {    // Get response body.
        hr = pIWinHttpRequest->get_ResponseBody(&amp;varResponse);
    }
    if (SUCCEEDED(hr))
    {    // Print response to file temp1.gif.
        long UpperBounds;
        long LowerBounds;
        unsigned char* buff;
        // Verify that varResponse contains array of unsigned bytes.
        if (varResponse.vt == (VT_ARRAY | VT_UI1)) {
            long Dims = SafeArrayGetDim(varResponse.parray);
            // The array should only have 1 dimension.
            if (Dims == 1) {
                // Get upper and lower array bounds.
                SafeArrayGetLBound(varResponse.parray, 1, 
                                   &amp;LowerBounds);
                SafeArrayGetUBound(varResponse.parray, 1, 
                                   &amp;UpperBounds);
                UpperBounds++;
                // Lock SAFEARRAY for access.
                SafeArrayAccessData (varResponse.parray, 
                                     (void**)&amp;buff);
                // Output array to file temp.gif.
                HANDLE hFile; 
                DWORD  dwBytesWritten;
                // Create file.
                hFile = CreateFile(TEXT("Temp1.gif"),     
                    GENERIC_WRITE,              // Open for writing. 
                    0,                          // Do not share. 
                    NULL,                       // No security. 
                    CREATE_ALWAYS,              // Overwrite existing.
                    FILE_ATTRIBUTE_NORMAL,      // Normal file.
                    NULL);                      // No attribute template.

                if (hFile == INVALID_HANDLE_VALUE) 
                    {
                    wprintf(L"Could not open file."); // Process error.
                    }
                else
                    {
                    WriteFile(hFile, buff, UpperBounds - LowerBounds, 
                        &amp;dwBytesWritten, NULL); 
                    }
                CloseHandle(hFile);
                SafeArrayUnaccessData (varResponse.parray);
            }
        }    
    }

    // ======== Get binary (.gif) file and write 
    // it to disk using IStream. ================
    if (SUCCEEDED(hr))
    {    // Open WinHttpRequest for synchronous access.
        BSTR bstrMethod = SysAllocString(L"GET");
        BSTR bstrUrl = SysAllocString(
            L"http://www.microsoft.com/library/homepage/images/ms-banner.gif");
        hr = pIWinHttpRequest->Open(bstrMethod, bstrUrl, varFalse);
        SysFreeString(bstrMethod);
        SysFreeString(bstrUrl);
    }
    if (SUCCEEDED(hr))
    {    // Send Request.
        hr = pIWinHttpRequest->Send(varEmpty);
    }
    if (SUCCEEDED(hr))
    {    // Get Response as an IStream.
        hr = pIWinHttpRequest->get_ResponseStream(&amp;varResponse);
    }
    if (SUCCEEDED(hr))
    {    // Print response to file temp1.gif.
        IStream*    pStream = NULL; 
        BYTE        bBuffer[8192]; 
        DWORD       cb, cbRead, cbWritten; 
        // Check that an IStream was received.
        if (VT_UNKNOWN == V_VT(&amp;varResponse) || 
            VT_STREAM == V_VT(&amp;varResponse)) 
        { 
            // Get IStream interface pStream.
            hr = V_UNKNOWN(&amp;varResponse)->QueryInterface(IID_IStream, 
                                 reinterpret_cast<void**>(&amp;pStream)); 
            Check(hr, "QI for IStream"); 
        } 
        else 
        { 
            wprintf(L"Unexpected vartype for Response\n"); 
            return -1; 
        } 

        HANDLE hFile; 
        // Open file Temp2.gif for output.
        hFile = CreateFile(TEXT("Temp2.gif"),     
            GENERIC_WRITE,                // Open for writing. 
            0,                            // Do not share. 
            NULL,                         // No security. 
            CREATE_ALWAYS,                // Overwrite existing.
            FILE_ATTRIBUTE_NORMAL,        // Normal file.
            NULL);                        // No attribute template.
        if (hFile == INVALID_HANDLE_VALUE) 
            {
            wprintf(L"Could not open file.");  // Process error.
            }
        else
            {
            // Copy data from the response stream to file. 
            cb = sizeof(bBuffer); 
            hr = pStream->Read(bBuffer, cb, &amp;cbRead); 
            while (SUCCEEDED(hr) &amp;&amp; 0 != cbRead) 
                { 
                if (!WriteFile(hFile, bBuffer, 
                               cbRead, &amp;cbWritten, NULL)) 
                    { 
                    TraceErr("WriteFile fails with 0x%08lx\n", 
                             HRESULT_FROM_WIN32(GetLastError())); 
                    return -1; 
                    } 
                hr = pStream->Read(bBuffer, cb, &amp;cbRead); 
                } 
            }
        CloseHandle(hFile);
        pStream->Release(); 
        VariantClear(&amp;varResponse); 
    }
    // Release memory.
    if (pIWinHttpRequest)
        pIWinHttpRequest->Release();
    if (bstrResponse)
        SysFreeString(bstrResponse);
    
    CoUninitialize();
    return 0;
}
```



## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP, Windows 2000 Professional with SP3 \[desktop apps only\]<br/>            |
| Minimum supported server<br/> | Windows Server 2003, Windows 2000 Server with SP3 \[desktop apps only\]<br/>         |
| Redistributable<br/>          | WinHTTP 5.0 and Internet Explorer 5.01 or later on Windows XP and Windows 2000.<br/> |
| IDL<br/>                      | <dl> <dt>HttpRequest.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Winhttp.lib</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Winhttp.dll</dt> </dl>     |



## See also

<dl> <dt>

[**IWinHttpRequest**](iwinhttprequest-interface.md)
</dt> <dt>

[**WinHttpRequest**](winhttprequest.md)
</dt> <dt>

[**ResponseBody**](iwinhttprequest-responsebody.md)
</dt> <dt>

[**ResponseText**](iwinhttprequest-responsetext.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




