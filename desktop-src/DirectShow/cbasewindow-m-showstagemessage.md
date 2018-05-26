---
Description: Private message that brings the window to the foreground.
ms.assetid: 88b28888-d729-4cf3-8b9d-618dbe150926
title: CBaseWindowm\_ShowStageMessage member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseWindow::m\_ShowStageMessage member

Private message that brings the window to the foreground.

## Syntax


```C++
UINT m_ShowStageMessage;
```



## Remarks

The [**CBaseWindow::DoSetWindowForeground**](cbasewindow-dosetwindowforeground.md) method sends this message.

## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




