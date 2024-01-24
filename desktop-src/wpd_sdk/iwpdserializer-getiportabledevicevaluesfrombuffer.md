---
description: The GetIPortableDeviceValuesFromBuffer method deserializes a byte array to an IPortableDeviceValues interface.
ms.assetid: 93bea711-74d5-407a-a707-a3abe47bc2cd
title: IWpdSerializer::GetIPortableDeviceValuesFromBuffer method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWpdSerializer.GetIPortableDeviceValuesFromBuffer
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IWpdSerializer::GetIPortableDeviceValuesFromBuffer method

The **GetIPortableDeviceValuesFromBuffer** method deserializes a byte array to an **IPortableDeviceValues** interface.

## Syntax


```C++
HRESULT GetIPortableDeviceValuesFromBuffer(
  [in]  BYTE                  *pBuffer,
  [in]  DWORD                 dwInputBufferLength,
  [out] IPortableDeviceValues **ppParams
);
```



## Parameters

<dl> <dt>

*pBuffer* \[in\]
</dt> <dd>

Pointer to the buffer to deserialize.

</dd> <dt>

*dwInputBufferLength* \[in\]
</dt> <dd>

**DWORD** that specifies the size of the buffer, in bytes.

</dd> <dt>

*ppParams* \[out\]
</dt> <dd>

Address of a variable that receives a pointer to an [**IPortableDeviceValues**](iportabledevicevalues.md) interface created from the buffer. The application is responsible for calling **Release** on the interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                  | Description                                          |
|----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | The method succeeded.<br/>                     |
| <dl> <dt>**E\_POINTER**</dt> </dl>    | A required pointer argument was **NULL**.<br/> |
| <dl> <dt>**E\_UNEXPECTED**</dt> </dl> | An unspecified conversion error occurred.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWpdSerializer Interface**](iwpdserializer.md)
</dt> </dl>

 

 




