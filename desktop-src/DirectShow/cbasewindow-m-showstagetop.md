---
description: Private message that sets the window style to WS\_EX\_TOPMOST.
ms.assetid: 4934400e-4ca5-4ace-b9b9-3889f4cf610e
title: CBaseWindow::m_ShowStageTop member (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_ShowStageTop
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow::m\_ShowStageTop member

Private message that sets the window style to WS\_EX\_TOPMOST.

## Syntax


```C++
UINT m_ShowStageTop;
```



## Remarks

Video renderers should send this message to the window if they switch to full-screen mode.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




