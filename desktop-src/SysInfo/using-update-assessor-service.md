---
Description: To use the WaaS Assessment Platform API, create an instance of the IWaaSAssessor interface, and then call the GetOSUpdateAssessment method.
ms.assetid: 810D4057-8319-4B9B-9098-CD7987CB292C
title: Using the WaaS Assessment Platform
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the WaaS Assessment Platform

To use the WaaS Assessment Platform API, create an instance of the [**IWaaSAssessor**](/windows/win32/waasapi/nn-waasapi-iwaasassessor?branch=master) interface, and then call the [**GetOSUpdateAssessment**](/windows/win32/waasapi/nf-waasapi-iwaasassessor-getosupdateassessment?branch=master) method. On a success, the *result* parameter will output an [**OSUpdateAssessment**](/windows/win32/waasapitypes/ns-waasapitypes-tagosupdateassessment?branch=master) object, which will contain the relevant information.

The following code sample shows how to retrieve an OS assessment from your local system, using the IWaaSAssessor.GetOSUpdateAssessment method.


```C++
//
// Copyright (c) Microsoft Corporation.  All rights reserved.
//
#include <windows.h>
#include <tchar.h>
#include <oaidl.h>
#include <atlbase.h>
#include <iostream>
#include <WaaSAPI.h>
#include <WaaSAPITypes.h>

using namespace std;

void __cdecl main(int argc, char** argv)
{
    HRESULT hr = S_OK;
    CComPtr<IWaaSAssessor> assessment;
    OSUpdateAssessment result;
    hr = CoInitialize(NULL);
    if (SUCCEEDED(hr))
    {
        hr = CoCreateInstance(
                __uuidof(WaaSAssessor),               // rclsid
                NULL,                                   // pUnkOuter
                CLSCTX_INPROC_SERVER,                   // dwClsContext
                __uuidof(IWaaSAssessor),              // riid
                (LPVOID*)&amp;assessment);                  // ppv
        if (SUCCEEDED(hr))
        {
            hr = assessment->GetOSUpdateAssessment(&amp;result);
            if (SUCCEEDED(hr))
            {
                wcout << L"End of Support:" << result.isEndOfSupport << endl;
                wcout << L"Up to date:" << result.assessmentForUpToDate.status << endl;
                wcout << L"Current:" << result.assessmentForCurrent.status << endl;
                wcout << L"Up to Date Days Behind:" << result.assessmentForUpToDate.daysOutOfDate << endl;
                wcout << L"Current Days Behind:" << result.assessmentForCurrent.daysOutOfDate << endl;
                wcout << L"Up to Date Impact:" << result.assessmentForUpToDate.impact << endl;
                wcout << L"Current Impact:" << result.assessmentForCurrent.impact << endl;
            }
            else
            {
                wcout << L"Assessment Failed hr = " << hr << endl;
            }
        }
        else
        {
            wcout << L"CoCreateInstance Failed hr = " << hr << endl;
        }
    }
    else
    {
        wcout << L"CoInitialize Failed hr = " << hr << endl;
    }
}
```



 

 



