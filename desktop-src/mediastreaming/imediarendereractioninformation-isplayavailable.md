---
title: IMediaRendererActionInformation IsPlayAvailable method
description: Retrieves a value that indicates whether the DMR is currently accepting the accepting the PlayAsync and PlayAtSpeedAsync methods.
ms.assetid: 969C55FA-872D-4063-B85C-573C8DA5593C
keywords:
- IsPlayAvailable method Media Streaming API
- IsPlayAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsPlayAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsPlayAvailable
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRendererActionInformation::IsPlayAvailable method

Retrieves a value that indicates whether the DMR is currently accepting the accepting the [**PlayAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-playasync) and [**PlayAtSpeedAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-playatspeedasync) methods.

## Syntax


```C++
HRESULT IsPlayAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is currently accepting the accepting the [**PlayAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-playasync) and [**PlayAtSpeedAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-playatspeedasync) methods and **False** if it is not.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation)
</dt> </dl>

 

