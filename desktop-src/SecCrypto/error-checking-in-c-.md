---
description: In C++, every Certificate Services method directly returns an HRESULT value that indicates whether the method call succeeded or failed. If the call failed, the return value indicates why it failed.
ms.assetid: 4ab1b5ba-dd19-4802-aa9c-02bd5406681f
title: Error Checking in C++
ms.topic: article
ms.date: 05/31/2018
---

# Error Checking in C++

In C++, every Certificate Services method directly returns an **HRESULT** value that indicates whether the method call succeeded or failed. If the call failed, the return value indicates why it failed.

The following example shows how the returned **HRESULT** values can be used for error checking. For example error codes, see [Common HRESULT Values](common-hresult-values.md).


```C++
HRESULT hr;
BSTR strAttributeName;
BSTR strAttributeValue = NULL;

if(!(strAttributeName = SysAllocString(L"TheAttribute")))
{
     printf("Could not allocate memory for attribute name.\n");
     exit(1);
}

hr = pICertServerPolicy->GetRequestAttribute(
                                strAttributeName,
                                &strAttributeValue);
if(S_OK != hr)          // Check to determine whether method failed
{
    if (E_INVALIDARG == hr)
    {
        //... Do something to recover from errors and so on.
    }
}
// Free BSTRs when finished.
if (NULL != strAttributeName)
    SysFreeString(strAttributeName);
if (NULL != strAttributeValue)
    SysFreeString(strAttributeValue);
```



 

 



