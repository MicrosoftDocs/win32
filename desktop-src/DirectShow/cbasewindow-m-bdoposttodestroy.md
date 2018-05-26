---
Description: Flag that specifies whether the window posts or sends its destruction message.
ms.assetid: 553a372e-1abe-4661-bfa5-b8a63be63c72
title: CBaseWindowm\_bDoPostToDestroy member
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CBaseWindow::m\_bDoPostToDestroy member

Flag that specifies whether the window posts or sends its destruction message. If **TRUE**, the [**CBaseWindow::DoneWithWindow**](cbasewindow-donewithwindow.md) method uses the **PostMessage** function to send itself a private destruction message. If **FALSE**, **DoneWithWindow** uses the **SendMessage** function to send the message. By default, the value is **FALSE**.

## Syntax


```C++
BOOL m_bDoPostToDestroy;
```



## Requirements



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




