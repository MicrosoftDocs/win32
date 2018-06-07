---
Description: The SetStretchMode method calculates whether the video image must be stretched.
ms.assetid: ffdcaf9c-e157-4557-9193-8430c1c451bf
title: CDrawImage.SetStretchMode method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




