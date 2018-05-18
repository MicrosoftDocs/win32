---
title: D3D12\_RECT
description: D3D12\_RECT is declared as a RECT.
ms.assetid: '39511ACE-7AC5-42A2-896D-7E0977A346C6'
keywords: ["D3D12_RECT"]
topic_type:
- apiref
api_name:
- D3D12_RECT
api_location:
- D3D12.h
api_type:
- HeaderDef
---

# D3D12\_RECT

D3D12\_RECT is declared as a RECT. For more information about this GDI rectangle structure, see [**RECT**](https://msdn.microsoft.com/library/windows/desktop/dd162897).

``` syntax
typedef RECT D3D12_RECT;
```

## Remarks

This structure is used by the following methods:

-   [**RSSetScissorRects**](id3d12graphicscommandlist-rssetscissorrects.md)
-   [**ClearDepthStencilView**](id3d12graphicscommandlist-cleardepthstencilview.md)
-   [**ClearRenderTargetView**](id3d12graphicscommandlist-clearrendertargetview.md)
-   [**ClearUnorderedAccessViewUint**](id3d12graphicscommandlist-clearunorderedaccessviewuint.md)
-   [**ClearUnorderedAccessViewFloat**](id3d12graphicscommandlist-clearunorderedaccessviewfloat.md)

This structure is a member of the [**D3D12\_DISCARD\_REGION**](d3d12-discard-region.md) structure.

## Requirements



|                   |                                                                                    |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D3D12.h</dt> </dl> |



## See also

<dl> <dt>

[Core Structures](direct3d-12-structures.md)
</dt> <dt>

[**CD3DX12\_RECT**](cd3dx12-rect.md)
</dt> </dl>

 

 





