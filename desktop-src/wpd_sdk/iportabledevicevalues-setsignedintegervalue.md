---
description: The SetSignedIntegerValue method adds a new LONG value (type VT\_I4) or overwrites an existing one.
ms.assetid: b0bb2992-2906-446c-be9a-20bff13f8e1d
title: IPortableDeviceValues::SetSignedIntegerValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetSignedIntegerValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetSignedIntegerValue method

The **SetSignedIntegerValue** method adds a new **LONG** value (type VT\_I4) or overwrites an existing one.

## Syntax


```C++
HRESULT SetSignedIntegerValue(
  [in]       REFPROPERTYKEY key,
  [in] const LONG           Value
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

A **LONG** that specifies the new value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If an existing value has the same key that is specified by the *key* parameter, it overwrites the existing value without any warning.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetSignedIntegerValue**](iportabledevicevalues-getsignedintegervalue.md)
</dt> </dl>

 

 




