---
description: You can directly access the surface memory by using the IDirect3DSurface9::LockRect method.
ms.assetid: ad669c22-6163-4fbb-bad0-160ced5bc558
title: Accessing Surface Memory Directly (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Accessing Surface Memory Directly (Direct3D 9)

You can directly access the surface memory by using the [**IDirect3DSurface9::LockRect**](/windows/desktop/api) method. When you call this method, the pRect parameter is a pointer to a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that describes the rectangle on the surface to access directly. To request that the entire surface be locked, set pRect to **NULL**. Also, you can specify a **RECT** that covers only a portion of the surface. Providing that no two rectangles overlap, two threads or processes can simultaneously lock multiple rectangles in a surface. Note that a multisample back buffer cannot be locked.

The [**IDirect3DSurface9::LockRect**](/windows/desktop/api) method fills a [**D3DLOCKED\_RECT**](d3dlocked-rect.md) structure with all the information to properly access the surface memory. The structure includes information about the pitch and has a pointer to the locked bits. When you finish accessing the surface memory, call the [**IDirect3DSurface9::UnlockRect**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3dsurface9-unlockrect) method to unlock it.

While you have a surface locked, you can directly manipulate the contents. The following list describes some tips for avoiding common problems with directly rendering surface memory.

-   Never assume a constant display pitch. Always examine the pitch information returned by the [**IDirect3DSurface9::LockRect**](/windows/desktop/api) method. This pitch can vary for a number of reasons, including the location of the surface memory, the display card type, or even the version of the Direct3D driver. For more information, see [Width vs. Pitch (Direct3D 9)](width-vs--pitch.md).
-   Make certain you copy to unlocked surfaces. Direct3D copy methods will fail if called on a locked surface.
-   Limit your application's activity while a surface is locked.
-   Always copy data aligned to display memory. Windows 98 uses a page fault handler, Vflatd.386, to implement a virtual flat-frame buffer for display cards with bank-switched memory. The handler allows these display devices to present a linear frame buffer to Direct3D. Copying data unaligned to display memory can cause the system to suspend operations if the copy spans memory banks.
-   A surface may not be locked if it belongs to a resource assigned to the D3DPOOL\_DEFAULT memory pool unless it is a dynamic texture or a surface created using [**IDirect3DDevice9::CreateOffscreenPlainSurface**](/windows/desktop/api). Back buffer surfaces, which may be accessed using the [**IDirect3DDevice9::GetBackBuffer**](/windows/desktop/api) and [**IDirect3DSwapChain9::GetBackBuffer**](/windows/desktop/api) methods, may be locked only if the swap chain was created with the Flags member of [**D3DPRESENT\_PARAMETERS**](d3dpresent-parameters.md) to include D3DPRESENTFLAG\_LOCKABLE\_BACKBUFFER.

## Related topics

<dl> <dt>

[Direct3D Surfaces](direct3d-surfaces.md)
</dt> </dl>

 

 
