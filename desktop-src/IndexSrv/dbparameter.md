---
title: DBPARAMETER
description: DBPARAMETER
ms.assetid: 'cc41bd64-acbd-4922-9e2d-493889852a9d'
keywords: ["DBPARAMETER"]
---

# DBPARAMETER

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **DBPARAMETER** structure is used to define values for scalar parameters.

``` syntax
typedef struct tagDBPARAMETER {
  LPWSTR       pwszName;     // parameter name
  ITypeInfo *  pTypeInfo;    // if not a null pointer, type is described
                             // by the ITypeInfo
  DBNUMERIC *  pNum;         // Structure describing the
                             // precision, scale and value of
                             // the numeric value.
  DBLENGTH     cbMaxLength;  // the maximum length of the parameter
  DBPARAMFLAGS dwFlags;      // bitmask describing parameter characteristics
  DBTYPE       wType;        // type of the parameter
} DBPARAMETER;
```

### Remarks

Note that there is no entry for the ordinal position of the parameter. The assumption is that the ordinal position will be determined by the provider after evaluating the tree as a whole, and not by assigning a specific value to an individual member within the tree. Data consumers can determine the ordinal position based on the name using **ICommandWithParameters::MapParameterNames**. For more information about the interface, see [**ICommandWithParameters**](2cacfa5c-766b-4e1f-a31f-320f390de681).

 

 




