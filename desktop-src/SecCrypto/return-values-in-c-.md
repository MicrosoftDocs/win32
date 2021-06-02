---
description: In C++, the return value is typically of type HRESULT.
ms.assetid: 7abf1b3e-b94b-4846-a813-5eab5b34324c
title: Return Values in C++
ms.topic: article
ms.date: 05/31/2018
---

# Return Values in C++

In C++, the return value is typically of type **HRESULT**. It is from this return value that it can be determined whether the method succeeded or not, and if not, what the error was. Certificate Services typically returns S\_OK for the **HRESULT** when the method has completed successfully. Programmatic values that need to be returned are returned through "out" parameters in the method. The following example shows a C++ method call to retrieve a request property:


```C++
BSTR      bstrPropName = NULL;
VARIANT   varProp;
HRESULT   hr;

VariantInit(&varProp);

bstrPropName = SysAllocString(L"RequestID");
if (NULL == bstrPropName)
{
    printf("Failed SysAllocString\n");
    // Take application-specific error action.
    exit(1);
}

// Retrieve the request property.
// pCertServerPolicy is a pointer to a previously
// instantiated ICertServerPolicy object.
hr = pCertServerPolicy->GetRequestProperty(bstrPropName,
                                           PROPTYPE_LONG,
                                           &varProp);
if (S_OK != hr)
{
    printf("Failed GetRequestProperty [%x]\n", hr);
    // Take application-specific error action.
    // ...
}
else
{
    // Successfully retrieved property; use varProp as needed.
    // ...
}

// Done processing.
VariantClear(&varProp);
if (NULL != bstrPropName)
    SysFreeString(bstrPropName);
```



In the preceding code fragment, success or failure is returned to the **HRESULT** variable, *hr*. It is imperative to check the **HRESULT** variable for success \[handled in the code by the condition (S\_OK != hr)\]. If the method completed successfully, the request property value is returned in the **VARIANT** *varProp* parameter.

 

 



