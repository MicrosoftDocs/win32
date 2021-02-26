---
title: IBasicDevice remove_ConnectionStatusChanged method
description: Unregisters an event handler for the ConnectionStatusChanged event. | IBasicDevice remove_ConnectionStatusChanged method
ms.assetid: 577D9C50-486D-441A-A9FE-AF79D1FC2B52
keywords:
- remove_ConnectionStatusChanged method Media Streaming API
- remove_ConnectionStatusChanged method Media Streaming API , IBasicDevice interface
- IBasicDevice interface Media Streaming API , remove_ConnectionStatusChanged method
topic_type:
- apiref
api_name:
- IBasicDevice.remove_ConnectionStatusChanged
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IBasicDevice::remove\_ConnectionStatusChanged method

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

A reference to a token obtained from the [**add\_ConnectionStatusChanged**](ibasicdevice-add-connectionstatuschanged.md) method when the event handler was registered.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## See also

<dl> <dt>

[**IBasicDevice**](ibasicdevice.md)
</dt> </dl>

 

 





