---
title: IMediaRendererActionInformation PlaySpeeds method
description: Retrieves the complete list of PlaySpeed values that are accepted by the DMR.
ms.assetid: 0AB63E39-6A26-4199-9978-A10866A7C805
keywords:
- PlaySpeeds method Media Streaming API
- PlaySpeeds method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , PlaySpeeds method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.PlaySpeeds
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRendererActionInformation::PlaySpeeds method

Retrieves the complete list of [**PlaySpeed**](/previous-versions/windows/desktop/api/windows.media.streaming/ns-windows-media-streaming-playspeed) values that are accepted by the DMR.

## Syntax


```C++
HRESULT PlaySpeeds(
  [out] IVector< PlaySpeed > **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Receives a vector of [**PlaySpeed**](/previous-versions/windows/desktop/api/windows.media.streaming/ns-windows-media-streaming-playspeed) structures specifying the complete list of **PlaySpeed** values that are accepted by the DMR.

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

 

