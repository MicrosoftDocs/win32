---
Description: Constructor method.
ms.assetid: db0a3f78-ddb9-43b5-aab5-da2faaebb527
title: CTransInPlaceInputPin.CTransInPlaceInputPin constructor
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CTransInPlaceInputPin.CTransInPlaceInputPin constructor

Constructor method.

## Syntax


```C++
CTransInPlaceInputPin(
   TCHAR               *pObjectName,
   CTransInPlaceFilter *pFilter,
   HRESULT             *phr,
   LPCWSTR             pName
);
```



## Parameters

<dl> <dt>

*pObjectName* 
</dt> <dd>

String containing the debug name of the object. For more information, see [**CBaseObject**](cbaseobject.md).

</dd> <dt>

*pFilter* 
</dt> <dd>

Pointer to the filter that created this pin, which must be a [**CTransInPlaceFilter**](ctransinplacefilter.md) object.

</dd> <dt>

*phr* 
</dt> <dd>

Pointer to a variable that receives an **HRESULT** value indicating the success or failure of the method. Initialize the value to S\_OK before creating the object. The value is changed only if an error occurs.

</dd> <dt>

*pName* 
</dt> <dd>

Wide-character string containing the pin name.

</dd> </dl>

## Remarks

The *pName* parameter specifies the pin name, which is returned by the [**IPin::QueryPinInfo**](/windows/win32/Strmif/nf-strmif-ipin-querypininfo?branch=master) method. However, this string is not used for the pin identifier. The pin identifier for this class is always In. For more information, see [**CTransformInputPin::QueryId**](ctransforminputpin-queryid.md).

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transip.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransInPlaceInputPin Class**](ctransinplaceinputpin.md)
</dt> </dl>

 

 




