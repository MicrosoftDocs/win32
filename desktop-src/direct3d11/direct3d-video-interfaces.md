---
title: Direct3D Video Interfaces
description: This topic lists the Direct3D video interfaces that are available in Direct3D 9Ex and that are supported on Windows 7 and later versions of Windows client operating systems and on Windows Server 2008 R2 and later versions of Windows server operating systems.
ms.assetid: 922AC983-B9C0-494C-BADD-CEF20931FC26
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D Video Interfaces

This topic lists the Direct3D video interfaces that are available in Direct3D 9Ex and that are supported on Windows 7 and later versions of Windows client operating systems and on Windows Server 2008 R2 and later versions of Windows server operating systems. You can use these interfaces and their methods to obtain the video content protection capabilities of the graphics driver and the overlay hardware capabilities of a Direct3D device. You can also use these interfaces and their methods to protect video content. These interfaces and their methods are defined in D3d9.h and described in the [Microsoft Media Foundation](/windows/desktop/medfound/microsoft-media-foundation-sdk) section.



| Interface                                                                                                                                                                                                                             | Description                                                                                                                    |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <span id="IDirect3D9ExOverlayExtension"></span><span id="idirect3d9exoverlayextension"></span><span id="IDIRECT3D9EXOVERLAYEXTENSION"></span>[**IDirect3D9ExOverlayExtension**](/windows/desktop/api/d3d9/nn-d3d9-idirect3d9exoverlayextension)<br/>           | Queries the overlay hardware capabilities of a Direct3D device.<br/>                                                     |
| <span id="IDirect3DAuthenticatedChannel9"></span><span id="idirect3dauthenticatedchannel9"></span><span id="IDIRECT3DAUTHENTICATEDCHANNEL9"></span>[**IDirect3DAuthenticatedChannel9**](/windows/desktop/api/d3d9/nn-d3d9-idirect3dauthenticatedchannel9)<br/> | Provides a communication channel with the graphics driver or the Direct3D runtime.<br/>                                  |
| <span id="IDirect3DCryptoSession9"></span><span id="idirect3dcryptosession9"></span><span id="IDIRECT3DCRYPTOSESSION9"></span>[**IDirect3DCryptoSession9**](/windows/desktop/api/d3d9/nn-d3d9-idirect3dcryptosession9)<br/>                                    | Represents a cryptographic session that is used to access a protected surface.<br/>                                      |
| <span id="IDirect3DDevice9Video"></span><span id="idirect3ddevice9video"></span><span id="IDIRECT3DDEVICE9VIDEO"></span>[**IDirect3DDevice9Video**](/windows/desktop/api/d3d9/nn-d3d9-idirect3ddevice9video)<br/>                                              | Enables an application to use content protection and encryption services that are implemented by a graphics driver.<br/> |



 

## Related topics

<dl> <dt>

[Effects (Direct3D 11)](d3d11-graphics-programming-guide-effects.md)
</dt> <dt>

[Programming Guide for Direct3D 11](dx-graphics-overviews.md)
</dt> </dl>

 

