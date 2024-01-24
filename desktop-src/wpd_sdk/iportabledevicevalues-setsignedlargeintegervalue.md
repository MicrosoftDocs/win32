---
description: The SetSignedLargeIntegerValue method adds a new LONGLONG value (type VT\_I8) or overwrites an existing one.
ms.assetid: 604b48ed-3e3f-4a06-91dd-7ece9f146824
title: IPortableDeviceValues::SetSignedLargeIntegerValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetSignedLargeIntegerValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetSignedLargeIntegerValue method

The **SetSignedLargeIntegerValue** method adds a new **LONGLONG** value (type VT\_I8) or overwrites an existing one.

## Syntax


```C++
HRESULT SetSignedLargeIntegerValue(
  [in]       REFPROPERTYKEY key,
  [in] const LONGLONG       Value
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

A **LONGLONG** that specifies the new value.

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

[**IPortableDeviceValues::GetSignedLargeIntegerValue**](iportabledevicevalues-getsignedlargeintegervalue.md)
</dt> </dl>

 

 




