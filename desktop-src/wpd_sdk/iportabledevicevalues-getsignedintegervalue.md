---
description: The GetSignedIntegerValue method retrieves a LONG value (type VT\_I4) specified by a key.
ms.assetid: d2291a64-d0b3-4a30-a37c-2b6cd9880a11
title: IPortableDeviceValues::GetSignedIntegerValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.GetSignedIntegerValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::GetSignedIntegerValue method

The **GetSignedIntegerValue** method retrieves a **LONG** value (type VT\_I4) specified by a key.

## Syntax


```C++
HRESULT GetSignedIntegerValue(
  [in]  REFPROPERTYKEY key,
  [out] LONG           *pValue
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

Pointer to the retrieved **LONG** value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                            | Description                                                          |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                                   | The method succeeded.<br/>                                     |
| <dl> <dt>**DISP\_E\_TYPEMISMATCH**</dt> </dl>                   | The property specified by *key* is not a **LONG** type.<br/>   |
| <dl> <dt>**HRESULT\_FROM\_WIN32(ERROR\_NOT\_FOUND)**</dt> </dl> | The property specified by *key* is not in the collection.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::SetSignedIntegerValue**](iportabledevicevalues-setsignedintegervalue.md)
</dt> </dl>

 

 




