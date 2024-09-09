---
title: BasicDevice.remove_ConnectionStatusChanged method
description: Unregisters an event handler for the ConnectionStatusChanged event. | BasicDevice.remove_ConnectionStatusChanged method
ms.assetid: 537CA8FE-D2E1-4CC7-BB80-FBE36A2D4A1E
keywords:
- remove_ConnectionStatusChanged method Media Streaming API
- remove_ConnectionStatusChanged method Media Streaming API , BasicDevice interface
- BasicDevice interface Media Streaming API , remove_ConnectionStatusChanged method
topic_type:
- apiref
api_name:
- BasicDevice.remove_ConnectionStatusChanged
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# BasicDevice.remove\_ConnectionStatusChanged method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Unregisters an event handler for the [**ConnectionStatusChanged**](connectionstatuschanged.md) event.

## Syntax


```C++
HRESULT remove_ConnectionStatusChanged(
  [in] EventRegistrationToken *token
);
```



## Parameters

<dl> <dt>

*token* \[in\]
</dt> <dd>

A reference to a token obtained from the [**add\_ConnectionStatusChanged**](basicdevice-add-connectionstatuschanged.md) method when the event handler was registered.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**BasicDevice**](/previous-versions/windows/desktop/legacy/hh828813(v=vs.85))
</dt> </dl>

 

