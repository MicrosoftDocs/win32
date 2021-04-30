---
description: The GetAt method retrieves a value from the collection using the supplied zero-based index.
ms.assetid: d52675f0-55b4-43ef-bb1d-ff6aa8a70647
title: IPortableDeviceValues::GetAt method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetAt
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetAt method

The **GetAt** method retrieves a value from the collection using the supplied zero-based index.

## Syntax


```C++
HRESULT GetAt(
  [in]      const DWORD       index,
  [in, out]       PROPERTYKEY *pKey,
  [in, out]       PROPVARIANT *pValue
);
```



## Parameters

<dl> <dt>

*index* \[in\]
</dt> <dd>

A **DWORD** that specifies a zero-based index in the collection.

</dd> <dt>

*pKey* \[in, out\]
</dt> <dd>

An optional **PROPERTYKEY** pointer that retrieves the key of the specified item.

</dd> <dt>

*pValue* \[in, out\]
</dt> <dd>

An optional **PROPVARIANT** that retrieves the value of the specified item. The caller must free the memory by calling **PropVariantClear** when done with it.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                       |
|----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | An invalid index number was specified.<br/> |



 

## Remarks

If a property indicates a value of type VT\_UNKNOWN, the property will be one of the Windows Portable Devices ([**IPortableDeviceKeyCollection**](iportabledevicekeycollection.md), [**IPortableDeviceValuesCollection**](iportabledevicevaluescollection.md), [**IPortableDeviceValues**](iportabledevicevalues.md) or [**IPortableDevicePropVariantCollection**](iportabledevicepropvariantcollection.md)). No other interfaces can be returned by Windows Portable Devices.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetStringValue**](iportabledevicevalues-getstringvalue.md)
</dt> </dl>

 

 




