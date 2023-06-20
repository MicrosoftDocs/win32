---
title: ITransportParameters ActionInformation method
description: Obtains an IMediaRendererActionInformation interface that provides information about which methods can currently be invoked on the DMR.
ms.assetid: 3EEB94E1-B6BC-4111-AEF1-D5724BD0A2E7
keywords:
- ActionInformation method Media Streaming API
- ActionInformation method Media Streaming API , ITransportParameters interface
- ITransportParameters interface Media Streaming API , ActionInformation method
topic_type:
- apiref
api_name:
- ITransportParameters.ActionInformation
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# ITransportParameters::ActionInformation method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Obtains an [**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation) interface that provides information about which methods can currently be invoked on the DMR.

## Syntax


```C++
HRESULT ActionInformation(
  [out, retval] IMediaRendererActionInformation **value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

Receives a reference to an [**IMediaRendererActionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-imediarendereractioninformation) interface.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**ITransportParameters**](/previous-versions/windows/desktop/api/windows.media.streaming/nn-windows-media-streaming-itransportparameters)
</dt> </dl>

 

