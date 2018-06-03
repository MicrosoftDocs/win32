---
title: Registering with Windows Firewall Without Taking Ownership of Firewall Policy Management
description: This example registers a product with Windows Firewall without taking ownership of Firewall policy management using the Windows Firewall with Advanced Security APIs.
ms.assetid: 85a568ad-a5eb-4248-bb25-d012593302da
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Registering with Windows Firewall Without Taking Ownership of Firewall Policy Management

This example registers a product with Windows Firewall without taking ownership of Firewall policy management using the Windows Firewall with Advanced Security APIs.


```C++
/********************************************************************++
Copyright (C) Microsoft. All Rights Reserved.

Abstract:
  This C++ file includes sample code that registers itself with the 
    Windows Firewall using the Microsoft Windows Firewall APIs but does
    not take ownership of any NET_FW_RULE_CATEGORY.

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

#pragma comment(lib, "ole32.lib")
#pragma comment(lib, "oleaut32.lib")

#define BAIL_ON_ALLOC_FAILURE(ptr, fnName) \
   if ((ptr) == NULL) \
   { \
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
    
      HRESULT hr = S_OK;
    INetFwProduct* product = NULL;
    INetFwProducts* products = NULL;
    IUnknown* registration = NULL;
    BSTR displayName = NULL;
    VARIANT varCategories = { VT_EMPTY };
   
    long count=0;
    BOOL comInit =  FALSE;

    //  For localization purposes, the display name can be 
    //    provided as an indirect string. The indirect strings can be defined in an rc file.
    //  Examples of the indirect string definition in the rc file -
    //    127                     "A Test Firewall Product"
    //    displayName = SysAllocString(L"@RegisterWithoutCategoryOwnership.exe,-127");

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



 

 




