---
description: The mouse cursor methods enable the application to specify a color cursor by providing a surface that contains an image.
ms.assetid: 300a8a6f-abcd-49c9-889b-14b12ff5c821
title: Working with Mouse Cursors (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Mouse Cursors (Direct3D 9)

The mouse cursor methods enable the application to specify a color cursor by providing a surface that contains an image. The system will ensure that this cursor will be updated at half the display rate or more if the application's frame rate is slow. However, the cursor will never be updated more frequently than the display refresh rate.

The mouse cursor position is tied to the system cursor, appropriately scaled for the current display mode spatial resolution, but it can be moved explicitly by the application. This is analogous to the behavior of the Win32 API - supported system mouse cursor. For more information about how to use a mouse cursor in your Direct3D application, see the following reference topics.

-   [**IDirect3DDevice9::ShowCursor**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-showcursor)
-   [**IDirect3DDevice9::SetCursorPosition**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setcursorposition)
-   [**IDirect3DDevice9::SetCursorProperties**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-setcursorproperties)

Direct3D ensures that the mouse is supported either by hardware implementations or by the Direct3D run time that performs hardware-accelerated blitting operations when calling [**IDirect3DDevice9::Present**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-present).

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
