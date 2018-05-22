---
Description: 'This section contains info about the functions provided by DXGI.'
ms.assetid: '209d2e65-b118-47a7-aece-fb140fdede3f'
title: DXGI Functions
---

# DXGI Functions

This section contains info about the functions provided by DXGI.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDXGIFactory**](createdxgifactory.md)<br/>                               | Creates a DXGI 1.0 factory that you can use to generate other DXGI objects.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**CreateDXGIFactory1**](createdxgifactory1.md)<br/>                             | Creates a DXGI 1.1 factory that you can use to generate other DXGI objects.<br/>                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**CreateDXGIFactory2**](createdxgifactory2.md)<br/>                             | Creates a DXGI 1.3 factory that you can use to generate other DXGI objects.<br/> In Windows 8, any DXGI factory created while DXGIDebug.dll was present on the system would load and use it. Starting in Windows 8.1, apps explicitly request that DXGIDebug.dll be loaded instead. Use [**CreateDXGIFactory2**](createdxgifactory2.md) and specify the DXGI\_CREATE\_FACTORY\_DEBUG flag to request DXGIDebug.dll; the DLL will be loaded if it is present on the system.<br/> |
| [**DXGIDeclareAdapterRemovalSupport**](dxgideclareadapterremovalsupport.md)<br/> | Allows a process to indicate that it's resilient to any of its graphics devices being removed.<br/>                                                                                                                                                                                                                                                                                                                                                                                    |
| [**DXGIGetDebugInterface**](dxgigetdebuginterface.md)<br/>                       | Retrieves a debugging interface.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**DXGIGetDebugInterface1**](dxgigetdebuginterface1.md)<br/>                     | Retrieves an interface that Windows Store apps use for debugging the Microsoft DirectX Graphics Infrastructure (DXGI).<br/>                                                                                                                                                                                                                                                                                                                                                            |



 

## Related topics

<dl> <dt>

[DXGI Reference](d3d10-graphics-reference-dxgi.md)
</dt> </dl>

 

 




