---
title: CreateMediaRendererOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by CreateMediaRendererAsync or CreateMediaRendererFromBasicDeviceAsync is completed.
ms.assetid: B62CF929-13D0-4665-89E4-DEC48A38DDF7
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , CreateMediaRendererOperation interface
- CreateMediaRendererOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- CreateMediaRendererOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# CreateMediaRendererOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**CreateMediaRendererAsync**](imediarendererfactory-createmediarendererasync.md) or [**CreateMediaRendererFromBasicDeviceAsync**](imediarendererfactory-createmediarendererfrombasicdeviceasync.md) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  ICreateMediaRendererCompletedHandler value
);

HRESULT get_Completed(
  [out] ICreateMediaRendererCompletedHandler *value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**CreateMediaRendererOperation**](createmediarendereroperation.md)
</dt> </dl>

 

 




