---
Description: Constructor method.
ms.assetid: 996adc69-8727-431e-a7f5-8fbcc0e305ae
title: CDynamicOutputPin.CDynamicOutputPin constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CDynamicOutputPin.CDynamicOutputPin constructor

Constructor method.

## Syntax


```C++
CDynamicOutputPin(
   TCHAR       *pObjectName,
   CBaseFilter *pFilter,
   CCritSec    *pLock,
   HRESULT     *phr,
   LPCWSTR     pName
);
```



## Parameters

<dl> <dt>

*pObjectName* 
</dt> <dd>

Pointer to a string containing the name of the object. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*pFilter* 
</dt> <dd>

Pointer to the filter that created this pin.

</dd> <dt>

*pLock* 
</dt> <dd>

Pointer to a [**CCritSec**](ccritsec.md) lock, used to serialize state changes. Use the same critical section as the filter lock, [**CBaseFilter::m\_pLock**](cbasefilter-m-plock.md)

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value indicating the success or failure of the method. Initialize the value to S\_OK before creating the object. The value is changed only if an error occurs.

</dd> <dt>

*pName* 
</dt> <dd>

Pointer to a wide-character string containing the pin identifier. For more information, see [**IPin::QueryId**](/windows/win32/Strmif/nf-strmif-ipin-queryid?branch=master).

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Amfilter.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDynamicOutputPin Class**](cdynamicoutputpin.md)
</dt> </dl>

 

 




