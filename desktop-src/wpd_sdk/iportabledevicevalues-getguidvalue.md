---
description: The GetGuidValue method retrieves a GUID value (type VT\_CLSID) specified by a key.
ms.assetid: 1cfa75e8-2c3b-4893-954e-dae25a6b8220
title: IPortableDeviceValues::GetGuidValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetGuidValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetGuidValue method

The **GetGuidValue** method retrieves a **GUID** value (type VT\_CLSID) specified by a key.

## Syntax


```C++
HRESULT GetGuidValue(
  [in]  REFPROPERTYKEY key,
  [out] GUID           *pValue
);
```



## Parameters

<dl> <dt>

*key* \[in\]
</dt> <dd>

A **REFPROPERTYKEY** key that specifies the item to retrieve.

</dd> <dt>

*pValue* \[out\]
</dt> <dd>

Pointer to the retrieved **GUID** value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                          |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                     |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>                   | The property specified by *key* is not a **GUID** type.<br/>   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/> |



 

## Examples

For an example of how to use this method, see [Retrieving Supported Service Methods](retrieving-supported-methods.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetGuidValue**](iportabledevicevalues-setguidvalue.md)
</dt> <dt>

[Retrieving Supported Service Methods](retrieving-supported-methods.md)
</dt> <dt>

[Retrieving the Rendering Capabilities Supported by a Device](retrieving-the-rendering-capabilities-supported-by-a-device.md)
</dt> </dl>

 

 




