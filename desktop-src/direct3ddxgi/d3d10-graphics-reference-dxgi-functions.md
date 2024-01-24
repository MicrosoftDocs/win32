---
description: This section contains info about the functions provided by DXGI.
ms.assetid: 209d2e65-b118-47a7-aece-fb140fdede3f
title: DXGI functions
ms.topic: article
ms.date: 04/26/2022
---

# DXGI functions

This section contains info about the functions provided by DXGI.

## In this section

| Topic | Description |
|-|-|
| [**CreateDXGIFactory**](/windows/win32/api/DXGI/nf-dxgi-createdxgifactory) | Creates a DXGI 1.0 factory that you can use to generate other DXGI objects. |
| [**CreateDXGIFactory1**](/windows/win32/api/DXGI/nf-dxgi-createdxgifactory1) | Creates a DXGI 1.1 factory that you can use to generate other DXGI objects. |
| [**CreateDXGIFactory2**](/windows/win32/api/dxgi1_3/nf-dxgi1_3-createdxgifactory2) | Creates a DXGI 1.3 factory that you can use to generate other DXGI objects.<br/> In Windows 8, any DXGI factory created while DXGIDebug.dll was present on the system would load and use it. Starting in Windows 8.1, apps explicitly request that DXGIDebug.dll be loaded instead. Use [**CreateDXGIFactory2**](/windows/win32/api/dxgi1_3/nf-dxgi1_3-createdxgifactory2) and specify the DXGI\_CREATE\_FACTORY\_DEBUG flag to request DXGIDebug.dll; the DLL will be loaded if it is present on the system. |
| [**DXGIDeclareAdapterRemovalSupport**](/windows/win32/api/dxgi1_6/nf-dxgi1_6-dxgideclareadapterremovalsupport) | Allows a process to indicate that it's resilient to any of its graphics devices being removed. |
| [**DXGIDisableVBlankVirtualization**](/windows/win32/api/dxgi1_6/nf-dxgi1_6-dxgidisablevblankvirtualization) | Disables v-blank virtualization for the process. This virtualization is used by the dynamic refresh rate (DRR) feature by default for all swap chains to maintain a steady virtualized present rate and v-blank cadence from [IDXGIOutput::WaitForVBlank](/windows/win32/api/dxgi/nf-dxgi-idxgioutput-waitforvblank). By disabling virtualization, these APIs will see the changing refresh rate. |
| [**DXGIGetDebugInterface**](/windows/win32/api/DXGIDebug/nf-dxgidebug-dxgigetdebuginterface) | Retrieves a debugging interface. |
| [**DXGIGetDebugInterface1**](/windows/win32/api/dxgi1_3/nf-dxgi1_3-dxgigetdebuginterface1) | Retrieves an interface that Windows Store apps use for debugging the Microsoft DirectX Graphics Infrastructure (DXGI). |

## Related topics

* [DXGI reference](d3d10-graphics-reference-dxgi.md)
