---
description: The SetErrorValue method adds a new HRESULT value (type VT\_ERROR) or overwrites an existing one.
ms.assetid: 87369791-42bd-4523-b15a-acf0ea1e5af8
title: IPortableDeviceValues::SetErrorValue method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPortableDeviceValues.SetErrorValue
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IPortableDeviceValues::SetErrorValue method

The **SetErrorValue** method adds a new **HRESULT** value (type VT\_ERROR) or overwrites an existing one.

## Syntax


```C++
HRESULT SetErrorValue(
  [in]       REFPROPERTYKEY key,
  [in] const HRESULT        Value
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

An **HRESULT** that contains the new value.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

If an existing value has the same key specified by the *key* parameter, it overwrites the existing value without any warning.

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IPortableDeviceValues Interface**](iportabledevicevalues.md)
</dt> <dt>

[**IPortableDeviceValues::GetErrorValue**](iportabledevicevalues-geterrorvalue.md)
</dt> </dl>

 

 




