---
title: Indexed Properties
description: When you invoke indexed properties of any dimension, you must pass the indexes as additional arguments.
ms.assetid: '1bb6e0a6-260d-4a37-be9b-9fb78cc2710a'
---

# Indexed Properties

When you invoke indexed properties of any dimension, you must pass the indexes as additional arguments. To set an indexed property, place the new value in the first element of the rgvarg\[ \] vector, and the indexes in the subsequent elements. To get an indexed property, pass the indexes in the first n elements of rgvarg, and the number of indexes in cArg. [**Invoke**](idispatch-invoke.md) returns the value of the property in pVarResult.

Automation stores array data in column-major order, which is the same ordering scheme used by Visual Basic and FORTRAN, but different from C, C++, and Pascal. If you are programming in C, C++, or Pascal, you must pass the indexes in the reverse order. The following example shows how to fill the DISPPARAMS structure in C++.


```C++
dispparams.rgvarg[0].vt = VT_I2;
dispparams.rgvarg[0].iVal = 99;
dispparams.rgvarg[1].vt = VT_I2;
dispparams.rgvarg[1].iVal = 2;
dispparams.rgvarg[2].vt = VT_I2;
dispparams.rgvarg[2].iVal = 1;
dispparams.rgdispidNamedArgs = DISPID_PROPERTYPUT;
dispparams.cArgs = 3;
dispparams.cNamedArgs = 1;
```



The example changes the value of Prop\[1,2\] to 99. The new property value is passed in rgvarg\[0\]. The right-most index is passed in rgvarg\[1\], and the next index in rgvarg\[2\]. The cArgs field specifies the number of elements of rgvarg\[ \] that contain data, and cNamedArgs is 1, indicating the new value for the property.

Property collections are an extension of this feature.

 

 




