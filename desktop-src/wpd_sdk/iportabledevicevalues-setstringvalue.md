---
description: The SetStringValue method adds a new string value (type VT\_LPWSTR) or overwrites an existing one.
ms.assetid: a6eba2b9-de18-431e-874e-af68695e8d3f
title: IPortableDeviceValues::SetStringValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetStringValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetStringValue method

The **SetStringValue** method adds a new string value (type VT\_LPWSTR) or overwrites an existing one.

## Syntax


```C++
HRESULT SetStringValue(
  [in] REFPROPERTYKEY key,
  [in] LPCWSTR        Value
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** that specifies the item to create or overwrite.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

A **LPCWSTR** that specifies the new value. The string is copied, so the caller can release the memory allocated for this value after calling this method.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

Any existing key memory will be released appropriately.

## Examples

For an example of how to use this method, see [Specifying Client Information](specifying-client-information.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[Adding a Resource to an Object](adding-a-resource-to-an-object.md)
</dt> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetStringValue**](iportabledevicevalues-getstringvalue.md)
</dt> <dt>

[Setting Properties for a Single Object](setting-properties-for-a-single-object.md)
</dt> <dt>

[Setting Properties for Multiple Objects](setting-properties-for-multiple-objects.md)
</dt> <dt>

[Specifying Client Information](specifying-client-information.md)
</dt> <dt>

[Writing Content-Object Properties](writing-content-object-properties.md)
</dt> </dl>

 

 




