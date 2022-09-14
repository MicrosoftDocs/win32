---
description: The SetIPortableDeviceValuesCollectionValue method adds a new IPortableDeviceValuesCollection value (type VT\_UNKNOWN) or overwrites an existing one.
ms.assetid: 29bdecaa-4820-4b1d-be59-ae82f7715a53
title: IPortableDeviceValues::SetIPortableDeviceValuesCollectionValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetIPortableDeviceValuesCollectionValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetIPortableDeviceValuesCollectionValue method

The **SetIPortableDeviceValuesCollectionValue** method adds a new **IPortableDeviceValuesCollection** value (type VT\_UNKNOWN) or overwrites an existing one.

## Syntax


```C++
HRESULT SetIPortableDeviceValuesCollectionValue(
  [in] REFPROPERTYKEY                  key,
  [in] IPortableDeviceValuesCollection *pValue
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

Pointer to an **IPortableDeviceValuesCollection** interface that specifies the new value. The SDK copies a reference to the submitted interface and calls **AddRef** on it.

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

[**IPortableDeviceValues::GetIPortableDeviceValuesCollectionValue**](iportabledevicevalues-getiportabledevicevaluescollectionvalue.md)
</dt> </dl>

 

 




