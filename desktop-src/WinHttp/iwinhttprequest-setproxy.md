---
description: Sets proxy server information.
ms.assetid: 279d0557-2718-4c50-b84c-cc7c8def57a6
title: IWinHttpRequest::SetProxy method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWinHttpRequest.SetProxy
- WinHttpRequest.SetProxy
api_type: 
- COM
api_location: 
- Winhttp.dll
---

# IWinHttpRequest::SetProxy method

The **SetProxy** method sets proxy server information.

## Syntax


```C++
HRESULT SetProxy(
  [in]           HTTPREQUEST_PROXY_SETTING ProxySetting,
  [in, optional] VARIANT                   ProxyServer,
  [in, optional] VARIANT                   BypassList
);
```



## Parameters

<dl> <dt>

*ProxySetting* \[in\]
</dt> <dd>

The flags that control this method. Can be one of the following values.



| Value                                                                                                           | Meaning                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>HTTPREQUEST\_PROXYSETTING\_DEFAULT</dt> </dl>   | Default proxy setting. Equivalent to **HTTPREQUEST\_PROXYSETTING\_PRECONFIG**.<br/>                                                                                                                                                                                                                                                             |
| <dl> <dt>HTTPREQUEST\_PROXYSETTING\_PRECONFIG</dt> </dl> | Indicates that the proxy settings should be obtained from the registry. This assumes that [Proxycfg.exe](proxycfg-exe--a-proxy-configuration-tool.md) has been run. If Proxycfg.exe has not been run and **HTTPREQUEST\_PROXYSETTING\_PRECONFIG** is specified, then the behavior is equivalent to **HTTPREQUEST\_PROXYSETTING\_DIRECT**.<br/> |
| <dl> <dt>HTTPREQUEST\_PROXYSETTING\_DIRECT</dt> </dl>    | Indicates that all HTTP and HTTPS servers should be accessed directly. Use this command if there is no proxy server.<br/>                                                                                                                                                                                                                       |
| <dl> <dt>HTTPREQUEST\_PROXYSETTING\_PROXY</dt> </dl>     | When **HTTPREQUEST\_PROXYSETTING\_PROXY** is specified, *varProxyServer* should be set to a proxy server string and *varBypassList* should be set to a domain bypass list string. This proxy configuration applies only to the current instance of the [**WinHttpRequest**](winhttprequest.md) object.<br/>                                    |



 

</dd> <dt>

*ProxyServer* \[in, optional\]
</dt> <dd>

Set to a proxy server string when *ProxySetting* equals **HTTPREQUEST\_PROXYSETTING\_PROXY**.

</dd> <dt>

*BypassList* \[in, optional\]
</dt> <dd>

Set to a domain bypass list string when *ProxySetting* equals **HTTPREQUEST\_PROXYSETTING\_PROXY**.

</dd> </dl>

## Return value

The return value is **S\_OK** on success or an error value otherwise.

## Remarks

Enables the calling application to specify use of default proxy information (configured by the proxy configuration tool) or to override [Proxycfg.exe](proxycfg-exe--a-proxy-configuration-tool.md). This method must be called before calling the [**Send**](iwinhttprequest-send.md) method. If this method is called after the [**Send**](iwinhttprequest-send.md) method, it has no effect.

[**IWinHttpRequest**](iwinhttprequest-interface.md) passes these parameters to Microsoft Windows HTTP Services (WinHTTP).

> [!Note]  
> For Windows XP and Windows 2000, see the [Run-Time Requirements](winhttp-start-page.md) section of the WinHTTP Start Page.

 

## Examples

The following example shows how to set the proxy settings for a particular proxy server, open an HTTP connection, send an HTTP request, and read the response text. This example must be run from a command prompt. These proxy settings work only if you have a proxy server named "proxy\_server" that uses port 80 and your computer can bypass the proxy server when the host name ends with ".microsoft.com".


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

    // Initialize COM
    hr = CoInitialize( NULL );

    IWinHttpRequest *  pIWinHttpRequest = NULL;

    BSTR            bstrResponse = NULL;
    VARIANT         varFalse;
    VARIANT         varEmpty;
    VARIANT         varProxy;
    VARIANT         varUrl;
    
    CLSID           clsid;

    VariantInit(&varFalse);
    V_VT(&varFalse)   = VT_BOOL;
    V_BOOL(&varFalse) = VARIANT_FALSE;

    VariantInit(&varEmpty);
    V_VT(&varEmpty) = VT_ERROR;

    VariantInit(&varProxy);
    VariantInit(&varUrl);

    hr = CLSIDFromProgID(L"WinHttp.WinHttpRequest.5.1", &clsid);

    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(clsid, NULL, 
                              CLSCTX_INPROC_SERVER, 
                              IID_IWinHttpRequest, 
                              (void **)&pIWinHttpRequest);
    }
    if (SUCCEEDED(hr))
    {   // Specify proxy and URL.
                varProxy.vt = VT_BSTR;
                varProxy.bstrVal = SysAllocString(L"proxy_server:80");
                varUrl.vt = VT_BSTR;
                varUrl.bstrVal = SysAllocString(L"*.microsoft.com");
                hr = pIWinHttpRequest->SetProxy(HTTPREQUEST_PROXYSETTING_PROXY,
                                    varProxy, varUrl); 
        }
    if (SUCCEEDED(hr))
    {   // Open WinHttpRequest.
            BSTR bstrMethod  = SysAllocString(L"GET");
                BSTR bstrUrl = SysAllocString(L"https://microsoft.com");
        hr = pIWinHttpRequest->Open(bstrMethod, bstrUrl, varFalse);
                SysFreeString(bstrMethod);
                SysFreeString(bstrUrl);
    }
    if (SUCCEEDED(hr))
    {   // Send Request.
        hr = pIWinHttpRequest->Send(varEmpty);
    }
    if (SUCCEEDED(hr))
    {   // Get Response text.
                hr = pIWinHttpRequest->get_ResponseText(&bstrResponse);
    }
    if (SUCCEEDED(hr))
    {   // Print the response to a console.
                wprintf(L"%.256s",bstrResponse);
    }
        
        // Release memory.
    if (pIWinHttpRequest)
        pIWinHttpRequest->Release();
        if (varProxy.bstrVal)
                SysFreeString(varProxy.bstrVal);
        if (varUrl.bstrVal)
                SysFreeString(varUrl.bstrVal);
    if (bstrResponse)
        SysFreeString(bstrResponse);
        
        CoUninitialize();
        return 0;
}
```



The following scripting example shows how to set the proxy settings for a particular proxy server, open an HTTP connection, send an HTTP request, and read the response text. These proxy settings work only if you have a proxy server named "proxy\_server" that uses port 80 and your computer can bypass the proxy server when the host name ends with ".microsoft.com".


```JScript
// HttpRequest SetCredentials flags.
HTTPREQUEST_PROXYSETTING_DEFAULT   = 0;
HTTPREQUEST_PROXYSETTING_PRECONFIG = 0;
HTTPREQUEST_PROXYSETTING_DIRECT    = 1;
HTTPREQUEST_PROXYSETTING_PROXY     = 2;

// Instantiate a WinHttpRequest object.
var WinHttpReq = new ActiveXObject("WinHttp.WinHttpRequest.5.1");

// Use proxy_server for all requests outside of 
// the microsoft.com domain.
WinHttpReq.SetProxy( HTTPREQUEST_PROXYSETTING_PROXY, 
                     "proxy_server:80", 
                     "*.microsoft.com");

// Initialize an HTTP request.  
WinHttpReq.Open("GET", "https://www.microsoft.com", false);

// Send the HTTP request.
WinHttpReq.Send(); 

// Display the response text.
WScript.Echo( WinHttpReq.ResponseText);
```



## Requirements



| Requirement | Value |
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

[WinHTTP Versions](winhttp-versions.md)
</dt> </dl>

 

 




