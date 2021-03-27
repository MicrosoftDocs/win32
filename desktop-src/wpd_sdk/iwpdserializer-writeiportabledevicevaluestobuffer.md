---
description: The WriteIPortableDeviceValuesToBuffer method serializes an IPortableDeviceValues interface to a caller-allocated byte array.
ms.assetid: 4d0108f1-563e-42df-897b-7cc0e9ff5b3a
title: IWpdSerializer::WriteIPortableDeviceValuesToBuffer method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWpdSerializer.WriteIPortableDeviceValuesToBuffer
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IWpdSerializer::WriteIPortableDeviceValuesToBuffer method

The **WriteIPortableDeviceValuesToBuffer** method serializes an **IPortableDeviceValues** interface to a caller-allocated byte array.

## Syntax


```C++
HRESULT WriteIPortableDeviceValuesToBuffer(
  [in]  DWORD                 dwOutputBufferLength,
  [in]  IPortableDeviceValues *pResults,
  [out] BYTE                  *pBuffer,
  [out] DWORD                 *pdwBytesWritten
);
```



## Parameters

<dl> <dt>

*dwOutputBufferLength* \[in\]
</dt> <dd>

**DWORD** that specifies the size of *pBuffer*, in bytes.

</dd> <dt>

*pResults* \[in\]
</dt> <dd>

Pointer to an [**IPortableDeviceValues**](iportabledevicevalues.md) interface to serialize.

</dd> <dt>

*pBuffer* \[out\]
</dt> <dd>

Pointer to a caller-allocated buffer. To learn the size of the required buffer, call **GetSerializedSize**.

</dd> <dt>

*pdwBytesWritten* \[out\]
</dt> <dd>

Pointer to a **DWORD** that indicates the number of bytes that was actually written to the caller-allocated buffer.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                   | Description                                               |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                          |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A required pointer argument was **NULL**.<br/>      |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | The caller-provided buffer was not big enough.<br/> |



 

## Remarks

This method copies an **IPortableDeviceValues** interface into an existing buffer. If you want to allocate a new buffer, use [**GetBufferFromIPortableDeviceValues**](iwpdserializer-getbufferfromiportabledevicevalues.md).

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWpdSerializer Interface**](iwpdserializer.md)
</dt> </dl>

 

 




