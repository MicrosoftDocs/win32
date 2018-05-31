---
Description: It is recommended that you use native Component Object Model (COM) support (using the \#import compiler directive) when programming with the fax objects in C++. For more information, see Fax Extended COM Visual C++ Programming.
ms.assetid: 0c7f2397-f88b-4de3-9dd3-2de50361d914
title: Creating the Root Object in C++
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating the Root Object in C++

It is recommended that you use native Component Object Model (COM) support (using the [\#import](http://msdn.microsoft.com/library/en-us/vclang/html/_predir_The_.23.import_Directive.asp) compiler directive) when programming with the fax objects in C++. For more information, see [Fax Extended COM Visual C++ Programming](-mfax-fax-extended-com-visual-c-programming.md).

If you use native COM support, create the root object in C++ using the following code:


```
hr = sipFaxServer.CreateInstance("FaxComEx.FaxServer");
```



The following code examples demonstrate how to create the root objects if you do not use native COM support.

## FaxServer Object


```
#include <windows.h>
#include <faxcomex.h>
#include <faxcomex_i.c>
#include <tchar.h>

int main (int argc, TCHAR *argv[])
{
    HRESULT hr;
    IFaxServer *pIFaxServer = NULL;
    IUnknown   *pIUnknown = NULL;
    
    hr = CoInitialize (NULL);
    if (FAILED(hr))
    {
        //
        // handle failure
        // 
        return 1;
    }
    __try
    {
        hr = CoCreateInstance (CLSID_FaxServer, 
                               NULL, 
                               CLSCTX_LOCAL_SERVER | 
                                          CLSCTX_INPROC_HANDLER |
                                                         CLSCTX_INPROC_SERVER, 
                               __uuidof(IUnknown), 
                               reinterpret_cast<void**>(&amp;pIUnknown));
        if (FAILED(hr))
        {
            //
            // handle failure
            // 
            return 1;
        }
        hr = pIUnknown->QueryInterface(IID_IFaxServer, 
                                       reinterpret_cast<void**>(&amp;pIFaxServer));
        if (FAILED(hr))
        {
            //
            // handle failure
            // 
            return 1;
        }
        //
        // Use the IFaxServer object
        //
    }
    __finally
    {
        if (pIUnknown)
        {
            pIUnknown->Release();
        }
        if (pIFaxServer)
        {
            pIFaxServer->Release();
        }
        CoUninitialize();
    }
    return 0;
}
```



## FaxDocument Object


```
#include <windows.h>
#include <faxcomex.h>
#include <faxcomex_i.c>
#include <tchar.h>

int main (int argc, TCHAR *argv[])
{
    HRESULT hr;
    IFaxDocument *pIFaxDocument = NULL;
    IUnknown     *pIUnknown = NULL;
    
    hr = CoInitialize (NULL);
    if (FAILED(hr))
    {
        //
        // handle failure
        // 
        return 1;
    }
    __try
    {
        hr = CoCreateInstance (CLSID_FaxDocument, 
                                NULL, 
                                CLSCTX_LOCAL_SERVER | 
                                          CLSCTX_INPROC_HANDLER | 
                                                        CLSCTX_INPROC_SERVER, 
                                __uuidof(IUnknown), 
                                reinterpret_cast<void**>(&amp;pIUnknown));
        if (FAILED(hr))
        {
            //
            // handle failure
            // 
            return 1;
        }
        hr = pIUnknown->QueryInterface(IID_IFaxDocument, 
                                       reinterpret_cast<void**>(&amp;pIFaxDocument));
        if (FAILED(hr))
        {
            //
            // handle failure
            // 
            return 1;
        }
        //
        // Use the IFaxDocument object
        //
    }
    __finally
    {
        if (pIUnknown)
        {
            pIUnknown->Release();
        }
        if (pIFaxDocument)
        {
            pIFaxDocument->Release();
        }    
        CoUninitialize();
    }
    return 0;
}
```



 

 



