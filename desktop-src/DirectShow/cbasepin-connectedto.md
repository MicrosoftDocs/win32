---
Description: The ConnectedTo method retrieves a pointer to the connected pin, if any. This method implements the IPinConnectedTo method.
ms.assetid: d8978c9a-e498-4411-a052-f3c2fca570ef
title: CBasePin.ConnectedTo method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBasePin.ConnectedTo method

The `ConnectedTo` method retrieves a pointer to the connected pin, if any. This method implements the [**IPin::ConnectedTo**](/windows/win32/Strmif/nf-strmif-ipin-connectedto?branch=master) method.

## Syntax


```C++
HRESULT ConnectedTo(
   IPin **ppPin
);
```



## Parameters

<dl> <dt>

*ppPin* 
</dt> <dd>

Address of a variable that receives a pointer to the [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface of the other pin.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those in the following table.



| Return code                                                                                           | Description                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Success.<br/>                   |
| <dl> <dt>**E\_POINTER**</dt> </dl>             | **NULL** pointer argument.<br/> |
| <dl> <dt>**VFW\_E\_NOT\_CONNECTED**</dt> </dl> | Pin is not connected.<br/>      |



 

## Remarks

If the method succeeds, the **IPin** interface that it returns has an outstanding reference count. Be sure to release it when you are done.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBasePin Class**](cbasepin.md)
</dt> </dl>

 

 




