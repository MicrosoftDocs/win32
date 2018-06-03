---
Description: Sets the FOURCC portion of the FOURCCMap object.
ms.assetid: cc821e39-e565-4255-a289-2c9507d43433
title: FOURCCMap::SetFOURCC method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# FOURCCMap::SetFOURCC method

Sets the **FOURCC** portion of the [**FOURCCMap**](fourccmap.md) object.

## Syntax


```C++
void SetFOURCC(
   const GUID *pguid
);
```



## Parameters

<dl> <dt>

*pguid* 
</dt> <dd>

Pointer to the returned globally unique identifier (**GUID**) part of the **FOURCCMap** object.

</dd> </dl>

## Return value

No return value.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Fourcc.h (include Streams.h)</dt> </dl>                                                                                    |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**FOURCCMap Class**](fourccmap.md)
</dt> </dl>

 

 




