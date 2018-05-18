---
title: GetMuteOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetMuteAsync is completed.
ms.assetid: 'B8E1DE71-46AC-4F6A-B873-AE3239BE492C'
keywords: ["Completed property Media Streaming API", "Completed property Media Streaming API , GetMuteOperation interface", "GetMuteOperation interface Media Streaming API , Completed property"]
topic_type:
- apiref
api_name:
- GetMuteOperation.Completed
api_type:
- COM
---

# GetMuteOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](imediarenderer-getmuteasync.md) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  GetMuteCompletedHandler *value
);

HRESULT get_Completed(
  [out] GetMuteCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**GetMuteOperation**](getmuteoperation.md)
</dt> </dl>

 

 




