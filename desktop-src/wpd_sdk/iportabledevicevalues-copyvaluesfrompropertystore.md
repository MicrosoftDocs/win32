---
description: The CopyValuesFromPropertyStore method copies the contents of an IPropertyStore into the collection.
ms.assetid: 887c9569-ff76-41cf-8782-62c59c04e831
title: IPortableDeviceValues::CopyValuesFromPropertyStore method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.CopyValuesFromPropertyStore
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::CopyValuesFromPropertyStore method

The **CopyValuesFromPropertyStore** method copies the contents of an **IPropertyStore** into the collection.

## Syntax


```C++
HRESULT CopyValuesFromPropertyStore(
  [in] IPropertyStore *pStore
);
```



## Parameters

<dl> <dt>

*pStore* \[in\]
</dt> <dd>

Pointer to an **IPropertyStore** to copy into the collection.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

This method automatically converts all **VT\_BSTR** values to **VT\_LPWSTR** values.

Many external applications or components that communicate with your application, such as some shell applications, use the **IPropertyStore** interface. This method provides a quick and easy way to exchange data with these programs.

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

[**IPortableDeviceValues::CopyValuesToPropertyStore**](iportabledevicevalues-copyvaluestopropertystore.md)
</dt> </dl>

 

 




