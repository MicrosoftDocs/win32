---
title: NDF Helper Class Extension with Handoff
description: This Helper Class has a low-health dependency on the SimpleFileHelperClass coded in the first example.
ms.assetid: b59cd855-c68a-4f5c-b145-ceac395ddcc4
ms.topic: article
ms.date: 05/31/2018
---

# NDF Helper Class Extension with Handoff

This Helper Class has a low-health dependency on the SimpleFileHelperClass coded in the first example.

The second handoff helper class is a simple pass-through helper class which does not perform any diagnosis itself. Instead, it always generates lower health hypothesis for the SimpleFileHelperClass. This is useful in serving as a placeholder for future addition of diagnostics capability in this helper class. The handoff helper class implements two methods.

The LowHealth method is used to set the Diagnosis Status to DS\_INDETERMINATE. This makes NDF call GetLowerHypotheses.


```C++
#include <windows.h>

HRESULT HandOffTestHelperClass::LowHealth( 
    /* [unique][string][in] */ LPCWSTR pwszInstanceDescription,
    /* [string][out] */ LPWSTR *ppwszDescription,
    /* [out] */ long *pDeferredTime,
    /* [out] */ DIAGNOSIS_STATUS *pStatus) 

{
    *pStatus = DS_INDETERMINATE;
    return S_OK;
}

```



Next, GetLowerHypotheses is implemented to tell NDF which Helper Class to diagnose.


```C++
#include <windows.h>

HRESULT HandOffTestHelperClass::GetLowerHypotheses( 
ULONG *Count,
HYPOTHESIS **Hypotheses)
{
    HRESULT hr = S_OK;
    HYPOTHESIS *pHypothesis=NULL;
    HELPER_ATTRIBUTE *pAttr=NULL;

    pHypothesis = (PHYPOTHESIS)CoTaskMemAlloc(sizeof(HYPOTHESIS));
    if (pHypothesis == NULL)
    {
        return E_OUTOFMEMORY;
    }
    SecureZeroMemory(pHypothesis, sizeof(HYPOTHESIS));

    pAttr = (PHELPER_ATTRIBUTE)CoTaskMemAlloc(sizeof(HELPER_ATTRIBUTE));
    if (pAttr  == NULL)
    {
       hr = E_OUTOFMEMORY;
       goto Error;
    }
    SecureZeroMemory(pAttr, sizeof(HELPER_ATTRIBUTE));

    //set the helper class name to hand off to
    hr = StringCchCopyWithAlloc(&pHypothesis->pwszClassName, MAX_PATH,
                 L"SimpleFileHelperClass");
    if (FAILED(hr))
    {
        goto Error;
    }

    //populate the attribute
    //set the attribute name
    hr = StringCchCopyWithAlloc(&pAttr->pwszName, MAX_PATH, L"filename");
    if (FAILED(hr))
    {
        goto Error;  
    }

    //set attribute data
    pAttr->type = AT_STRING;
    hr = StringCchCopyWithAlloc(&pAttr->PWStr, MAX_PATH, m_pwszTestFile);
    if (FAILED(hr))
    {
        goto Error;
    }

    //set the attributes to the hypothesis  
    pHypothesis->celt = 1; //number of attributes
    pHypothesis->rgAttributes=pAttr;

    //pass data back
    *pcelt = 1; //one hypothesis
    *pprgHypotheses = pHypothesis;

    return S_OK;

Error:

    if (pAttr)
    {
        if (pAttr->PWStr) 
            CoTaskMemFree(pAttr->PWStr);
        if (pAttr->pwszName) 
            CoTaskMemFree(pAttr->pwszName);
    }

    if (pHypothesis)
    {
        if (pHypothesis->pwszClassName) 
            CoTaskMemFree(pHypothesis->pwszClassName);
        CoTaskMemFree(pHypothesis);
    }
    return hr;
}

```



 

 




