---
Description: The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.6 in order to detect HDR displays.
ms.assetid: C68EC437-7600-43A8-8DEA-5A6AEE75D5AA
title: DXGI 1.6 Improvements
ms.topic: article
ms.date: 09/24/2019
---

# DXGI 1.6 improvements

The following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.6 in order to detect HDR displays.

## High dynamic range (HDR) detection

The following APIs have been added in order to detect HDR displays.

- [**IDXGIAdapter4**](/windows/desktop/api/DXGI1_6/nn-dxgi1_6-idxgiadapter4)
- [**IDXGIOutput6**](/windows/desktop/api/DXGI1_6/nn-dxgi1_6-idxgioutput6)

Additional fields in [**DXGI\_ADAPTER\_FLAG3**](https://msdn.microsoft.com/library/Mt825227(v=VS.85).aspx) and [**DXGI\_COLOR\_SPACE\_TYPE**](/windows/desktop/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) have been added to support these APIs.

## Related topics

[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
