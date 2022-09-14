---
description: Private message that brings the window to the foreground.
ms.assetid: 88b28888-d729-4cf3-8b9d-618dbe150926
title: CBaseWindow::m_ShowStageMessage member (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_ShowStageMessage
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
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



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




