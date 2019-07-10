---
title: ID2D1Factory CreateHwndRenderTarget methods
description: Creates an ID2D1HwndRenderTarget, a render target that renders to a window.
ms.assetid: 3b55b1b0-a423-40dc-9581-c1fbe8134ca5
keywords:
- CreateHwndRenderTarget methods Direct2D
topic_type:
- apiref
api_location:
- D2d1.dll
api_type:
- DllExport
ms.date: 07/02/2019
---

# ID2D1Factory::CreateHwndRenderTarget methods

Creates an [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx), a render target that renders to a window.

### Overload list



| Method                                                                                                                                                                                                                                                                              | Description                                                                                                             |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**CreateHwndRenderTarget(D2D1\_RENDER\_TARGET\_PROPERTIES\*,D2D1\_HWND\_RENDER\_TARGET\_PROPERTIES\*,ID2D1HwndRenderTarget\*\*)**](id2d1factory-createhwndrendertarget-ptr-d2d1-render-target-properties-ptr-d2d1-hwnd-render-target-properties-ptr-ptr-https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx) | Creates an [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx), a render target that renders to a window.<br/> |
| [**CreateHwndRenderTarget(D2D1\_RENDER\_TARGET\_PROPERTIES&,D2D1\_HWND\_RENDER\_TARGET\_PROPERTIES&,ID2D1HwndRenderTarget\*\*)**](id2d1factory-createhwndrendertarget-ref-d2d1-render-target-properties-ref-d2d1-hwnd-render-target-properties-ptr-ptr-https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx)   | Creates an [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx), a render target that renders to a window.<br/> |



## Remarks

When you create a render target and hardware acceleration is available, you allocate resources on the computer's GPU. By creating a render target once and retaining it as long as possible, you gain performance benefits. Your application should create render targets once and hold onto them for the life of the application or until the [**D2DERR\_RECREATE\_TARGET**](direct2d-error-codes.md) error is received. When you receive this error, you need to recreate the render target (and any resources it created).

## Examples

The following example creates an [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/Dd371275(v=VS.85).aspx).


```C++
RECT rc;
GetClientRect(m_hwnd, &amp;rc);

D2D1_SIZE_U size = D2D1::SizeU(
    rc.right - rc.left,
    rc.bottom - rc.top
    );

// Create a Direct2D render target.
hr = m_pD2DFactory->CreateHwndRenderTarget(
    D2D1::RenderTargetProperties(),
    D2D1::HwndRenderTargetProperties(m_hwnd, size),
    &amp;m_pRenderTarget
    );
```



## Requirements



|                    |                                                                                     |
|--------------------|-------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D2d1.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D2d1.lib</dt> </dl> |
| DLL<br/>     | <dl> <dt>D2d1.dll</dt> </dl> |



## See also

<dl> <dt>

[**ID2D1Factory**](https://msdn.microsoft.com/en-us/library/Dd371246(v=VS.85).aspx)
</dt> </dl>

�

�





