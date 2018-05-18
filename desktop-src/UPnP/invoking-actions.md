---
title: Invoking Actions
description: The IUPnPService InvokeAction method allows actions to be invoked on Service objects.
ms.assetid: '671e9280-5ead-43f2-bb6b-12792a6a4487'
---

# Invoking Actions

The [**IUPnPService::InvokeAction**](iupnpservice-invokeaction.md) method allows actions to be invoked on Service objects. This method has two input parameters: the name of an action and an array of input arguments to that action. The method has two parameters:

-   Parameter one — an input/output parameter: an array of output arguments for that action.
-   Parameter two — an output parameter: a return value.

The method causes the action to be invoked on the device. The device generates event notifications if the action causes state variables of the device to change.

## VBScript Example

The following VBScript code example invokes two actions on a Service object. The first action, *GetTrackInfo*, takes one input argument, a track number. The *GetTrackInfo* action returns the track length as the return value. The action also has one output argument, which contains the track title if the method returns success.

After invoking the *GetTrackInfo* action, the example invokes the Play action, which takes no arguments. However, because the syntax of [**InvokeAction**](iupnpservice-invokeaction.md) requires an array of both input and output arguments, the example must create an empty array, *emptyArgs*, with no elements. The example passes this array to **InvokeAction** for both the input and output arguments, along with the name of the action.


```VB
Dim returnVal
Dim outArgs(1)
Dim args(1)
args(0) = 3
returnVal = service.InvokeAction("GetTrackInfo", args, outArgs)
'return Val now contains the track length
'and outArgs(0) contains the track title
Dim emptyArgs(0)
returnVal = service.InvokeAction("Play", emptyArgs, emptyArgs)
'returnVal indicates if the action was successful
```



## C++ Example

The following example defines a C++ function that invokes an action with no arguments. Because [**InvokeAction**](iupnpservice-invokeaction.md) requires a [**SAFEARRAY**](9ec8025b-4763-4526-ab45-390c5d8b3b1e) of arguments to be passed in, this example creates an empty **SAFEARRAY**. Since this action does not return a value or have output arguments, this example ignores the last two [**VARIANT**](f0940eea-077f-4b68-9dac-d49e3fc62e43) values passed to **InvokeAction**.

The device generates event notifications if the action causes state variables of the device to change.


```C++
#include <windows.h>
#include <upnp.h>
#include <iostream>
#include <iomanip>

#pragma comment(lib, "oleaut32.lib")

using namespace std;

void InvokePlay(IUPnPService * pService)
{
    HRESULT hr;
    BSTR bstrActionName;

    bstrActionName = SysAllocString(L"Play");

    if (bstrActionName)
    {
        SAFEARRAYBOUND  rgsaBound[1];
        SAFEARRAY       * psa = NULL;

        rgsaBound[0].lLbound = 0;
        rgsaBound[0].cElements = 0;

        psa = SafeArrayCreate(VT_VARIANT, 1, rgsaBound);

        if (psa)
        {
            LONG    lStatus;
            VARIANT varInArgs;

            VariantInit(&amp;varInArgs);

            varInArgs.vt = VT_VARIANT | VT_ARRAY;

            V_ARRAY(&amp;varInArgs) = psa;

            hr = pService->InvokeAction(bstrActionName,
                                        varInArgs,
                                        NULL,
                                        NULL);

            if (SUCCEEDED(hr))
            {
                wcout << L"Action invoked successfully\n"; 
            }
            else
            {
                wcerr << L"Failed to invoke action - HRESULT 0x" 
                      << setbase(16)
                      << hr << L"\n";                        

            }                                   

            SafeArrayDestroy(psa);
        }
        else
        {
            wcerr << L"Failed to create safe array\n";
        }   

        SysFreeString(bstrActionName);
    }
    else
    {
        wcerr << L"Failed to allocate action name string\n";
    }
}
```



The following example invokes the fictitious *GetTrackInfo* action. It takes a track number as an argument, returns the track length as a return value, and returns the track title in an output argument. The code is similar to the previous example, except that instead of creating an empty [**SAFEARRAY**](9ec8025b-4763-4526-ab45-390c5d8b3b1e) of input arguments, this example inserts a [**VARIANT**](f0940eea-077f-4b68-9dac-d49e3fc62e43) that contains the track number. If [**InvokeAction**](iupnpservice-invokeaction.md) returns success, this example examines the return value and the array of output arguments.


```C++
#include <windows.h>
#include <upnp.h>
#include <iostream>
#include <iomanip>

#pragma comment(lib, "oleaut32.lib")

using namespace std;

void InvokeGetTrackInfo(IUPnPService * pService)
{
    HRESULT hr;
    BSTR bstrActionName;

    bstrActionName = SysAllocString(L"GetTrackInfo");

    if (bstrActionName)
    {
        SAFEARRAYBOUND  rgsaBound[1];
        SAFEARRAY       * psa = NULL;

        rgsaBound[0].lLbound = 0;
        rgsaBound[0].cElements = 1;

        psa = SafeArrayCreate(VT_VARIANT, 1, rgsaBound);

        if (psa)
        {
            long rgIndices[1];
            VARIANT varTrackNum;

            rgIndices[0] = 0;
            VariantInit(&amp;varTrackNum);

            varTrackNum.vt = VT_I4;
            // An arbitrary track is chosen (track 3)
            V_I4(&amp;varTrackNum) = 3;

            hr = SafeArrayPutElement(psa,
                                     rgIndices,
                                     (void *) &amp;varTrackNum);

            VariantClear(&amp;varTrackNum);

            if (SUCCEEDED(hr))
            {            
                LONG    lStatus;
                VARIANT varInArgs;
                VARIANT varOutArgs;
                VARIANT varReturnVal;

                VariantInit(&amp;varInArgs);
                VariantInit(&amp;varOutArgs);
                VariantInit(&amp;varReturnVal);

                varInArgs.vt = VT_VARIANT | VT_ARRAY;

                V_ARRAY(&amp;varInArgs) = psa;

                hr = pService->InvokeAction(bstrActionName,
                                            varInArgs,
                                            &amp;varOutArgs,
                                            &amp;varReturnVal);

                if (SUCCEEDED(hr))
                {
                    SAFEARRAY * psaOutArgs = NULL;
                    VARIANT   varTrackTitle;

                    psaOutArgs = V_ARRAY(&amp;varOutArgs);
                    VariantInit(&amp;varTrackTitle);

                    rgIndices[0] = 0;
                    hr = SafeArrayGetElement(psaOutArgs,
                                             rgIndices,
                                             (void *)&amp;varTrackTitle);                    

                    if (SUCCEEDED(hr))
                    {                    
                        wcout << L"Action invoked successfully\n"
                              << L"\tTrack Length == " 
                              << V_I4(&amp;varReturnVal) << L"\n"
                              << L"\tTrack Title == " 
                              << V_BSTR(&amp;varTrackTitle) << L"\n";
                    }
                    else
                    {
                        wcerr << L"Failed to get array element -"
                              << L" HRESULT 0x" 
                              << setbase(16)
                              << hr << L"\n";                        
                    }

                    VariantClear(&amp;varTrackTitle);
                    VariantClear(&amp;varReturnVal);
                    VariantClear(&amp;varOutArgs);
                }
                else
                {
                    wcerr << L"Failed to invoke action - HRESULT 0x" 
                          << setbase(16)
                          << hr << L"\n";                        
                }                                   
            }
            else
            {
                wcerr << L"Failed to insert argument into array - "
                      << L"HRESULT 0x" 
                      << setbase(16)
                      << hr << L"\n";                        
            }

            SafeArrayDestroy(psa);
        }
        else
        {
            wcerr << L"Failed to create safe array\n";
        }   

        SysFreeString(bstrActionName);
    }
    else
    {
        wcerr << L"Failed to allocate action name string\n";
    }
}
```



 

 




