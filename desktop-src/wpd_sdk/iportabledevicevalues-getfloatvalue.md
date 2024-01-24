---
description: The GetFloatValue method retrieves a FLOAT value (type VT\_R4) specified by a key.
ms.assetid: 8a134dfb-f671-4cde-ae35-c8a41be270cf
title: IPortableDeviceValues::GetFloatValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetFloatValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetFloatValue method

The **GetFloatValue** method retrieves a **FLOAT** value (type VT\_R4) specified by a key.

## Syntax


```C++
HRESULT GetFloatValue(
  [in]  REFPROPERTYKEY key,
  [out] FLOAT          *pValue
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

Pointer to the retrieved **FLOAT** value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                             | Description                                                          |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | The method succeeded.<br/>                                     |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>    | The property specified by *key* is not a **FLOAT** type.<br/>  |
| <dl> <dt>**E\_PROP\_ID\_UNSUPPORTED**</dt> </dl> | The property specified by *key* is not in the collection.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetFloatValue**](iportabledevicevalues-setfloatvalue.md)
</dt> </dl>

 

 




