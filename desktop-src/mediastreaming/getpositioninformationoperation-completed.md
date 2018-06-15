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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetPositionInformationOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetPositionInformationAsync**](https://msdn.microsoft.com/en-us/library/Hh828931(v=VS.85).aspx) is completed.

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

 

 




