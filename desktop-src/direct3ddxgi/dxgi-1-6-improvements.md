---
description: This topic describes what's new in Microsoft DirectX Graphics Infrastructure (DXGI) 1.6 for various releases of Windows 10.
ms.assetid: C68EC437-7600-43A8-8DEA-5A6AEE75D5AA
title: DXGI 1.6 improvements
ms.topic: article
ms.date: 12/04/2019
---

# DXGI 1.6 improvements

This topic describes what's new in Microsoft DirectX Graphics Infrastructure (DXGI) 1.6 for various releases of Windows 10.

## Windows 10 October 2018 Update

These APIs were added for Windows 10, version 1809 (10.0; Build 17763)&mdash;also known as Windows 10 October 2018 Update.

- [**IDXGIFactory7**](/windows/win32/api/dxgi1_6/nn-dxgi1_6-idxgifactory7) interface, and its methods.

## Windows 10 April 2018 Update

These APIs were added for Windows 10, version 1803 (10.0; Build 17134)&mdash;also known as Windows 10 April 2018 Update.

- [**DXGI_GPU_PREFERENCE**](/windows/win32/api/dxgi1_6/ne-dxgi1_6-dxgi_gpu_preference) enumeration.
- [**IDXGIFactory6**](/windows/win32/api/dxgi1_6/nn-dxgi1_6-idxgifactory6) interface, and its methods.

## Windows 10 Fall Creators Update

For Windows 10, version 1709 (10.0; Build 16299)&mdash;also known as Windows 10 Fall Creators Update&mdash;these constants have been added to the [**DXGI_ADAPTER_FLAG3**](/windows/win32/api/dxgi1_6/ne-dxgi1_6-dxgi_adapter_flag3) enumeration. 

- **DXGI_ADAPTER_FLAG3_SUPPORT_MONITORED_FENCES**
- **DXGI_ADAPTER_FLAG3_SUPPORT_NON_MONITORED_FENCES**
- **DXGI_ADAPTER_FLAG3_KEYED_MUTEX_CONFORMANCE**

## Windows 10 Creators Update

For Windows 10, version 1703 (10.0; Build 15063)&mdash;also known as Windows 10 Creators Update&mdash;the following functionality has been added to Microsoft DirectX Graphics Infrastructure (DXGI) 1.6 in order to detect HDR displays.

### High dynamic range (HDR) detection

These APIs have been added in order to detect HDR displays.

- [**DXGI_ADAPTER_DESC3**](/windows/win32/api/dxgi1_6/ns-dxgi1_6-dxgi_adapter_desc3) structure
- [**DXGI_ADAPTER_FLAG3**](/windows/win32/api/dxgi1_6/ne-dxgi1_6-dxgi_adapter_flag3) enumeration
- [**DXGI_HARDWARE_COMPOSITION_SUPPORT_FLAGS**](/windows/win32/api/dxgi1_6/ne-dxgi1_6-dxgi_hardware_composition_support_flags) enumeration
- [**DXGI_OUTPUT_DESC1**](/windows/win32/api/dxgi1_6/ns-dxgi1_6-dxgi_output_desc1) structure
- [**DXGIDeclareAdapterRemovalSupport**](/windows/win32/api/dxgi1_6/nf-dxgi1_6-dxgideclareadapterremovalsupport) function
- [**IDXGIAdapter4**](/windows/win32/api/dxgi1_6/nn-dxgi1_6-idxgiadapter4) interface, and its methods
- [**IDXGIOutput6**](/windows/win32/api/dxgi1_6/nn-dxgi1_6-idxgioutput6) interface, and its methods

Also, constants have been added to the [**DXGI_COLOR_SPACE_TYPE**](/windows/win32/api/dxgicommon/ne-dxgicommon-dxgi_color_space_type) enumeration to support these APIs.

## Related topics
[Programming Guide for DXGI](dx-graphics-dxgi-overviews.md)
