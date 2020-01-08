---
title: ICompositionDrawingSurfaceInterop2::CopySurface
description: Creates a copy of a composition surface, for use with a swap chain.
ms.localizationpriority: low
ms.topic: reference
ms.date: 01/07/2020
---

# ICompositionDrawingSurfaceInterop2::CopySurface method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description
Creates a copy of a composition surface, for use with a swap chain.

## Syntax

```cpp
HRESULT CopySurface(
  IUnknown* destinationResource,
  int destinationOffsetX,
  int destinationOffsetY,
  const RECT * sourceRectangle
);
```

## Parameters

`destinationResource [in]`

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

A pointer to the resource into which to copy the surface.

`destinationOffsetX [in]`

Type: **int**

The x coordinate of an offset into the destination resource.

`destinationOffsetY [in]`

Type: **int**

The y coordinate of an offset into the destination resource.

`sourceRectangle [in]`

Type: **const [RECT](/windows/win32/api/windef/ns-windef-rect)\***

An optional pointer to a constant **RECT** representing the source surface to copy.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

## Remarks

This interface is available on Windows 10, version 1903 (10.0; Build 18362), but it is not defined in the `windows.ui.composition.interop.h` header file for that version of the Windows Software Development Kit (SDK). If you first obtain a pointer to an [ICompositionDrawingSurfaceInterop](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop) interface, you can then query that (via [QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void))) for a pointer to an [ICompositionDrawingSurfaceInterop2](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop2) interface.

## See also

* [ICompositionDrawingSurfaceInterop interface](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop)
* [ICompositionDrawingSurfaceInterop2 interface](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop2)
* [Composition native interoperation overview](/windows/uwp/composition/composition-native-interop)