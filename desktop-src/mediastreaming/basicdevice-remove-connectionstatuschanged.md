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
ms.date: 05/31/2018
api_location: 
---

# BasicDevice.remove\_ConnectionStatusChanged method

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

 

