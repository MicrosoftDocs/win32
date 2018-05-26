---
Description: Retrieves the HTTP status text.
ms.assetid: 480babbd-432c-4722-98df-a73ba5928e1f
title: IWinHttpRequestStatusText property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWinHttpRequest::StatusText property

The **StatusText** property retrieves the HTTP status text.

This property is read-only.

## Syntax


```C++
HRESULT get_StatusText(
  [out, retval] BSTR *Status
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
<td><pre><code>StatusText = WinHttpRequest.StatusText</code></pre></td>
</tr>
</tbody>
</table>



## Property value

**BSTR** that receives the HTTP status text.

## Error codes

The return value is **S\_OK** on success or an error value otherwise.

## Remarks

Retrieves the text portion of the server response line, making available the "user-friendly" equivalent to the numeric HTTP status code. The results of this property are valid only after the [**Send**](iwinhttprequest-send.md) method has successfully completed.

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Examples

The following example shows how to open an HTTP connection, send an HTTP request, display the [**Status**](iwinhttprequest-status.md) and **StatusText**, and read the response text. This example must be run from a command prompt.


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

int main()
{
    // Variable for return value
    HRESULT    hr;

    // Initialize COM.
    hr = CoInitialize( NULL );

    IWinHttpRequest *  pIWinHttpRequest = NULL;

    BSTR            bstrResponse = NULL;
    VARIANT         varFalse;
    VARIANT         varEmpty;
    LONG            lStatus = 0;
    BSTR            bstrStatusText = NULL;

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
    if (SUCCEEDED(hr))
    {    // Open WinHttpRequest.
        BSTR bstrMethod  = SysAllocString(L"GET");
        BSTR bstrUrl = SysAllocString(L"http://microsoft.com");
        hr = pIWinHttpRequest->Open(bstrMethod, bstrUrl, varFalse);
        SysFreeString(bstrMethod);
        SysFreeString(bstrUrl);
    }
    if (SUCCEEDED(hr))
    {    // Send Request.
        hr = pIWinHttpRequest->Send(varEmpty);
    }
    if (SUCCEEDED(hr))
    {    // Send Request.
        hr = pIWinHttpRequest->get_Status(&amp;lStatus);
        hr = pIWinHttpRequest->get_StatusText(&amp;bstrStatusText);
    }
    if (SUCCEEDED(hr))
    {    // Get Response text.
        hr = pIWinHttpRequest->GetAllResponseHeaders(&amp;bstrResponse);
    }
    if (SUCCEEDED(hr))
    {    // Print response to console.
        wprintf(L"%s\n\n", bstrResponse);
        wprintf(L"%u - %s\n\n", lStatus, bstrStatusText);
    }

    // Release memory.
    if (pIWinHttpRequest)
        pIWinHttpRequest->Release();
    if (bstrStatusText)
        SysFreeString(bstrStatusText);
    if (bstrResponse)
        SysFreeString(bstrResponse);

    CoUninitialize();
    return 0;
}

```



The following scripting example shows how to open an HTTP connection, send an HTTP request, display the [**Status**](iwinhttprequest-status.md) and **StatusText**, and read the response headers.


```JScript
// Instantiate a WinHttpRequest object.
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");

// Initialize an HTTP request.  
WinHttpReq.Open("GET", "http://www.microsoft.com", false);

// Send the HTTP request.
WinHttpReq.Send(); 

// Display the status.
WScript.Echo( WinHttpReq.Status + " - " + WinHttpReq.StatusText);

// Display the date header.
WScript.Echo( WinHttpReq.GetAllResponseHeaders());
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

[**Status**](iwinhttprequest-status.md)
</dt> <dt>

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




