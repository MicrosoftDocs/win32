---
Description: The UnblockOutputPin method unblocks the pin. When the pin is unblocked, it can deliver samples, change its output format, and reconnect itself.
ms.assetid: ea6e6312-8c7f-44db-ac7f-165dc45dec23
title: CDynamicOutputPin.UnblockOutputPin method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDynamicOutputPin.UnblockOutputPin method

The `UnblockOutputPin` method unblocks the pin. When the pin is unblocked, it can deliver samples, change its output format, and reconnect itself.

## Syntax


```C++
HRESULT UnblockOutputPin();
```



## Parameters

This method has no parameters.

## Return value

Returns one of the **HRESULT** values shown in the following table.



| Return code                                                                             | Description                           |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Pin was already unblocked.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Success.<br/>                   |



 

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




