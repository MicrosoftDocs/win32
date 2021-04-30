---
title: IBasicDevice add_ConnectionStatusChanged method
description: Registers an event handler for the ConnectionStatusChanged event. | IBasicDevice add_ConnectionStatusChanged method
ms.assetid: 1A4CCEFE-B6B6-4AFD-9296-EE923B9EF399
keywords:
- add_ConnectionStatusChanged method Media Streaming API
- add_ConnectionStatusChanged method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , add_ConnectionStatusChanged method
topic_type:
- apiref
api_name:
- IBasicDevice.add_ConnectionStatusChanged
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::add\_ConnectionStatusChanged method

Registers an event handler for the [**ConnectionStatusChanged**](connectionstatuschanged.md) event.

## Syntax


```C++
HRESULT add_ConnectionStatusChanged(
  [in]          ConnectionStatusHandler *handler,
  [out, retval] EventRegistrationToken  *token
);
```



## Parameters

<dl> <dt>

*handler* \[in\]
</dt> <dd>

A [**ConnectionStatusHandler**](/previous-versions/windows/desktop/legacy/hh828836(v=vs.85)) event handler function.

</dd> <dt>

*token* \[out, retval\]
</dt> <dd>

Reference to a token that can be used to unregister the event handler.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

To unregister the event handler that was registered by this method, pass the *token* value to the [**remove\_ConnectionStatusChanged**](ibasicdevice-remove-connectionstatuschanged.md) method.

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

