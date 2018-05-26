---
Description: Constructor method.
ms.assetid: 48143a61-5ba7-4bf9-bffa-244f2769144d
title: CPersistStream.CPersistStream constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CPersistStream.CPersistStream constructor

Constructor method.

## Syntax


```C++
CPersistStream(
   IUnknown *pUnk,
   HRESULT  *phr
);
```



## Parameters

<dl> <dt>

*pUnk* 
</dt> <dd>

Pointer to the **IUnknown** interface of the delegating object.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to the general COM return value. This value is changed only if this function fails.

</dd> </dl>

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Pstream.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CPersistStream Class**](cpersiststream.md)
</dt> </dl>

 

 




