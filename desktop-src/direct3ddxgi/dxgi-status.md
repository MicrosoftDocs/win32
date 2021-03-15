---
description: Status codes that can be returned by DXGI functions.
ms.assetid: dd7480b4-8218-4716-ab9f-74a9955b8aa7
title: DXGI_STATUS (DXGI.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DXGI\_STATUS

Status codes that can be returned by DXGI functions.



| Constant/value                                                                                                                                                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="DXGI_STATUS_OCCLUDED"></span><span id="dxgi_status_occluded"></span><dl> <dt>**DXGI\_STATUS\_OCCLUDED**</dt> <dt>0x087A0001</dt> </dl>                                                 | The window content is not visible. When receiving this status, an application can stop rendering and use DXGI\_PRESENT\_TEST to determine when to resume rendering. You will not receive DXGI\_STATUS\_OCCLUDED if you're using a flip model swap chain.<br/>                                                                                                                           |
| <span id="DXGI_STATUS_MODE_CHANGED"></span><span id="dxgi_status_mode_changed"></span><dl> <dt>**DXGI\_STATUS\_MODE\_CHANGED**</dt> <dt>0x087A0007</dt> </dl>                                    | The desktop display mode has been changed, there might be color conversion/stretching. The application should call [**IDXGISwapChain::ResizeBuffers**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-resizebuffers) to match the new display mode.<br/>                                                                       |
| <span id="DXGI_STATUS_MODE_CHANGE_IN_PROGRESS"></span><span id="dxgi_status_mode_change_in_progress"></span><dl> <dt>**DXGI\_STATUS\_MODE\_CHANGE\_IN\_PROGRESS**</dt> <dt>0x087A0008</dt> </dl> | [**IDXGISwapChain::ResizeTarget**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-resizetarget) and [**IDXGISwapChain::SetFullscreenState**](/windows/desktop/api/DXGI/nf-dxgi-idxgiswapchain-setfullscreenstate) will return DXGI\_STATUS\_MODE\_CHANGE\_IN\_PROGRESS if a fullscreen/windowed mode transition is occurring when either API is called.<br/> |



## Remarks

The **HRESULT** value for each **DXGI\_STATUS** value is determined from this macro that is defined in DXGItype.h:


```
#define _FACDXGI    0x87a
#define MAKE_DXGI_STATUS(code)  MAKE_HRESULT(0, _FACDXGI, code)
```



For example, **DXGI\_STATUS\_OCCLUDED** is defined as **0x087A0001**:


```
#define DXGI_STATUS_OCCLUDED                    MAKE_DXGI_STATUS(1)
```



## Requirements



| Requirement | Value |
|-------------------|-----------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DXGI.h</dt> </dl> |



## See also

<dl> <dt>

[DXGI Constants](d3d10-graphics-reference-dxgi-constants.md)
</dt> </dl>

 

 




