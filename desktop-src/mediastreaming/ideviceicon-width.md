---
title: IDeviceIcon Width method
description: Retrieves the width of the icon in pixels.
ms.assetid: 28ADA921-6808-43B8-966E-BA42B1B52931
keywords:
- Width method Media Streaming API
- Width method Media Streaming API , IDeviceIcon interface
- IDeviceIcon interface Media Streaming API , Width method
topic_type:
- apiref
api_name:
- IDeviceIcon.Width
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IDeviceIcon::Width method

Retrieves the width of the icon in pixels.

## Syntax


```C++
HRESULT Width(
  [out] UINT32 *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a pointer to the width of the icon in pixels.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IDeviceIcon**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-ideviceicon)
</dt> </dl>

 

