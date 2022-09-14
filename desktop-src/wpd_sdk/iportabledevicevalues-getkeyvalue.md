---
description: The GetKeyValue method retrieves a PROPERTYKEY value specified by a key.
ms.assetid: 2c92b1c0-3ea6-4a14-8b63-d57752b649b8
title: IPortableDeviceValues::GetKeyValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetKeyValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetKeyValue method

The **GetKeyValue** method retrieves a **PROPERTYKEY** value specified by a key.

## Syntax


```C++
HRESULT GetKeyValue(
  [in]  REFPROPERTYKEY key,
  [out] PROPERTYKEY    *pValue
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

Pointer to the retrieved **PROPERTYKEY** value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                               |
|------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                          |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>                   | The property specified by *key* is not a **PROPERTYKEY** type.<br/> |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/>      |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetKeyValue**](iportabledevicevalues-setkeyvalue.md)
</dt> </dl>

 

 




