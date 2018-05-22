---
Description: 'Gets the effective value of the specified dependency property.'
ms.assetid: '6FC5A7CF-A5EF-48B1-8DCD-4885BAFA0055'
title: 'IVisualTreeService2::GetProperty method'
---

# IVisualTreeService2::GetProperty method

Gets the effective value of the specified dependency property.

## Syntax


```C++
virtual HRESULT GetProperty(
  [in]  InstanceHandle object,
  [in]  unsigned int   propertyIndex,
  [out] InstanceHandle *pValue
) = 0;
```



## Parameters

<dl> <dt>

*object* \[in\]
</dt> <dd>

The dependency object to get the property value from.

</dd> <dt>

*propertyIndex* \[in\]
</dt> <dd>

The index of the property to get the value from.

</dd> <dt>

*pValue* \[out\]
</dt> <dd>

The effective value of the property.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IVisualTreeService2**](ivisualtreeservice2.md)
</dt> </dl>

 

 



