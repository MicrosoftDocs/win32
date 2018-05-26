---
title: Registering with Windows Firewall And Taking Ownership of Firewall Policy Management
description: This example registers a product with Windows Firewall and takes ownership of Firewall policy management using the Windows Firewall with Advanced Security APIs.C++ /\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ ++ Copyright (C) Microsoft. All Rights Reserved. Abstract This C++ file includes sample code that takes ownership of the NET\_FW\_RULE\_CATEGORY\_FIREWALL using the Microsoft Windows Firewall APIs. The API to register for NET\_FW\_RULE\_CATEGORY\_FIREWALL needs the binary that is making this call to be linked with /integritycheck option to ensure code integrity. Failure to do so can lead to error SEC\_E\_CANNOT\_INSTALL at runtime. For more details on code integrity read http //msdn2.microsoft.com/library/ms680339.aspx --\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ / \ include windows.h \ include strsafe.h \ include netfw.h \ include conio.h \ include stdio.h \ pragma comment( lib, \ 0034;ole32.lib \ 0034; ) \ pragma comment( lib, \ 0034;oleaut32.lib \ 0034; ) \ define BAIL\_ON\_ALLOC\_FAILURE(ptr, fnName) \\ if ((ptr) NULL) \\ \\ result ERROR\_NOT\_ENOUGH\_MEMORY; \\ printf(\ fnName \ 0034; ERROR\_NOT\_ENOUGH\_MEMORY\\n \ 0034;); \\ goto CLEANUP; \\ // Forward declarations DWORD ArrayOfLongsToVariant( \_\_in unsigned long numItems, \_\_in\_ecount(numItems) const long\ items, \_\_out VARIANT\ dst ); // // Purpose // Entry point for the process // // Parameters // None // // Return value // None // void \_\_cdecl main() DWORD result NO\_ERROR; HRESULT hr S\_OK; INetFwProduct\ product NULL; INetFwProducts\ products NULL; IUnknown\ registration NULL; long \ categories NULL; BSTR displayName NULL; VARIANT varCategories VT\_EMPTY ; int numberOfCategories 1; long count 0; BOOL comInit FALSE; //Allocate Memory categories (long \ )calloc (numberOfCategories , sizeof(long)); BAIL\_ON\_ALLOC\_FAILURE(categories, calloc); //Take Firewall Category Ownership categories\ 0\ NET\_FW\_RULE\_CATEGORY\_FIREWALL; result ArrayOfLongsToVariant(numberOfCategories, categories, varCategories); // For localization purposes, the display name can be // provided as an indirect string. The indirect strings can be defined in an rc file. // Examples of the indirect string definition in the rc file - // 127 \ 0034;A Test Firewall Product \ 0034; // displayName SysAllocString(L \ 0034; RegisterFirewallSample.exe,-127 \ 0034;); displayName SysAllocString(L \ 0034;A Test Firewall Product \ 0034;); BAIL\_ON\_ALLOC\_FAILURE(displayName, SysAllocString); hr CoInitializeEx(NULL, COINIT\_MULTITHREADED); if (FAILED(hr)) //COM initialize failed wprintf(L \ 0034;CoInitialize failed 0x 08lx\\n \ 0034;, hr); goto CLEANUP; comInit TRUE; hr CoCreateInstance(\_\_uuidof(NetFwProduct),NULL,CLSCTX\_INPROC\_SERVER,\_\_uuidof(INetFwProduct),(void\ \ ) product ); if (FAILED(hr)) //CoCreateInstance Failed wprintf(L \ 0034;CoCreateInstance for INetFwProduct failed 0x 08lx\\n \ 0034;, hr); goto CLEANUP; hr product- put\_DisplayName(displayName); if (FAILED(hr)) //Put\_displayName failed wprintf(L \ 0034;put\_DisplayName for INetFwProduct failed Error 0x 08lx\\n \ 0034;, hr); goto CLEANUP; hr product- put\_RuleCategories(varCategories); if (FAILED(hr)) //Put\_rulecategories failed wprintf(L \ 0034;put\_RuleCategories failed for INetFwProduct Error 0x 08lx\\n \ 0034;, hr); goto CLEANUP; hr CoCreateInstance(\_\_uuidof(NetFwProducts),NULL,CLSCTX\_INPROC\_SERVER,\_\_uuidof(INetFwProducts),(void\ \ ) products ); if (FAILED(hr)) //CoCreateInstance Failed wprintf(L \ 0034;CoCreateInstance for INetFwProducts failed 0x 08lx\\n \ 0034;, hr); goto CLEANUP; hr products- Register(product, registration); if (FAILED(hr)) //Failed to Register Products wprintf(L \ 0034;Register failed 0x 08lx\\n \ 0034;, hr); goto CLEANUP; hr products- get\_Count( count); if (FAILED(hr)) //Failed to get Count of Products wprintf(L \ 0034;Get count failed 0x 08lx\\n \ 0034;, hr); goto CLEANUP; wprintf(L \ 0034;INetFwProducts\_Count returned ld.\\n \ 0034;, count); wprintf(L \ 0034;Hit any key to unregister.\\n \ 0034;); \_getch(); CLEANUP if (registration NULL) registration- Release(); if (products NULL) products- Release(); if (product NULL) product- Release(); if (comInit) CoUninitialize(); free(categories); SysFreeString(displayName); VariantClear( varCategories); return; //This Function Converts and Array of Longs to Variant DWORD ArrayOfLongsToVariant( \_\_in unsigned long numItems, \_\_in\_ecount(numItems) const long\ items, \_\_out VARIANT\ dst ) DWORD result NO\_ERROR; SAFEARRAYBOUND bound\ 1\ ; SAFEARRAY\ sa NULL; VARIANT\ data; unsigned long i; VariantInit(dst); // If there are no items, just return VT\_EMPTY. if (numItems 0) goto CLEANUP; bound\ 0\ .lLbound 0; bound\ 0\ .cElements numItems; sa SafeArrayCreate(VT\_VARIANT, ARRAYSIZE(bound), bound); BAIL\_ON\_ALLOC\_FAILURE(sa, SafeArrayCreate); data (VARIANT\ )(sa- pvData); for (i 0; i numItems; ++i) V\_VT(data + i) VT\_I4; V\_I4(data + i) items\ i\ ; V\_VT(dst) VT\_ARRAY \ VT\_VARIANT; V\_ARRAY(dst) sa; CLEANUP return result;
ms.assetid: 87dd0457-a1d8-4de5-8e0a-660ea2aacbf0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Registering with Windows Firewall And Taking Ownership of Firewall Policy Management

This example registers a product with Windows Firewall and takes ownership of Firewall policy management using the Windows Firewall with Advanced Security APIs.


```C++
/********************************************************************++
Copyright (C) Microsoft. All Rights Reserved.

Abstract:
  This C++ file includes sample code that takes ownership
    of the NET_FW_RULE_CATEGORY_FIREWALL using the Microsoft 
    Windows Firewall APIs.

    The API to register for NET_FW_RULE_CATEGORY_FIREWALL 
    needs the binary that is making this call to be linked
    with /integritycheck option to ensure code integrity. Failure 
    to do so can lead to error SEC_E_CANNOT_INSTALL at runtime.

    For more details on code integrity read
    http://msdn2.microsoft.com/library/ms680339.aspx

--********************************************************************/

#include <windows.h>
#include <strsafe.h>
#include <netfw.h>
#include <conio.h>
#include <stdio.h>

#pragma comment( lib, "ole32.lib" )
#pragma comment( lib, "oleaut32.lib" )

#define BAIL_ON_ALLOC_FAILURE(ptr, fnName) \
   if ((ptr) == NULL) \
   { \
      result = ERROR_NOT_ENOUGH_MEMORY; \
      printf(#fnName " = ERROR_NOT_ENOUGH_MEMORY\n"); \
      goto CLEANUP; \
   }



// Forward declarations
DWORD ArrayOfLongsToVariant(
                            __in unsigned long numItems,
                            __in_ecount(numItems) const long* items,
                            __out VARIANT* dst
                            );
//
// Purpose: 
//   Entry point for the process
//
// Parameters:
//   None
// 
// Return value:
//   None
//
void __cdecl main() 
{ 
    DWORD result = NO_ERROR;
    HRESULT hr = S_OK;
    INetFwProduct* product = NULL;
    INetFwProducts* products = NULL;
    IUnknown* registration = NULL;
    long *categories = NULL;
    BSTR displayName = NULL;
    VARIANT varCategories = { VT_EMPTY };
    int numberOfCategories = 1;
    long count=0;
    BOOL comInit =  FALSE;

    //Allocate Memory
    categories = (long *)calloc (numberOfCategories , sizeof(long));
    BAIL_ON_ALLOC_FAILURE(categories, calloc);

    //Take Firewall Category Ownership
    categories[0] = NET_FW_RULE_CATEGORY_FIREWALL;
    result = ArrayOfLongsToVariant(numberOfCategories, categories, &amp;varCategories);
    
    //  For localization purposes, the display name can be 
    //    provided as an indirect string. The indirect strings can be defined in an rc file.
    //  Examples of the indirect string definition in the rc file -
    //    127                     "A Test Firewall Product"
    //    displayName = SysAllocString(L"@RegisterFirewallSample.exe,-127");

    displayName = SysAllocString(L"A Test Firewall Product");
    BAIL_ON_ALLOC_FAILURE(displayName, SysAllocString);

    hr = CoInitializeEx(NULL, COINIT_MULTITHREADED);
    if (FAILED(hr))
    {
        //COM initialize failed
        wprintf(L"CoInitialize failed: 0x%08lx\n", hr);
        goto CLEANUP;
    }
    comInit = TRUE;


    hr = CoCreateInstance(__uuidof(NetFwProduct),NULL,CLSCTX_INPROC_SERVER,__uuidof(INetFwProduct),(void**)&amp;product );

    if (FAILED(hr))
    {
        //CoCreateInstance Failed
        wprintf(L"CoCreateInstance for INetFwProduct failed: 0x%08lx\n", hr);
        goto CLEANUP;
    }

    hr = product->put_DisplayName(displayName);

    if (FAILED(hr))
    {
        //Put_displayName failed
        wprintf(L"put_DisplayName for INetFwProduct failed Error: 0x%08lx\n", hr);
        goto CLEANUP;
    }
    hr = product->put_RuleCategories(varCategories);

    if (FAILED(hr))
    {
        //Put_rulecategories failed
        wprintf(L"put_RuleCategories failed for INetFwProduct Error: 0x%08lx\n", hr);
        goto CLEANUP;
    }


    hr = CoCreateInstance(__uuidof(NetFwProducts),NULL,CLSCTX_INPROC_SERVER,__uuidof(INetFwProducts),(void**)&amp;products );

    if (FAILED(hr))
    {
        //CoCreateInstance Failed
        wprintf(L"CoCreateInstance for INetFwProducts failed: 0x%08lx\n", hr);
        goto CLEANUP;
    }

    hr = products->Register(product, &amp;registration);
    if (FAILED(hr))
    {
        //Failed to Register Products
        wprintf(L"Register failed: 0x%08lx\n", hr);
        goto CLEANUP;
    }            

    hr = products->get_Count( &amp;count);
    if (FAILED(hr))
    {
        //Failed to get Count of Products
        wprintf(L"Get count failed: 0x%08lx\n", hr);
        goto CLEANUP;
    }        
    wprintf(L"INetFwProducts_Count returned %ld.\n", count);

    wprintf(L"Hit any key to unregister.\n");
    _getch();

CLEANUP:
    if (registration != NULL)
   {
      registration->Release();
   }
   if (products != NULL)
   {
      products->Release();
   }
   if (product != NULL)
   {
      product->Release();
   }
   if (comInit)
   {
      CoUninitialize();
   }
   free(categories);
   SysFreeString(displayName);
   VariantClear(&amp;varCategories);
   return;
} 




//This Function Converts and Array of Longs to Variant

DWORD ArrayOfLongsToVariant(
                            __in unsigned long numItems,
                            __in_ecount(numItems) const long* items,
                            __out VARIANT* dst
                            )
{
    DWORD result = NO_ERROR;
    SAFEARRAYBOUND bound[1];
    SAFEARRAY* sa = NULL;
    VARIANT* data;
    unsigned long i;

    VariantInit(dst);

    // If there are no items, just return VT_EMPTY.
    if (numItems == 0)
    {
        goto CLEANUP;
    }

    bound[0].lLbound = 0;
    bound[0].cElements = numItems;

    sa = SafeArrayCreate(VT_VARIANT, ARRAYSIZE(bound), bound);
    BAIL_ON_ALLOC_FAILURE(sa, SafeArrayCreate);

    data = (VARIANT*)(sa->pvData);

    for (i = 0; i < numItems; ++i)
    {
        V_VT(data + i) = VT_I4;
        V_I4(data + i) = items[i];
    }

    V_VT(dst) = VT_ARRAY | VT_VARIANT;
    V_ARRAY(dst) = sa;

CLEANUP:
    return result;
}



```



 

 




