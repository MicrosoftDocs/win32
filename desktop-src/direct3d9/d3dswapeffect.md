---
description: Defines swap effects.
ms.assetid: 522a5f71-3ad9-4cfc-a899-e25b9b721b1b
title: D3DSWAPEFFECT enumeration (D3D9Types.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- D3DSWAPEFFECT
api_type:
- HeaderDef
api_location:
- D3D9Types.h
---

# D3DSWAPEFFECT enumeration

Defines swap effects.

## Syntax

```cpp
typedef enum D3DSWAPEFFECT { 
  D3DSWAPEFFECT_DISCARD      = 1,
  D3DSWAPEFFECT_FLIP         = 2,
  D3DSWAPEFFECT_COPY         = 3,
  D3DSWAPEFFECT_OVERLAY      = 4,
  D3DSWAPEFFECT_FLIPEX       = 5,
  D3DSWAPEFFECT_FORCE_DWORD  = 0xFFFFFFFF
} D3DSWAPEFFECT, *LPD3DSWAPEFFECT;
```

## Constants

<dl> <dt>

<span id="D3DSWAPEFFECT_DISCARD"></span><span id="d3dswapeffect_discard"></span>**D3DSWAPEFFECT\_DISCARD**
</dt> <dd>

When a swap chain is created with a swap effect of D3DSWAPEFFECT\_FLIP or D3DSWAPEFFECT\_COPY, the runtime will guarantee that an [**IDirect3DDevice9::Present**](/windows/desktop/api) operation will not affect the content of any of the back buffers. Unfortunately, meeting this guarantee can involve substantial video memory or processing overheads, especially when implementing flip semantics for a windowed swap chain or copy semantics for a full-screen swap chain. An application may use the D3DSWAPEFFECT\_DISCARD swap effect to avoid these overheads and to enable the display driver to select the most efficient presentation technique for the swap chain. This is also the only swap effect that may be used when specifying a value other than D3DMULTISAMPLE\_NONE for the MultiSampleType member of [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md).

Like a swap chain that uses D3DSWAPEFFECT\_FLIP, a swap chain that uses D3DSWAPEFFECT\_DISCARD might include more than one back buffer, any of which may be accessed using [**IDirect3DDevice9::GetBackBuffer**](/windows/desktop/api) or [**IDirect3DSwapChain9::GetBackBuffer**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dswapchain9-getbackbuffer). The swap chain is best envisaged as a queue in which 0 always indexes the back buffer that will be displayed by the next Present operation and from which buffers are discarded when they have been displayed.

An application that uses this swap effect cannot make any assumptions about the contents of a discarded back buffer and should therefore update an entire back buffer before invoking a Present operation that would display it. Although this is not enforced, the debug version of the runtime will overwrite the contents of discarded back buffers with random data to enable developers to verify that their applications are updating the entire back buffer surfaces correctly.

</dd> <dt>

<span id="D3DSWAPEFFECT_FLIP"></span><span id="d3dswapeffect_flip"></span>**D3DSWAPEFFECT\_FLIP**
</dt> <dd>

The swap chain might include multiple back buffers and is best envisaged as a circular queue that includes the front buffer. Within this queue, the back buffers are always numbered sequentially from 0 to (n - 1), where n is the number of back buffers, so that 0 denotes the least recently presented buffer. When Present is invoked, the queue is "rotated" so that the front buffer becomes back buffer (n - 1), while the back buffer 0 becomes the new front buffer.

</dd> <dt>

<span id="D3DSWAPEFFECT_COPY"></span><span id="d3dswapeffect_copy"></span>**D3DSWAPEFFECT\_COPY**
</dt> <dd>

This swap effect may be specified only for a swap chain comprising a single back buffer. Whether the swap chain is windowed or full-screen, the runtime will guarantee the semantics implied by a copy-based Present operation, namely that the operation leaves the content of the back buffer unchanged, instead of replacing it with the content of the front buffer as a flip-based Present operation would.

For a full-screen swap chain, the runtime uses a combination of flip operations and copy operations, supported if necessary by hidden back buffers, to accomplish the Present operation. Accordingly, the presentation is synchronized with the display adapter's vertical retrace and its rate is constrained by the chosen presentation interval. A swap chain specified with the D3DPRESENT\_INTERVAL\_IMMEDIATE flag is the only exception. (Refer to the description of the **PresentationIntervals** member of the [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) structure.) In this case, a Present operation copies the back buffer content directly to the front buffer without waiting for the vertical retrace.

</dd> <dt>

<span id="D3DSWAPEFFECT_OVERLAY"></span><span id="d3dswapeffect_overlay"></span>**D3DSWAPEFFECT\_OVERLAY**
</dt> <dd>

Use a dedicated area of video memory that can be overlayed on the primary surface. No copy is performed when the overlay is displayed. The overlay operation is performed in hardware, without modifying the data in the primary surface.

|                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 9Ex:<br/> D3DSWAPEFFECT\_OVERLAY is only available in Direct3D9Ex running on Windows 7 (or more current operating system).<br/> |

</dd> <dt>

<span id="D3DSWAPEFFECT_FLIPEX"></span><span id="d3dswapeffect_flipex"></span>**D3DSWAPEFFECT\_FLIPEX**
</dt> <dd>

Designates when an application is adopting flip mode, during which time an application's frame is passed instead of copied to the Desktop Window Manager(DWM) for composition when the application is presenting in windowed mode. Flip mode allows an application to more efficiently use memory bandwidth as well as enabling an application to take advantage of full-screen-present statistics. Flip mode does not affect full-screen behavior.

> [!Note]  
> If you create a swap chain with D3DSWAPEFFECT\_FLIPEX, you can't override the **hDeviceWindow** member of the [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) structure when you present a new frame for display. That is, you must pass **NULL** to the *hDestWindowOverride* parameter of [**IDirect3DDevice9Ex::PresentEx**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9ex-presentex) to instruct the runtime to use the **hDeviceWindow** member of **D3DPRESENT\_PARAMETERS** for the presentation.

|                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Differences between Direct3D 9 and Direct3D 9Ex:<br/> D3DSWAPEFFECT\_FLIPEX is only available in Direct3D9Ex running on Windows 7 (or more current operating system).<br/> |

</dd> <dt>

<span id="D3DSWAPEFFECT_FORCE_DWORD"></span><span id="d3dswapeffect_force_dword"></span>**D3DSWAPEFFECT\_FORCE\_DWORD**
</dt> <dd>

Forces this enumeration to compile to 32 bits in size. Without this value, some compilers would allow this enumeration to compile to a size other than 32 bits. This value is not used.

</dd> </dl>

## Remarks

The state of the back buffer after a call to Present is well-defined by each of these swap effects, and whether the Direct3D device was created with a full-screen swap chain or a windowed swap chain has no effect on this state. In particular, the D3DSWAPEFFECT\_FLIP swap effect operates the same whether windowed or full-screen, and the Direct3D runtime guarantees this by creating extra buffers. As a result, it is recommended that applications use D3DSWAPEFFECT\_DISCARD whenever possible to avoid any such penalties. This is because this swap effect will always be the most efficient in terms of memory consumption and performance.

Applications that use D3DSWAPEFFECT\_FLIP or D3DSWAPEFFECT\_DISCARD should not expect full-screen destination alpha to work. This means that the D3DRS\_DESTBLEND render state will not work as expected because full-screen swap chains with these swap effects do not have an explicit pixel format from the driver's point of view. The driver infers that they should take on the display format, which does not have an alpha channel. To work around this, take the following steps:

-   Use D3DSWAPEFFECT\_COPY.
-   Check the D3DCAPS3\_ALPHA\_FULLSCREEN\_FLIP\_OR\_DISCARD flag in the Caps3 member of the [**D3DCAPS9**](/windows/desktop/api/D3D9Caps/ns-d3d9caps-d3dcaps9) structure. This flag indicates whether the driver can do alpha blending when D3DSWAPEFFECT\_FLIP or D3DSWAPEFFECT\_DISCARD is used.
-   Applications using flip mode swap effect (D3DSWAPEFFECT\_FLIPEX) should call [**PresentEx**](/windows/desktop/api/d3d9/nf-d3d9-idirect3ddevice9ex-presentex) after a window resize or region change to ensure that the display content is updated.

An invisible window cannot receive user-mode events; furthermore, an invisible-fullscreen window will interfere with the presentation of another applications' windowed-mode window. Therefore, each application needs to ensure that a device window is visible when a swapchain is presented in fullscreen mode.

## Requirements

| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D9Types.h</dt> </dl> |

## See also

[Direct3D Enumerations](dx9-graphics-reference-d3d-enums.md)

[**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset)
