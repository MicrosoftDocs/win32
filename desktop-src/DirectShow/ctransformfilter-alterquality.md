---
description: The AlterQuality method notifies the filter that a quality change is requested.
ms.assetid: 46743d6b-65cf-4d63-8913-114277d76da4
title: CTransformFilter.AlterQuality method (Transfrm.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CTransformFilter.AlterQuality
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CTransformFilter.AlterQuality method

The `AlterQuality` method notifies the filter that a quality change is requested.

## Syntax


```C++
virtual HRESULT AlterQuality(
   Quality q
);
```



## Parameters

<dl> <dt>

*q* 
</dt> <dd>

[**Quality**](/windows/win32/api/strmif/ns-strmif-quality) structure that contains the quality control message.

</dd> </dl>

## Return value

Returns an **HRESULT** value. Possible values include those shown in the following table.



| Return code                                                                             | Description                                                                           |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | Did not handle the quality message. The message should be passed upstream.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | Handled the quality message. No further action is necessary.<br/>               |



 

## Remarks

Override this method if the filter can perform quality control. For more information, see [Quality-Control Management](quality-control-management.md).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Transfrm.h (include Streams.h)</dt> </dl>                                                                                  |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CTransformFilter Class**](ctransformfilter.md)
</dt> </dl>

 

 




