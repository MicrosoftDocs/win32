---
description: Handle to the module instance.
ms.assetid: ad889ebe-2bd8-4456-9517-9e2909697a02
title: CBaseWindow::m_hInstance member (Winutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- m_hInstance
api_type: 
- LibDef
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CBaseWindow::m\_hInstance member

Handle to the module instance.

## Syntax


```C++
HINSTANCE m_hInstance;
```



## Remarks

The DLL entry point function sets a global variable with a handle to the module instance. The **CBaseWindow** class stores this handle in its constructor method.

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




