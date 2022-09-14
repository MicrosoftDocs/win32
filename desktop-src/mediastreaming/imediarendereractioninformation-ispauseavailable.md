---
title: IMediaRendererActionInformation IsPauseAvailable method
description: Retrieves a value that indicates whether the DMR is currently accepting the PauseAsync method.
ms.assetid: 095A664F-D974-410D-8741-87A171EDD071
keywords:
- IsPauseAvailable method Media Streaming API
- IsPauseAvailable method Media Streaming API , IMediaRendererActionInformation interface
- IMediaRendererActionInformation interface Media Streaming API , IsPauseAvailable method
topic_type:
- apiref
api_name:
- IMediaRendererActionInformation.IsPauseAvailable
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IMediaRendererActionInformation::IsPauseAvailable method

Retrieves a value that indicates whether the DMR is currently accepting the [**PauseAsync**](imediarenderer-pauseasync.md) method.

## Syntax


```C++
HRESULT IsPauseAvailable(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

A boolean value that is **True** if the DMR is currently accepting the [**PauseAsync**](imediarenderer-pauseasync.md) method and **False** if it is not.

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

 

