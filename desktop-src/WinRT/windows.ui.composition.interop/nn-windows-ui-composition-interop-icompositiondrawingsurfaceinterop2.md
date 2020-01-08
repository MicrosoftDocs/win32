---
title: ICompositionDrawingSurfaceInterop2
description: A native interoperation interface that allows you to copy a surface object.
ms.localizationpriority: low
ms.topic: reference
ms.date: 01/07/2020
---

# ICompositionDrawingSurfaceInterop2 interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available only in the [Windows 10 SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

A native interoperation interface that allows you to copy a surface object. This interface is available in C++ only.

**ICompositionDrawingSurfaceInterop2** inherits from the [ICompositionDrawingSurfaceInterop](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop) interface.

## Remarks

This interface is available on Windows 10, version 1903 (10.0; Build 18362), but it is not defined in the `windows.ui.composition.interop.h` header file for that version of the Windows Software Development Kit (SDK). If you first obtain a pointer to an [ICompositionDrawingSurfaceInterop](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop) interface, you can then query that (via [QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void))) for a pointer to an **ICompositionDrawingSurfaceInterop2** interface.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Target Platform** | Windows |
| **Header** | windows.ui.composition.interop.h |

## See also

* [ICompositionDrawingSurfaceInterop interface](/windows/win32/api/windows.ui.composition.interop/nn-windows-ui-composition-interop-icompositiondrawingsurfaceinterop)
* [Composition native interoperation overview](/windows/uwp/composition/composition-native-interop)