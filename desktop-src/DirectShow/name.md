---
description: The NAME macro generates a debug-only string.
ms.assetid: '5cb9f803-dd2b-4055-bdcc-e754ef5fa505'
title: NAME (Wxdebug.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- NAME
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# NAME

The **NAME** macro generates a debug-only string.

``` syntax
NAME(strLiteral);
```

## Parameters

<dl> <dt>

<span id="strLiteral"></span><span id="strliteral"></span><span id="STRLITERAL"></span>*strLiteral*
</dt> <dd>

Text string.

</dd> </dl>

## Remarks

In debug builds, this macro is equivalent to the **TEXT** macro. In retail builds, it resolves to (TCHAR\*) **NULL**. This macro is useful when declaring the name of an object that derives from the [**CBaseObject**](cbaseobject.md) class.


```C++
pObject = new CBaseObject(NAME("My Object"));
```



## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




