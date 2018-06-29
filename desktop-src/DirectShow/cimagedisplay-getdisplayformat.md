---
Description: The GetDisplayFormat method retrieves a video format that describes the current display mode.
ms.assetid: 98134704-0453-4090-94de-d92cdf324538
title: CImageDisplay.GetDisplayFormat method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CImageDisplay.GetDisplayFormat
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CImageDisplay.GetDisplayFormat method

The `GetDisplayFormat` method retrieves a video format that describes the current display mode.

## Syntax


```C++
const VIDEOINFO* GetDisplayFormat();
```



## Parameters

This method has no parameters.

## Return value

Returns a pointer to a [**VIDEOINFO**](/windows/desktop/api/amvideo/ns-amvideo-tagvideoinfo) structure.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CImageDisplay Class**](cimagedisplay.md)
</dt> </dl>

 

 




