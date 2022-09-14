---
description: The GetSerializedSize method calculates the buffer size that is required to hold a serialized IPortableDeviceValues interface.
ms.assetid: 12fa6ed1-ce3b-4c5d-920a-87ff693fe0ea
title: IWpdSerializer::GetSerializedSize method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWpdSerializer.GetSerializedSize
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IWpdSerializer::GetSerializedSize method

The **GetSerializedSize** method calculates the buffer size that is required to hold a serialized [**IPortableDeviceValues**](iportabledevicevalues.md) interface.

## Syntax


```C++
HRESULT GetSerializedSize(
  [in]  IPortableDeviceValues *pSource,
  [out] DWORD                 *pdwSize
);
```



## Parameters

<dl> <dt>

*pSource* \[in\]
</dt> <dd>

Pointer to an [**IPortableDeviceValues**](iportabledevicevalues.md) interface whose size you want to request.

</dd> <dt>

*pdwSize* \[out\]
</dt> <dd>

Pointer to a **DWORD** that indicates the buffer size that is required to serialize *pSource*, in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                   | Description                                                            |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A required pointer argument was **NULL**.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There was not enough available memory to create the buffer.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWpdSerializer Interface**](iwpdserializer.md)
</dt> </dl>

 

 




