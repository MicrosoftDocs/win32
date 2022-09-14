---
description: The SetIPortableDevicePropVariantCollectionValue method adds a new IPortableDevicePropVariantCollection value (type VT\_UNKNOWN) or overwrites an existing one.
ms.assetid: 8ea6be5e-1d03-4d59-9acc-5cd56ee81cd3
title: IPortableDeviceValues::SetIPortableDevicePropVariantCollectionValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetIPortableDevicePropVariantCollectionValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetIPortableDevicePropVariantCollectionValue method

The **SetIPortableDevicePropVariantCollectionValue** method adds a new **IPortableDevicePropVariantCollection** value (type VT\_UNKNOWN) or overwrites an existing one.

## Syntax


```C++
HRESULT SetIPortableDevicePropVariantCollectionValue(
  [in] REFPROPERTYKEY                       key,
  [in] IPortableDevicePropVariantCollection *pValue
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** that specifies the item to create or overwrite.

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Pointer to an **IPortableDevicePropVariantCollection** interface that specifies the new value. The SDK copies a reference to the submitted interface and calls **AddRef** on it.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If an existing value has the same key that is specified by the *key* parameter, it overwrites the existing value without any warning. The existing key memory is released appropriately.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetIPortableDevicePropVariantCollectionValue**](iportabledevicevalues-getiportabledevicepropvariantcollectionvalue.md)
</dt> </dl>

 

 




