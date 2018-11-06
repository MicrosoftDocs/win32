---
title: ActiveBasicDevice SetCachedBitrateMeasurement method
description: Sets the cached bitrate.
ms.assetid: 53530217-CFF7-4376-B155-E11044621E2D
keywords:
- SetCachedBitrateMeasurement method Media Streaming API
- SetCachedBitrateMeasurement method Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , SetCachedBitrateMeasurement method
topic_type:
- apiref
api_name:
- ActiveBasicDevice.SetCachedBitrateMeasurement
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: article
ms.date: 05/31/2018
---

# ActiveBasicDevice::SetCachedBitrateMeasurement method

Sets the cached bitrate.

## Syntax


```C++
HRESULT SetCachedBitrateMeasurement(
  [in] GUID   physicalNetworkInterface,
  [in] UINT64 bitrate
);
```



## Parameters

<dl> <dt>

*physicalNetworkInterface* \[in\]
</dt> <dd>

Specifies the physical network interface.

</dd> <dt>

*bitrate* \[in\]
</dt> <dd>

The value to set the bitrate to.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>PlayToDevice.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>PlayToDevice.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Playtodevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**ActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385755(v=VS.85).aspx)
</dt> </dl>

 

 





