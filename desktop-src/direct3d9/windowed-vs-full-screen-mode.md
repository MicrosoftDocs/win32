---
description: 'Direct3D applications can run in either of two modes: full-screen or windowed.'
ms.assetid: 6ec30c6e-93d1-4b77-9638-86308bbf8f3c
title: Windowed vs Full-Screen Mode (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Windowed vs Full-Screen Mode (Direct3D 9)

Direct3D applications can run in either of two modes: full-screen or windowed.

Full-screen mode means the window that the application runs in covers the entire desktop, hiding all running applications (including your development environment). Games typically default to full-screen mode to fully immerse the user in the game by hiding all running applications. An application running in windowed-mode shares the desktop with all running applications. Code differences between full-screen mode and windowed mode are very small.

Because an application running in full-screen mode takes over the screen, debugging the application requires either a separate monitor or the use of a remote debugger. Use the [DirectX Control Panel Tool](https://msdn.microsoft.com/library/Ee416791(v=VS.85).aspx) to enable multiple-monitor debugging. One advantage of a windowed-mode application is that you can step through the code in a debugger without multiple monitors or a remote debugger.

## Related topics

<dl> <dt>

[Direct3D Devices](direct3d-devices.md)
</dt> </dl>

 

 



