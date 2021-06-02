---
description: Returns an HRESULT. In this an HRESULT, a value of S\_OK indicates that the method was successfully executed.
ms.assetid: 6722a74a-1ec1-4c71-84c6-fb103aca149f
title: Certificate Enrollment Control Properties in C++
ms.topic: article
ms.date: 05/31/2018
---

# Certificate Enrollment Control Properties in C++

When you set or retrieve a Certificate Enrollment Control property in C++, the method call returns an **HRESULT**. In this an **HRESULT**, a value of S\_OK indicates that the method was successfully executed.

Programs written in C++ can retrieve the Certificate Enrollment Control properties by method calls in the following form.


```C++
#include <windows.h>

HRESULT get_propertyName( datatype * pPropValue);
```



Where *propertyName* specifies the name of the property being accessed, and *pPropValue* is a pointer to a variable of the appropriate data type. After successful completion of this method call, *pPropValue* will point to the variable that contains the value of the *propertyName* property.

For example, to retrieve the value for the **RootStoreType** property, you use the following code.


```C++
// Get the store type.
// hr is an HRESULT.
// bstrStoreType is a BSTR variable.
hr = pEnroll->get_RootStoreType( &bstrStoreType );
```



Programs written in C++ can set the Certificate Enrollment Control properties by calling methods in the following form.


```C++
#include <windows.h>

HRESULT put_propertyName( datatype PropValue);
```



Where *propertyName* specifies the name of the property being accessed, and *PropValue* is a value of the appropriate data type. After successful completion of this method call, the new value of the *propertyName* property will be *PropValue*.

For example, to set the property value for the **RootStoreType**, the following code could be used.


```C++
// Set the store type.
// bstrNewType previously set to a valid store type
hr = pEnroll->put_RootStoreType( bstrNewType );
```



 

 



