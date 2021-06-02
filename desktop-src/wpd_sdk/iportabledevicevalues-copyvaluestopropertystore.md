---
description: The CopyValuesToPropertyStore method copies all the values from a collection into an IPropertyStore interface.
ms.assetid: 417a8723-fa46-44c8-9bdc-412c0f20969a
title: IPortableDeviceValues::CopyValuesToPropertyStore method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.CopyValuesToPropertyStore
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::CopyValuesToPropertyStore method

The **CopyValuesToPropertyStore** method copies all the values from a collection into an **IPropertyStore** interface.

## Syntax


```C++
HRESULT CopyValuesToPropertyStore(
  [in] IPropertyStore *pStore
);
```



## Parameters

<dl> <dt>

*pStore* \[in\]
</dt> <dd>

Pointer to a store object.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

This method does not convert values of VT\_LPWSTR into VT\_BSTR. Many external applications or components that communicate with your application, such as some shell applications, use the **IPropertyStore** interface. This method provides a quick and easy way to exchange data with these programs.

This method is supported in Windows Vista and later versions of Windows.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::CopyValuesFromPropertyStore**](iportabledevicevalues-copyvaluesfrompropertystore.md)
</dt> </dl>

 

 




