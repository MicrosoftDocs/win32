---
title: GetPositionInformationOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetPositionInformationAsync is completed.
ms.assetid: 144065AE-6C23-4E9D-B9D0-6849E7FB74C4
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , GetPositionInformationOperation interface
- GetPositionInformationOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- GetPositionInformationOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetPositionInformationOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](/previous-versions/windows/desktop/api/windows.media.streaming/nf-windows-media-streaming-imediarenderer-getpositioninformationasync) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  GetPositionInformationCompletedHandler *value
);

HRESULT get_Completed(
  [out] GetPositionInformationCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**GetPositionInformationOperation**](getpositioninformationoperation.md)
</dt> </dl>

 

 