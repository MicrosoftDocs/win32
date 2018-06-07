---
Description: The PerformanceAlignWindow method aligns the window position to DWORD boundaries, for maximum performance.
ms.assetid: e28950bc-2510-45b9-9c9c-c2a9dbc3dc02
title: CBaseWindow.PerformanceAlignWindow method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CBaseWindow.PerformanceAlignWindow method

The `PerformanceAlignWindow` method aligns the window position to **DWORD** boundaries, for maximum performance.

## Syntax


```C++
HRESULT PerformanceAlignWindow();
```



## Parameters

This method has no parameters.

## Return value

Returns S\_OK.

## Remarks

This method aligns the left and top edges of the window to DWORD boundaries, which can improve performance. If the window has a parent, the method returns S\_OK but does perform the alignment.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




