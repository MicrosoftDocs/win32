---
description: For an application to run properly, the host computer must have the appropriate DLLs installed. These DLLs may be provided by either the operating system, or the applications' redistributable package.
ms.assetid: fa5405e9-116f-4b7f-8f8e-791a79942570
title: Linking Static and Dynamic Libraries (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Linking Static and Dynamic Libraries (Direct3D 10)

For an application to run properly, the host computer must have the appropriate DLLs installed. These DLLs may be provided by either the operating system, or the applications' redistributable package.

## Libraries Load Appropriate DLLs

The libraries included with the DirectX SDK will automatically load the proper DLLs at runtime. The exception to this rule is d3dx10.lib/d3dx10d.lib, which will load the d3dx10.dll that was shipped with that version of the SDK. For example, if the downloaded SDK includes d3dx10\_33.dll and d3dx10\_34.dll, then the library (d3dx10.lib) that shipped with that SDK will load d3dx10\_34.dll. If a subsequent SDK is installed later containing d3dx10\_35.lib, the d3dx10.lib from the previous SDK will still load d3dx10\_34.dll. The d3dx10.lib from the newer SDK will load d3dx10\_35.dll.

## Redistributing Binaries

Only d3dx10.dll (and subsequent versions of the same file) can be redistributed. To redistribute this file, you must use the **DirectXSetup** function. For details on using this function and putting together a redistributable package, see [Installing DirectX with DirectSetup](https://msdn.microsoft.com/library/Ee418267(v=VS.85).aspx). All other necessary binaries are included in Windows Vista. The only binaries that can be redistributed are those located in the following directory.


```
(SDK root)\Redist
```



The following table describes the binaries developers should be aware of.



| Direct3D 10 Binaries   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| d3dx10.dll/d3dx10d.dll | Retail and debug D3DX10 components; the retail components can be redistributed in the REDIST CAB.                                                                                                                                                                                                                                                                                                                                                                                                             |
| d3d10ref.dll           | Reference Rasterizer. Provides software implementation of the graphics pipeline. Only included as part of the Windows SDK or legacy DirectX SDK and cannot be redistributed. The Reference Rasterizer is intended for debugging only. Explicit linking is not necessary; attempting to create a reference device (see [**D3D10CreateDevice**](/windows/desktop/api/D3D10Misc/nf-d3d10misc-d3d10createdevice)) will load this dll if it is present.                                                                                                    |
| d3d10sdklayers.dll     | A series of SDK utilities that act as a layer between API calls and runtime execution, including the [debug layer](d3d10-graphics-programming-guide-api-features-layers.md) and the switch-to-reference layer. Explicit linking is not necessary; if a device is created with the appropriate layer flag, this DLL is loaded automatically. This component is meant for development and debugging purposes only. Only included as part of the Windows SDK or legacy DirectX SDK and cannot be redistributed. |



 

## Related topics

<dl> <dt>

[Programming Guide for Direct3D 10](d3d10-graphics-programming-guide.md)
</dt> <dt>

[Direct3D 10 Graphics](d3d10-graphics.md)
</dt> </dl>

 

 



