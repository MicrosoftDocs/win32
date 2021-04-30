---
description: The GetBufferFromIPortableDeviceValues method serializes a submitted IPortableDeviceValues interface to an allocated byte array. The byte array returned is allocated for the caller and should be freed by the caller using CoTaskMemFree.
ms.assetid: fd856394-9cb3-41cb-875b-1d490ca859df
title: IWpdSerializer::GetBufferFromIPortableDeviceValues method (PortableDeviceTypes.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWpdSerializer.GetBufferFromIPortableDeviceValues
api_type: 
- COM
api_location: 
- PortableDeviceGUIDs.lib
- PortableDeviceGUIDs.dll
---

# IWpdSerializer::GetBufferFromIPortableDeviceValues method

The **GetBufferFromIPortableDeviceValues** method serializes a submitted **IPortableDeviceValues** interface to an allocated byte array. The byte array returned is allocated for the caller and should be freed by the caller using **CoTaskMemFree**.

## Syntax


```C++
HRESULT GetBufferFromIPortableDeviceValues(
  [in]  IPortableDeviceValues *pSource,
  [out] BYTE                  **ppBuffer,
  [out] DWORD                 *pdwBufferSize
);
```



## Parameters

<dl> <dt>

*pSource* \[in\]
</dt> <dd>

Pointer to an [**IPortableDeviceValues**](iportabledevicevalues.md) interface to serialize.

</dd> <dt>

*ppBuffer* \[out\]
</dt> <dd>

Pointer to a **BYTE\*** that contains the serialized data. Windows Portable Devices allocates this memory; the caller must free it by calling **CoTaskMemFree**.

</dd> <dt>

*pdwBufferSize* \[out\]
</dt> <dd>

Pointer to a **DWORD** that specifies the size of allocated buffer, in bytes.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                   | Description                                                            |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | The method succeeded.<br/>                                       |
| <dl> <dt>**E\_POINTER**</dt> </dl>     | A required pointer argument was **NULL**.<br/>                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | There was not enough memory available to create the buffer.<br/> |



 

## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>PortableDeviceTypes.h</dt> </dl>   |
| Library<br/> | <dl> <dt>PortableDeviceGUIDs.lib</dt> </dl> |



## See also

<dl> <dt>

[**IWpdSerializer Interface**](iwpdserializer.md)
</dt> </dl>

 

 




