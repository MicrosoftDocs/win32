---
Description: The m\_StartSample member variable specifies the start time of the most recent sample.
ms.assetid: 2e6d6893-d57b-4009-a6ec-40dc0878d9c4
title: CDrawImage::m\_StartSample member
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDrawImage::m\_StartSample member

The **m\_StartSample** member variable specifies the start time of the most recent sample.

## Syntax


```C++
CRefTime m_StartSample;
```



## Remarks

The value is only valid inside the [**CDrawImage::DisplaySampleTimes**](cdrawimage-displaysampletimes.md) method.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDrawImage Class**](cdrawimage.md)
</dt> </dl>

 

 




