---
description: The Certificate Enrollment Control Instantiated in C++
ms.assetid: 19dd2fce-b4a9-44fd-9572-897ee7943914
title: The Certificate Enrollment Control Instantiated in C++
ms.topic: article
ms.date: 05/31/2018
---

# The Certificate Enrollment Control Instantiated in C++

The following C++ example initializes COM, creates an instance of the [Certificate Enrollment Control](certificate-enrollment-control.md), uses the Certificate Enrollment Control, and frees resources.

## Example in C++

The following example creates an instance of the [Certificate Enrollment Control](certificate-enrollment-control.md) and displays the value of the [**MyStoreName**](/windows/win32/api/xenroll/nf-xenroll-icenroll-get_mystorename) property. This example uses the [**ICEnroll4**](/windows/desktop/api/Xenroll/nn-xenroll-icenroll4) interface.


```C++
#include <windows.h>
#include <stdio.h>
#include <xenroll.h>

// Copyright (C) Microsoft.  All rights reserved.
HRESULT __cdecl main(void)
{
    HRESULT hr = 0;
    ICEnroll4 *pEnroll = NULL;
    BSTR bstrStoreName = NULL;

    // Initialize COM.
    hr = CoInitializeEx( NULL, COINIT_APARTMENTTHREADED );
    if ( FAILED( hr ) )
    {
        printf("Failed CoInitializeEx - [0x%x]\n", hr);
        exit(hr);
    }

    // Create an instance of the object.
    hr = CoCreateInstance( __uuidof(CEnroll),
                           NULL,
                           CLSCTX_INPROC_SERVER,
                           __uuidof(ICEnroll4),
                           (void **)&pEnroll);
    if ( FAILED( hr ) )
    {
        printf("Failed CoCreateInstance - pEnroll [0x%x]\n", hr);
        exit(hr);
    }

    hr = pEnroll->get_MyStoreName(&bstrStoreName);
    if (SUCCEEDED(hr))
    {
        printf("The value of MyStoreName is %ws\n", bstrStoreName);
    }
    else
    {
        printf("pEnroll->GetMyStoreName failed: 0x%x\n", hr);
    }

    pEnroll->Release();
    SysFreeString(bstrStoreName);
    CoUninitialize();

    return hr;
}
```



 

 
