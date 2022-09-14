---
title: D3D12_RECT (D3D12.h)
description: D3D12\_RECT is declared as a RECT.
ms.assetid: 39511ACE-7AC5-42A2-896D-7E0977A346C6
keywords:
- D3D12_RECT
topic_type:
- apiref
api_name:
- D3D12_RECT
api_location:
- D3D12.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# D3D12\_RECT

D3D12\_RECT is declared as a RECT. For more information about this GDI rectangle structure, see [**RECT**](/previous-versions//dd162897(v=vs.85)).

``` syntax
typedef RECT D3D12_RECT;
```

## Remarks

This structure is used by the following methods:

-   [**RSSetScissorRects**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-rssetscissorrects)
-   [**ClearDepthStencilView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-cleardepthstencilview)
-   [**ClearRenderTargetView**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearrendertargetview)
-   [**ClearUnorderedAccessViewUint**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewuint)
-   [**ClearUnorderedAccessViewFloat**](/windows/desktop/api/d3d12/nf-d3d12-id3d12graphicscommandlist-clearunorderedaccessviewfloat)

This structure is a member of the [**D3D12\_DISCARD\_REGION**](/windows/desktop/api/d3d12/ns-d3d12-d3d12_discard_region) structure.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D12.h</dt> </dl> |



## See also

<dl> <dt>

[Core Structures](direct3d-12-structures.md)
</dt> <dt>

[**CD3DX12\_RECT**](cd3dx12-rect.md)
</dt> </dl>

 

