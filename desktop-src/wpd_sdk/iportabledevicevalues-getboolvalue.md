---
description: The GetBoolValue method retrieves a Boolean value (type VT\_BOOL) specified by a key.
ms.assetid: cb5fed7a-50b5-4af1-806a-c6582409d265
title: IPortableDeviceValues::GetBoolValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetBoolValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetBoolValue method

The **GetBoolValue** method retrieves a **Boolean** value (type VT\_BOOL) specified by a key.

## Syntax


```C++
HRESULT GetBoolValue(
  [in]  REFPROPERTYKEY key,
  [out] BOOL           *pValue
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

Pointer to the retrieved **BOOL** value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                          |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                     |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>                   | The property specified by *key* is not a **BOOL** type.<br/>   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/> |



 

## Examples

For an example of how to use this method, see [Setting Properties for a Single Object](setting-properties-for-a-single-object.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetBoolValue**](iportabledevicevalues-setboolvalue.md)
</dt> <dt>

[Retrieving Supported Service Events](retrieving-supported-events.md)
</dt> <dt>

[Setting Properties for a Single Object](setting-properties-for-a-single-object.md)
</dt> <dt>

[Writing Content-Object Properties](writing-content-object-properties.md)
</dt> </dl>

 

 




