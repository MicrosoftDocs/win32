---
Description: The IsStreamTime method specifies whether the command is to be run at stream time or presentation time.
ms.assetid: 4fb315a4-1bc6-49c8-a47f-0a8a46f3f790
title: CDeferredCommand.IsStreamTime method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CDeferredCommand.IsStreamTime method

The `IsStreamTime` method specifies whether the command is to be run at stream time or presentation time.

## Syntax


```C++
BOOL IsStreamTime();
```



## Parameters

This method has no parameters.

## Return value

Returns **TRUE** if set to stream time; otherwise, returns **FALSE**.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CDeferredCommand Class**](cdeferredcommand.md)
</dt> </dl>

 

 




