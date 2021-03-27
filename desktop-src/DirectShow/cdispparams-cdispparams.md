---
description: Constructor method.
ms.assetid: da67a5e4-b4a1-4a38-93fe-0965695e93f5
title: CDispParams.CDispParams constructor (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDispParams.CDispParams
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDispParams.CDispParams constructor

Constructor method.

## Syntax


```C++
CDispParams(
   UINT    nArgs,
   VARIANT *pArgs
);
```



## Parameters

<dl> <dt>

*nArgs* 
</dt> <dd>

Number of arguments passed to the method or property.

</dd> <dt>

*pArgs* 
</dt> <dd>

Pointer to the list of arguments. In the list, each argument is stored with its variant type.

</dd> </dl>

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDispParams Class**](cdispparams.md)
</dt> </dl>

 

 




