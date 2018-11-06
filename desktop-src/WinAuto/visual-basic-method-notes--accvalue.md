---
title: Visual Basic Method Notes accValue
description: The Object Description Language (ODL) file, Oleacc.odl, contains information that differs from the C/C++ implementation. The file Oleacc.odl contains the following definition for the version that sets the property of the function.
ms.assetid: 8c27d63a-ae69-4667-9b65-be743a00b49d
ms.topic: article
ms.date: 05/31/2018
---

# Visual Basic Method Notes: accValue

The Object Description Language (ODL) file, Oleacc.odl, contains information that differs from the C/C++ implementation. The file Oleacc.odl contains the following definition for the version that sets the property of the function.


```C++
    [hidden, propput, id(DISPID_ACC_VALUE)]
    HRESULT accValue(
        [in, optional] VARIANT varChild,
        [in] BSTR szValue);
```



Although the *varChild* parameter is listed as optional in the ODL file and the object browser, you must include it when calling the property-setting version of [**accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-put_accvalue).

 

 




