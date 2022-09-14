---
title: Visual Basic Method Notes accName
description: The Object Description Language (ODL) file, Oleacc.odl, contains information that differs from the C/C++ implementation.
ms.assetid: f7960acd-cb1a-4c34-a392-0243155a100f
ms.topic: article
ms.date: 05/31/2018
---

# Visual Basic Method Notes: accName

The Object Description Language (ODL) file, Oleacc.odl, contains information that differs from the C/C++ implementation. The file Oleacc.odl contains the following definition for the version that sets the property of the function:


```C++
    [hidden, propput, id(DISPID_ACC_NAME)]
    HRESULT accName(
        [in, optional] VARIANT varChild,
        [in] BSTR szName);
```



Although the *varChild* parameter is listed as optional in the ODL file and the object browser, you must include it when calling the property-setting version of [**accName**](https://www.bing.com/search?q=**accName**).

 

 




