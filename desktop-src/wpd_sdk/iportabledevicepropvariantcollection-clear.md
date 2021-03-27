---
description: The Clear method frees, and then removes, all items from the collection. The collection is considered empty after calling this method.
ms.assetid: f4b46713-8224-443a-99cc-13fa75e59e5d
title: IPortableDevicePropVariantCollection::Clear method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDevicePropVariantCollection.Clear
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDevicePropVariantCollection::Clear method

The **Clear** method frees, and then removes, all items from the collection. The collection is considered empty after calling this method.

## Syntax


```C++
HRESULT Clear();
```



## Parameters

This method has no parameters.

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

After calling **Clear**, the collection is considered type-less, meaning that the VARTYPE it was previously set to is no longer restricting **Add** operations. A call to **Add** after calling **Clear** is considered the "first" **Add** for this collection.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDevicePropVariantCollection Interface**](iportabledevicepropvariantcollection.md)
</dt> </dl>

 

 




