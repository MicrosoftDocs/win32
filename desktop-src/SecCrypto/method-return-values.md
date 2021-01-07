---
description: The return value for C++ interface methods is always of type HRESULT; this value can be checked to determine success or failure.
ms.assetid: f6478e72-0fe9-4c3b-b08a-f71c9c943910
title: Method Return Values
ms.topic: article
ms.date: 05/31/2018
---

# Method Return Values

The return value for C++ interface methods is always of type **HRESULT**; this value can be checked to determine success or failure. The use of "output" parameters allows values to be assigned to variables during the method or property call. The following example shows a C++ method call to enumerate providers.


```C++
UINT          ucEnumProvIndex = 0;
BSTR          bstrProvider = NULL;
HRESULT       hr;

// pEnroll is previously instantiated CEnroll interface pointer
hr = pEnroll->enumProviders(ucEnumProvIndex, 0, &bstrProvider);
```



In the preceding code fragment, success or failure is returned to the "hr" variable. If the call was successful, hr will be set to S\_OK and the variable bstrProvider will contain the name of the enumerated provider.

A C++ call to retrieve a property value would be as follows.


```C++
BSTR     bstrStoreName = NULL;
HRESULT  hr;

// pEnroll is previously instantiated CEnroll interface pointer

// get the storename
hr = pEnroll->get_CAStoreName( &bstrStoreName );

// (When done using bstrStoreName, free it by calling SysFreeString).
```



A C++ call to set a property value would be as follows.


```C++
// bstrNewName previously set to a valid store name
hr = pEnroll->put_CAStoreName( bstrNewName );
```



 

 



