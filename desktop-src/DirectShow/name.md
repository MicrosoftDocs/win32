---
Description: The NAME macro generates a debug-only string.
ms.assetid: 50762bce-a78c-4009-8552-94b2849c2b24
title: NAME
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wxdebug.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[Debug Output Functions](debug-output-functions.md)
</dt> </dl>

 

 




