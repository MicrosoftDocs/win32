---
title: GetMuteOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetMuteAsync is completed.
ms.assetid: B8E1DE71-46AC-4F6A-B873-AE3239BE492C
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , GetMuteOperation interface
- GetMuteOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- GetMuteOperation.Completed
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location: 
---

# GetMuteOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetMuteAsync**](https://msdn.microsoft.com/en-us/library/Hh828930(v=VS.85).aspx) is completed.

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

 

 




