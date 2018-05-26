---
Description: Constructor method.
ms.assetid: b7d5264a-2a5f-4111-96bb-1ea2b13405be
title: CMediaType.CMediaType constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CMediaType.CMediaType constructor

Constructor method.

## Syntax


```C++
CMediaType(
  [ref] const AM_MEDIA_TYPE &amp;mtype,
              HRESULT       *phr = NULL
);
```



## Parameters

<dl> <dt>

*mtype* \[ref\]
</dt> <dd>

Reference to an [**AM\_MEDIA\_TYPE**](/windows/win32/strmif/ns-strmif-_ammediatype?branch=master) structure. The constructor copies the media type to the new object, including the format block, if any.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an HRESULT value. This parameter can be a **NULL** pointer. Otherwise, the caller must set the value to S\_OK before calling the constructor. If the constructor fails, it sets the value to a failure code.

</dd> </dl>

## Remarks

The constructor calls the [**CMediaType::InitMediaType**](cmediatype-initmediatype.md) method to initialize the media type.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Mtype.h (include Streams.h)</dt> </dl>                                                                                     |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CMediaType Class**](cmediatype.md)
</dt> </dl>

 

 




