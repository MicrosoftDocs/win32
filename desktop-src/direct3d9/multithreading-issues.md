---
description: Full-screen Direct3D applications provide a window handle to the Direct3D run time.
ms.assetid: 66a9e14f-46c8-45e8-ae0e-4d8cf5106acc
title: Multithreading Issues (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Multithreading Issues (Direct3D 9)

Full-screen Direct3D applications provide a window handle to the Direct3D run time. The window is hooked by the run time. This means that all messages passed to the application's window message procedure have first been examined by the Direct3D run time's own message-handling procedure.

Display mode changes are affected by support routines built into the underlying operating system. When mode changes occur, the system broadcasts several messages to all applications. In Direct3D applications, the messages are received on the window procedure thread, which is not necessarily the same thread that called [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset) or [**IDirect3D9::CreateDevice**](/windows/desktop/api) (or the final Release of [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9), which can cause a display mode change). The Direct3D run time maintains several critical sections internally. Because at least one of these critical sections is held across the mode switch caused by **IDirect3DDevice9::Reset** or **IDirect3D9::CreateDevice**, these critical sections are still held when the application receives the mode-change related window messages.

This design has some implications for multithreaded applications. In particular, an application must be sure to strongly segregate its window message handling threads from its Direct3D threads. An application that causes a mode change on one thread but makes Direct3D calls on a different thread in its window procedure is in danger of deadlock.

For these reasons, Direct3D is designed so that the methods [**IDirect3DDevice9::Reset**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-reset), [**IDirect3D9::CreateDevice**](/windows/desktop/api), [**IDirect3DDevice9::TestCooperativeLevel**](/windows/win32/api/d3d9helper/nf-d3d9helper-idirect3ddevice9-testcooperativelevel), or the final Release of [**IDirect3DDevice9**](/windows/win32/api/d3d9helper/nn-d3d9helper-idirect3ddevice9) can only be called from the same thread that handles window messages.

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 
