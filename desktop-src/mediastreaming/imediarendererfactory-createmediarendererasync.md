---
title: IMediaRendererFactory CreateMediaRendererAsync method
description: Asynchronously creates a new instance of an object that implements the IMediaRenderer interface using the specified Unique Device Name (UDN).
ms.assetid: FD1242F8-4C2E-4027-B1DE-5FD69557684C
keywords:
- CreateMediaRendererAsync method Media Streaming API
- CreateMediaRendererAsync method Media Streaming API , IMediaRendererFactory interface
- IMediaRendererFactory interface Media Streaming API , CreateMediaRendererAsync method
topic_type:
- apiref
api_name:
- IMediaRendererFactory.CreateMediaRendererAsync
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRendererFactory::CreateMediaRendererAsync method

Asynchronously creates a new instance of an object that implements the [**IMediaRenderer**](imediarenderer.md) interface using the specified Unique Device Name (UDN).

## Syntax


```C++
HRESULT CreateMediaRendererAsync(
  [in]          HSTRING                      deviceIdentifier,
  [out, retval] CreateMediaRendererOperation **value
);
```



## Parameters

<dl> <dt>

*deviceIdentifier* \[in\]
</dt> <dd>

An HSTRING containing a UDN that identifies the DLNA DMR device for which an instance of [**IMediaRenderer**](imediarenderer.md) will be created.

</dd> <dt>

*value* \[out, retval\]
</dt> <dd>

Receives a reference to a [**CreateMediaRendererOperation**](createmediarendereroperation.md) object that is used to get results from the asynchronous operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererFactory**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendererfactory)
</dt> </dl>

 

