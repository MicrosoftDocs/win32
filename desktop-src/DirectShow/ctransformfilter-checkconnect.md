---
Description: The CheckConnect method determines whether a pin connection is suitable.
ms.assetid: 4bec4b19-3f7c-43d8-9a45-2eb2cc15a0d4
title: CTransformFilter.CheckConnect method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransformFilter.CheckConnect method

The `CheckConnect` method determines whether a pin connection is suitable.

## Syntax


```C++
virtual HRESULT CheckConnect(
   PIN_DIRECTION dir,
   IPin          *pPin
);
```



## Parameters

<dl> <dt>

*dir* 
</dt> <dd>

Member of the [**PIN\_DIRECTION**](/windows/win32/strmif/ne-strmif-_pindirection?branch=master) enumerated type, specifying which pin on the filter is making the connection.

</dd> <dt>

*pPin* 
</dt> <dd>

Pointer to the [**IPin**](/windows/win32/Strmif/nn-strmif-ipin?branch=master) interface of the other pin in this connection attempt.

</dd> </dl>

## Return value

Returns S\_OK.

## Remarks

The [**CTransformInputPin::CheckConnect**](ctransforminputpin-checkconnect.md) and [**CTransformOutputPin::CheckConnect**](ctransformoutputpin-checkconnect.md) methods call this method during the pin connection process. This method does nothing in the base class. The derived class can override it. For example, the derived class might query the other pin for a particular interface.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




