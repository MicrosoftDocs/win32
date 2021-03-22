---
description: The SetStretchMode method calculates whether the video image must be stretched.
ms.assetid: ffdcaf9c-e157-4557-9193-8430c1c451bf
title: CDrawImage.SetStretchMode method (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CDrawImage.SetStretchMode
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CDrawImage.SetStretchMode method

The `SetStretchMode` method calculates whether the video image must be stretched.

## Syntax


```C++
void SetStretchMode();
```



## Parameters

This method has no parameters.

## Return value

This method does not return a value.

## Remarks

The **CDrawImage** class automatically calls this method whenever the source or target rectangle changes.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




