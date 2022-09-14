---
title: IMediaRendererActionInformation IsMuteAvailable method
description: Retrieves a value that indicates whether the DMR is capable of muting the audio.
ms.assetid: F744C2D7-5518-4A9F-A71E-60CF0B312177
keywords:
- IsMuteAvailable method Media Streaming API
- IsMuteAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsMuteAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsMuteAvailable
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRendererActionInformation::IsMuteAvailable method

Retrieves a value that indicates whether the DMR is capable of muting the audio.

## Syntax


```C++
HRESULT IsMuteAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is capable of muting the audio and **False** if it is not.

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

 

