---
title: GetStreamPropertiesOperation.Completed property
description: Gets or sets an event handler that is invoked when the asynchronous operation started by GetStreamPropertiesAsync is completed.
ms.assetid: 97194F8E-DE36-4DC6-ADB5-F1EDE8AEF079
keywords:
- Completed property Media Streaming API
- Completed property Media Streaming API , GetStreamPropertiesOperation interface
- GetStreamPropertiesOperation interface Media Streaming API , Completed property
topic_type:
- apiref
api_name:
- GetStreamPropertiesOperation.Completed
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# GetStreamPropertiesOperation.Completed property

Gets or sets an event handler that is invoked when the asynchronous operation started by [**GetStreamPropertiesAsync**](/previous-versions/windows/desktop/legacy/hh829001(v=vs.85)) is completed.

This property is read/write.

## Syntax


```C++
HRESULT put_Completed(
  [in]  IGetStreamPropertiesCompletedHandler *value
);

HRESULT get_Completed(
  [out] IGetStreamPropertiesCompletedHandler **value
);
```



## Property value

The event handler.

## See also

<dl> <dt>

[**GetStreamPropertiesOperation**](getstreampropertiesoperation.md)
</dt> </dl>

 

 