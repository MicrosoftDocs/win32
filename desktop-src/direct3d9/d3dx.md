---
description: D3DX is a library of tools designed to provide additional graphics functionality on top of Direct3D. D3DX is provided as a dynamic-link library (DLL).
ms.assetid: d7b8c6ba-5c4f-494c-a24f-3b81a176725f
title: D3DX (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# D3DX (Direct3D 9)

> [!NOTE]
> The D3DX library is deprecated. If upgrading to a newer version of Direct3D and associated utility code is not an option, you can make use of the [Microsoft.DXSDK.D3DX](https://www.nuget.org/packages/Microsoft.DXSDK.D3DX) NuGet package rather than relying on the legacy DirectX SDK or DirectSetup.

D3DX is a library of tools designed to provide additional graphics functionality on top of Direct3D. D3DX is provided as a dynamic-link library (DLL).

Only one version of D3DX is provided in this release of the DirectX SDK. The retail D3DX DLL is included in the redistributable provided in the SDK, and is automatically installed as part of **Installing DirectX with DirectSetup**. The D3DX library included in this release is dependent on the Direct3D runtimes that shipped with this SDK. Applications linking against the version of D3DX in this release must also redistribute the runtime from this SDK.

Multiple releases of D3DX can reside independently on a single system simultaneously. By statically linking an application to D3dx9.lib, the application dynamically links to the corresponding retail D3DX DLL at run-time. This DLL corresponds to the D3DX headers the application is compiled against (named with the D3DX\_SDK\_VERSION constant in D3dx9core.h). As new versions of D3DX are shipped in future releases of the DirectX SDK, applications linking to earlier D3DX libraries will remain unaffected.

The D3DX library addresses these general areas of functionality:

-   [Line Drawing Support in D3DX (Direct3D 9)](line-drawing-support-in-d3dx.md)
-   [Mesh Support in D3DX (Direct3D 9)](mesh-support-in-d3dx.md)
-   [Math Function Support in D3DX (Direct3D 9)](math-function-support-in-d3dx.md)
-   [Texture Support in D3DX (Direct3D 9)](texture-support-in-d3dx.md)

## Related topics

<dl> <dt>

[Getting Started](getting-started.md)
</dt> </dl>

 

 



