---
Description: Gets the property index for the specified property name.
ms.assetid: E23FA0C6-7822-4CEA-AF0C-75B42941B143
title: IVisualTreeService2GetPropertyIndex method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVisualTreeService2::GetPropertyIndex method

Gets the property index for the specified property name.

## Syntax


```C++
virtual HRESULT GetPropertyIndex(
  [in]  InstanceHandle object,
  [in]  LPCWSTR        propertyName,
  [out] unsigned int   *pPropertyIndex
) = 0;
```



## Parameters

<dl> <dt>

*object* \[in\]
</dt> <dd>

The dependency object to get the property index from.

</dd> <dt>

*propertyName* \[in\]
</dt> <dd>

The name of the dependency property for which to get the index.

</dd> <dt>

*pPropertyIndex* \[out\]
</dt> <dd>

The index of the specified property.

</dd> </dl>

## Return value

The possible return codes include, but are not limited to, the values shown in the following table.



| Return code                                                                                  | Description                                                                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                                                                     |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | No property with *propertyName* was found, or the property cannot be applied to *object*.<br/> |



 

## Remarks

This index can be passed to the [**GetProperty**](ivisualtreeservice2-getproperty.md) method in order to retrieve a specific property on an object.

## See also

<dl> <dt>

[**IVisualTreeService2**](/windows/previous-versions/xamlom/nn-xamlom-ivisualtreeservice2?branch=master)
</dt> </dl>

 

 




