---
title: GetPositionInformationOperation.GetResults method
description: Returns the results of the asynchronous operation started by GetPositionInformationAsync.
ms.assetid: 1DC7CD65-1F0F-44A5-9836-C77A5C23F91E
keywords:
- GetResults method Media Streaming API
- GetResults method Media Streaming API , GetPositionInformationOperation interface
- GetPositionInformationOperation interface Media Streaming API , GetResults method
topic_type:
- apiref
api_name:
- GetPositionInformationOperation.GetResults
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetPositionInformationOperation.GetResults method

Returns the results of the asynchronous operation started by [**GetPositionInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getpositioninformationasync).

## Syntax


```C++
HRESULT GetResults(
  [out, retval] PositionInformation *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

A reference to a [**PositionInformation**](/previous-versions/windows/desktop/api/windows.media.streaming/ns-windows-media-streaming-positioninformation) structure that contains the results of the operation.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The **GetResults** method is typically called from the event handler that was registered by setting the [**Completed**](getpositioninformationoperation-completed.md) property.

## See also

<dl> <dt>

[**GetPositionInformationOperation**](getpositioninformationoperation.md)
</dt> </dl>

 

