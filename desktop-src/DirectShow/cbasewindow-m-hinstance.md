---
Description: 'Handle to the module instance.'
ms.assetid: 'ad889ebe-2bd8-4456-9517-9e2909697a02'
title: 'CBaseWindow::m\_hInstance member'
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



|                    |                                                                                                                                                                                            |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Winutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



## See also

<dl> <dt>

[**CBaseWindow Class**](cbasewindow.md)
</dt> </dl>

 

 




