---
description: The CancelNotification method cancels the timer event that schedules rendering.
ms.assetid: 56ddf692-a2e3-40f2-848f-2d592601ec00
title: CBaseRenderer.CancelNotification method (Renbase.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CBaseRenderer.CancelNotification
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseRenderer.CancelNotification method

The `CancelNotification` method cancels the timer event that schedules rendering.

## Syntax


```C++
virtual HRESULT CancelNotification();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                                  |
|-----------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | There was no pending timer event.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                          |



 

## Remarks

The filter calls this method when streaming stops. The method cancels any scheduled rendering.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Renbase.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseRenderer Class**](cbaserenderer.md)
</dt> </dl>

 

 




