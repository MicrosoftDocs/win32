---
title: StreamSelectOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by SelectBestStreamAsync is completed.
ms.assetid: 693CC002-2D91-4656-954D-8A556480155C
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , StreamSelectOperation interface
- StreamSelectOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- StreamSelectOperation.Completed
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StreamSelectOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**SelectBestStreamAsync**](streamselector-selectbeststreamasync.md) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  IStreamSelectCompletedHandler *value
);

HRESULT get_Completed(
  [out] IStreamSelectCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**StreamSelectOperation**](streamselectoperation.md)
</dt> </dl>

 

 




