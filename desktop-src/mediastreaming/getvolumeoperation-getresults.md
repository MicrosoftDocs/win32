---
title: GetVolumeOperation.GetResults method
description: Returns the results of the asynchronous operation started by GetVolumeAsync.
ms.assetid: 71DC4D76-4CC2-4D40-960F-AF56E1F33557
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , GetVolumeOperation interface
- GetVolumeOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- GetVolumeOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetVolumeOperation.GetResults method

Returns the results of the asynchronous operation started by [**GetVolumeAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getvolumeasync).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] UINT32 *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

The volume. A value between 0 and 100. 0 indicates minimum volume, and 100 indicates maximum volume.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The **GetResults** method is typically called from the event handler that was registered by setting the [**Completed**](getvolumeoperation-completed.md) property.

## See also

<dl> <dt>

[**GetVolumeOperation**](getvolumeoperation.md)
</dt> </dl>

 

